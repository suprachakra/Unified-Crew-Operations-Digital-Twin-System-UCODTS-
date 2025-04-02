# Centralized ORM Models using SQLAlchemy

from sqlalchemy import Column, Integer, String, Date, DateTime, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Crew(Base):
    __tablename__ = 'crew'
    crew_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    role = Column(String(50))
    fatigue_score = Column(Numeric(5,2))
    last_scheduled = Column(Date)

class Flight(Base):
    __tablename__ = 'flight'
    flight_id = Column(Integer, primary_key=True)
    flight_number = Column(String(10), nullable=False)
    departure = Column(String(5))
    arrival = Column(String(5))
    scheduled_departure = Column(DateTime)
    scheduled_arrival = Column(DateTime)
    status = Column(String(20))
    delay_reason = Column(String(255))

class Maintenance(Base):
    __tablename__ = 'maintenance'
    maintenance_id = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey('flight.flight_id'))
    equipment = Column(String(100))
    maintenance_date = Column(Date)
    status = Column(String(20))
    description = Column(String)

class Safety(Base):
    __tablename__ = 'safety'
    incident_id = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey('flight.flight_id'))
    incident_type = Column(String(50))
    severity = Column(String(10))
    incident_time = Column(DateTime)
    resolution = Column(String)

class Disruption(Base):
    __tablename__ = 'disruption'
    disruption_id = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey('flight.flight_id'))
    type = Column(String(50))
    description = Column(String)
    detected_time = Column(DateTime)
