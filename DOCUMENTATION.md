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
│ └── policy.py
├── tests/
│ └── test_.py
├── .github/
│ └── workflows/
│ └── job_update.yml
├── requirements.txt
├── README.md
├── DOCUMENTATION.md
└── .env

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

## 🔄 Workflow

1. 🕒 **Scheduling**
   - Scraper runs every 8 hours
   - Updates sent 30 minutes after scraping
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

Need more details? Contact @cfjsupport on Telegram!
