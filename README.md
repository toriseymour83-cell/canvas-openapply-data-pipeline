# Canvas + OpenApply Data Pipeline

## Overview
This project demonstrates a simple end-to-end data pipeline using Python and PostgreSQL.

It uses realistic fake data based on:
- Canvas (course + submission data)
- OpenApply (student + school data)

The goal is to show how data from different systems can be combined and analysed.

---

## Tools Used
- Python (data generation)
- PostgreSQL (data storage)
- SQL (analysis)

---

## Data Model
The project includes 4 tables:

- canvas_enrollments
- canvas_submissions
- openapply_students
- openapply_guardians

The main join key between systems is:
- student_email

---

## Example Analysis

### 1. Students with low engagement or poor grades

```sql
SELECT
    ce.student_name,
    ce.course_name,
    cs.engagement_rating,
    cs.term_grade,
    cs.teacher_comment
FROM canvas_submissions cs
JOIN canvas_enrollments ce
    ON cs.student_id = ce.student_id
   AND cs.course_id = ce.course_id
WHERE cs.engagement_rating IN ('IE', 'NE')
   OR cs.term_grade IN ('D', 'E');

---
```sql
2. Schools with most missing submissions
SELECT
    oa.school_name,
    COUNT(*) AS missing_submissions
FROM canvas_submissions cs
JOIN canvas_enrollments ce
    ON cs.student_id = ce.student_id
   AND cs.course_id = ce.course_id
JOIN openapply_students oa
    ON ce.student_email = oa.student_email
WHERE cs.missing = TRUE
GROUP BY oa.school_name
ORDER BY missing_submissions DESC;

---
```sql
3. Courses with most late submissions
SELECT
    ce.course_name,
    COUNT(*) AS total_submissions,
    SUM(CASE WHEN cs.late THEN 1 ELSE 0 END) AS late_submissions
FROM canvas_submissions cs
JOIN canvas_enrollments ce
    ON cs.student_id = ce.student_id
   AND cs.course_id = ce.course_id
GROUP BY ce.course_name
ORDER BY late_submissions DESC;
---
```
Notes

All data in this project is fake and generated for practice purposes only.
