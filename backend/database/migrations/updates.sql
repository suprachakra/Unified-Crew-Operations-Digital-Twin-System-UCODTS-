-- Example update: Ensure delay_reason column exists in flight table
ALTER TABLE flight
ADD COLUMN IF NOT EXISTS delay_reason VARCHAR(255);
