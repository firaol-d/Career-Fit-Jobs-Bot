import logging
import asyncio
from telegram import Update
from telegram.ext import Application
from bot import setup_handlers
from config import TOKEN
from database import init_db
# from apscheduler.schedulers.background import BackgroundScheduler
import time

# Import your update scripts
# from send_updates import send_updates_function  # Adjust the import based on your function
# from scraper import job_updates_function    # Adjust the import based on your function

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start_bot(application: Application):
    await application.initialize()
    await application.start()
    await application.updater.start_polling(allowed_updates=Update.ALL_TYPES)

async def main():
    init_db()
    
    # Create the Application
    application = Application.builder().token(TOKEN).build()
    
    # Set up handlers
    setup_handlers(application)
    
    # Start the scheduler
    # start_scheduler()

    try:
        await start_bot(application)
        logger.info("Bot started. Press Ctrl+C to stop.")
        # Keep the bot running
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        logger.info("Bot stopping...")
    finally:
        await application.stop()
        await application.shutdown()

# def start_scheduler():
#     scheduler = BackgroundScheduler()

#     # Schedule the job updates function
#     scheduler.add_job(job_updates_function, 'cron', minute='24', hour='4,10,12,16,22')  # Adjust as needed
#     # Schedule the send updates function
#     scheduler.add_job(send_updates_function, 'cron', minute='27', hour='4,10,12,16,22')  # Adjust as needed

#     scheduler.start()
#     logging.info("Scheduler started.")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        logger.info("Bot stopped.")
