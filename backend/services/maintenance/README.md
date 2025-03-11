## Maintenance Service

### Overview
The Maintenance Service is responsible for predictive maintenance. It processes flight and sensor data to forecast maintenance requirements and generate alerts.

### Endpoints
- **GET /api/v1/maintenance/list**: Returns maintenance event records with status and descriptions.

### Setup Instructions
1. Navigate to `backend/services/maintenance/`.
2. Build the Docker image:
   ```bash
   docker build -t ucodts-maintenance .
3. Run the container:
``` docker run -p 8004:8000 ucodts-maintenance
