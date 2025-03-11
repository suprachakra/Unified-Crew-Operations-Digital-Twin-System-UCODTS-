## Disruption Service

### Overview
The Disruption Service monitors external factors such as weather and geopolitical events that may affect flight operations. It generates re-routing suggestions and alerts when disruptions are detected.

### Endpoints
- **GET /api/v1/disruption/list**: Retrieves a list of disruption events affecting flights.

### Setup Instructions
1. Navigate to `backend/services/disruption/`.
2. Build the Docker image:
   ```bash
   docker build -t ucodts-disruption
3. Run the container:
```
docker run -p 8006:8000 ucodts-disruption .
