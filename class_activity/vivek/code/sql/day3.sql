CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT,
    CONSTRAINT fk_employee_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);


INSERT INTO departments (department_id, department_name)
VALUES
    (10, 'IT'),
    (20, 'HR'),
    (30, 'Sales');

INSERT INTO employees (emp_id, name, department_id)
VALUES
    (1, 'Ravi', 10),
    (2, 'Priya', 20),
    (3, 'Aman', NULL);





SELECT *
FROM 
departments FULL OUTER JOIN employees
ON employees.department_id = departments.department_id;

select * from employees;


INSERT INTO departments (department_id, department_name)
VALUES
    (40, 'Finance'),
    (50, 'Marketing'),
    (60, 'Operations');

INSERT INTO departments (department_id, department_name)
VALUES
    (70, 'Data dept')

INSERT INTO employees (emp_id, name, department_id)
VALUES
    (4, 'Neha',   10),
    (5, 'Vikram', 20),
    (6, 'Sneha',  30),
    (7, 'Arjun',  30),
    (8, 'Kiran',  40),
    (9, 'Meera',  50),
    (10, 'Rahul', 10),
    (11, 'Pooja', NULL),
    (12, 'Sanjay', 60),
    (13, 'Anita', 40),
    (14, 'Rohit', 50),
    (15, 'Deepa', NULL);


-- departname, count
-- hr 45

select department_id, count(*) 
from employees
group by department_id
order by department_id asc;


select d.department_name, count(*)
from 
departments d left join employees e
on d.department_id = e.department_id
group by d.department_name;




