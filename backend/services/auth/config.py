# config.py - Auth Service Configuration

import os

SECRET_KEY = os.getenv("AUTH_SECRET_KEY", "your_default_secret_key")
ALGORITHM = os.getenv("AUTH_ALGORITHM", "HS256")
