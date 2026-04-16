from faker import Faker
import pandas as pd
import random

fake = Faker("en_GB")

courses = [
    (201, "Business Management HL"),
    (202, "Psychology SL"),
    (203, "Economics HL"),
    (204, "Digital Society SL")
]

teachers = [
    ("Adam Yusuf", "adam.yusuf@school.org"),
    ("Sarah Khan", "sarah.khan@school.org"),
    ("James Lee", "james.lee@school.org")
]

cohorts = ["M2027", "N2027"]

rows = []

for student_id in range(1, 101):
    student_email = f"student{student_id}@example-school.org"
    student_name = fake.name()

    # each student does 2–3 courses
    student_courses = random.sample(courses, k=random.choice([2, 3]))

    for course_id, course_name in student_courses:
        teacher_name, teacher_email = random.choice(teachers)

        rows.append({
            "student_id": student_id,
            "student_name": student_name,
            "student_email": student_email,
            "course_id": course_id,
            "course_name": course_name,
            "section_name": f"Class 1 - {teacher_name}",
            "teacher_name": teacher_name,
            "teacher_email": teacher_email,
            "enrollment_state": "active",
            "observer_name": fake.name(),
            "observer_email": fake.email(),
            "cohort_code": random.choice(cohorts)
        })

df = pd.DataFrame(rows)
df.to_csv("data/raw/canvas_enrollments_fake.csv", index=False)

print("Fake Canvas enrollments created.")
