-- from https://raw.githubusercontent.com/HAILGAMBO/MySql-Exercises-with-Sakila/master/Sakila%20Exercises.sql
USE sakila;

-- 1a. Display the first and last names of all actors from the table actor.
SELECT first_name, last_name FROM actor;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
SELECT CONCAT(first_name , ' ' , last_name) AS 'Actor Name' FROM actor;

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
SELECT actor_id, first_name, last_name FROM actor WHERE first_name = 'Joe';

-- 2b. Find all actors whose last name contain the letters GEN:
SELECT * FROM actor WHERE last_name LIKE '%GEN%';

-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
SELECT first_name, last_name FROM actor WHERE last_name LIKE '%LI%' ORDER BY last_name, first_name ASC;

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT country_id, country FROM country WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

-- 3a. Add a middle_name column to the table actor. Position it between first_name and last_name. Hint: you will need to specify the data type.

ALTER TABLE actor
ADD COLUMN middle_name VARCHAR(65) AFTER first_name;

-- 3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.
ALTER TABLE actor
MODIFY COLUMN middle_name BLOB;

-- 3c. Now delete the middle_name column.

ALTER TABLE actor
DROP COLUMN middle_name;

-- 4a. List the last names of actors, as well as how many actors have that last name.
SELECT last_name, COUNT(*) as count FROM actor GROUP BY last_name;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
SELECT last_name, COUNT(*) as count FROM actor GROUP BY last_name HAVING count > 1;

-- 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
UPDATE actor
SET first_name = 'HARPO'
WHERE first_name = 'GROUCHO' AND last_name = 'WILLIAMS';

SELECT * FROM actor WHERE last_name = 'WILLIAMS';
-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO. Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! (Hint: update the record using a unique identifier.)
UPDATE actor
SET first_name = CASE
	WHEN first_name = 'HARPO'
		THEN 'GROUCHO'
	ELSE 'MUCHO GROUCHO'
END
WHERE actor_id = 172;

-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
SHOW CREATE TABLE address;

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
SELECT staff.first_name, staff.last_name, address.address
FROM staff
INNER JOIN address
ON (staff.address_id = address.address_id);

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment#.
SELECT staff.first_name, staff.last_name, COUNT(payment.rental_id) AS 'Rang Up', SUM(payment.amount) AS 'Total $$'
FROM staff
INNER JOIN payment
ON (staff.staff_id = payment.staff_id)
WHERE payment_date LIKE '2005-08-%'
GROUP BY staff.staff_id;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
SELECT film.title, COUNT(film_actor.actor_id) AS 'Number of Actors'
FROM film
INNER JOIN film_actor
ON (film.film_id = film_actor.film_id)
GROUP BY film.film_id LIMIT 1000;

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT film.title, COUNT(inventory.inventory_id) AS "Copies"
FROM film
INNER JOIN inventory
ON (film.film_id = inventory.film_id)
GROUP BY film.film_id
HAVING film.title = "Hunchback Impossible";

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
SELECT c.first_name, c.last_name, SUM(p.amount)
FROM customer c
INNER JOIN payment p
ON (c.customer_id = p.customer_id)
GROUP BY c.customer_id
ORDER BY c.last_name ASC
LIMIT 600;

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
SELECT title from film  WHERE title LIKE 'Q%' OR title LIKE 'K%' AND language_id IN
(
	SELECT language_id FROM language WHERE name = 'English'
);


-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
SELECT first_name, last_name FROM actor WHERE actor_id IN
(
	SELECT actor_id FROM film_actor WHERE film_id IN
	(
		SELECT film_id FROM film WHERE title = 'Alone Trip'
	)
);

-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
SELECT c.first_name, c.last_name, c.email
FROM customer c
INNER JOIN address a
	ON (c.address_id = a.address_id)
INNER JOIN city
	ON (a.city_id = city.city_id)
INNER JOIN country
	ON (city.country_id = country.country_id)
