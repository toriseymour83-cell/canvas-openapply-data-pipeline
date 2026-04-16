from faker import Faker
import pandas as pd

fake = Faker("en_GB")

students = []

for i in range(1, 101):
    name = fake.name()
    students.append({
        "student_id": i,
        "student_name": name,
        "student_email": f"student{i}@example-school.org"
    })

df = pd.DataFrame(students)

# save to raw data folder
df.to_csv("data/raw/openapply_students_fake.csv", index=False)

print("Fake students dataset created.")
