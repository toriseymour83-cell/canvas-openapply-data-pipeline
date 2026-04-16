from faker import Faker
import pandas as pd
import random

fake = Faker("en_GB")

students = pd.read_csv("data/raw/openapply_students_fake.csv")

rows = []
guardian_id = 1

for _, row in students.iterrows():
    # 1–2 guardians per student
    for _ in range(random.choice([1, 2])):
        rows.append({
            "guardian_id": guardian_id,
            "oa_student_id": row["oa_student_id"],
            "guardian_name": fake.name(),
            "guardian_email": fake.email(),
            "guardian_role": random.choice(["Parent", "Guardian", "SBC"])
        })
        guardian_id += 1

df = pd.DataFrame(rows)
df.to_csv("data/raw/openapply_guardians_fake.csv", index=False)

print("Fake OpenApply guardians created.")
