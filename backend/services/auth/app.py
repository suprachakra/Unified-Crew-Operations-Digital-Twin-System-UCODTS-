# app.py - Auth Service Entry Point

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt, time
from .config import SECRET_KEY, ALGORITHM

app = FastAPI(title="UCODTS Auth Service")

# Dummy user store (in production, use a secure database and hashed passwords)
users_db = {
    "user@example.com": {
        "username": "user@example.com",
        "password": "securePassword"
    }
}

class AuthRequest(BaseModel):
    username: str
    password: str

class AuthResponse(BaseModel):
    token: str

@app.post("/api/v1/auth/login", response_model=AuthResponse)
async def login(auth_request: AuthRequest):
    user = users_db.get(auth_request.username)
    if not user or user["password"] != auth_request.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    payload = {
        "sub": auth_request.username,
        "iat": int(time.time()),
        "exp": int(time.time()) + 3600  # Token valid for 1 hour
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"token": token}

@app.get("/api/v1/auth/health")
async def health_check():
    return {"status": "Auth service is operational"}
