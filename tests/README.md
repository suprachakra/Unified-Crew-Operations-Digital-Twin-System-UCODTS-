## Testing Strategy and Instructions

### Overview
This directory contains comprehensive test suites for the UCODTS project, covering backend, frontend, data pipelines, and security.

#### Subdirectories:
- **backend_tests/**: Unit and integration tests for backend services using pytest.
- **frontend_tests/**: End-to-end tests for the frontend (e.g., using Cypress).
- **data_tests/**: Tests for data processing, cleaning, and feature engineering using pytest.
- **security_tests/**: Automated security and penetration tests for API endpoints.

### Running Tests

#### Backend Tests:
From the project root, run:
```bash
pytest tests/backend_tests/
