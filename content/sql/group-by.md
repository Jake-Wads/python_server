# GROUP BY

**Lesson Goals**

- Understand how to use the `GROUP BY` clause

---

Using the `GROUP BY` clause removes duplicate values from columns, much like using `DISTINCT`. We will often use `GROUP BY` in combination with *aggregate functions*.

## Using the GROUP BY clause

`GROUP BY` specifies a column or columns to group by.

```sql
SELECT column FROM table GROUP BY column_name;
```

`GROUP BY` returns only the unique values of the column specified.

```sql
SELECT DISTINCT first_name
FROM employees;
```

The above query should return the same result set as:

```sql
SELECT first_name
FROM employees
GROUP BY first_name;
```

You can specify `ASC` or `DESC` for your output by adding `ORDER BY` to your clause after the `GROUP BY`.

```sql
SELECT first_name
FROM employees
GROUP BY first_name 
ORDER BY first_name DESC;
```

We can also group by multiple columns:

```sql
SELECT last_name, first_name
FROM employees
GROUP BY last_name, first_name
ORDER BY last_name ASC;
```

The above query will return all of the unique combinations of first and last
names, grouped by their last name sorted alphebetically, and within each last
name group.

!!!warning ""
    Any column(s) that appear in the `SELECT` statement should also be in the `GROUP BY`
    clause, unless they have a 1-to-1 relationship or are at the same level of granularity.

## Aggregate Functions

The functions we have seen so far look at data in a single column or possibly across an entire row. An *aggregate* function works with data across all the rows in our result set. There are many aggregate functions listed in the [MySQL documentation page](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html). `COUNT()` is the most commonly used, and that is the one we will use here. Other useful aggregate functions include `MIN`, `MAX`, `AVG`, and `SUM`.

### COUNT

The [`COUNT()` function](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_count) will return the number of non-null expression values in a result set. 
> For example,  `COUNT(expression)` for a count of non-null values or `COUNT(DISTINCT expression)` for a count of non-null unique values.

If we are only concerned about the values in a given column, we can pass that column name to the `COUNT()` function:

```sql
SELECT COUNT(first_name)
FROM employees
WHERE first_name NOT LIKE '%a%';
```

This query will return a count of all first name values that do not have an `a` in them from the `employees` table. The result should be `118_195`. If for some reason an employee's first name was `NULL`, it would not be counted here.

You will commonly see this function used as `COUNT(*)`. This returns the total number of rows in the table, including `NULL` values.

If we want to see how many rows are in our `employees` table, we can run:

```sql
SELECT COUNT(*) FROM employees;
```

## Using `GROUP BY` with Aggregate Functions

We can combine our use of aggregate functions with the `GROUP BY` clause to
produce more meaningful results.

If we want to find out how many *unique* first names do not contain an 'a',
we know we can use a `GROUP BY`. We can combine this with the aggregate
`COUNT` function to find how many employees have each unique first name:

```sql
SELECT first_name, COUNT(first_name)
FROM employees
WHERE first_name NOT LIKE '%a%'
GROUP BY first_name;
```

This query will output each unique first name without an 'a', as well as the
number of employees with that first name. Notice that this query returns
500 results. While there are 118,195 employees with a first name that did not
have the letter _a_, there are only 500 *unique* first names that do not have
an 'a' in them.

---

Take the query below as another example:

```sql
SELECT hire_date, COUNT(*)
FROM employees
GROUP BY hire_date
ORDER BY COUNT(*) DESC
LIMIT 10;
```

This will show us the 10 most common hire dates for employees.

The `COUNT()` function will be the one you used most frequently, but there are many others such as `SUM()`, `AVG()`, `MIN()` and `MAX()`. There are functions that do statistical analysis such as `STDDEV()` and `VARIANCE()`. Aggregate functions will save tedious looping and arithmetic on your end.

## Adding Conditions to Group By with `HAVING`
So far, we have used `WHERE` to filter results based on a condition. `WHERE` does not work with aggregate values, which are the results of a `GROUP BY` clause and an aggregate function. The appropriate clause for filtering these results is `HAVING`. For example:

```sql
SELECT last_name, count(*) AS n_same_last_name
FROM employees
GROUP BY last_name
HAVING n_same_last_name < 150;
```

and

```sql
SELECT concat(first_name, " ", last_name) AS full_name, count(*) AS n_same_full_name
FROM employees
GROUP BY full_name
HAVING n_same_full_name >= 5;
```

## Further Reading

- [Aggregate Function Descriptions](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html)
- [Examples on using the HAVING clause](https://www.w3schools.com/sql/sql_having.asp)

## Exercises

**Exercise Goals**

- Use the `GROUP BY` clause to create more complex queries

---

Create a new file named `group_by_exercises.sql` and save in your `database-exercises` repo.

1. In your script, use `DISTINCT` to find the unique titles in the `titles`
   table. How many unique titles have there ever been? Answer that in a comment in your SQL file. 

1. Write a query to find a list of all unique last names that start **and** end with `'E'` using `GROUP BY`.

1. Write a query to to find all unique combinations of first and last names of all employees whose last names start **and** end with `'E'` using `GROUP BY`

1. Write a query to find the unique last names with a `'q'` but not `'qu'` using `GROUP BY`.

1. Add a `COUNT()` to your results for exercise 5 to find the number of employees with the same last name.

1. Find all employees with first names `'Irena'`, `'Vidya'`, or `'Maya'`. Use `COUNT(*)` and `GROUP BY` to find the number of employees with those names for each gender.   

1. Using your query that generates a username for all employees, generate a count of employees with each unique username. 

1. From your previous query, are there any duplicate usernames? What is the highest number of times a username shows up? 

1. Determine the historic average salary for each employee. When you hear, read, or think "for each" with regard to SQL, you'll probably be grouping by that exact column. 

1. Using the `dept_emp` table, count how many current employees work in each department. The query result should show 9 rows, one for each department and the employee count.

1. Determine how many different salaries each employee has had

1. For each employee, find their minimum and maximum salary, and standard deviation of salaries.

1. Find the max salary for each employee where that max salary is greater than $150,000.

1. Find the average salary for each employee where that average salary is between $80k and $90k.

**Bonus:** From Q9, how many usernames are duplicated? 