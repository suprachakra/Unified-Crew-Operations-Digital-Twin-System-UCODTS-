#!/usr/bin/env python
"""
Digital Twin Sync Service – Entry point.
Enables bidirectional synchronization and simulation.
"""

from fastapi import FastAPI
from routes import router as twin_sync_router
import logging

app = FastAPI(
    title="Digital Twin Sync Service",
    description="Bidirectional synchronization between physical systems and the digital twin.",
    version="1.0.0"
)

app.include_router(twin_sync_router, prefix="/api/v1/twin-sync")

if __name__ == "__main__":
    import uvicorn
    try:
        logging.info("Starting Digital Twin Sync Service...")
        uvicorn.run("src.app:app", host="0.0.0.0", port=8030, reload=True)
    except Exception as e:
        logging.error("Error starting Digital Twin Sync Service: %s", e)
