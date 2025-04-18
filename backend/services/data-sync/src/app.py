"""
Real-Time Data Sync Service – Entry point.
Fetches and synchronizes aircraft, weather, and airport data.
"""

from fastapi import FastAPI
from connectors import aircraft_connector, weather_connector, airport_connector
import logging

app = FastAPI(
    title="Real-Time Data Sync Service",
    description="Syncs real-time data for aircraft, weather, and airport operations.",
    version="1.0.0"
)

@app.get("/sync")
async def sync_data():
    try:
        aircraft_data = aircraft_connector.get_aircraft_data()
        weather_data = weather_connector.get_weather_data()
        airport_data = airport_connector.get_airport_data()
        logging.info("Data sync successful.")
        return {
            "aircraft": aircraft_data,
            "weather": weather_data,
            "airport": airport_data
        }
    except Exception as e:
        logging.error("Error in syncing data: %s", e)
        return {"error": "Data sync failed."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)
