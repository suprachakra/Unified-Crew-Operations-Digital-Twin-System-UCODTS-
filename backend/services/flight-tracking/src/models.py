"""
Flight Tracking Models.
Defines the structure for flight positions.
"""

from pydantic import BaseModel

class FlightPosition(BaseModel):
    flight_id: int
    latitude: float
    longitude: float
    altitude: float
    timestamp: str
