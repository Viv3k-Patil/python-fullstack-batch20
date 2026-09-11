-- sql queries to create table
CREATE TABLE students (
    student_id INT,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50)
);

-- add a new column
ALTER TABLE students ADD COLUMN email VARCHAR(50);
-- modify existing column
ALTER TABLE students ALTER COLUMN age TYPE SMALLINT;
-- rename column
ALTER TABLE students RENAME COLUMN city TO hometown;
-- drop column
ALTER TABLE students DROP COLUMN email;

SELECT * FROM students;


CREATE TABLE students (
    stud_id   VARCHAR(10) PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname  VARCHAR(50) NOT NULL,
    gender    VARCHAR(10),
    age       INTEGER,
    city      VARCHAR(50),
    email     VARCHAR(100) UNIQUE
);

CREATE TABLE courses (
    course_id   VARCHAR(10) PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    department  VARCHAR(100) NOT NULL,
    credits     INTEGER NOT NULL
);

CREATE TABLE colleges (
    college_id      VARCHAR(10) PRIMARY KEY,
    college_name    VARCHAR(100) NOT NULL,
    university      VARCHAR(100),
    department      VARCHAR(100),
    city            VARCHAR(50),
    established_year INTEGER,
    total_students  INTEGER,
    principal_name  VARCHAR(100),
    contact_email   VARCHAR(100)
);


INSERT INTO students
    (stud_id, firstname, lastname, gender, age, city, email)
VALUES
    ('STU001', 'Aarav',  'Sharma',    'Male',   19, 'Pune',      'aarav.sharma@example.com'),
    ('STU002', 'Ananya', 'Patil',     'Female', 20, 'Mumbai',    'ananya.patil@example.com'),
    ('STU003', 'Rohan',  'Deshmukh',  'Male',   21, 'Nashik',    'rohan.deshmukh@example.com'),
    ('STU004', 'Priya',  'Kulkarni',  'Female', 18, 'Pune',      'priya.kulkarni@example.com'),
    ('STU005', 'Aditya', 'Joshi',     'Male',   22, 'Nagpur',    'aditya.joshi@example.com'),
    ('STU006', 'Sneha',  'Mehata',    'Female', 20, 'Ahmedabad', 'sneha.mehta@example.com'),
    ('STU007', 'Vihaan', 'Singh',     'Male',   19, 'Delhi',     'vihaan.singh@example.com'),
    ('STU008', 'Isha',   'Verma',     'Female', 21, 'Bengaluru', 'isha.verma@example.com'),
    ('STU009', 'Kabir',  'Gupta',     'Male',   18, 'Jaipur',    'kabir.gupta@example.com'),
    ('STU010', 'Neha',   'Rao',       'Female', 22, 'Hyderabad', 'neha.rao@example.com');

INSERT INTO courses
    (course_id, course_name, department, credits)
VALUES
    ('C001', 'Introduction to Programming', 'Computer Science', 4),
    ('C002', 'Data Structures', 'Computer Science', 4),
    ('C003', 'Database Management Systems', 'Information Technology', 3),
    ('C004', 'Web Development', 'Information Technology', 3),
    ('C005', 'Operating Systems', 'Computer Science', 4),
    ('C006', 'Computer Networks', 'Computer Science', 3),
    ('C007', 'Software Engineering', 'Information Technology', 3),
    ('C008', 'Business Management', 'Management', 3),
    ('C009', 'Financial Accounting', 'Commerce', 4),
    ('C010', 'Business Statistics', 'Management', 3);

INSERT INTO colleges
    (college_id, college_name, university, department, city,
     established_year, total_students, principal_name, contact_email)
