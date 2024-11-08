import asyncio
import pytz
from datetime import datetime
from telegram.ext import Application
from database import get_all_users
from config import TOKEN

async def send_sleep_notification(notification_type: str):
    app = Application.builder().token(TOKEN).build()
    users = get_all_users()
    
    ethiopia_tz = pytz.timezone('Africa/Addis_Ababa')
    current_time = datetime.now(ethiopia_tz)
    next_active = (current_time.hour + 1) % 24

    if notification_type == "break":
        message = (
            "🔄 *Break Time*\n\n"
            f"Bot is taking a short break\n"
            f"Will be back at {next_active:02d}:00 EAT"
        )
    else:  # night
        message = (
            "😴 *Night Mode*\n\n"
            "Bot is going to sleep\n"
            "Will be back at 07:00 AM EAT\n\n"
            "_Regular hours: 7:00 AM - 1:00 AM_"
        )

    for user in users:
        try:
            await app.bot.send_message(
                chat_id=user['user_id'],
                text=message,
                parse_mode='Markdown'
            )
        except Exception as e:
            print(f"Failed to notify user {user['user_id']}: {e}")

if __name__ == "__main__":
    import sys
    notification_type = sys.argv[1] if len(sys.argv) > 1 else "break"
    asyncio.run(send_sleep_notification(notification_type)) 