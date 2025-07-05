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


## 🚀 Deployment & Scheduling (Render + cron-job.org)

### Steps to Automate with Render & cron-job.org

1. **Configure Environment Variables**: Set your secrets in Render's dashboard.
2. **Deploy to Render**: Deploy your FastAPI app (`src/server.py`) as a web service.
3. **Set Up cron-job.org**: Schedule HTTP POST requests to your endpoints:
   - `/run-scraper` for scraping jobs
   - `/send-updates` for sending updates
   - Adjust schedule as needed (e.g., every 8 hours for scraping, 10 minutes after for updates)

### Example Local Run

```bash
python src/main.py         # Start the bot (for Telegram interaction)
uvicorn src.server:app --host 0.0.0.0 --port 8000  # Start FastAPI server for HTTP endpoints
```

## 🔄 Workflow

1. 🕒 **Scheduling**
   - Scraper runs every 8 hours
   - Updates sent 10 minutes after scraping
   - Bot runs continuously with 2-hour active periods (if run on a VM or locally)

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
