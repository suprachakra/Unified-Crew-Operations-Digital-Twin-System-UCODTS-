# service.py - Crew Service Entry Point

from fastapi import FastAPI
from .routes import router as crew_router

app = FastAPI(title="UCODTS Crew Service")
app.include_router(crew_router, prefix="/api/v1/crew")

@app.get("/health")
async def health_check():
    return {"status": "Crew service is operational"}
