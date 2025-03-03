## Backend System for UCODTS

### Overview
This directory contains the backend microservices for the Unified Crew & Operations Digital Twin System (UCODTS). The backend is divided into multiple services, each handling a distinct operational domain such as authentication, crew scheduling, flight tracking, predictive maintenance, safety, and disruption management. Shared utilities and configurations are maintained in the `common` folder, and the database and message queue configurations are provided separately.

### Structure
- **services/**: Contains all microservices (auth, crew, flight, maintenance, safety, disruption, common).
- **database/**: Contains migration scripts, ORM models, and documentation for database setup.
- **message_queue/**: Contains Kafka configuration and documentation.
- **docker-compose.yml**: Used for local integration testing of backend services.
