# Global Configuration for Backend Services

import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://ucodts:password@database:5432/ucodts_db")
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
