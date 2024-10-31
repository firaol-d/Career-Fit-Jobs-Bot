-- Users table
CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT PRIMARY KEY,
    preferences JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Job listings table
CREATE TABLE IF NOT EXISTS job_listings (
    id SERIAL PRIMARY KEY,
    channel TEXT NOT NULL,
    summary TEXT NOT NULL,
    message_id BIGINT NOT NULL,
    message_link TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create index on channel and message_id for faster lookups
CREATE INDEX IF NOT EXISTS idx_job_listings_channel_message_id ON job_listings (channel, message_id);

-- Create index on created_at for faster sorting and filtering
CREATE INDEX IF NOT EXISTS idx_job_listings_created_at ON job_listings (created_at);

-- Add message_link column if it doesn't exist
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns 
                   WHERE table_name='job_listings' AND column_name='message_link') THEN
        ALTER TABLE job_listings ADD COLUMN message_link TEXT;
    END IF;
END $$;

-- Pending users table
CREATE TABLE IF NOT EXISTS pending_users (
    user_id BIGINT PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
