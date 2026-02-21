from sqlalchemy import Column, String, Integer, Boolean
from app.db.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(String, primary_key=True, index=True)
    stage = Column(String)
    priority = Column(Integer)


class Instructor(Base):
    __tablename__ = "instructors"

    id = Column(String, primary_key=True, index=True)
    rating = Column(String)
    max_duty_hours = Column(Integer)


class Aircraft(Base):
    __tablename__ = "aircraft"

    id = Column(String, primary_key=True, index=True)
    type = Column(String)
    available = Column(Boolean)


class Simulator(Base):
    __tablename__ = "simulators"

    id = Column(String, primary_key=True, index=True)
    type = Column(String)
    max_sessions = Column(Integer)


class RulesDoc(Base):
    __tablename__ = "rules_docs"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    content = Column(String)


class TimeSlot(Base):
    __tablename__ = "time_slots"

    id = Column(String, primary_key=True, index=True)
    start = Column(String)
    end = Column(String)


class IngestionRun(Base):
    __tablename__ = "ingestion_runs"

    id = Column(String, primary_key=True, index=True)
    status = Column(String)