import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
API_ID = os.getenv('TELEGRAM_API_ID')
API_HASH = os.getenv('TELEGRAM_API_HASH')
PHONE_NUMBER = os.getenv('TELEGRAM_PHONE_NUMBER')

CHANNELS = ['@Maroset', '@freelance_ethio', '@addis_ababa_jobs', '@ethio_job_vacancy1', '@jobs_in_ethio',
             '@josad_software', '@hahujobs', "@effoyjobs" ]
JOB_CATEGORIES = [
    'Technology', 'Finance', 'Bank', 'Insurance', 'NGO',
    'Healthcare', 'Education', 'Marketing', 'Sales', 'Human Resources',
    'Lawyer', 'Engineering', 'Design', 'Media', 'Hospitality',
    'Specialist', 'Analyst', 'Developer', 'Engineer',
    'Accountant', 'Auditor', 'Teacher', 'Consultant', 'Manager', 'Director', 'Executive', 'Coordinator'
]

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

UPDATE_INTERVAL = 28800  # 8 hours in seconds
