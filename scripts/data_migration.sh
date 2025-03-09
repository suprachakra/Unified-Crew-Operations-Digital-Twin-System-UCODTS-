#!/bin/bash
# Script to execute database migration and seeding for UCODTS

echo "Starting database migration..."

# Variables (adjust if needed)
DB_USER="ucodts"
DB_NAME="ucodts_db"
DB_HOST="localhost"
MIGRATION_DIR="../backend/database/migrations"

# Apply the initial schema
echo "Applying initial schema..."
psql -U $DB_USER -d $DB_NAME -h $DB_HOST -f $MIGRATION_DIR/initial_schema.sql

# Apply any updates
echo "Applying schema updates..."
psql -U $DB_USER -d $DB_NAME -h $DB_HOST -f $MIGRATION_DIR/updates.sql

echo "Database migration completed successfully."
