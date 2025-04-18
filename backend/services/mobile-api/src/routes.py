"""
Mobile API Routes
Provides endpoints for offline synchronization and push notifications.
"""

from fastapi import APIRouter
from controllers import offline_sync, push_notification
import logging

router = APIRouter()

@router.get("/offline_sync")
async def offline_sync_data():
    try:
        result = offline_sync.sync_data()
        logging.info("Offline sync data fetched.")
        return result
    except Exception as e:
        logging.error("Error in offline sync: %s", e)
        return {"error": "Offline sync failed."}

@router.post("/push_notification")
async def send_push_notification(data: dict):
    try:
        result = push_notification.send_notification(data)
        logging.info("Push notification sent.")
        return result
    except Exception as e:
        logging.error("Error sending push notification: %s", e)
        return {"error": "Push notification failed."}
