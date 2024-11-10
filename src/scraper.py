import os
import logging
from telethon import TelegramClient
from config import API_ID, API_HASH, PHONE_NUMBER, CHANNELS
from database import add_job_listing
from datetime import datetime, timezone, timedelta
import asyncio

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_keywords():
    keywords_path = os.path.join(os.path.dirname(__file__), 'keywords.txt')
    with open(keywords_path, 'r') as f:
        return [line.strip().lower() for line in f]

def get_last_run_time():
    try:
        with open('last_scrape.txt', 'r') as f:
            # Parse the time as timezone-aware UTC
            return datetime.strptime(f.read().strip(), '%a %d %b %Y %H:%M:%S %Z').replace(tzinfo=timezone.utc)
    except Exception as e:
        logger.error(f"Error reading last run time: {e}")
        return datetime.now(timezone.utc) - timedelta(days=1)  # Default to 1 day ago if error occurs

def update_last_run_time():
    with open('last_scrape.txt', 'w') as f:
        f.write(datetime.now(timezone.utc).strftime('%a %d %b %Y %H:%M:%S %Z'))

async def scrape_messages(client, channel):
    messages = []
    last_run_time = get_last_run_time()  # Get the last run time, timezone-aware
    async for message in client.iter_messages(channel, limit=100):
        # Ensure message.date is also timezone-aware by setting to UTC if not already
        message_date = message.date if message.date.tzinfo else message.date.replace(tzinfo=timezone.utc)
        if message_date < last_run_time:  # Only scrape messages after the last run time
            break
        messages.append(message)
    return messages

async def process_messages(messages, channel):
    for message in messages:
        try:
            channel_name = channel.lstrip('@')
            job_listing = {
                'channel': channel,
                'summary': message.text[:250],  # Limit summary to 250 characters
                'message_id': message.id,
                'message_link': f"https://t.me/{channel_name}/{message.id}"
            }
            add_job_listing(**job_listing)
            logger.info(f"Added job listing from {channel}, message ID: {message.id}")
        except Exception as e:
            logger.error(f"Error processing message from {channel}, message ID: {message.id}: {e}")

async def main():
    logger.info("Starting the scraping process...")
    client = TelegramClient('session', API_ID, API_HASH)
    await client.start(phone=PHONE_NUMBER)

    try:
        for channel in CHANNELS:
            messages = await scrape_messages(client, channel)
            await process_messages(messages, channel)
        update_last_run_time()
    except Exception as e:
        logger.error(f"Error in scraping process: {e}")
    finally:
        await client.disconnect()
        logger.info("Scraping process completed.")

async def scheduler():
    schedule_times = [(5, 0), (9, 0), (13, 0), (17, 0), (23, 0)]  # (hour, minute) pairs

    while True:
        now = datetime.now(timezone.utc)
        current_time = (now.hour, now.minute)

        logger.info(f"Checking time: current time is {now.strftime('%H:%M:%S')} UTC.")

        if current_time in schedule_times:
            logger.info(f"Time matched schedule at {now.strftime('%H:%M:%S')} UTC. Starting the scraping process.")
            await main()  # Run main() if it's the right time
            await asyncio.sleep(60)  # Wait a minute to avoid re-running within the same minute
        else:
            logger.info("No match with scheduled times. Waiting before the next check.")
            await asyncio.sleep(30)  # Check the time every 30 seconds

if __name__ == "__main__":
    asyncio.run(scheduler())
