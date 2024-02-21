<style>
    ol li { padding-bottom: 4em; }
    ul li { padding: 0.5em 0; }
    table { page-break-inside: avoid; }
</style>

# SQL Assessment

## Instructions

- Write your name at the top of this page
- Answer all the questions below

## Questions

1. Which of the following `WHERE` clauses will complete the query to find all
   the stores with a zip code that starts with `78`?

    ```sql
    SELECT *
    FROM stores
    WHERE ....
    ```

    - `zipcode = '78___'`
    - `zipcode LIKE '%78'`
    - `zipcode IN (78, '78')`
    - `zipcode LIKE '78%'`
    - None of the above

1. What is the relationship between databases, tables, columns, and rows?

1. Give examples of two SQL functions and explain what they do.

1. Which of the following queries will return the first 10 rows and all the
   columns from the `invoices` table?

    - `SELECT % FROM invoives WHERE <= 10`
    - `SELECT * FROM invoices WHERE < 10`
    - `SELECT * FROM invoices WHERE <= 10`
    - `SELECT * FROM invoices LIMIT 10`
    - `SELECT ALL FROM invoices LIMIT 10`
    - None of the above

1. What is a primary key?

1. What is a foreign key?

1. What operator is used to search for a specified pattern in a column?

1. Given the following data in a table named `numbers`:

    | n   | category |
    | --- | -------- |
    | 1   | A        |
    | 1   | B        |
    | 2   | A        |
    | 2   | B        |

    Will the following query run without an error? If it runs, what output will
    it produce?

    ```sql
    SELECT *
    FROM numbers
    ORDER BY category DESC, n;
    ```

1. Give an example of a one-to-many relationship.

1. Give an example of a many-to-many relationship.

1. What is the difference in the database structure for a one-to-many and
    many-to-many relationship?

1. Given the data in the following table named `students`:

    | id  | student_name | class_type      |
    | --- | ------------ | ------          |
    | 1   | Ada          | Data Science    |
    | 2   | Bayes        | Data Science    |
    | 3   | Marie        | Web Development |
    | 4   | Rosalind     | Web Development |
    | 5   | Grace        | Data Science    |

    Will the following query run without an error? If it runs, what output will
    it produce?

    ```sql
    SELECT student_name, COUNT(*)
    FROM students
    GROUP BY class_type;
    ```

1. Will the following query run without error? If so, what will it produce as
   output?

    ```sql
    SELECT SUBSTR("Data Scienterrific", 10, LENGTH("Data Scienterrific"));
    ```

1. Which table is considered the left table in the example below?

    ```sql
    SELECT columns FROM table_a as A JOIN table_b as B ON B.id = A.id;
    ```

1. What is the difference between `JOIN` AND `LEFT JOIN`?

1. Use the `customers` table below to answer the following questions:

    | id   |  firstname  |  lastname  |  phonenumber  | prod_id  |
    |------|-------------|------------|---------------|----------|
    | 1    |  joanne     |  smith     | 123.123.1234  |    2     |
    | 2    |  sam        |  jones     | (123) 456-1234|    3     |
    | 3    |  jorge      |  gutierrez | 123-456-7890  |    1     |
    | 4    |  ann marie  |  hooper    | 1231234567    |    2     |
    | 5    |  stephanie  |  sanchez   | NULL          |  NULL    |

    The following questions ask you to write just a part of a SQL query, you do
    **not** need to write out an entire query.

    1. Write a SQL **clause** that would return only the records having
       'firstname' that begins with 'a'.

    1. Write a SQL **clause** to return only the records that have 'ann' as part
       of the 'firstname' (e.g. 'ann marie', 'mary ann', 'joanne').

    1. Write a SQL **function** that joins 'firstname' and 'lastname' into a
       column with the alias of 'fullname'

    1. Use the `customers` table above and `current_products` table below to
       write a query that will return the customers' `firstname`, `lastname`,
       and the `product_desc` for all customers with a current product.

        |  prod_id  |  prod_desc  |
        |-----------|-------------|
        |  1        |  phone      |
        |  2        |  internet   |
        |  4        |  security   |

1. Use the `numbers` table below to answer the following questions:

    | id   |  n  |
    |------|-----|
    | 1    |  1  |
    | 2    |  6  |
    | 3    | 24  |
    | 4    |  2  |
    | 5    | 15  |

    1. Which of the following queries will show the `id` and `n` value from the
       numbers table, with the results sorted with the highest value of `n`
       occuring first, and the smallest value of `n` occuring last?

        - `SELECT * FROM numbers ORDER BY n`
        - `SELECT id, n FROM numbers ORDER BY n`
        - `SELECT * FROM numbers ORDER BY n DESC`
        - None of these

    1. What will the following query produce?

        ```sql
        SELECT *
        FROM numbers
        WHERE n < 20 OR id >= 3;
        ```

    1. What will the following query produce?

        ```sql
        SELECT *
        FROM numbers
        WHERE n + 2 > 7 AND id < 4;
        ```

    1. Write a SQL query to compute the average, min, max, sum, and standard
       deviation of n.

1. What is the difference between SQL and MySQL?

1. Use the database structure below to write the following SQL queries:

    Here the `engine_id` column on the `cars` table is a foreign key that
    references the `engine_id` of the `engines` table.

    | cars        |
    | ----        |
    | `car_id`    |
    | `engine_id` |
    | `make`      |
    | `model`     |

    | engines      |
    | -------      |
    | `engine_id`  |
    | `name`       |
    | `horsepower` |

    1. Write a query that displays a list of each unique make of car.
    1. Write a query that displays how many total cars are in the database.
    1. Write a query that shows the make and model of each car, along with the
       horsepower for that car.
    1. Write a query that shows a list of the unique car makes in the database,
       as well as the number of cars with that make.

1. Which of the following will insert a new record into the `people` table?

    - `INSERT INTO people(first_name, last_name) VALUES ('Ada', 'Lovelace');`
    - `INSERT ('Ada', 'Lovelace') INTO people(first_name, last_name)`
    - `INSERT VALUES ('Ada', 'Lovelace') INTO people(first_name, last_name)`
    - None of the above

1. BONUS: What is `USING(colname)` equivalent to?

1. BONUS: What is the difference between a temporary table and a view?
