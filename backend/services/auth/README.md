## Auth Service

### Overview
The Auth Service handles user authentication and authorization using JWT and OAuth standards. It provides endpoints for user login and service health checks.

### Key Endpoints
- **POST /api/v1/auth/login:** Authenticates a user and returns a JWT token.
- **GET /api/v1/auth/health:** Returns the health status of the Auth Service.

### Setup Instructions
1. Navigate to the `services/auth` directory.
2. Build the Docker image:
   ```bash
   docker build -t ucodts-auth .