WHERE country = 'Canada'
ORDER BY c.last_name ASC;

-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as famiy films.
SELECT title as 'Family Movies' FROM film WHERE film_id IN
(
	SELECT film_id from film_category WHERE category_id IN
    (
		SELECT category_id from category WHERE name = 'Family'
    )
);

-- 7e. Display the most frequently rented movies in descending order#.
SELECT film.title, COUNT(rental.inventory_id) AS Times_Rented
FROM film
INNER JOIN inventory
	ON (film.film_id = inventory.film_id)
INNER JOIN rental
	ON (inventory.inventory_id = rental.inventory_id)
GROUP BY film.title
ORDER BY Times_Rented DESC
LIMIT 1000;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
SELECT s.store_id, SUM(amount) AS 'Gross Revenue'
FROM store s
INNER JOIN staff
	ON (s.store_id = staff.store_id)
INNER JOIN payment
	ON (staff.staff_id = payment.staff_id)
GROUP BY s.store_id;

-- 7g. Write a query to display for each store its store ID, city, and country.
SELECT store.store_id, city.city, country.country
FROM store
INNER JOIN address
	ON (store.address_id = address.address_id)
INNER JOIN city
	ON (address.city_id = city.city_id)
INNER JOIN country
	ON (city.country_id = country.country_id);


-- 7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT cat.name AS 'Genre', SUM(amount) AS 'Gross Revenue'
FROM category cat
INNER JOIN film_category fc
	ON (cat.category_id = fc.category_id)
INNER JOIN inventory i
	ON (fc.film_id = i.film_id)
INNER JOIN rental r
	ON (i.inventory_id = r.inventory_id)
INNER JOIN payment p
	ON (r.rental_id = p.rental_id)
GROUP BY cat.name
ORDER BY sum(amount) DESC
LIMIT 5;

-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
CREATE VIEW top_five_genres_by_gross AS
SELECT cat.name AS 'Genre', SUM(amount) AS 'Gross Revenue'
FROM category cat
INNER JOIN film_category fc
	ON (cat.category_id = fc.category_id)
INNER JOIN inventory i
	ON (fc.film_id = i.film_id)
INNER JOIN rental r
	ON (i.inventory_id = r.inventory_id)
INNER JOIN payment p
	ON (r.rental_id = p.rental_id)
GROUP BY cat.name
ORDER BY sum(amount) DESC
LIMIT 5;

-- 8b. How would you display the view that you created in 8a?
SELECT * FROM top_five_genres_by_gross;

SET @row = 0;
SELECT  (@row:=@row + 1) AS Rank, Genre, 'Gross Revenue'
FROM top_five_genres_by_gross;

-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
DROP VIEW top_five_genres_by_gross;

-- from https://raw.githubusercontent.com/sschadt/sakila/master/sakila.sql
/* SQL "Sakila" database query exercises */

-- Database context
USE sakila;

-- 1a. Display the first and last names of all actors from the table actor.
SELECT first_name, last_name
FROM actor;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
SELECT CONCAT(first_name, ' ', last_name) AS 'Actor Name'
FROM actor;

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe."
--      What is one query would you use to obtain this information?
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = 'Joe';

-- 2b. Find all actors whose last name contain the letters GEN:
SELECT *
FROM actor
WHERE last_name LIKE '%GEN%';

-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
SELECT *
FROM actor
WHERE last_name LIKE '%LI%'
ORDER BY last_name, first_name;

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT country_id, country
FROM country
WHERE country IN
('Afghanistan', 'Bangladesh', 'China')
;

-- 3a. Add a middle_name column to the table actor. Position it between first_name and last_name. Hint: you will need to specify the data type.
ALTER TABLE `sakila`.`actor`
ADD COLUMN `middle_name` VARCHAR(45) NULL AFTER `first_name`;

-- 3b. You realize that some of these actors have tremendously long last names.
--  Change the data type of the middle_name column to blobs.
ALTER TABLE actor
MODIFY last_name TEXT NOT NULL;

