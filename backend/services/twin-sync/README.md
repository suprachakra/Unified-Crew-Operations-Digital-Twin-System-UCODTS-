## Digital Twin Synchronization Service

This service synchronizes data between physical operations and the digital twin, and supports simulation.
 
### Endpoints
- **POST /api/v1/twin-sync/update_physical**: Update digital twin with physical sensor data.
- **POST /api/v1/twin-sync/update_digital**: Send commands to physical assets.
- **GET /api/v1/twin-sync/simulate**: Run system simulations.

### Running the Service
1. `pip install -r requirements.txt`
2. `uvicorn src.app:app --reload`
