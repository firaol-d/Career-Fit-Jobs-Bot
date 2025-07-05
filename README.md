# 🤖 Career Fit Job Bot

Your personal job hunting assistant that brings opportunities right to your Telegram! Currently focused on job opportunities in Ethiopia 🇪🇹

## ✨ Features

🔍 Smart job scraping from Ethiopian Telegram channels
🎯 Personalized job matching based on your preferences
📬 Automated updates 5 times daily
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

1. 📋 Clone the repository

    ```bash
    git clone https://github.com/Dagmawi-M/Career-Fit-Job-bot.git
    cd Career-Fit-Job-bot
    ```

2. 📦 Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

3. 🔑 Configure environment variables

- Copy `.env.example` to `.env`
- Add your credentials:
  - `TELEGRAM_BOT_TOKEN`
  - `TELEGRAM_API_ID`
  - `TELEGRAM_API_HASH`
  - `SUPABASE_URL`
  - `SUPABASE_KEY`


### 3. Deployment & Scheduling (Render + cron-job.org)

- Deploy the bot as a web service on [Render](https://render.com) using FastAPI (`src/server.py`).
- Scheduled jobs (scraper, send updates) are triggered by [cron-job.org](https://cron-job.org) making HTTP POST requests to your Render endpoints.
- No paid hosting or GitHub Actions required for scheduling!

#### Running Locally

```bash
python src/main.py         # Start the bot (for interactive Telegram use)
uvicorn src.server:app --host 0.0.0.0 --port 8000  # Start FastAPI server for HTTP endpoints
```

#### Using Render + cron-job.org

- Deploy your FastAPI app (`src/server.py`) to Render as a web service.
- Set up cron jobs on cron-job.org to POST to:
  - `https://<your-render-url>/run-scraper` (for scraping)
  - `https://<your-render-url>/send-updates` (for sending updates)
  - Adjust schedule as needed (e.g., every 8 hours for scraping, 10 minutes after for updates).

See `src/server.py` for endpoint details.

## 💡 How it Works

1. 🤖 Scraper collects jobs from Ethiopian Telegram channels
2. 🎯 Bot matches jobs with user preferences
3. 📬 Sends personalized updates via Telegram
4. 🧹 Auto-cleans database to maintain performance

## 📝 License

MIT License - feel free to use and modify!