VALUES
    ('COL001', 'Modern College of Arts', 
     'Savitribai Phule Pune University', 'Arts', 'Pune',
     1970, 4500, 'Dr. Rajesh Kulkarni', 'contact@moderncollege.edu'),

    ('COL002', 'Pune Institute of Technology',
     'Savitribai Phule Pune University', 'Computer Science', 'Pune',
     1985, 6200, 'Dr. Anita Sharma', 'info@pit.edu'),

    ('COL003', 'Mumbai College of Commerce',
     'University of Mumbai', 'Commerce', 'Mumbai',
     1965, 5100, 'Dr. Meena Patil', NULL),

    ('COL004', 'Nashik Institute of Science',
     'Savitribai Phule Pune University', 'Science', 'Nashik',
     1978, NULL, 'Dr. Amit Joshi', 'admin@nis.edu'),

    ('COL005', 'Nagpur Business School',
     'Rashtrasant Tukadoji Maharaj Nagpur University', 'Management', 'Nagpur',
     1992, 3800, NULL, 'info@nbs.edu'),

    ('COL006', 'Ahmedabad Engineering College',
     'Gujarat University', 'Engineering', 'Ahmedabad',
     1980, 7200, 'Dr. Vikram Shah', NULL),

    ('COL007', 'Delhi Institute of Computer Studies',
     'University of Delhi', 'Computer Science', 'Delhi',
     2001, NULL, 'Dr. Neha Verma', 'contact@dics.edu'),

    ('COL008', 'Bengaluru College of Management',
     'Bangalore University', 'Management', 'Bengaluru',
     1995, 4600, NULL, NULL),

    ('COL009', 'Jaipur College of Arts and Science',
     'University of Rajasthan', NULL, 'Jaipur',
     1975, 4100, 'Dr. Suresh Gupta', 'info@jcas.edu'),

    ('COL010', 'Hyderabad Institute of Technology',
     NULL, 'Information Technology', 'Hyderabad',
     1988, 6800, 'Dr. Priya Rao', 'contact@hit.edu');


-- 1. read data from table
-- SELECT <column_names> FROM <table_name>;

SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM colleges;

-- 2. filter WHERE
-- SELECT <column names> FROM <table_name> WHERE <condition>
-- WHERE column <operator> value

SELECT * FROM students WHERE gender = 'Male' AND city = 'Pune';

-- 3. between
-- SELECT columns FROM table WHERE age BETWEEN val1 and val2;
SELECT * FROM students WHERE age BETWEEN 21 and 25;

-- 4. in
SELECT * FROM students WHERE city IN ('Nashik', 'Pune', 'Nagpur');

-- 5. LIKE pattern matching

SELECT * FROM courses WHERE department LIKE '%echnology%';
SELECT * FROM courses WHERE course_name LIKE '%neering%';

-- 6. handling null
SELECT * FROM colleges WHERE total_students IS NULL;
SELECT * FROM colleges WHERE total_students IS NOT NULL;

-- combine all
SELECT *
FROM colleges
WHERE
    university LIKE '%une%'
    AND department IN ('Arts', 'Engineering');





CREATE TABLE students (
    stud_id   VARCHAR(10) PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname  VARCHAR(50) NOT NULL,
    gender    VARCHAR(10),
    age       INTEGER,
    city      VARCHAR(50),
    email     VARCHAR(100) UNIQUE
);

CREATE TABLE courses (
    course_id   VARCHAR(10) PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    department  VARCHAR(100) NOT NULL,
    credits     INTEGER NOT NULL
);

CREATE TABLE colleges (
    college_id      VARCHAR(10) PRIMARY KEY,
    college_name    VARCHAR(100) NOT NULL,
    university      VARCHAR(100),
    department      VARCHAR(100),
    city            VARCHAR(50),
    established_year INTEGER,
    total_students  INTEGER,
    principal_name  VARCHAR(100),
    contact_email   VARCHAR(100)
);


INSERT INTO students
    (stud_id, firstname, lastname, gender, age, city, email)
VALUES
    ('STU001', 'Aarav',  'Sharma',    'Male',   19, 'Pune',      'aarav.sharma@example.com'),
    ('STU002', 'Ananya', 'Patil',     'Female', 20, 'Mumbai',    'ananya.patil@example.com'),
    ('STU003', 'Rohan',  'Deshmukh',  'Male',   21, 'Nashik',    'rohan.deshmukh@example.com'),
    ('STU004', 'Priya',  'Kulkarni',  'Female', 18, 'Pune',      'priya.kulkarni@example.com'),
    ('STU005', 'Aditya', 'Joshi',     'Male',   22, 'Nagpur',    'aditya.joshi@example.com'),
    ('STU006', 'Sneha',  'Mehata',    'Female', 20, 'Ahmedabad', 'sneha.mehta@example.com'),
    ('STU007', 'Vihaan', 'Singh',     'Male',   19, 'Delhi',     'vihaan.singh@example.com'),
    ('STU008', 'Isha',   'Verma',     'Female', 21, 'Bengaluru', 'isha.verma@example.com'),
    ('STU009', 'Kabir',  'Gupta',     'Male',   18, 'Jaipur',    'kabir.gupta@example.com'),
    ('STU010', 'Neha',   'Rao',       'Female', 22, 'Hyderabad', 'neha.rao@example.com');

