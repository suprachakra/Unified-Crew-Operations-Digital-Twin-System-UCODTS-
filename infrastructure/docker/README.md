## Docker Configuration

### Overview
This directory contains Dockerfiles and related documentation for building container images for UCODTS backend and supporting services.

### Files
- **Dockerfile.generic**: A generic Dockerfile template that can be customized for individual services.Builds a production-ready image using Python 3.9-slim, installs dependencies from `requirements.txt`, copies the application code, and sets the default command.

- **(Additional Dockerfiles)**: Place additional service-specific Dockerfiles here.

### Usage
- Customize the `Dockerfile.generic` as needed.
- Use the provided Dockerfiles in your CI/CD pipeline to build images.
     ```bash
   docker build -f Dockerfile.generic -t ucodts:latest .
- For local testing, refer to the root `docker-compose.yml` in the backend folder.
