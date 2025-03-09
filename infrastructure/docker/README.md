## Docker Configuration

### Overview
This directory contains Dockerfiles and related documentation for building container images for UCODTS backend and supporting services.

### Files
- **Dockerfile.generic**: A generic Dockerfile template that can be customized for individual services.
- **(Additional Dockerfiles)**: Place additional service-specific Dockerfiles here.

### Usage
- Customize the `Dockerfile.generic` as needed.
- Use the provided Dockerfiles in your CI/CD pipeline to build images.
- For local testing, refer to the root `docker-compose.yml` in the backend folder.
