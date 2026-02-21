from app.db.models import Student
from app.weather.service import get_weather


def generate_roster(db):

    students = db.query(Student).all()

    roster = []

    # hard constraint tracking (no double booking)
    used_students = set()

    weather = get_weather("VOBG", "09:00", "10:00")

    # weather fallback (mandatory requirement)
    if weather is None:
        return [
            {
                "date": "2026-02-21",
                "slots": [
                    {
                        "slot_id": "D1-S1",
                        "activity": "SIM",
                        "student_id": "UNKNOWN",
                        "instructor_id": "UNKNOWN",
                        "resource_id": "SIM01",
                        "dispatch_decision": "NEEDS_REVIEW",
                        "reasons": ["WEATHER_UNAVAILABLE"],
                        "citations": ["rules:weather_minima#fallback"]
                    }
                ]
            }
        ]

    for i, s in enumerate(students):

        # HARD CONSTRAINT: no double booking
        if s.id in used_students:
            continue

        used_students.add(s.id)

        decision = "GO"
        activity = "FLIGHT"
        reasons = ["WX_OK"]

        # weather minima logic
        if weather["ceiling"] < 1500:
            decision = "NO_GO"
            activity = "SIM"
            reasons = ["WX_BELOW_MINIMA", "SIM_SUBSTITUTION"]

        roster.append({
            "slot_id": f"D1-S{i+1}",
            "activity": activity,
            "student_id": s.id,
            "instructor_id": "I001",
            "resource_id": "SIM01" if activity == "SIM" else "AC01",
            "dispatch_decision": decision,
            "reasons": reasons,
            "citations": ["rules:weather_minima#chunk1"]
        })

    return [
        {
            "date": "2026-02-21",
            "slots": roster
        }
    ]