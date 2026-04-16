-- 1. Students with low engagement or poor grades
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


-- 2. Schools with most missing submissions
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


-- 3. Courses with most late submissions
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
