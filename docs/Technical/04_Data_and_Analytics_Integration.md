## Data and Analytics Integration

### Overview
This document outlines the data integration strategy for UCODTS, ensuring high data quality, real-time analytics, and continuous improvement of machine learning models. It details our ETL pipelines, data storage architecture, and schema design, including the necessary data model and database diagrams.

### Data Sources and ETL Pipelines
- **Data Sources:**  
  - **Real-Time Feeds:** IoT sensors from aircraft, crew check-in systems, and external APIs (flight status, weather, geopolitical events).
  - **Historical Data:** Past crew schedules, maintenance logs, and safety incident reports.
- **ETL Process:**  
  - **Extract:** Automated extraction of data from all sources.
  - **Transform:** Data cleaning, normalization, and validation using Python scripts.
  - **Load:**  
    - Processed data is loaded into PostgreSQL for transactional needs.
    - Redis is used for caching dynamic data.
    - A data lake (or NoSQL database) stores large volumes of historical data for analytics.
- **Risk Mitigation:**  
  - Automated anomaly detection ensures data consistency.
  - Redundant data sources and caching prevent data loss during peak times.

### Data Model and Schema
- **ERD Diagrams:**  
  - **Crew:** Stores crew profiles, schedules, and fatigue scores.
  - **Flight:** Contains flight details, schedules, statuses, and delay reasons.
  - **Maintenance:** Records maintenance events, statuses, and descriptions.
  - **Safety:** Logs safety incidents, including timestamps and resolutions.
  - **Disruption:** Captures external disruption events and their operational impacts.
- **Schema Documentation:**  
  - Detailed descriptions of tables, fields, primary/foreign keys, and indexing strategies are maintained in our database schema files.
  - ERD diagrams visually represent relationships among key entities.
- **ML Model Specifics:**  
  - Documentation of data requirements for training models (e.g., crew fatigue prediction, predictive maintenance).
- **Continuous Improvement:**  
  - Scheduled updates and retraining pipelines ensure that our ML models remain accurate over time.
  - Continuous monitoring of data quality and pipeline performance, with automated alerts to address issues promptly.


```mermaid
erDiagram
    CREW {
      int crewId PK "Unique crew member ID"
      string name "Crew member name"
      string role "Role (e.g., Pilot, Attendant)"
      float fatigueScore "Calculated fatigue risk score"
      date lastScheduled "Date of last scheduling update"
    }
    
    FLIGHT {
      int flightId PK "Unique flight ID"
      string flightNumber "Flight number"
      string departure "Departure airport code"
      string arrival "Arrival airport code"
      datetime scheduledDeparture "Planned departure time"
      datetime scheduledArrival "Planned arrival time"
      string status "Current flight status"
    }
    
    MAINTENANCE {
      int maintenanceId PK "Unique maintenance event ID"
      int flightId FK "Associated flight ID"
      string equipment "Equipment/component details"
      date maintenanceDate "Scheduled/Performed maintenance date"
      string status "Maintenance status (Pending, Completed)"
      string description "Maintenance details"
    }
    
    SAFETY {
      int incidentId PK "Unique incident ID"
      int flightId FK "Associated flight ID"
      string incidentType "Type of incident (e.g., system failure)"
      string severity "Severity (Low, Medium, High)"
      datetime incidentTime "Timestamp of incident"
      string resolution "Resolution details"
    }
    
    DISRUPTION {
      int disruptionId PK "Unique disruption event ID"
      int flightId FK "Affected flight ID"
      string type "Type of disruption (Weather, Geopolitical)"
      string description "Detailed description of disruption"
      datetime detectedTime "Time when disruption was detected"
    }

    %% Relationships
    CREW ||--o{ FLIGHT : "assigned to"
    FLIGHT ||--o{ MAINTENANCE : "requires"
    FLIGHT ||--o{ SAFETY : "generates"
    FLIGHT ||--o{ DISRUPTION : "affected by"
```
### Schema Documentation
- **Tables and Fields:**
  - Detailed descriptions of each table including primary and foreign keys, data types, and indexing strategies are documented separately in our database schema files. However, its high-level design there can be many more tables and mappings
- **ML Model Specifics:**
  - Data requirements for training models (e.g., crew fatigue prediction, predictive maintenance) are documented, including necessary features, normalization processes, and expected data formats.

### Analytics Integration
- **Data Pipeline Integration:**  
  - Seamless integration between ETL processes and analytical dashboards.
- **Real-Time Analytics:**  
  - Dashboards (React-based) connected to Redis and PostgreSQL visualize key operational KPIs.
- **Reporting:**  
  - Regular analytics reports monitor performance metrics and trigger model retraining as needed.

### Summary
This document guarantees a robust, scalable, and continuously improving data integration framework for UCODTS, ensuring that our analytics are accurate, actionable, and essential for proactive decision-making.
