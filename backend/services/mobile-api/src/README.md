## Mobile API Service

This service provides endpoints optimized for mobile clients:
- **GET /api/v1/mobile/offline_sync**: Retrieve offline data.
- **POST /api/v1/mobile/push_notification**: Send push notifications.

### How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `uvicorn src.app:app --reload`
