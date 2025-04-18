"""
Models for digital twin synchronization.
"""

from pydantic import BaseModel
from datetime import datetime

class SyncData(BaseModel):
    asset_id: str
    physical_state: dict
    digital_state: dict
    timestamp: datetime
