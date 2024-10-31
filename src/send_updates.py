import logging
import sys
from telegram.ext import Application
from config import TOKEN, JOB_CATEGORIES
from database import get_all_users, get_job_listings, get_user_preferences, clear_job_listings
from message_formatter import create_job_update
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def match_jobs_with_preferences(jobs, preferences):
    matched_jobs = defaultdict(list)
    for job in jobs:
        job_summary_lower = job['summary'].lower()
        for pref in preferences:
            pref_keywords = pref.lower().split('/')
            if any(keyword in job_summary_lower for keyword in pref_keywords):
                matched_jobs[pref].append(job)
                break
    return matched_jobs

async def send_job_updates():
    logger.info("Starting send_job_updates function")
    try:
        application = Application.builder().token(TOKEN).build()
        logger.info("Application built successfully")
        
        job_listings = get_job_listings()
        logger.info(f"Retrieved {len(job_listings)} job listings")
        
        if job_listings:
            users = get_all_users()
            logger.info(f"Retrieved {len(users)} users")
            
            for user in users:
                user_preferences = get_user_preferences(user['user_id'])
                if user_preferences:
                    matched_jobs = match_jobs_with_preferences(job_listings, user_preferences)
                    if matched_jobs:
                        update_url = create_job_update(matched_jobs)
                        
                        message = (
                            "✨ *Latest Job Matches*\n"
                            f"{format_summary(matched_jobs)}"
                            "──────────────\n"
                            f"🔍 [View Full Details]({update_url})"
                        )
                        
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
                            
        await clear_job_listings()
    except Exception as e:
        logger.error(f"Error in send_job_updates: {e}")

def format_summary(matched_jobs):
    summary = ""
    for category, jobs in matched_jobs.items():
        channels = set(job['channel'] for job in jobs)
        summary += f"📌 *{category}*\n└ {len(jobs)} jobs from:\n"
        channel_list = [f"  • _{channel}_" for channel in channels]
        summary += f"{', '.join(channel_list)}\n\n"
    return summary

if __name__ == "__main__":
    logger.info("Script started")
    import asyncio
    asyncio.run(send_job_updates())
    logger.info("Script finished")
