import os
from telethon import TelegramClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_ID = os.getenv('TELEGRAM_API_ID')
API_HASH = os.getenv('TELEGRAM_API_HASH')
PHONE_NUMBER = os.getenv('TELEGRAM_PHONE_NUMBER')

if not (API_ID and API_HASH and PHONE_NUMBER):
    print("Please set TELEGRAM_API_ID, TELEGRAM_API_HASH, and TELEGRAM_PHONE_NUMBER in your .env file.")
    exit(1)

# The session file will be named 'session.session' in the project root
def main():
    client = TelegramClient('session', API_ID, API_HASH)
    print("\n--- Telethon Session Generator ---")
    print(f"Using phone: {PHONE_NUMBER}")
    print("You will be prompted to enter the code sent to your Telegram.")
    client.start(phone=PHONE_NUMBER)
    print("\nSession generated and saved as 'session.session'. You can now upload this file to your server.")
    client.disconnect()

if __name__ == "__main__":
    main()
