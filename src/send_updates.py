import logging
from telegram.ext import Application
from config import TOKEN
from database import get_all_users, get_job_listings, get_user_preferences, clear_job_listings
from message_formatter import create_job_update

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def send_job_updates():
    logger.info("Starting send_job_updates function")
    try:
        # Initialize the Telegram application
        application = Application.builder().token(TOKEN).build()
        logger.info("Application built successfully")
        
        # Retrieve job listings
        job_listings = get_job_listings()
        logger.info(f"Retrieved {len(job_listings)} job listings")
        
        if job_listings:
            # Retrieve all users
            users = get_all_users()
            logger.info(f"Retrieved {len(users)} users from the database")
            
            for user in users:
                user_preferences = get_user_preferences(user['user_id'])
                if user_preferences:
                    matched_jobs = match_jobs_with_preferences(job_listings, user_preferences)
                    if matched_jobs:
                        update_url = create_job_update(matched_jobs)
                        
                        # Format the message
                        message = (
                            "✨ *Latest Job Matches*\n"
                            f"{format_summary(matched_jobs)}"
                            "──────────────\n"
                            f"🔍 [View Full Details]({update_url})"
                        )
                        
                        # Escape the message to prevent Markdown parsing errors
                        message = escape_markdown(message)
                        
                        try:
                            await application.bot.send_message(
                                chat_id=user['user_id'],
                                text=message,
                                parse_mode='MarkdownV2',
                                disable_web_page_preview=False  # Enable instant view
                            )
                            logger.info(f"Successfully sent update to user {user['user_id']}")
                        except Exception as e:
                            logger.error(f"Failed to send update to user {user['user_id']}: {e}")
                else:
                    logger.info(f"No preferences found for user {user['user_id']}, skipping.")
        else:
            logger.warning("No job listings available to send.")
        
        # Clear job listings after sending updates
        clear_job_listings()  # Call without await if it's not an async function
        logger.info("Cleared job listings from the database.")
        
    except Exception as e:
        logger.error(f"Error in send_job_updates: {e}")

def match_jobs_with_preferences(jobs, preferences):
    matched_jobs = {}
    for job in jobs:
        job_summary_lower = job['summary'].lower()
        for pref in preferences:
            if pref.lower() in job_summary_lower:
                if pref not in matched_jobs:
                    matched_jobs[pref] = []
                matched_jobs[pref].append(job)
    return matched_jobs

def format_summary(matched_jobs):
    summary = "✨ *Latest Job Matches*\n"
    for category, jobs in matched_jobs.items():
        channels = set(job['channel'] for job in jobs)  # Assuming each job has a 'channel' field
        summary += f"📌 {category}\n"
        summary += f"└ {len(jobs)} jobs from:\n"
        channel_list = [f"  • {channel}" for channel in channels]  # Format channels with '@'
        summary += f"{', '.join(channel_list)}\n\n"  # Join channels with a comma
    return summary.strip()  # Remove any trailing whitespace

def escape_markdown(text):
    # Escape characters that have special meaning in Markdown
    return text.replace('_', '\\_') \
               .replace('*', '\\*') \
               .replace('[', '\\[') \
               .replace(']', '\\]') \
               .replace('`', '\\`') \
               .replace('(', '\\(') \
               .replace(')', '\\)') \
               .replace('~', '\\~') \
               .replace('>', '\\>') \
               .replace('#', '\\#') \
               .replace('+', '\\+') \
               .replace('-', '\\-') \
               .replace('=', '\\=') \
               .replace('|', '\\|') \
               .replace('{', '\\{') \
               .replace('}', '\\}') \
               .replace('.', '\\.') \
               .replace('!', '\\!')

def send_updates_function():
    # Your logic for sending updates
    print("Sending updates...")  # Replace with actual logic

if __name__ == "__main__":
    import asyncio
    asyncio.run(send_job_updates())
