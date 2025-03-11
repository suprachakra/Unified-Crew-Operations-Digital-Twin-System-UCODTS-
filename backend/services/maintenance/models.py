# Maintenance Service Data Models

from pydantic import BaseModel
from datetime import date

class MaintenanceEvent(BaseModel):
    maintenance_id: int
    flight_id: int
    equipment: str
    maintenance_date: date
    status: str
    description: str
