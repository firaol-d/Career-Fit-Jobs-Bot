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
  - `HEROKU_API_KEY` (for deployment)
  - `HEROKU_APP_NAME` (for deployment)

### 3. Deploying to Heroku

1. **Create a Heroku Account**: If you don't have one, sign up at [Heroku](https://www.heroku.com).

2. **Install the Heroku CLI**: Follow the instructions [here](https://devcenter.heroku.com/articles/heroku-cli) to install the Heroku Command Line Interface.

3. **Login to Heroku**: Open your terminal and run:

    ```bash
    heroku login
    ```

4. **Create a New Heroku App**:

    ```bash
    heroku create your-app-name
    ```

5. **Set Environment Variables**: Set your environment variables on Heroku:

    ```bash
    heroku config:set TELEGRAM_BOT_TOKEN=your_token_here
    heroku config:set TELEGRAM_API_ID=your_api_id_here
    heroku config:set TELEGRAM_API_HASH=your_api_hash_here
    heroku config:set SUPABASE_URL=your_supabase_url_here
    heroku config:set SUPABASE_KEY=your_supabase_key_here
    heroku config:set HEROKU_API_KEY=your_heroku_api_key_here
    ```

6. **Deploy Your Code**: Push your code to Heroku:

    ```bash
    git push heroku main  # or your branch name
    ```

7. **Scale Your Dynos**: Ensure your worker dyno is running:

    ```bash
    heroku ps:scale worker=1 --app your-app-name
    ```

8. **Monitor Logs**: Check the logs to ensure everything is running smoothly:

    ```bash
    heroku logs --tail --app your-app-name
    ```

## 💡 How it Works

1. 🤖 Scraper collects jobs from Ethiopian Telegram channels
2. 🎯 Bot matches jobs with user preferences
3. 📬 Sends personalized updates via Telegram
4. 🧹 Auto-cleans database to maintain performance

## 📝 License

MIT License - feel free to use and modify!
