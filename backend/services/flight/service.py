# Flight Service Entry Point

from fastapi import FastAPI
from .routes import router as flight_router

app = FastAPI(title="UCODTS Flight Service")
app.include_router(flight_router, prefix="/api/v1/flight")

@app.get("/health")
async def health_check():
    return {"status": "Flight service is operational"}
