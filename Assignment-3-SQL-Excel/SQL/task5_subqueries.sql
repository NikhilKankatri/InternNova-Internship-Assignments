-- Task 5: SQL Subqueries

-- 1. Employees earning more than the average salary
SELECT emp_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC;

-- 2. Products with a price higher than the average product price
SELECT product_name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products)
ORDER BY price DESC;

-- 3. Employee with the highest salary
SELECT emp_name, salary
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- 4. Employees who work in departments located in Mangalore (subquery with IN)
SELECT emp_name, dept_id
FROM employees
WHERE dept_id IN (SELECT dept_id FROM departments WHERE location = 'Mangalore');

-- 5. Departments that have no employees (subquery with NOT IN)
SELECT dept_name, location
FROM departments
WHERE dept_id NOT IN (SELECT dept_id FROM employees WHERE dept_id IS NOT NULL);
