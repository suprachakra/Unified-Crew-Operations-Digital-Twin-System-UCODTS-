# Safety Service Data Models

from pydantic import BaseModel
from datetime import datetime

class SafetyIncident(BaseModel):
    incident_id: int
    flight_id: int
    incident_type: str
    severity: str
    incident_time: datetime
    resolution: str
