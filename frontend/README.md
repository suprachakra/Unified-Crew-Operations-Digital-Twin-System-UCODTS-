## UCODTS Frontend

### Overview
This is the frontend application for the Unified Crew & Operations Digital Twin System (UCODTS). Built with Next.js and React, it provides a real-time dashboard for monitoring crew scheduling, flight operations, maintenance alerts, safety incidents, and disruptions.

### Features
- **Dashboard:** Centralized view of operational data.
- **Crew View:** Detailed component for crew scheduling and fatigue analytics.
- **Responsive Design:** Optimized for both desktop and mobile devices.
- **Integration:** Communicates with backend microservices via RESTful APIs.

### Setup Instructions
1. Install dependencies:
   ```bash
   npm install
   ```
2. Run the development server:
   ```bash
   npm run dev
   ```
3. Build for production:
   ```bash
   npm run build
   npm start
   ```

### Configuration
```env
### Environment configuration for UCODTS Frontend

### Base URL for backend API
API_BASE_URL=http://localhost:8000

### Any additional configuration variables can be added here.
```
