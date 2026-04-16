CREATE TABLE canvas_enrollments (
    student_id INT,
    student_name TEXT,
    student_email TEXT,
    course_id INT,
    course_name TEXT,
    section_name TEXT,
    teacher_name TEXT,
    teacher_email TEXT,
    enrollment_state TEXT,
    observer_name TEXT,
    observer_email TEXT,
    cohort_code TEXT
);

CREATE TABLE canvas_submissions (
    submission_id INT,
    student_id INT,
    course_id INT,
    assignment_name TEXT,
    assignment_type TEXT,
    assignment_group TEXT,
    due_at TIMESTAMP,
    submitted_at TIMESTAMP,
    score NUMERIC,
    grade TEXT,
    term_grade TEXT,
    engagement_rating TEXT,
    teacher_comment TEXT,
    missing BOOLEAN,
    late BOOLEAN
);

CREATE TABLE openapply_students (
    oa_student_id INT,
    student_name TEXT,
    student_email TEXT,
    school_name TEXT,
    school_id INT,
    programme TEXT,
    enrollment_year INT,
    country TEXT,
    status TEXT
);

CREATE TABLE openapply_guardians (
    guardian_id INT,
    oa_student_id INT,
    guardian_name TEXT,
    guardian_email TEXT,
    guardian_role TEXT
);
