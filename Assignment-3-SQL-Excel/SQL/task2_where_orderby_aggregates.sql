-- Task 2: WHERE, ORDER BY & Aggregate Functions

-- 1. WHERE with a comparison operator (salary greater than 60000)
SELECT emp_name, salary FROM employees WHERE salary > 60000;

-- 2. WHERE with = and AND (Mangalore employees earning 50000 or more)
SELECT emp_name, city, salary FROM employees
WHERE city = 'Mangalore' AND salary >= 50000;

-- 3. WHERE with OR and not-equal (not from Mangalore, or salary below 45000)
SELECT emp_name, city, salary FROM employees
WHERE city <> 'Mangalore' OR salary < 45000;

-- 4. WHERE with IN
SELECT emp_name, dept_id FROM employees WHERE dept_id IN (1, 3);

-- 5. WHERE with BETWEEN (hired in 2021 and 2022)
SELECT emp_name, hire_date FROM employees
WHERE hire_date BETWEEN '2021-01-01' AND '2022-12-31';

-- 6. WHERE with LIKE (names starting with A)
SELECT emp_name FROM employees WHERE emp_name LIKE 'A%';

-- 7. ORDER BY ascending
SELECT emp_name, salary FROM employees ORDER BY salary ASC LIMIT 5;

-- 8. ORDER BY descending
SELECT emp_name, salary FROM employees ORDER BY salary DESC LIMIT 5;

-- 9. ORDER BY more than one column
SELECT emp_name, dept_id, salary FROM employees
WHERE dept_id IS NOT NULL
ORDER BY dept_id ASC, salary DESC;

-- 10. COUNT, SUM, AVG, MIN, MAX on the salary column
SELECT COUNT(*)            AS total_employees,
       SUM(salary)         AS total_salary,
       ROUND(AVG(salary),2) AS average_salary,
       MIN(salary)         AS lowest_salary,
       MAX(salary)         AS highest_salary
FROM employees;

-- 11. Aggregate functions together with WHERE (only the Sales and IT departments)
SELECT COUNT(*) AS employees, AVG(salary) AS average_salary, MAX(salary) AS highest_salary
FROM employees
WHERE dept_id IN (1, 4);

-- 12. Aggregates on the products table
SELECT COUNT(*) AS total_products, MIN(price) AS cheapest, MAX(price) AS costliest,
       ROUND(AVG(price),2) AS average_price, SUM(stock) AS total_stock
FROM products;
