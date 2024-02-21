-- Basic SELECT Statement

-- Use the database fruits_db.
USE fruits_db;


-- Inspect the columns and data types from a table.
DESCRIBE fruits;


-- Another way to Inspect the columns and data types from a table.
SHOW COLUMNS
FROM fruits;


-- Return all of the rows and columns from a table.
SELECT *
FROM fruits;


-- Select specific column(s) and all of the rows from those column(s).
SELECT name
FROM fruits;

SELECT 
	name,
	quantity
FROM fruits;

-- SELECT DISTINCT Statement
SELECT DISTINCT name
FROM fruits;

-- Use chiplotle database to demo a db with duplicates.
USE chipotle;


-- Inspect the columns and data types from the orders table.
DESCRIBE orders;


-- Return all of the rows and columns from a table. (4622 records returned)
SELECT *
FROM orders;


/*
Select specific column(s) and all of the rows from those column(s). 
(4622 records returned)
*/
SELECT item_name
FROM orders;



/*
Return only the unique values from a column using the DISTINCT keyword 
(50 records returned)
*/
SELECT DISTINCT item_name
FROM orders;



/*
Filter so that only records with the value 'Chicken Bowl' in item_name are returned.
(726 records returned)
*/
SELECT *
FROM orders
WHERE item_name = 'Chicken Bowl';


-- Why doesn't the query below run? Never forget this lesson!
SELECT *
FROM orders
WHERE item_price = '$4.45';


/*
Filter using the primary key column; only one record will be returned because the value must be unique.
*/
SELECT *
FROM orders
WHERE id = 15;


-- Filter using a WHERE clause with the BETWEEN & AND operators. (Returns 39 records)
SELECT *
FROM orders
WHERE quantity BETWEEN 3 AND 5;


-- Filter using a WHERE statement >, <, <> operators.
SELECT *
FROM orders WHERE order_id > 1500;

SELECT *
FROM orders
WHERE order_id != 1;


-- Create Alias Using AS

-- Create an alias for a column using the AS keyword. (Returns 267 records)
SELECT 
	item_name AS 'Multiple Item Order', 
	quantity AS Number
FROM orders AS o
WHERE quantity >= 2;


/*
Notice that if I have spaces in my column alias, I have to put it in single quotes.
If I do not have a space in my colum alias, I do not have to put it in quotes.