-- 3c. Now delete the middle_name column.
ALTER TABLE actor
DROP middle_name;

-- 4a. List the last names of actors, as well as how many actors have that last name.
SELECT last_name, COUNT(*)
FROM actor
GROUP BY 1
ORDER BY 2 DESC;

-- 4b. List last names of actors and the number of actors who have that last name,
--     but only for names that are shared by at least two actors
SELECT last_name, COUNT(*)
FROM actor
GROUP BY 1
HAVING COUNT(*) >= 2

-- 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS,
--     the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
UPDATE actor
SET first_name = 'HARPO'
WHERE first_name = 'GROUCHO'
AND last_name = 'WILLIAMS';

-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct
-- name after all!
-- In a single query, if the first name of the actor is currently HARPO,
-- change it to GROUCHO. Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what
-- the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR
-- TO MUCHO GROUCHO, HOWEVER!
-- (Hint: update the record using a unique identifier.)
UPDATE actor
SET first_name = (
		CASE WHEN first_name = 'HARPO'
		THEN 'GROUCHO'
		ELSE 'MUCHO GROUCHO'
        END
	)
 WHERE actor_id = 172;

-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
DESCRIBE address;

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
SELECT s.first_name, s.last_name, a.address
FROM staff s LEFT OUTER JOIN address a ON s.address_id = a.address_id;

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
SELECT SUM(p.amount), s.last_name
FROM payment p
INNER JOIN staff s ON p.staff_id = s.staff_id AND p.payment_date BETWEEN '2005-08-01' AND '2005-08-31'
GROUP BY 2;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
SELECT f.title, count(fa.actor_id)
FROM film f INNER JOIN film_actor fa ON f.film_id = fa.film_id
GROUP BY f.title;

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT COUNT(f.title)
FROM film f INNER JOIN inventory i ON f.film_id = i.film_id
WHERE f.title = 'Hunchback Impossible';

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer.
--     List the customers alphabetically by last name:
SELECT c.first_name, c.last_name, SUM(p.amount)
FROM payment p INNER JOIN customer c ON p.customer_id = c.customer_id
GROUP BY c.last_name
ORDER BY c.last_name;

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence,
--  films starting with the letters K and Q have also soared in popularity. Use subqueries to display the titles of
--  movies starting with the letters K and Q whose language is English.
select title
FROM film
WHERE language_id = (
	SELECT language_id FROM language WHERE name = 'English'
    )
AND (title LIKE 'K%' or title LIKE 'Q%');

-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
SELECT a.first_name, a.last_name
FROM actor a
WHERE a.actor_id IN
	(SELECT actor_id
    FROM film_actor
    WHERE film_id = (SELECT film_id FROM  film WHERE title = 'Alone Trip')
    );

-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and
--     email addresses of all Canadian customers.
--     Use joins to retrieve this information.
SELECT c.first_name, c.last_name, c.email
FROM customer c INNER JOIN address a ON c.address_id = a.address_id
	INNER JOIN city ci ON a.city_id = ci.city_id
    INNER JOIN country co ON ci.country_id = co.country_id
WHERE co.country = 'Canada';

-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion.
--  Identify all movies categorized as famiy films.
SELECT f.title
FROM film f
INNER JOIN film_category fc ON f.film_id = fc.film_id
INNER JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Family' ;

-- 7e. Display the most frequently rented movies in descending order.
SELECT COUNT(r.rental_id), f.title as "Film"
FROM film f
INNER JOIN inventory i ON f.film_id = i.film_id
INNER JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY 2
ORDER BY 2 DESC;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
SELECT SUM(p.amount), s.store_id
FROM payment p
INNER JOIN rental r ON p.rental_id = r.rental_id
INNER JOIN staff s ON r.staff_id = s.staff_id
INNER JOIN store st ON s.store_id = st.store_id
GROUP BY s.store_id;

