CREATE TABLE IF NOT EXISTS openapply_students (
    oa_student_id INT PRIMARY KEY,
    student_name TEXT NOT NULL,
    student_email TEXT NOT NULL UNIQUE,
    school_name TEXT NOT NULL,
    school_id INT NOT NULL,
    programme TEXT NOT NULL,
    enrollment_year INT NOT NULL,
    country TEXT NOT NULL,
    status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS openapply_guardians (
    guardian_id INT PRIMARY KEY,
    oa_student_id INT NOT NULL,
    guardian_name TEXT NOT NULL,
    guardian_email TEXT NOT NULL,
    guardian_role TEXT NOT NULL,
    CONSTRAINT fk_openapply_guardians_student
        FOREIGN KEY (oa_student_id)
        REFERENCES openapply_students (oa_student_id)
);

CREATE TABLE IF NOT EXISTS canvas_enrollments (
    student_id INT NOT NULL,
    student_name TEXT NOT NULL,
    student_email TEXT NOT NULL,
    course_id INT NOT NULL,
    course_name TEXT NOT NULL,
    section_name TEXT NOT NULL,
    teacher_name TEXT NOT NULL,
    teacher_email TEXT NOT NULL,
    enrollment_state TEXT NOT NULL,
    observer_name TEXT,
    observer_email TEXT,
    cohort_code TEXT NOT NULL,
    CONSTRAINT pk_canvas_enrollments
        PRIMARY KEY (student_id, course_id)
);

CREATE TABLE IF NOT EXISTS canvas_submissions (
    submission_id INT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    assignment_name TEXT NOT NULL,
    assignment_type TEXT NOT NULL,
    assignment_group TEXT NOT NULL,
    due_at TIMESTAMP NOT NULL,
    submitted_at TIMESTAMP,
    score NUMERIC,
    grade TEXT,
    term_grade TEXT,
    engagement_rating TEXT,
    teacher_comment TEXT,
    missing BOOLEAN NOT NULL,
    late BOOLEAN NOT NULL,
    CONSTRAINT fk_canvas_submissions_enrollment
        FOREIGN KEY (student_id, course_id)
        REFERENCES canvas_enrollments (student_id, course_id)
);
