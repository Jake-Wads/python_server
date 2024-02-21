
-- Select the title, description, rating, movie length columns from the films
-- table that last 3 hours or longer.
SELECT title, description, rating, length
FROM film
WHERE length > (3 * 60);
-- 39 rows

-- Select the payment id, amount, and payment date columns from the payments
-- table for payments made on or after May 27, 2005.
SELECT payment_id, amount, payment_date
FROM payment
WHERE payment_date >= '2005-05-27';
-- 15730 rows

-- Select the primary key, amount, and payment date columns from the payment
-- table for payments made on May 27, 2005.
SELECT payment_id, amount, payment_date
FROM payment
WHERE payment_date LIKE '2005-05-27%';
-- 167 rows

-- Select all columns from the customer table for rows that have a last names
-- beginning with S and a first names ending with N.
SELECT * FROM customer WHERE last_name LIKE 'S%' AND first_name LIKE '%N';
-- 11 rows

-- Select all columns from the customer table for rows where the customer is
-- inactive or has a last name beginning with "M".
SELECT * FROM customer
WHERE last_name LIKE 'M%' OR active = 0;
-- 72 rows

-- Select all columns from the category table for rows where the primary key is
-- greater than 4 and the name field begins with either C, S or T.
SELECT * FROM category
WHERE category_id > 4 AND (
    name LIKE 'C%' OR
    name LIKE 'S%' OR
    name LIKE 'T%'
);
-- 4 rows

------------------------------------------------------------------------------

-- most frequently rented movies
SELECT f.title, COUNT(*) AS total
FROM rental r
JOIN inventory i USING(inventory_id)
JOIN film f USING (film_id)
GROUP BY film_id, f.title
ORDER BY total DESC
LIMIT 5
;

-- top revenue producing movies
select
    f.title,
    SUM(amount) AS total
FROM payment p
JOIN rental r USING(rental_id)
JOIN inventory i USING(inventory_id)
JOIN film f USING(film_id)
GROUP BY film_id, f.title
ORDER BY total DESC
LIMIT 5
;

-- best customer
SELECT
    CONCAT(c.last_name, ', ', c.first_name) AS name,
    SUM(amount) AS total
FROM payment p
JOIN customer c USING(customer_id)
GROUP BY customer_id, c.first_name, c.last_name
ORDER BY total DESC
limit 1
;

-- which actor has been in the most films?

SELECT
    CONCAT(a.last_name, ', ', a.first_name) AS actor_name,
    COUNT(actor_id) AS total
FROM film_actor
JOIN actor a USING(actor_id)
GROUP BY a.first_name, a.last_name, actor_id
ORDER BY total DESC
LIMIT 5
;

-- sales for each month we have data for in in 2005
SELECT
    DATE_FORMAT(payment_date, '%Y-%m') as month,
    store_id,
    SUM(amount) as sales
FROM payment
JOIN rental USING(rental_id)
JOIN inventory USING(inventory_id)
WHERE payment_date <= '2006-01-01'
GROUP BY month, store_id
;

-- overdue movies
SELECT
    film.title,
    CONCAT(customer.last_name, ', ', customer.first_name) as customer_name,
    address.phone
FROM rental
JOIN inventory USING(inventory_id)
JOIN film USING(film_id)
JOIN customer USING(customer_id)
JOIN address USING(address_id)
WHERE return_date IS NULL
LIMIT 5
;

SELECT AVG(replacement_cost) FROM film;

SELECT rating, AVG(replacement_cost) FROM film GROUP BY rating;

------------------------------------------------------------------------------

-- number db / table / seeder

CREATE DATABASE IF NOT EXISTS numbers;

USE numbers;

DROP TABLE IF EXISTS numbers;

CREATE TABLE numbers(
    n INT
);

INSERT INTO numbers VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9), (10),
  (11), (12), (13), (14), (15), (16), (17), (18), (19), (20), (21), (22), (23),
  (24), (25), (26), (27), (28), (29), (30), (31), (32), (33), (34), (35), (36),
  (37), (38), (39), (40), (41), (42), (43), (44), (45), (46), (47), (48), (49),
  (50), (51), (52), (53), (54), (55), (56), (57), (58), (59), (60), (61), (62),
  (63), (64), (65), (66), (67), (68), (69), (70), (71), (72), (73), (74), (75),
  (76), (77), (78), (79), (80), (81), (82), (83), (84), (85), (86), (87), (88),
  (89), (90), (91), (92), (93), (94), (95), (96), (97), (98), (99), (100);

------------------------------------------------------------------------------

CREATE TEMPORARY TABLE employees_with_departments AS
SELECT emp_no, first_name, last_name, dept_no, dept_name
FROM employees.employees
JOIN dept_emp USING(emp_no)
JOIN departments USING(dept_no);

