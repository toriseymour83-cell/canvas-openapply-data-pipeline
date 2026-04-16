# Canvas + OpenApply Data Pipeline

## Overview
This project demonstrates a simple end-to-end data pipeline using Python and PostgreSQL.

It uses realistic fake data based on:
- Canvas (course and submission data)
- OpenApply (student and school data)

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