INSERT INTO courses
    (course_id, course_name, department, credits)
VALUES
    ('C001', 'Introduction to Programming', 'Computer Science', 4),
    ('C002', 'Data Structures', 'Computer Science', 4),
    ('C003', 'Database Management Systems', 'Information Technology', 3),
    ('C004', 'Web Development', 'Information Technology', 3),
    ('C005', 'Operating Systems', 'Computer Science', 4),
    ('C006', 'Computer Networks', 'Computer Science', 3),
    ('C007', 'Software Engineering', 'Information Technology', 3),
    ('C008', 'Business Management', 'Management', 3),
    ('C009', 'Financial Accounting', 'Commerce', 4),
    ('C010', 'Business Statistics', 'Management', 3);

INSERT INTO colleges
    (college_id, college_name, university, department, city,
     established_year, total_students, principal_name, contact_email)
VALUES
    ('COL001', 'Modern College of Arts', 
     'Savitribai Phule Pune University', 'Arts', 'Pune',
     1970, 4500, 'Dr. Rajesh Kulkarni', 'contact@moderncollege.edu'),

    ('COL002', 'Pune Institute of Technology',
     'Savitribai Phule Pune University', 'Computer Science', 'Pune',
     1985, 6200, 'Dr. Anita Sharma', 'info@pit.edu'),

    ('COL003', 'Mumbai College of Commerce',
     'University of Mumbai', 'Commerce', 'Mumbai',
     1965, 5100, 'Dr. Meena Patil', NULL),

    ('COL004', 'Nashik Institute of Science',
     'Savitribai Phule Pune University', 'Science', 'Nashik',
     1978, NULL, 'Dr. Amit Joshi', 'admin@nis.edu'),

    ('COL005', 'Nagpur Business School',
     'Rashtrasant Tukadoji Maharaj Nagpur University', 'Management', 'Nagpur',
     1992, 3800, NULL, 'info@nbs.edu'),

    ('COL006', 'Ahmedabad Engineering College',
     'Gujarat University', 'Engineering', 'Ahmedabad',
     1980, 7200, 'Dr. Vikram Shah', NULL),

    ('COL007', 'Delhi Institute of Computer Studies',
     'University of Delhi', 'Computer Science', 'Delhi',
     2001, NULL, 'Dr. Neha Verma', 'contact@dics.edu'),

    ('COL008', 'Bengaluru College of Management',
     'Bangalore University', 'Management', 'Bengaluru',
     1995, 4600, NULL, NULL),

    ('COL009', 'Jaipur College of Arts and Science',
     'University of Rajasthan', NULL, 'Jaipur',
     1975, 4100, 'Dr. Suresh Gupta', 'info@jcas.edu'),

    ('COL010', 'Hyderabad Institute of Technology',
     NULL, 'Information Technology', 'Hyderabad',
     1988, 6800, 'Dr. Priya Rao', 'contact@hit.edu');


-- 1. read data from table
-- SELECT <column_names> FROM <table_name>;

SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM colleges;

-- 2. filter WHERE
-- SELECT <column names> FROM <table_name> WHERE <condition>
-- WHERE column <operator> value

SELECT * FROM students WHERE gender = 'Male' AND city = 'Pune';

-- 3. between
-- SELECT columns FROM table WHERE age BETWEEN val1 and val2;
SELECT * FROM students WHERE age BETWEEN 21 and 25;

-- 4. in
SELECT * FROM students WHERE city IN ('Nashik', 'Pune', 'Nagpur');

-- 5. LIKE pattern matching

SELECT * FROM courses WHERE department LIKE '%echnology%';
SELECT * FROM courses WHERE course_name LIKE '%neering%';

-- 6. handling null
SELECT * FROM colleges WHERE total_students IS NULL;
SELECT * FROM colleges WHERE total_students IS NOT NULL;

-- combine all
SELECT *
FROM colleges
WHERE
	university LIKE '%une%'
	AND department IN ('Arts', 'Engineering');


-- aggregations
-- SELECT COUNT()
SELECT * FROM students;

SELECT COUNT(firstname) FROM students;
SELECT AVG(age) from students;
SELECT SUM(firstname) from students;
SELECT MIN(firstname) from students;
SELECT MAX(age) from students;

SELECT 
	COUNT(age), 
	MIN(age), 
	MAX(age), 
	AVG(age), 
	SUM(age) 
FROM students;

SELECT MAX(age) AS max_column from students;
-- SELECT firstname AS firstttttttnameeeee from students;
