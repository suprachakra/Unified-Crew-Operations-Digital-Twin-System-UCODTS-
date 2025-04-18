## Real-Time Data Sync Service

This service integrates real-time data from aircraft, weather, and airport sources.
It publishes events to Kafka and provides WebSocket updates for real-time clients.

### Endpoints
- **GET /sync**: Returns the latest synchronized data.

### How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the service: `uvicorn src.app:app --reload`
3. To run the WebSocket server, ensure port 8765 is exposed.
