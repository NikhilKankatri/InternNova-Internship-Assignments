-- Task 1: Introduction to Databases & SELECT Statement

-- 1. How many records does each table have?
SELECT 'departments' AS table_name, COUNT(*) AS total_rows FROM departments
UNION ALL
SELECT 'employees', COUNT(*) FROM employees
UNION ALL
SELECT 'products', COUNT(*) FROM products;

-- 2. Display all records of the departments table
SELECT * FROM departments;

-- 3. Display all records of the employees table
SELECT * FROM employees;

-- 4. Select specific columns
SELECT emp_name, salary, city FROM employees;

-- 5. Select specific columns using column aliases
SELECT emp_name AS "Employee Name",
       salary   AS "Monthly Salary",
       city     AS "Work City"
FROM employees;

-- 6. Alias with a calculated column (yearly salary)
SELECT emp_name AS "Employee", salary * 12 AS "Yearly Salary" FROM employees;

-- 7. Display unique cities
SELECT DISTINCT city AS "Cities" FROM employees;
