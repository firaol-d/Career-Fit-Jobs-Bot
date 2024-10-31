import asyncio
import os
from telethon import TelegramClient
from config import API_ID, API_HASH, PHONE_NUMBER, CHANNELS
from database import add_job_listing
from datetime import datetime, timedelta, timezone
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_keywords():
    keywords_path = os.path.join(os.path.dirname(__file__), 'keywords.txt')
    with open(keywords_path, 'r') as f:
        return [line.strip().lower() for line in f]

async def scrape_messages(client, channel):
    messages = []
    eight_hours_ago = datetime.now(timezone.utc) - timedelta(hours=8)
    async for message in client.iter_messages(channel, limit=100):
        if message.date < eight_hours_ago:
            break
        messages.append(message)
    return messages

async def process_messages(messages, channel):
    for message in messages:
        try:
            # Remove the '@' symbol from the channel name for the message link
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
    client = TelegramClient('session', API_ID, API_HASH)
    await client.start(phone=PHONE_NUMBER)

    try:
        for channel in CHANNELS:
            messages = await scrape_messages(client, channel)
            await process_messages(messages, channel)
    except Exception as e:
        logger.error(f"Error in scraping process: {e}")
    finally:
        await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
