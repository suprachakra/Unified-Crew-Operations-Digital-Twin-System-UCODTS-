# Maintenance Service Entry Point

from fastapi import FastAPI
from .routes import router as maintenance_router

app = FastAPI(title="UCODTS Maintenance Service")
app.include_router(maintenance_router, prefix="/api/v1/maintenance")

@app.get("/health")
async def health_check():
    return {"status": "Maintenance service is operational"}
