## Sustainability Tracking Service

This service calculates and tracks flight emissions and fuel efficiency metrics.

### Endpoints
- **POST /api/v1/sustainability/calculate**: Calculate emissions for a flight.
- **GET /api/v1/sustainability/summary**: Retrieve aggregated sustainability metrics.

### Running Instructions
1. Install dependencies: `pip install -r requirements.txt`
2. Run with: `uvicorn src.app:app --reload`
3. Docker: `docker build -t sustainability-service .` then `docker run -p 8020:8020 sustainability-service`
