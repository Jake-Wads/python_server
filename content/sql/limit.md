# LIMIT

**Lesson Goals**

- Understand how to get query results in batches using the `LIMIT` clause

---

The LIMIT clause limits the number of results returned to a number or range you specify.

## Using LIMIT

Generally, a query with a LIMIT clause follows this form:

```sql
SELECT columns FROM table LIMIT count [OFFSET count];
```

The simplest use of the LIMIT clause just specifies a number after the keyword.

```sql
SELECT emp_no, first_name, last_name
FROM employees
WHERE first_name LIKE 'M%'
LIMIT 10;
```

Adding an `OFFSET` tells MySQL which row to start with.

```sql
SELECT emp_no, first_name, last_name
FROM employees
WHERE first_name LIKE 'M%'
LIMIT 25 OFFSET 50;
```

`LIMIT` and `OFFSET` are commonly used for pagination, or creating pages of data.

The above query asks for the employee number, first name, and last name, where the first name starts with an 'M'. The results are offset by fifty and will  start at the fifty-first record, limiting the results to twenty-five records.

## Exercises

**Exercise Goals**

- Add the `LIMIT` clause to our existing queries

---

1. Create a new SQL script named `limit_exercises.sql`.

1. MySQL provides a way to return only unique results from our queries with the
   keyword `DISTINCT`. For example, to find all the unique titles within the
   company, we could run the following query:

    ```sql
    SELECT DISTINCT title FROM titles;
    ```

    List the first 10 distinct last names sorted in descending order. 

1. Find all previous or current employees hired in the 90s **and** born on Christmas. Find the first 5 employees hired in the 90's by sorting by hire date and limiting your results to the first 5 records. Write a comment in your code that lists the five names of the employees returned. 

1. Try to think of your results as *batches*, *sets*, or *pages*. The first five results are your first page. The five after that would be your second page, etc. Update the query to find the tenth page of results. 

    `LIMIT` and `OFFSET` can be used to create multiple pages of data. What is
    the relationship between `OFFSET` (number of results to skip), `LIMIT`
    (number of results per page), and the page number?
