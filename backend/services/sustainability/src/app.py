"""
Sustainability Tracking Service
Calculates and tracks fuel consumption and CO₂ emissions.
"""

from fastapi import FastAPI
from routes import router as sustainability_router
import logging

app = FastAPI(
    title="Sustainability Tracking Service",
    description="Tracks flight emissions and fuel efficiency metrics.",
    version="1.0.0"
)

app.include_router(sustainability_router, prefix="/api/v1/sustainability")

if __name__ == "__main__":
    import uvicorn
    try:
        logging.info("Starting Sustainability Tracking Service...")
        uvicorn.run("src.app:app", host="0.0.0.0", port=8020, reload=True)
    except Exception as e:
        logging.error("Failed to start Sustainability Service: %s", e)
