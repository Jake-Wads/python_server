# Where Advanced

**Lesson Goals**

- Introduce complexity to the `WHERE` clause
- Understand how to chain clauses `AND` and `OR` to create more complex queries

---

Here we are introducing more complexity to our where clause for further filtering on our data. 


## BETWEEN

We can use WHERE with BETWEEN to find specific ranges of values.

To find all the employees between employee number 10026 and 10082:

```sql
SELECT emp_no, first_name, last_name
FROM employees
WHERE emp_no BETWEEN 10026 AND 10082;
```


## LIKE / NOT LIKE

We can use `WHERE` with the `LIKE` option to find similarities.  The `%` are wildcards.

This query will select all first names with the letters combination 'sus':

```sql
SELECT first_name
FROM employees
WHERE first_name LIKE '%sus%';
```


Recall, we can add the `DISTINCT` keyword to our `SELECT` statement to only get non-repeating values.

```sql
SELECT DISTINCT first_name
FROM employees
WHERE first_name NOT LIKE '%sus%';
```

Now, instead of seeing over 1,600 names with `sus` in them, we can see the 7 distinct names with 'sus' in them.


`NOT LIKE` will return the results that do not match the pattern.

This query selects all the first names without 'sus' in them.

```sql
SELECT DISTINCT first_name
FROM employees
WHERE first_name NOT LIKE '%sus%';
```


## IN 

We can use WHERE with IN to query only very specific sets of values.  The () are required when you use IN.

To find all the employees with the last name of 'Herber', 'Dredge', 'Lipner', and 'Baek':

```sql
SELECT emp_no, first_name, last_name
FROM employees
WHERE last_name IN ('Herber', 'Dredge', 'Lipner', 'Baek');
```


## NULL / NOT NULL 

We can also use IS NULL and IS NOT NULL to see if a value is NULL or not.

```sql
SELECT emp_no, title
FROM titles
WHERE to_date IS NOT NULL;
```

## Chaining WHERE clauses

We can chain any condition statements together using `AND` and `OR`. A complete conditional statement must be written on both sides of the `AND` or `OR`. 

```sql
SELECT emp_no, first_name, last_name
FROM employees
WHERE last_name IN ('Herber','Baek')
  AND emp_no < 20000;
```

The important thing is that we can chain as many of these as we please together, but it can get messy very quickly.

```sql
SELECT emp_no, first_name, last_name
FROM employees
WHERE emp_no < 20000
  AND last_name IN ('Herber','Baek')
   OR first_name = 'Shridhar';
```

We can force evaluation grouping using ().

```sql
SELECT emp_no, first_name, last_name
FROM employees
WHERE emp_no < 20000
  AND (
      last_name IN ('Herber','Baek')
   OR first_name = 'Shridhar'
);
```

## Further Reading

- [MySQL Expression Syntax](https://dev.mysql.com/doc/refman/5.7/en/expressions.html)


## Exercises

Create a file named `where_advanced_exercises.sql`. Use the `employees` database. 

1. Find all current or previous employees with first names `'Irena'`, `'Vidya'`, or `'Maya'` using `IN`. What is the employee number of the top three results? 

1. Find all current or previous employees with first names `'Irena'`, `'Vidya'`, or `'Maya'`, as the previous question, but use `OR` instead of `IN`. What is the employee number of the top three results? Does it match the previous question?   

1. Find all current or previous employees with first names `'Irena'`, `'Vidya'`, or `'Maya'`, using `OR`, and who is male. What is the employee number of the top three results? 

1. Find all unique last names that start with `'E'`.    

1. Find all unique last names that start **or** end with `'E'`. 

1. Find all unique last names that end with `E`, but does not start with `E`?   

1. Find all unique last names that start **and** end with `'E'`. 

1. Find all current or previous employees hired in the 90s. Enter a comment with the top three employee numbers.   

1. Find all current or previous employees born on Christmas. Enter a comment with the top three employee numbers.  

1. Find all current or previous employees hired in the 90s **and** born on Christmas. Enter a comment with the top three employee numbers.   

1. Find all unique last names that have a `'q'` in their last name.   

1. Find all unique last names that have a `'q'` in their last name but **not** `'qu'`. 