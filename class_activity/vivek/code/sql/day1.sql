-- sql queries to create table
CREATE TABLE IF NOT EXISTS students (
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

-- delete table
DROP TABLE IF EXISTS newgen;
DROP TABLE students2;

SELECT * FROM students;


-- data types and contraints
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT CHECK (age >= 18),
    membership_status VARCHAR(20) DEFAULT 'Basic'
);

-- insert data in table
INSERT INTO students
VALUES
	(1, 'Riya', 20, 'Pune'),
	(2, 'Piya', 22, 'Solapur');


SELECT * FROM students;

UPDATE students
SET city = 'London'
-- WHERE student_id = 1;

DELETE FROM students
WHERE student_id = 1;





