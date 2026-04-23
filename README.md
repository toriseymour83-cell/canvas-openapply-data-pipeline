# Canvas + OpenApply Data Pipeline

## Overview
I built this project to practise combining data from two separate systems into one usable dataset for reporting and analysis.

It uses fake data based on the kind of records you might get from:
- Canvas, for course and submission data
- OpenApply, for student and school data

The aim was to recreate a realistic workflow where data from different platforms needs to be cleaned, matched, stored in PostgreSQL, and then queried in SQL.

## Tools
- Python for generating fake source data
- PostgreSQL for storing the data
- SQL for querying and analysis

## Data model
The project includes four tables:
- `canvas_enrollments`
- `canvas_submissions`
- `openapply_students`
- `openapply_guardians`

The main join key across systems is `student_email`.

## Example analysis

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


### 2. Schools with the most missing submissions
``` sql
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

### 3. Courses with the most late submissions
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


Full queries are available in:

sql/analysis_queries.sql
Notes

All data in this project is fake and generated for practice purposes only.

I used fake data because the real version of this kind of work would contain sensitive student information.

How to run
1. Install the required packages

python -m pip install -r requirements.txt

2. Generate the fake data
python src/generate_fake_students.py
python src/generate_canvas_enrollments.py
python src/generate_canvas_submissions.py
python src/generate_openapply_guardians.py
3. Create the PostgreSQL tables

Run:

sql/01_create_tables.sql
4. Import the CSV files

Import the generated CSV files from data/raw/ into the matching PostgreSQL tables.

5. Run the analysis queries

Run:

sql/analysis_queries.sql
