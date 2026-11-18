-- Task 3: GROUP BY & HAVING

-- 1. Number of employees in each city
SELECT city, COUNT(*) AS total_employees
FROM employees
GROUP BY city;

-- 2. Employee count, average and highest salary for each department
SELECT dept_id,
       COUNT(*)              AS total_employees,
       ROUND(AVG(salary),2)  AS average_salary,
       MAX(salary)           AS highest_salary
FROM employees
WHERE dept_id IS NOT NULL
GROUP BY dept_id;

-- 3. HAVING: only departments with average salary above 55000
SELECT dept_id, ROUND(AVG(salary),2) AS average_salary
FROM employees
WHERE dept_id IS NOT NULL
GROUP BY dept_id
HAVING AVG(salary) > 55000;

-- 4. HAVING with COUNT: cities that have 5 or more employees
SELECT city, COUNT(*) AS total_employees
FROM employees
GROUP BY city
HAVING COUNT(*) >= 5;

-- 5. Products grouped by category
SELECT category,
       COUNT(*)             AS total_products,
       ROUND(AVG(price),2)  AS average_price,
       SUM(stock)           AS total_stock
FROM products
GROUP BY category;

-- 6. HAVING on grouped products: categories with average price above 5000
SELECT category, ROUND(AVG(price),2) AS average_price
FROM products
GROUP BY category
HAVING AVG(price) > 5000
ORDER BY average_price DESC;
