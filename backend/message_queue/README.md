## Message Queue Configuration

### Overview
This directory contains configurations for the Kafka message queue, which is used for asynchronous communication between UCODTS backend services.

### Files
- **kafka_setup.yml**: Contains Kafka and Zookeeper configuration details.

### Setup Instructions
1. Ensure Docker and Docker Compose are installed.
2. From the `backend/message_queue/` directory, run:
   ```bash
   docker-compose -f kafka_setup.yml up -d
