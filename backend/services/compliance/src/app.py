"""
Regulatory Compliance Service – Entry point.
This service exposes endpoints to validate crew schedules according to multi‐regional regulations.
"""

from fastapi import FastAPI
from routes import router as compliance_router
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s [%(module)s] %(message)s")

app = FastAPI(
    title="Regulatory Compliance Service",
    description="Service for multi-region regulatory compliance checks (FTL, rest requirements, etc.)",
    version="1.0.0"
)

app.include_router(compliance_router, prefix="/api/v1/compliance")

if __name__ == "__main__":
    import uvicorn
    try:
        logging.info("Starting Regulatory Compliance Service...")
        uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
    except Exception as e:
        logging.error("Error in starting the service: %s", e)