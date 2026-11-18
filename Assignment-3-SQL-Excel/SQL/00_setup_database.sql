-- Database setup: company database with three related tables
-- (works in SQLite, and also in MySQL with minor changes)

CREATE TABLE departments (
    dept_id    INTEGER PRIMARY KEY,
    dept_name  VARCHAR(30) NOT NULL,
    location   VARCHAR(30)
);

CREATE TABLE employees (
    emp_id     INTEGER PRIMARY KEY,
    emp_name   VARCHAR(40) NOT NULL,
    dept_id    INTEGER,
    salary     INTEGER,
    hire_date  DATE,
    city       VARCHAR(30),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE products (
    product_id    INTEGER PRIMARY KEY,
    product_name  VARCHAR(40) NOT NULL,
    category      VARCHAR(30),
    price         INTEGER,
    stock         INTEGER
);

INSERT INTO departments VALUES
(1, 'IT',       'Mangalore'),
(2, 'HR',       'Bengaluru'),
(3, 'Finance',  'Mumbai'),
(4, 'Sales',    'Mangalore'),
(5, 'Research', 'Pune');

INSERT INTO employees VALUES
(1,  'Aarav Shetty',   1,    65000, '2021-06-15', 'Mangalore'),
(2,  'Ananya Rao',     1,    72000, '2020-03-10', 'Bengaluru'),
(3,  'Rohan Nayak',    1,    58000, '2022-08-01', 'Mangalore'),
(4,  'Priya Bhat',     2,    48000, '2019-11-20', 'Udupi'),
(5,  'Karan Kamath',   2,    52000, '2021-01-05', 'Mangalore'),
(6,  'Sneha Pai',      3,    61000, '2018-07-12', 'Mumbai'),
(7,  'Vikram Hegde',   3,    75000, '2017-02-28', 'Mumbai'),
(8,  'Divya Poojary',  4,    45000, '2023-04-17', 'Mangalore'),
(9,  'Arjun Kulal',    4,    50000, '2022-10-03', 'Udupi'),
(10, 'Meera Acharya',  4,    55000, '2020-12-09', 'Mangalore'),
(11, 'Rahul Shetty',   1,    80000, '2016-05-30', 'Bengaluru'),
(12, 'Kavya Rao',      2,    43000, '2023-01-16', 'Bengaluru'),
(13, 'Suresh Nayak',   3,    68000, '2019-09-23', 'Mumbai'),
(14, 'Isha Bhat',      4,    47000, '2022-02-14', 'Mangalore'),
(15, 'Manoj Kamath',   1,    62000, '2021-11-08', 'Udupi'),
(16, 'Neha Pai',       3,    59000, '2020-06-18', 'Mumbai'),
(17, 'Varun Hegde',    4,    52000, '2021-08-25', 'Mangalore'),
(18, 'Shruti Poojary', 2,    46000, '2022-12-12', 'Udupi'),
(19, 'Pooja Kulal',    1,    70000, '2018-04-04', 'Mangalore'),
(20, 'Kiran Acharya',  NULL, 30000, '2024-07-01', 'Mangalore');

INSERT INTO products VALUES
(1,  'Laptop',          'Computers',   55000, 25),
(2,  'Tablet',          'Computers',   28000, 40),
(3,  'Monitor',         'Peripherals', 12000, 60),
(4,  'Printer',         'Peripherals',  9500, 18),
(5,  'Keyboard',        'Accessories',  1500, 150),
(6,  'Mouse',           'Accessories',   800, 200),
(7,  'Headphones',      'Accessories',  3200, 90),
(8,  'Webcam',          'Accessories',  2500, 75),
(9,  'External Drive',  'Accessories',  4800, 55),
(10, 'Router',          'Peripherals',  2200, 80);
