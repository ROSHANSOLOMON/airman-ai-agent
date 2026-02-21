from fastapi import APIRouter, Depends
from app.scheduler.roster import generate_roster
from sqlalchemy.orm import Session
import json

from app.db.database import get_db
from app.db.models import Student

router = APIRouter()


@router.post("/ingest/run")
def run_ingestion(db: Session = Depends(get_db)):

    with open("data/students.json", "r") as f:
        students = json.load(f)

    inserted = 0
    skipped = 0

    for s in students:

        existing = db.query(Student).filter(
            Student.id == s["id"]
        ).first()

        if existing:
            skipped += 1
            continue

        student = Student(
            id=s["id"],
            stage=s["stage"],
            priority=s["priority"]
        )

        db.add(student)
        inserted += 1

    db.commit()

    return {
        "inserted": inserted,
        "skipped": skipped
    }

@router.post("/roster/generate")
def roster_generate(db: Session = Depends(get_db)):

    roster = generate_roster(db)

    return {
    "week_start": "2026-02-21",
    "base_icao": "VOBG",
    "roster": roster,
    "unassigned": [],
    "decision_summary": {
        "strategy": "weather-first safety dispatch",
        "primary_constraints": [
            "weather minima",
            "no double booking"
        ]
    }
}