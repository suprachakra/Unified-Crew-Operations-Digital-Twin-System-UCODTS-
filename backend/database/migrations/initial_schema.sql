CREATE TABLE crew (
    crew_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(50),
    fatigue_score NUMERIC(5,2),
    last_scheduled DATE
);

CREATE TABLE flight (
    flight_id SERIAL PRIMARY KEY,
    flight_number VARCHAR(10) NOT NULL,
    departure VARCHAR(5),
    arrival VARCHAR(5),
    scheduled_departure TIMESTAMP,
    scheduled_arrival TIMESTAMP,
    status VARCHAR(20),
    delay_reason VARCHAR(255)
);

CREATE TABLE maintenance (
    maintenance_id SERIAL PRIMARY KEY,
    flight_id INT REFERENCES flight(flight_id),
    equipment VARCHAR(100),
    maintenance_date DATE,
    status VARCHAR(20),
    description TEXT
);

CREATE TABLE safety (
    incident_id SERIAL PRIMARY KEY,
    flight_id INT REFERENCES flight(flight_id),
    incident_type VARCHAR(50),
    severity VARCHAR(10),
    incident_time TIMESTAMP,
    resolution TEXT
);

CREATE TABLE disruption (
    disruption_id SERIAL PRIMARY KEY,
    flight_id INT REFERENCES flight(flight_id),
    type VARCHAR(50),
    description TEXT,
    detected_time TIMESTAMP
);
