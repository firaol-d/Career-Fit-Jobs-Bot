# 🤖 Career Fit Job Bot

Your personal job hunting assistant that brings opportunities right to your Telegram! Currently focused on job opportunities in Ethiopia 🇪🇹

## ✨ Features

🔍 Smart job scraping from Ethiopian Telegram channels
🎯 Personalized job matching based on your preferences
📬 Automated updates 3 times daily
📱 Easy-to-use Telegram interface

## 🚀 Try it Now!

1. Start chatting with [@CareerFitJobsBot](https://t.me/CareerFitJobsBot)
2. Set your job preferences
3. Receive tailored job updates

## 🛠️ Development Setup

### Prerequisites

- Python 3.9+
- Supabase account
- Telegram Bot Token
- Telegram API credentials

### 1. Database Setup

1. Create a new project in [Supabase](https://supabase.com)
2. Copy the SQL from `schema.sql` into Supabase SQL Editor
3. Run the SQL script to create necessary tables

### 2. Environment Setup

1. 📋Clone the repository

    git clone https://github.com/Dagmawi-M/Career-Fit-Job-bot.git
    cd Career-Fit-Job-bot

2. 📦 Install dependencies

    pip install -r requirements.txt

3. 🔑 Configure environment variables

- Copy `.env.example` to `.env`
- Add your credentials:
  - `TELEGRAM_BOT_TOKEN`
  - `TELEGRAM_API_ID`
  - `TELEGRAM_API_HASH`
  - `SUPABASE_URL`
  - `SUPABASE_KEY`

4. 🏃‍♂️Running the Bot

#### Option 1: Manual Running

1. Start the scraper:

    python src/scraper.py

2. Run the bot:

    python src/main.py

3. Send updates:

    python src/send_updates.py

#### Option 2: GitHub Actions (Recommended)

1. Fork the repository
2. Add your secrets to GitHub repository settings
3. Enable GitHub Actions
4. The bot will run automatically according to:
   - `bot_runner.yml`: Runs every 3 hours (3,6,9,12,15,18,21 UTC)
   - `job_update.yml`: Scrapes jobs every 8 hours
   - `send_updates.yml`: Sends updates 30 minutes after scraping

## 💡 How it Works

1. 🤖 Scraper collects jobs from Ethiopian Telegram channels
2. 🎯 Bot matches jobs with user preferences
3. 📬 Sends personalized updates via Telegraph and Telegram
4. 🧹 Auto-cleans database to maintain performance

## 📝 License

MIT License - feel free to use and modify!

## 📞 Support

Need help? Contact:
- 💬 Telegram: @cfjsupport

