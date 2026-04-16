from faker import Faker
import pandas as pd
import random

fake = Faker("en_GB")

schools = [
    ("Riverside International School", 101, "IB Diploma", "UK"),
    ("Westbridge Academy", 102, "IB Diploma", "UAE"),
    ("Oakwood College", 103, "IB Diploma", "Spain"),
    ("Northgate School", 104, "IB Diploma", "USA"),
    ("Greenfields International", 105, "IB Diploma", "Singapore")
]

students = []

for i in range(1, 101):
    name = fake.name()
    school_name, school_id, programme, country = random.choice(schools)

    students.append({
        "oa_student_id": i,
        "student_name": name,
        "student_email": f"student{i}@example-school.org",
        "school_name": school_name,
        "school_id": school_id,
        "programme": programme,
        "enrollment_year": random.choice([2025, 2026]),
        "country": country,
        "status": random.choice(["active", "active", "active", "withdrawn"])
    })

df = pd.DataFrame(students)
df.to_csv("data/raw/openapply_students_fake.csv", index=False)

print("Fake OpenApply students dataset created.")
