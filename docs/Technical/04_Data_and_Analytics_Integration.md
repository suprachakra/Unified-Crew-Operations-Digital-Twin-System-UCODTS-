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
    %% Core Entities
    AIRLINE {
      int airline_id PK "Primary Key"
      string name "Airline Name"
      string code "IATA Code"
      string region "Region"
    }
    
    AIRCRAFT {
      int aircraft_id PK "Primary Key"
      int airline_id FK "Foreign Key: AIRLINE.airline_id"
      string tail_number "Tail Number"
      string model "Aircraft Model"
      string manufacturer "Manufacturer"
      int capacity "Capacity"
      string service_status "Operational Status"
    }
    
    CREW {
      int crew_id PK "Primary Key"
      int airline_id FK "Foreign Key: AIRLINE.airline_id"
      string name "Crew Member Name"
      string role "Role (Pilot, Attendant, etc.)"
      float fatigue_score "Latest Fatigue Score"
      date last_scheduled "Last Scheduled Date"
    }
    
    FLIGHT {
      int flight_id PK "Primary Key"
      int airline_id FK "Foreign Key: AIRLINE.airline_id"
      int aircraft_id FK "Foreign Key: AIRCRAFT.aircraft_id"
      string flight_number "Flight Number"
      string departure "Departure Airport"
      string arrival "Arrival Airport"
      datetime scheduled_departure "Scheduled Departure Time"
      datetime scheduled_arrival "Scheduled Arrival Time"
      string status "Flight Status"
      string delay_reason "Delay Reason (if any)"
    }
    
    %% Linking Entities
    CREW_ASSIGNMENT {
      int assignment_id PK "Primary Key"
      int crew_id FK "Foreign Key: CREW.crew_id"
      int flight_id FK "Foreign Key: FLIGHT.flight_id"
      date assignment_date "Assignment Date"
      string duty_status "Duty Status"
    }
    
    %% Operational Event Entities
    MAINTENANCE {
      int maintenance_id PK "Primary Key"
      int flight_id FK "Foreign Key: FLIGHT.flight_id"
      string equipment "Equipment Under Maintenance"
      date maintenance_date "Maintenance Date"
      string status "Maintenance Status"
      string description "Maintenance Description"
      float cost "Cost"
    }
    
    SAFETY {
      int safety_id PK "Primary Key"
      int flight_id FK "Foreign Key: FLIGHT.flight_id"
      string incident_type "Incident Type"
      string severity "Incident Severity"
      datetime incident_time "Incident Timestamp"
      string resolution "Resolution Details"
    }
    
    DISRUPTION {
      int disruption_id PK "Primary Key"
      int flight_id FK "Foreign Key: FLIGHT.flight_id"
      string type "Disruption Type"
      string description "Disruption Description"
      datetime detected_time "Time Detected"
    }
    
    %% User and Feedback Entities
    USER {
      int user_id PK "Primary Key"
      string username "Username"
      string email "User Email"
      string password_hash "Password Hash"
      string role "User Role (Admin, Manager, etc.)"
    }
    
    FEEDBACK {
      int feedback_id PK "Primary Key"
      int user_id FK "Foreign Key: USER.user_id"
      int flight_id FK "Optional: Foreign Key: FLIGHT.flight_id"
      string category "Feedback Category"
      string comments "Detailed Comments"
      datetime feedback_date "Feedback Date"
      int rating "Rating (1-5)"
      string follow_up_status "Follow-Up Status"
    }
    
    %% Audit and Change Entities
    AUDIT_LOG {
      int audit_id PK "Primary Key"
      string table_name "Affected Table"
      int record_id "Record ID"
      string change_type "Change Type (INSERT, UPDATE, DELETE)"
      string changed_by "Changed By"
      datetime change_time "Timestamp of Change"
      string old_value "Previous Value"
      string new_value "New Value"
    }
    
    CHANGE_REQUEST {
      int change_id PK "Primary Key"
      string title "Change Title"
      string description "Change Description"
      int requested_by FK "Foreign Key: USER.user_id"
      datetime submitted_at "Submission Timestamp"
      string status "Current Status"
      string impact_analysis "Impact Analysis"
      string priority "Priority Level"
    }
    
    %% Performance and Scheduling Entities
    PERFORMANCE_METRIC {
      int metric_id PK "Primary Key"
      string entity "Entity Name"
      string metric_name "Metric Name"
      float value "Metric Value"
      datetime recorded_at "Recorded At"
      string unit "Measurement Unit"
      float target_value "Target Value"
    }
    
    SCHEDULING_EVENT {
      int event_id PK "Primary Key"
      int crew_id FK "Foreign Key: CREW.crew_id"
      int flight_id FK "Foreign Key: FLIGHT.flight_id"
      string event_type "Type of Scheduling Event"
      datetime event_timestamp "Timestamp"
      string description "Event Description"
      string impact "Impact of Event"
    }
    
    %% Additional Utility Entities
    ALERT {
      int alert_id PK "Primary Key"
      string entity_type "Entity Type"
      int entity_id "Entity ID"
      string alert_type "Type of Alert"
      string severity "Alert Severity"
      datetime generated_at "Timestamp"
      string status "Alert Status"
      string description "Alert Description"
    }
    
    USER_ROLE {
      int role_id PK "Primary Key"
      string role_name "Role Name"
      string description "Role Description"
    }
    
    %% Relationships
    AIRLINE ||--o{ CREW : employs
    AIRLINE ||--o{ FLIGHT : operates
    AIRLINE ||--o{ AIRCRAFT : owns
    AIRCRAFT ||--o{ FLIGHT : "assigned to"
    CREW ||--o{ CREW_ASSIGNMENT : "assigned in"
    FLIGHT ||--o{ CREW_ASSIGNMENT : "receives assignment"
    FLIGHT ||--o{ MAINTENANCE : "undergoes"
    FLIGHT ||--o{ SAFETY : "records incident"
    FLIGHT ||--o{ DISRUPTION : "experiences"
    USER ||--o{ FEEDBACK : "provides"
    FLIGHT ||--o{ FEEDBACK : "receives feedback"
    USER ||--o{ CHANGE_REQUEST : "initiates"
    USER_ROLE ||--o{ USER : defines
    FLIGHT ||--o{ PERFORMANCE_METRIC : "measures"
    CREW ||--o{ SCHEDULING_EVENT : "triggers"
    FLIGHT ||--o{ SCHEDULING_EVENT : "records event"
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
