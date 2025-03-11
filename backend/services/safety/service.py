# Safety Service Entry Point

from fastapi import FastAPI
from .routes import router as safety_router

app = FastAPI(title="UCODTS Safety Service")
app.include_router(safety_router, prefix="/api/v1/safety")

@app.get("/health")
async def health_check():
    return {"status": "Safety service is operational"}