-- 7g. Write a query to display for each store its store ID, city, and country.
SELECT s.store_id, c.city, co.country
FROM store s
INNER JOIN address a ON s.address_id = a.address_id
INNER JOIN city c ON a.city_id = c.city_id
INNER JOIN country co ON c.country_id = co.country_id;

-- 7h. List the top five genres in gross revenue in descending order.
-- (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT c.name as "Genre", SUM(p.amount)
FROM category c
INNER JOIN film_category fc ON c.category_id = fc.category_id
INNER JOIN film f ON fc.film_id = f.film_id
INNER JOIN inventory i ON f.film_id = i.film_id
INNER JOIN rental r ON i.inventory_id = r.inventory_id
INNER JOIN payment p ON r.rental_id = p.rental_id
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;

-- 8a. In your new role as an executive, you would like to have an easy way of viewing
--      the Top five genres by gross revenue. Use the solution from the problem above to create a view.
--      If you haven't solved 7h, you can substitute another query to create a view.
CREATE VIEW top_five_revenue_generating_genres AS
	SELECT c.name as "Genre", SUM(p.amount)
	FROM category c
	INNER JOIN film_category fc ON c.category_id = fc.category_id
	INNER JOIN film f ON fc.film_id = f.film_id
	INNER JOIN inventory i ON f.film_id = i.film_id
	INNER JOIN rental r ON i.inventory_id = r.inventory_id
	INNER JOIN payment p ON r.rental_id = p.rental_id
	GROUP BY 1
	ORDER BY 2 DESC
	LIMIT 5;

-- 8b. How would you display the view that you created in 8a?
SELECT *
FROM top_five_revenue_generating_genres;

-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
DROP VIEW top_five_revenue_generating_genres;

-- https://raw.githubusercontent.com/christiangallego/MySQL-Exercises/master/sql/exercises.sql
--                               __
--  .--------.--.--.-----.-----.|  |
--  |        |  |  |__ --|  _  ||  |
--  |__|__|__|___  |_____|__   ||__|
--           |_____|        |__|
--
--         e x e r c i s e s

--  ---------------------------------------------------------#

-- # 1. SELECT statements

--  1a. Select all columns from the actor table.
SELECT * from actor;

--  1b. Select only the last_name column from the actor table.
SELECT last_name from actor;

--  1c. Select only the following columns from the film table.
--
--  COLUMN NAME           Note
--  title                 Exists in film table.
--  description           Exists in film table.
--  rental_duration       Exists in film table.
--  rental_rate           Exists in film table.
--  total_rental_cost     rental_duration * rental_rate

SELECT
    title,
    description,
    rental_duration,
    rental_rate,
    rental_duration * rental_rate as total_rental_cost
FROM film;

--  ---------------------------------------------------------#


-- # 2. DISTINCT operator

--  2a. Select all distinct (different) last names from the actor table.
SELECT DISTINCT last_name FROM actor;

--  2b. Select all distinct (different) postal codes from the address table.
SELECT DISTINCT postal_code FROM address;


--  2c. Select all distinct (different) ratings from the film table.
SELECT DISTINCT rating FROM film;


--  ---------------------------------------------------------#


-- # 3. WHERE clause

--  3a. Select the title, description, rating, movie length columns from the films table that last 3 hours or longer.
SELECT
title,
description,
rating,
length
FROM film
WHERE length >= 180;


--  3b. Select the payment id, amount, and payment date columns from the payments table for payments made on or after 05/27/2005.
SELECT
payment_id,
amount,
payment_date
FROM payment
WHERE payment_date >= '2005-05-27';


--  3c. Select the primary key, amount, and payment date columns from the payment table for payments made on 05/27/2005.
SELECT
payment_id,
amount,
payment_date
FROM payment
WHERE payment_date >= '2005-05-27' AND payment_date <= '2005-05-28';


--  3d. Select all columns from the customer table for rows that have a last names beginning with S and a first names ending with N.
SELECT *
FROM customer
WHERE last_name LIKE 'S%' AND first_name LIKE '%N';


--  3e. Select all columns from the customer table for rows where the customer is inactive or has a last name beginning with "M".
SELECT *
FROM customer
WHERE last_name LIKE 'M%' OR active = "false";


--  3f. Select all columns from the category table for rows where the primary key is greater than 4 and the name field begins with either C, S or T.
SELECT *
FROM category
WHERE category_id > 4 AND name LIKE 'C%' OR name LIKE 'S%' OR name LIKE 'T%';

--  3g. Select all columns minus the password column from the staff table for rows that contain a password.
SELECT
staff_id,
first_name,
last_name,
address_id,
email,
picture,
store_id,
active,
username,
last_update
FROM staff
WHERE password IS NULL;


--  3h. Select all columns minus the password column from the staff table for rows that do not contain a password.
SELECT
staff_id,
first_name,
last_name,
address_id,
email,
picture,
store_id,
active,
username,
last_update
FROM staff
WHERE password IS NOT NULL;

--  ---------------------------------------------------------#


-- # 4. IN operator

--  4a. Select the phone and district columns from the address table for addresses in California, England, Taipei, or West Java.
SELECT
phone,
district
FROM
address
WHERE district IN ('California', 'England', 'Taipei', 'West Java');

--  4b. Select the payment id, amount, and payment date columns from the payment table for payments made on 05/25/2005, 05/27/2005, and 05/29/2005.
--  (Use the IN operator and the DATE function, instead of the AND operator as in previous exercises.)
SELECT
payment_id,
amount,
payment_date
FROM
payment
WHERE
DATE(payment_date) IN('2005-05-25', '2005-05-27', '2005-05-29');

--  4c. Select all columns from the film table for films rated G, PG-13 or NC-17.
SELECT *
FROM film
WHERE rating IN ('G', 'PG-13', 'NC-17');


--  ---------------------------------------------------------#


-- # 5. BETWEEN operator

--  5a. Select all columns from the payment table for payments made between midnight 05/25/2005 and 1 second before midnight 05/26/2005.
SELECT *
FROM payment
WHERE payment_date BETWEEN '2005-05-25' AND '2005-05-26';


--  5b. Select the following columns from the film table for films where the length of the description is between 100 and 120.
--
--  COLUMN NAME           Note
--  title                 Exists in film table.
--  description           Exists in film table.
--  release_year          Exists in film table.
--  total_rental_cost     rental_duration * rental_rate

SELECT
title,
description,
release_year,
rental_duration * rental_rate AS total_rental_cost
FROM film
WHERE length BETWEEN 100 AND 120;

--  ---------------------------------------------------------#


-- # 6. LIKE operator

--  6a. Select the following columns from the film table for rows where the description begins with "A Thoughtful".
--  Title, Description, Release Year
SELECT
title,
description,
release_year
FROM film
WHERE description LIKE 'A Thoughtful%';


--  6b. Select the following columns from the film table for rows where the description ends with the word "Boat".
--  Title, Description, Rental Duration
SELECT
title, description, rental_duration
FROM film
WHERE description LIKE '%Boat';


--  6c. Select the following columns from the film table where the description contains the word "Database" and the length of the film is greater than 3 hours.
--  Title, Length, Description, Rental Rate
SELECT
title, length, description, rental_rate
FROM film
WHERE description LIKE '%Database%' && length > 180;


--  ---------------------------------------------------------#


-- # 7. LIMIT Operator

--  7a. Select all columns from the payment table and only include the first 20 rows.
SELECT *
FROM payment
LIMIT 20;

--  7b. Select the payment date and amount columns from the payment table for rows where the payment amount is greater than 5, and only select rows whose zero-based index in the result set is between 1000-2000.
SELECT
payment_date,
payment_id,
amount
FROM payment
WHERE amount > 5
LIMIT 1000 offset 2000;

--  7c. Select all columns from the customer table, limiting results to those where the zero-based index is between 101-200.
SELECT *
FROM customer
LIMIT 101 offset 200;

--  ---------------------------------------------------------#


-- # 8. ORDER BY statement

--  8a. Select all columns from the film table and order rows by the length field in ascending order.
SELECT *
FROM film
ORDER BY length ASC;


--  8b. Select all distinct ratings from the film table ordered by rating in descending order.
SELECT DISTINCT rating
FROM film
ORDER BY rating DESC;


--  8c. Select the payment date and amount columns from the payment table for the first 20 payments ordered by payment amount in descending order.
SELECT
payment_date,
amount
FROM payment
ORDER BY amount DESC
LIMIT 20;


--  8d. Select the title, description, special features, length, and rental duration columns from the film table for the first 10 films with behind the scenes footage under 2 hours in length and a rental duration between 5 and 7 days, ordered by length in descending order.
SELECT
title,
description,
special_features,
length,
rental_duration
FROM film
WHERE rental_duration BETWEEN 5 AND 7 AND length < 120
ORDER BY length DESC
LIMIT 10;

--  ---------------------------------------------------------#


-- # 9. JOINS

--  9a. Select customer first_name/last_name and actor first_name/last_name columns from performing a /left join/
--  between the customer and actor column on the last_name column in each table.
--  (i.e. `customer.last_name = actor.last_name`)
--  Label customer first_name/last_name columns as customer_first_name/customer_last_name
--  Label actor first_name/last_name columns in a similar fashion.

SELECT
customer.first_name AS customer_first_name,
customer.last_name AS customer_last_name,
actor.first_name AS actor_first_name,
actor.last_name AS actor_last_name
FROM customer
LEFT JOIN actor ON customer.first_name = actor.first_name AND customer.last_name = actor.last_name;
--  returns correct number of records: 599

--  9b. Select the customer first_name/last_name and actor first_name/last_name columns from performing a /right join between the customer and actor column on the last_name column in each table. (i.e. `customer.last_name = actor.last_name`)
SELECT
customer.first_name AS customer_first_name,
customer.last_name AS customer_last_name,
actor.first_name AS actor_first_name,
actor.last_name AS actor_last_name
FROM customer
RIGHT JOIN actor ON customer.first_name = actor.first_name AND customer.last_name = actor.last_name;
--  returns correct number of records: 200


--  9c. Select the customer first_name/last_name and actor first_name/last_name columns from performing an inner join between the customer and actor column on the last_name column in each table. (i.e. `customer.last_name = actor.last_name`)
SELECT
customer.first_name AS customer_first_name,
customer.last_name AS customer_last_name,
actor.first_name AS actor_first_name,
actor.last_name AS actor_last_name
FROM customer
INNER JOIN actor ON customer.last_name = actor.last_name;
--  returns correct number of records: 43

--  9d. Select the city name and country name columns from the city table, performing a left join with the country table to get the country name column.
SELECT
city.city AS city,
country.country_id AS country
FROM city
LEFT JOIN country ON city.country_id = country.country_id;
--  Returns correct records: 600


--  9e. Select the title, description, release year, and language name columns from the film table, performing a left join with the language table to get the "language" column.
--  Label the language.name column as "language" (e.g. `select language.name as language`)
SELECT
film.title AS title,
film.description AS description,
film.release_year,
film.language_id AS language
FROM film
LEFT JOIN language ON language.language_id = film.language_id;
--  returns 1000 rows: correct

--  9f. Select the first_name, last_name, address, address2, city name, district, and postal code columns from the staff table, performing 2 left joins with the address table then the city table to get the address and city related columns.
SELECT
staff.first_name,
staff.last_name,
staff.address_id AS address,
address.address2,
address.city_id AS city,
address.district,
address.postal_code
FROM staff
LEFT JOIN address ON staff.address_id = address.address_id
LEFT JOIN city ON address.city_id = city.city_id;
--  returns correct number of rows: 2

