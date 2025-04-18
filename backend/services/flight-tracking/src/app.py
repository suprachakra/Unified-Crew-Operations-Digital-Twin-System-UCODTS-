"""
Flight Tracking Service – Entry point.
Provides real-time position tracking, distress updates, and alert generation.
"""

from fastapi import FastAPI
from routes import router as tracking_router
import logging

app = FastAPI(
    title="Flight Tracking Service",
    description="Provides real-time flight tracking and distress monitoring.",
    version="1.0.0"
)

app.include_router(tracking_router, prefix="/api/v1/flight-tracking")

if __name__ == "__main__":
    import uvicorn
    try:
        logging.info("Starting Flight Tracking Service...")
        uvicorn.run("src.app:app", host="0.0.0.0", port=8040, reload=True)
    except Exception as e:
        logging.error("Error starting Flight Tracking Service: %s", e)
