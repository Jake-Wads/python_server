# Temporary Tables

In this lesson we will learn about temporary tables.

!!!caution "A Word of Warning"
    In this lesson, we will change the data in rows in a table, drop rows from a table, and change the structure of a table. This can be useful for the temporary tables that we create. However, you generally do not want to do this on actual production database tables.

We can create virtual, or temporary tables that we can use to perform data manipulations, without worrying about modifying the original data.

```sql
CREATE TEMPORARY TABLE table_name(...);
```

We create these tables the same way we would any other table, but add the `TEMPORARY` keyword.

The temporary table is removed when the database connection is closed or through the use of the explicit `DROP TABLE` statement.

## Table Creation Example

Let's walk through an example of creating a temporary table. We'll create a simple table that stores a single number in each row.

First, we will write the query to create the table. 

```sql
CREATE TEMPORARY TABLE my_numbers(
    n INT UNSIGNED NOT NULL 
);
```

Now we will insert some data into it.

```sql
INSERT INTO my_numbers(n) VALUES (1), (2), (3), (4), (5);
```

Let's take a look at what our table looks like:

```sql
SELECT * FROM my_numbers;
```

    +---+
    | n | 
    +---+
    | 1 | 
    | 2 | 
    | 3 | 
    | 4 | 
    | 5 | 
    +---+

Now we'll perform an `UPDATE` which will modify the information in our table. Note that we are *not* changing the data in the original table, just the data in the temporary table we created.

```sql
UPDATE my_numbers SET n = n + 1;
```

Note here that because we have no `WHERE` clause, the update will apply to **all rows** in the table.

Now let's remove some records. Again, this will only apply to our temporary table.

```sql
DELETE FROM my_numbers WHERE n % 2 = 0;
```

We have added 1 to each number, then removed the even numbers. Let's see the results:

```sql
SELECT * FROM my_numbers;
```

    +---+
    | n | 
    +---+
    | 3 | 
    | 5 | 
    +---+

## Creating a Table From Query Results

We can also create a temporary table from the results of another query. This allows us to quickly work with data from another table without explicitly specifying all of our data types. This can be particularly useful when we want to work with the results of a complex `JOIN`.

```sql
CREATE TEMPORARY TABLE employees_with_departments AS
SELECT emp_no, first_name, last_name, dept_no, dept_name
FROM employees
JOIN dept_emp USING(emp_no)
JOIN departments USING(dept_no)
LIMIT 100;
```

## Updating Table Structure

Once we have created a temporary table, we can change its structure with the `ALTER TABLE` command. For example, if we wanted to drop the `dept_no` column we could write the following SQL code.

```sql
ALTER TABLE employees_with_departments DROP COLUMN dept_no;
```

To add a column, we can use the `ADD` keyword like this:

```sql
ALTER TABLE employees_with_departments ADD email VARCHAR(100);
```

Note that after adding a column, the values will be `NULL` in all of the rows. We could populate that column with data by running an update:

```sql
-- a simple example where we want the email address to be just the first name
UPDATE employees_with_departments
SET email = CONCAT(first_name, '@company.com');
```

## An Important Note on Permissions 

In order to create a temporary table in a given database, your MySQL user account must have the `CREATE TEMPORARY TABLES` privilege enabled. 

Remember that `SELECT DATABASE();` shows the currently selected database. And the currently selected database is selected by `USE database_name;`

It is common to separate databases and specify different permissions for different users. One technique is to set only one database up as a sandbox with full permissions for a given user or analyst. If that same user only has SELECT privileges on all other databases, then the risk of accidental record deletion is addressed. This process also addresses other security risks.

Our workflow will be to create temporary tables on a database where you have the appropriate permissions. 

```sql
-- Use the read_only database
-- This avoids needing to re-type the db_name in front of every table_name
USE employees;

-- Specify the db where you have permissions and add the temp table name.
-- Replace "my_database_with_permissions"" with the database name where you have appropriate permissions. It should match your username.
CREATE TEMPORARY TABLE my_database_with_permissions.employees_with_salaries AS 
SELECT * FROM employees JOIN salaries USING(emp_no);

-- Change the current db.
USE my_database_with_permissions;
SELECT * FROM employees_with_salaries;
```


## Exercises

Create a file named `temporary_tables.sql` to do your work for this exercise.

1. Using the example from the lesson, create a temporary table called `employees_with_departments` that contains `first_name`, `last_name`, and `dept_name` for employees currently with that department. Be absolutely sure to create this table on your own database. If you see "Access denied for user ...", it means that the query was attempting to write a new table to a database that you can only read.

    1. Add a column named `full_name` to this table. It should be a VARCHAR whose length is the sum of the lengths of the first name and last name columns.
    1. Update the table so that the `full_name` column contains the correct data.
    1. Remove the `first_name` and `last_name` columns from the table.
    1. What is another way you could have ended up with this same table?

1. Create a temporary table based on the `payment` table from the `sakila` database.

    Write the SQL necessary to transform the `amount` column such that it is stored as an integer representing the number of cents of the payment. For example, 1.99 should become 199.

1. Go back to the `employees` database. Find out how the current average pay in *each department* compares to the overall current pay for *everyone* at the company. For this comparison, you will calculate the **z-score** for each salary. In terms of salary, what is the best department right now to work for? The worst? 

### Finding and using the z-score

A **z-score** is a way to standardize data and compare a data point to the mean of the sample. 

#### Formula for the z-score

$z = \dfrac{x - \mu }{\sigma}$



| Notation | Description |
|:-: |----------|
| $z$  |   the z-score for a data point |
| $x$   |  a data point |
| $\mu$ |  the average of the sample |
| $\sigma$ | the standard deviation of the sample |



**Hint** The following code will produce the z-score for current salaries. Compare this to the formula for z-score shown above.

```sql
    -- Returns the current z-scores for each salary
    -- Notice that there are 2 separate scalar subqueries involved
    SELECT salary,
        (salary - (SELECT AVG(salary) FROM salaries where to_date > now()))
        /
        (SELECT stddev(salary) FROM salaries where to_date > now()) AS zscore
    FROM salaries
    WHERE to_date > now();
```

**BONUS** Determine the overall historic average department average salary, the historic overall average, and the historic z-scores for salary. Do the z-scores for current department average salaries (from exercise 3) tell a similar or a different story than the historic department salary z-scores?

**Hint:** How should the SQL code used in exercise 3 be altered to instead use historic salary values?