select * from employees_with_departments limit 5;

describe employees_with_departments;

alter table employees_with_departments add full_name VARCHAR(30);

update employees_with_departments set full_name = concat(first_name, ' ', last_name);

select * from employees_with_departments limit 10;

SELECT
    LCASE(CONCAT(
        SUBSTR(first_name, 1, 1),
        SUBSTR(last_name, 1, 4),
        '_',
        SUBSTR(birth_date, 6, 2),
        SUBSTR(birth_date, 3, 2)
    )) AS username,
   first_name, last_name, birth_date
FROM employees
LIMIT 10;

SELECT
    LCASE(CONCAT(
        SUBSTR(first_name, 1, 1),
        SUBSTR(last_name, 1, 4),
        '_',
        SUBSTR(birth_date, 6, 2),
        SUBSTR(birth_date, 3, 2)
    )) AS username,
    count(*) as count
FROM employees
GROUP BY username
ORDER BY count;

SELECT
    SUM(count)
FROM (
    SELECT
    LCASE(CONCAT(
            SUBSTR(first_name, 1, 1),
            SUBSTR(last_name, 1, 4),
            '_',
            SUBSTR(birth_date, 6, 2),
            SUBSTR(birth_date, 3, 2)
    )) AS username,
    count(*) as count
    FROM employees
    GROUP BY username
    ORDER BY count
) username_counts
WHERE count > 1;

SELECT dept_no, dept_name, COUNT(*) as num_employees
FROM employees
JOIN dept_emp USING(emp_no)
JOIN departments USING(dept_no)
WHERE to_date > NOW()
GROUP BY dept_no, dept_name;

SELECT
    d.dept_name,
    AVG(s.salary) as average_salary
FROM employees
JOIN salaries s USING(emp_no)
JOIN dept_emp de USING(emp_no)
JOIN departments d USING(dept_no)
WHERE s.to_date > NOW()
    AND de.to_date > NOW()
GROUP BY d.dept_name
ORDER BY average_salary DESC
LIMIT 1
;

SELECT e.first_name, e.last_name
FROM employees e
JOIN salaries s USING(emp_no)
JOIN dept_emp de USING(emp_no)
JOIN departments d USING(dept_no)
WHERE s.to_date > NOW()
    AND de.to_date > NOW()
    AND d.dept_name = 'Marketing'
ORDER BY s.salary DESC
LIMIT 1;

SELECT e.first_name, e.last_name, s.salary, d.dept_name
FROM employees e
JOIN salaries s USING(emp_no)
JOIN dept_manager dm USING(emp_no)
JOIN departments d USING(dept_no)
WHERE dm.to_date > NOW()
    AND s.to_date > NOW()
ORDER BY s.salary DESC
LIMIT 1;

SELECT dept_name FROM departments WHERE dept_no IN (
    SELECT dept_no FROM dept_emp WHERE emp_no = (
        SELECT emp_no FROM salaries ORDER BY salary DESC LIMIT 1
    )
);

CREATE TEMPORARY TABLE employee_salaries AS
SELECT
    emp_no,
    (salary - (SELECT AVG(salary) FROM salaries WHERE to_date > NOW()))
        / (SELECT AVG(salary) FROM salaries WHERE to_date > NOW())
        as z_salary,
    dept_name
FROM employees e
JOIN salaries s USING(emp_no)
JOIN dept_emp de USING(emp_no)
JOIN departments d USING(dept_no)
WHERE de.to_date > NOW()
    AND s.to_date > NOW();

SELECT dept_name, AVG(z_salary) as salary_z_score
FROM employee_salaries
GROUP BY dept_name;

DROP TABLE employee_salaries;

CREATE TEMPORARY TABLE employee_salaries AS
SELECT
    emp_no,
    (salary - (SELECT AVG(salary) FROM salaries WHERE to_date > NOW()))
        / (SELECT AVG(salary) FROM salaries WHERE to_date > NOW())
        as z_salary,
    FLOOR(DATEDIFF(NOW(), hire_date) / 365) AS years_with_company
FROM employees e
JOIN salaries s USING(emp_no)
WHERE s.to_date > NOW();

SELECT MIN(years_with_company), MAX(years_with_company)
FROM employee_salaries;

SET @min_years = (SELECT MIN(years_with_company) FROM employee_salaries);

UPDATE employee_salaries
SET years_with_company = years_with_company - @min_years;

SELECT * FROM employee_salaries LIMIT 25;

SELECT MIN(years_with_company), MAX(years_with_company)
FROM employee_salaries;

SELECT years_with_company, AVG(z_salary) as salary_z_score
FROM employee_salaries
GROUP BY years_with_company;

DROP TABLE employee_salaries;