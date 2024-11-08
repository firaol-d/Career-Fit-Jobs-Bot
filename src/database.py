import os
from supabase import create_client, Client
import logging
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Supabase client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def init_db():
    # This function might not be necessary if Supabase handles schema creation
    logger.info("Database connection initialized")

def user_exists(user_id: int) -> bool:
    try:
        response = supabase.table('users').select('user_id').eq('user_id', user_id).execute()
        return bool(response.data)
    except Exception as e:
        logger.error(f"Error checking user existence {user_id}: {e}")
        return False

def add_user(user_id: int) -> bool:
    try:
        if not user_exists(user_id):
            supabase.table('users').insert({
                'user_id': user_id,
                'preferences': [],
                'created_at': datetime.now().isoformat()
            }).execute()
            logger.info(f"Successfully added new user {user_id}")
            return True
        return False
    except Exception as e:
        logger.error(f"Error adding user {user_id}: {e}")
        return False

def update_user_preferences(user_id: int, preferences: list):
    try:
        supabase.table('users').update({"preferences": preferences}).eq("user_id", user_id).execute()
        logger.info(f"Preferences updated for user {user_id}")
    except Exception as e:
        logger.error(f"Error updating preferences for user {user_id}: {e}")

def get_user_preferences(user_id: int) -> list:
    try:
        response = supabase.table('users').select('preferences').eq('user_id', user_id).execute()
        if response.data and response.data[0]['preferences'] is not None:
            return response.data[0]['preferences']
        logger.info(f"No preferences found for user {user_id}, returning empty list")
        return []
    except Exception as e:
        logger.error(f"Error getting preferences for user {user_id}: {e}")
        return []

def add_job_listing(channel: str, summary: str, message_id: int, message_link: str):
    try:
        supabase.table('job_listings').insert({
            'channel': channel,
            'summary': summary,
            'message_id': message_id,
            'message_link': message_link
        }).execute()
        logger.info(f"Job listing added from {channel}, message ID: {message_id}")
    except Exception as e:
        logger.error(f"Error adding job listing: {e}")

def get_job_listings():
    try:
        response = supabase.table('job_listings').select('*').execute()
        return response.data
    except Exception as e:
        logger.error(f"Error getting job listings: {e}")
        return []

def clear_job_listings():
    try:
        supabase.table('job_listings').delete().neq('id', 0).execute()
        logger.info("Job listings cleared")
    except Exception as e:
        logger.error(f"Error clearing job listings: {e}")

def get_all_users():
    try:
        response = supabase.table('users').select('*').execute()
        logger.info(f"Retrieved {len(response.data)} users from database")
        return response.data
    except Exception as e:
        logger.error(f"Error getting users: {e}")
        return []

def add_pending_user(user_id: int):
    try:
        supabase.table('pending_users').insert({"user_id": user_id}).execute()
        logger.info(f"Added pending user {user_id}")
    except Exception as e:
        logger.error(f"Error adding pending user {user_id}: {e}")

def process_pending_users():
    try:
        response = supabase.table('pending_users').select('*').execute()
        for user in response.data:
            add_user(user['user_id'])
        supabase.table('pending_users').delete().neq('id', 0).execute()
    except Exception as e:
        logger.error(f"Error processing pending users: {e}")

if __name__ == '__main__':
    # You can add test code here to verify database operations
    pass
