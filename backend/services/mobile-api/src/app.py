"""
Mobile API Service – Provides endpoints optimized for mobile clients.
"""

from fastapi import FastAPI
from routes import router as mobile_router
import logging

app = FastAPI(
    title="Mobile API Service",
    description="Optimized API for mobile endpoints including offline sync and push notifications.",
    version="1.0.0"
)

app.include_router(mobile_router, prefix="/api/v1/mobile")

if __name__ == "__main__":
    import uvicorn
    try:
        logging.info("Starting Mobile API Service...")
        uvicorn.run("app:app", host="0.0.0.0", port=8010, reload=True)
    except Exception as e:
        logging.error("Error launching Mobile API Service: %s", e)
