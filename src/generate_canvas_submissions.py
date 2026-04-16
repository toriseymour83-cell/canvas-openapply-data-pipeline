import pandas as pd
import random
from datetime import datetime, timedelta

enrollments = pd.read_csv("data/raw/canvas_enrollments_fake.csv")

assignment_templates = [
    ("Engagement Rating 1", "engagement", "Engagement Ratings"),
    ("Term Grade 1", "term_grade", "Term Grades"),
    ("Semester 1 Report", "report", "Reports")
]

rows = []
submission_id = 1

for _, row in enrollments.iterrows():
    for assignment_name, assignment_type, assignment_group in assignment_templates:
        due_at = datetime(2026, 3, 1) + timedelta(days=random.randint(0, 30))

        submitted = random.choice([True, True, True, False])
        late = False
        submitted_at = None

        if submitted:
            submitted_at = due_at + timedelta(days=random.randint(-2, 3))
            late = submitted_at > due_at

        engagement_rating = random.choice(["E", "IE", "NE"]) if assignment_type == "engagement" else None
        term_grade = random.choice(["A", "B", "C", "D", "E"]) if assignment_type == "term_grade" else None
        score = random.randint(50, 100) if submitted else None
        grade = term_grade if term_grade else None

        teacher_comment = None
        if engagement_rating in ["IE", "NE"] or term_grade in ["D", "E"]:
            teacher_comment = random.choice([
                "Student needs closer monitoring.",
                "Late submissions are affecting progress.",
                "More consistent engagement needed.",
                "Cause for concern based on recent performance."
            ])

        rows.append({
            "submission_id": submission_id,
            "student_id": row["student_id"],
            "course_id": row["course_id"],
            "assignment_name": assignment_name,
            "assignment_type": assignment_type,
            "assignment_group": assignment_group,
            "due_at": due_at,
            "submitted_at": submitted_at,
            "score": score,
            "grade": grade,
            "term_grade": term_grade,
            "engagement_rating": engagement_rating,
            "teacher_comment": teacher_comment,
            "missing": not submitted,
            "late": late
        })

        submission_id += 1

df = pd.DataFrame(rows)
df.to_csv("data/raw/canvas_submissions_fake.csv", index=False)

print("Fake Canvas submissions created.")
