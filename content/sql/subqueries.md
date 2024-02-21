# Subqueries

**Lesson Goals**

- Understand how to use subqueries
- Understand the difference between a subquery and a join

---

Subqueries, also called nested queries, refers to having more than one query expression in a query.

The main advantages of subqueries are:

- They allow queries that are structured so that it is possible to isolate each part of a statement.
- They provide alternative ways to perform operations that would otherwise require complex joins or unions.
- Subqueries can be easier to read and understand compared to more complex joins.

## Using Subqueries

Subqueries are helpful when we want to find if a value is within a subset of acceptable values. A subquery can return a scalar (a single value), a single row, a single column, or a table (one or more rows of one or more columns). These are called scalar, column, row, and table subqueries.

### Scalar Subqueries Return a Single Value

A Scalar Subquery is a subquery that returns a single value.

Below is an example of a scalar subquery. Notice how we can treat the subquery as if it were the single value produced. The scalar subquery `(SELECT AVG(salary) FROM salaries WHERE to_date > CURDATE())` operates with the comparison operator as if we had typed `72012.2359`.

```sql
SELECT emp_no, salary
FROM salaries
WHERE salary > (SELECT AVG(salary) FROM salaries WHERE to_date > CURDATE())
AND to_date > CURDATE();
```

And consider that we can do arithmetic on the scalars returned from a scalar subquery. The following query
returns all the current employee numbers w/ salary figures if they make more than twice the current average salary.

```sql
SELECT emp_no, salary
FROM salaries
WHERE salary > 2 * (SELECT AVG(salary) FROM salaries WHERE to_date > CURDATE())
AND to_date > CURDATE();
```

### Column Subqueries

A column subquery returns a single column. A column query follows this syntax:

```sql
SELECT column_a, column_b, column_c
FROM table_a
WHERE column_a IN (
    SELECT column_a
    FROM table_b
);
```

From our employees database, we can use this example query to find all the department managers names and birth dates:

```sql
SELECT first_name, last_name, birth_date
FROM employees
WHERE emp_no IN (
    SELECT emp_no
    FROM dept_manager
)
LIMIT 10;
```

That query should return the following result:

    +------------+--------------+------------+
    | first_name | last_name    | birth_date |
    +------------+--------------+------------+
    | Margareta  | Markovitch   | 1956-09-12 |
    | Vishwani   | Minakawa     | 1963-06-21 |
    | Ebru       | Alpin        | 1959-10-28 |
    | Isamu      | Legleitner   | 1957-03-28 |
    | Shirish    | Ossenbruggen | 1953-06-24 |
    | Karsten    | Sigstam      | 1958-12-02 |
    | Krassimir  | Wegerle      | 1956-06-08 |
    | Rosine     | Cools        | 1961-09-07 |
    | Shem       | Kieras       | 1953-10-04 |
    | Oscar      | Ghazalie     | 1963-07-27 |
    +------------+--------------+------------+

### Row Subqueries Return a Single Row

A row subquery is a subquery that returns a single row.

```sql
SELECT first_name, last_name, birth_date
FROM employees
WHERE emp_no = (
    SELECT emp_no
    FROM employees
    WHERE emp_no = 101010
);
```

### Table Subqueries

A table subquery returns a single table. The returned table needs to have an alias. Once aliased, a table subquery can be treated like its own table.

```sql
SELECT g.birth_date, g.emp_no, g.first_name from
(
    SELECT *
    FROM employees
    WHERE first_name like 'Geor%'
) as g;
```

or

```sql
SELECT g.first_name, g.last_name, salaries.salary
FROM
    (
        SELECT *
        FROM employees
        WHERE first_name like 'Geor%'
    ) as g
JOIN salaries ON g.emp_no = salaries.emp_no
WHERE to_date > CURDATE();
```

Notice in the second example that we can even join onto a table subquery. If table subqueries get too complex or computationally intensive, however, it may be a better idea to store the table query to a temporary table. For example, if you notice you keep copying and pasting the subquery, then it will be a good idea to turn that particular subquery into a temporary table.

## Exercises

**Exercise Goals**

- Use subqueries to find information in the employees database

---

Create a file named `subqueries_exercises.sql` and craft queries to return the results for the following criteria:

1. Find all the current employees with the same hire date as employee `101010` using a subquery.

1. Find all the titles ever held by all current employees with the first name `Aamod`.

1. How many people in the `employees` table are no longer working for the company? Give the answer in a comment in your code.

1. Find all the current department managers that are female.  List their names in a comment in your code.

1. Find all the employees who *currently* have a higher salary than the companie's overall, historical average salary.

1. How many *current* salaries are within 1 standard deviation of the current highest salary? (Hint: you can use a built-in function to calculate the standard deviation.) What percentage of all salaries is this?
    - *Hint* You will likely use multiple subqueries in a variety of ways
    - *Hint* It's a good practice to write out all of the small queries that you can. Add a comment above the query showing the number of rows returned. You will use this number (or the query that produced it) in other, larger queries.
    
**BONUS**

1. Find all the department names that currently have female managers.
1. Find the first and last name of the employee with the highest salary.
1. Find the department name that the employee with the highest salary works in.

1. Who is the highest paid employee within each department.
    