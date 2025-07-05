# 📚 Career Fit Job Bot Documentation

## 🏗️ Project Architecture

Carrer-Fit-Job-bot/
├── src/
│ ├── bot.py
│ ├── scraper.py
│ ├── main.py
│ ├── config.py
│ ├── database.py
│ ├── message_formatter.py
│ ├──.env
│ └── policy.py
├── tests/
│ └── test_.py
├── .github/
│ └── workflows/
│ └── job_update.yml
├── requirements.txt
├── procfile
├── README.md
└── DOCUMENTATION.md

## 🔧 Core Components

### 🤖 Bot Module (`bot.py`)
- Handles user interactions
- Manages preferences
- Processes commands (/start, /help, /preferences)

### 🕷️ Scraper Module (`scraper.py`)
- Collects jobs from Telegram channels
- Filters relevant content
- Stores in database

### 📊 Database Module (`database.py`)
- Manages user data
- Stores job listings
- Handles preferences

### 📬 Updates Module (`send_updates.py`)
- Matches jobs with preferences
- Formats messages
- Sends updates to users

## 🚀 Deployment on Heroku

### Steps to Deploy

1. **Create a Heroku Account**: Sign up at [Heroku](https://www.heroku.com).

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

## 🔄 Workflow

1. 🕒 **Scheduling**
   - Scraper runs every 8 hours
   - Updates sent 10 minutes after scraping
   - Bot runs continuously with 2-hour active periods

2. 🎯 **Job Matching**
   - Analyzes job descriptions
   - Matches with user preferences
   - Filters by relevance

3. 📨 **Update Delivery**
   - Creates Telegraph pages
   - Sends summaries via Telegram
   - Includes direct links

## 🗄️ Database Schema

### 👤 Users Table
- user_id (BIGINT, PRIMARY KEY)
- preferences (JSONB)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

### 📋 Job Listings Table
- id (SERIAL, PRIMARY KEY)
- channel (TEXT)
- summary (TEXT)
- message_id (BIGINT)
- message_link (TEXT)
- created_at (TIMESTAMP)

## 🚀 Getting Started

1. 🤖 Test the bot: [@CareerFitJobsBot](https://t.me/CareerFitJobsBot)
2. 📋 Set your preferences using /start
3. 📬 Receive personalized job updates

## ⚠️ Error Handling

- 📝 Logs all errors
- 🚨 Alerts admins for critical issues
- 🔄 Automatic recovery mechanisms

## 🔜 Future Plans

- 🌐 Multi-language support
- 🤖 AI-powered job matching
- 📊 Analytics dashboard
- 💬 User feedback system
