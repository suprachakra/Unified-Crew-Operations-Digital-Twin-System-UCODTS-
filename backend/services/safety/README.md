## Safety Service

### Overview
The Safety Service monitors safety incidents and manages incident reporting for regulatory compliance. It logs incidents and provides real-time status updates.

### Endpoints
- **GET /api/v1/safety/list**: Retrieves safety incident records with details and resolutions.

### Setup Instructions
1. Navigate to `backend/services/safety/`.
2. Build the Docker image:
   ```bash
   docker build -t ucodts-safety .
3. Run the container:
```
docker run -p 8005:8000 ucodts-safety
