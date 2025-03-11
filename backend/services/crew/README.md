## Crew Service

### Overview
The Crew Service manages crew scheduling and predicts fatigue levels. It exposes endpoints to fetch crew data and compute fatigue risk.

### Endpoints
- **GET /api/v1/crew/list**: Returns a list of crew members with their fatigue scores.

### Setup Instructions
1. Navigate to `backend/services/crew/`.
2. Build the Docker image:
   ```bash
   docker build -t ucodts-crew

3. Run the container
```
docker run -p 8002:8000 ucodts-crew
```
