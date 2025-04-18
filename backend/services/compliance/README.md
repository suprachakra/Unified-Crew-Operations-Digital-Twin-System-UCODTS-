# Regulatory Compliance Service

This microservice validates crew schedules against multi-region regulatory requirements.
It applies flight time limitations, rest period checks, and custom business rules.

## Endpoints
- **POST /api/v1/compliance/validate**: Validate a crew schedule.

## Running Locally
1. Install dependencies: `pip install -r requirements.txt`
2. Start the service: `uvicorn src.app:app --reload`
3. Alternatively, build the Docker image:
