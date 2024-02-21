# ORDER BY

**Lesson Goals**

- Understand how to use an `ORDER BY` clause.
- Understand how to chain multiple `ORDER BY` clauses.

---

The ORDER BY clause allows us to specify the order in which we wish to view our data.

## Using the ORDER BY clause

Queries with a ORDER BY clause normally follow this form:

```sql
SELECT column FROM table ORDER BY column_name [ASC|DESC];
```

Columns selected for output can be referred to in ORDER BY and GROUP BY clauses using column names, column aliases, or column positions. Column positions are integers and begin with 1.

```sql
SELECT first_name, last_name
FROM employees
ORDER BY last_name;
```

To sort in reverse order, add the DESC (descending) keyword to the name of the column in the ORDER BY clause that you are sorting by.

```sql
SELECT first_name, last_name
FROM employees
ORDER BY last_name DESC;
```

The default is ascending order; this can be specified explicitly using the ASC keyword.

```sql
SELECT first_name, last_name
FROM employees
ORDER BY last_name ASC;
```

The `ORDER BY` clause can be used with any `SELECT` query.

## Chaining ORDER BY clauses

The ORDER BY clause also allows you to chain together column names, column aliases, or column positions.

```sql
SELECT first_name, last_name
FROM employees
ORDER BY last_name DESC, first_name ASC;
```

## Exercises

**Exercise Goals**

- Use `ORDER BY` clauses to create more complex queries for our database

---

1. Create a new file named `order_by_exercises.sql` and copy in the contents of your exercise from the previous lesson.  

1. Find all employees with first names `'Irena'`, `'Vidya'`, or `'Maya'`, and order your results returned by first name. In your comments, answer: What was the first and last name in the first row of the results?  What was the first and last name of the last person in the table?   

1. Find all employees with first names `'Irena'`, `'Vidya'`, or `'Maya'`, and order your results returned by first name and then last name. In your comments, answer: What was the first and last name in the first row of the results?  What was the first and last name of the last person in the table?   

1. Find all employees with first names `'Irena'`, `'Vidya'`, or `'Maya'`, and order your results returned by last name and then first name. In your comments, answer: What was the first and last name in the first row of the results?  What was the first and last name of the last person in the table?   

1. Write a query to find all employees whose last name starts **and** ends with `'E'`. Sort the results by their employee number. Enter a comment with the number of employees returned, the first employee number and their first and last name, and the last employee number with their first and last name.  

1. Write a query to find all employees whose last name starts **and** ends with `'E'`. Sort the results by their hire date, so that the newest employees are listed first. Enter a comment with the number of employees returned, the name of the newest employee, and the name of the oldest employee. 

1. Find all employees hired in the 90s **and** born on Christmas. Sort the results so that the oldest employee who was hired last is the first result. Enter a comment with the number of employees returned, the name of the oldest employee who was hired last, and the name of the youngest employee who was hired first.  