# Disruption Service Entry Point

from fastapi import FastAPI
from .routes import router as disruption_router

app = FastAPI(title="UCODTS Disruption Service")
app.include_router(disruption_router, prefix="/api/v1/disruption")

@app.get("/health")
async def health_check():
    return {"status": "Disruption service is operational"}
