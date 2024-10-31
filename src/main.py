import logging
import asyncio
from telegram import Update
from telegram.ext import Application
from bot import setup_handlers
from config import TOKEN
from database import init_db

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

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        logger.info("Bot stopped.")
