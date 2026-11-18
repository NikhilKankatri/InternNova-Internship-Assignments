-- Task 4: SQL Joins (employees and departments joined on dept_id)

-- 1. INNER JOIN: only employees that belong to a department
SELECT e.emp_name, e.salary, d.dept_name, d.location
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- 2. LEFT JOIN: all employees, even if they have no department
SELECT e.emp_name, e.salary, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- 3. LEFT JOIN to find employees without a department
SELECT e.emp_name, e.salary, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;

-- 4. RIGHT JOIN: all departments, even if they have no employees
SELECT d.dept_name, d.location, e.emp_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id
ORDER BY d.dept_name;

-- 5. RIGHT JOIN to find departments without any employee
SELECT d.dept_name, d.location, e.emp_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id
WHERE e.emp_id IS NULL;

-- 6. JOIN with GROUP BY: total salary paid by each department
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees, COALESCE(SUM(e.salary),0) AS total_salary
FROM departments d
LEFT JOIN employees e ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY total_salary DESC;
