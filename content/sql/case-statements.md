# Case Statements

CASE statements and the IF() function are used to return a value when a
condition is true. Other programming languages have if *statements*, which will
execute code when a condition is true, but these serve a different purpose than
the use cases we are covering here.

**Lesson Goals**

- Understand how to use the IF() function
- Understand how to use a case statement
- Understand the difference between a case statement and an IF() function


## Using the IF() Function

It is recommended to only use the IF() function if you are evaluating a
true/false condition, as the code can get messy and hard to follow very quickly if you are
going beyond that.

IF() follows the following syntax:

```sql
SELECT IF(condition, value_1, value_2) AS new_column
FROM table_a;
```

In this example, we will select the department name, and add a field
"is_research" that returns a 1 if the department name is "Research" and 0
otherwise.

```sql
SELECT
    dept_name,
    IF(dept_name = 'Research', True, False) AS is_research
FROM employees.departments;
```

    +--------------------+-------------+
    | dept_name          | is_research |
    +--------------------+-------------+
    | Customer Service   | 0           |
    | Development        | 0           |
    | Finance            | 0           |
    | Human Resources    | 0           |
    | Marketing          | 0           |
    | Production         | 0           |
    | Quality Management | 0           |
    | Research           | 1           |
    | Sales              | 0           |
    +--------------------+-------------+


## Using Case Statements

Use CASE statements when:

- you have more than 2 optional values
- you need more flexibility in your conditional tests

There are 2 common ways to write case statements.

```sql
SELECT
    CASE column_a
        WHEN condition_a THEN value_1
        WHEN condition_b THEN value_2
        ELSE value_3
    END AS new_column_name
FROM table_a;
```

The first option is more concise, but it has its limitations:

- Can only test for *equality*.
- Can't test for NULL
- The value being tested can only come from a single column. In the statement below, the case value is coming from column_a.

From our employees database, we can use this example query to pull the research department under the development department, and pull marketing under sales. If the department name is "research" then set the department group to "Development". If the department name is "marketing" then set the department group to "Sales". Otherwise, set the department group to the department name.

Notice that the string is NOT case sensitive when evaluating the condition ("research" == "Research").

```sql
USE employees;

SELECT
    dept_name,
    CASE dept_name
        WHEN 'research' THEN 'Development'
        WHEN 'marketing' THEN 'Sales'
        ELSE dept_name
    END AS dept_group
FROM departments;
```

The output looks like this:

    +-------------------+--------------------+
    | dept_name         | dept_group         |
    +-------------------+--------------------+
    | Customer Service  | Customer Service   |
    | Development       | Development        |
    | Finance           | Finance            |
    | Human Resources   | Human Resources    |
    | Marketing         | Sales              |
    | Production        | Production         |
    | Quality Management| Quality Management |
    | Research          | Development        |
    | Sales             | Sales              |
    +-------------------+--------------------+

The second option is more verbose, but is also more flexible than the first
option. The benefits include:

- Ability to test for >, <, =, LIKE, IN, ...
- Ability to test for NULL values
- Ability to test values from multiple columns

The basic syntax looks like this:

```sql
SELECT
    CASE
       WHEN column_a > condition_1 THEN value_1
       WHEN column_b <= condition_2 THEN value_2
       ELSE value_3
   END AS new_column_name
FROM table_a;
```

Let's use this syntax to enhance our grouping and improve our earlier query.
Let's say we want to reduce the number of departments by grouping similar
departments together. We will create the following groups: R&D (Research &
Development), Sales & Marketing, and Prod & QM (Product & Quality Management).
Finance, HR and Customer Service will remain on their own.

```sql
USE employees;

SELECT dept_name,
   CASE
       WHEN dept_name IN ('research', 'development') THEN 'R&D'
       WHEN dept_name IN ('sales', 'marketing') THEN 'Sales & Marketing'
       WHEN dept_name IN ('Production', 'Quality Management') THEN 'Prod & QM'
       ELSE dept_name
   END AS dept_group
FROM departments;
```

The output looks like this:

    +-------------------+--------------------+
    | dept_name         | dept_group         |
    +-------------------+--------------------+
    | Customer Service  | Customer Service   |
    | Development       | R&D                |
    | Finance           | Finance            |
    | Human Resources   | Human Resources    |
    | Marketing         | Sales & Marketing  |
    | Production        | Prod & QM          |
    | Quality Management| Prod & QM          |
    | Research          | R&D                |
    | Sales             | Sales & Marketing  |
    +-------------------+--------------------+

## Summary

To summarize and compare these side by side, we will look at 4 different queries that return the same values.

1. IF(column_a = condition, value_1, value_2)

```sql
SELECT
    dept_name,
    IF(dept_name = 'Research', True, False) AS is_research
FROM departments;
```


1. column_a = condition

```sql
SELECT
    dept_name,
    dept_name = 'Research' AS is_research
FROM departments;
```


1. CASE column_a WHEN condition THEN value_1 ELSE value_2

    ```sql
    SELECT
        dept_name,
        CASE dept_name
            WHEN 'Research' THEN 1
            ELSE 0
        END AS is_research
    FROM departments;
    ```


1. CASE WHEN column_a = condition THEN value_1 ELSE value_2

```sql
SELECT
    dept_name,
    CASE
        WHEN dept_name IN ('Marketing', 'Sales') THEN 'Money Makers'
        WHEN dept_name LIKE '%research%' OR dept_name LIKE '%resources%' THEN 'People People'
        ELSE 'Others'
    END AS department_categories
FROM departments;
```

        +--------------------+-------------+
        | dept_name          | is_research |
        +--------------------+-------------+
        | Customer Service   | 0           |
        | Development        | 0           |
        | Finance            | 0           |
        | Human Resources    | 0           |
        | Marketing          | 0           |
        | Production         | 0           |
        | Quality Management | 0           |
        | Research           | 1           |
        | Sales              | 0           |
        +--------------------+-------------+

## BONUS Material

We can create a pivot table using the `COUNT` function with `CASE` statements.
For example, if I wanted to view the number of employee titles by department, I
can do that by combining these two SQL powerhouses.

```sql
-- Here, I'm building up my columns and values before I group by departments and use an aggregate function to get a count of values in each column.
SELECT
    dept_name,
    CASE WHEN title = 'Senior Engineer' THEN title ELSE NULL END AS 'Senior Engineer',
    CASE WHEN title = 'Staff' THEN title ELSE NULL END AS 'Staff',
    CASE WHEN title = 'Engineer' THEN title ELSE NULL END AS 'Engineer',
    CASE WHEN title = 'Senior Staff' THEN title ELSE NULL END AS 'Senior Staff',
    CASE WHEN title = 'Assistant Engineer' THEN title ELSE NULL END AS 'Assistant Engineer',
    CASE WHEN title = 'Technique Leader' THEN title ELSE NULL END AS 'Technique Leader',
    CASE WHEN title = 'Manager' THEN title ELSE NULL END AS 'Manager'
FROM departments
JOIN dept_emp USING(dept_no)
JOIN titles USING(emp_no);

-- Next, I add my GROUP BY clause and COUNT function to get a count of all employees who have historically ever held a title by department. (I'm not filtering for current employees or current titles.)
SELECT
    dept_name,
    COUNT(CASE WHEN title = 'Senior Engineer' THEN title ELSE NULL END) AS 'Senior Engineer',
    COUNT(CASE WHEN title = 'Staff' THEN title ELSE NULL END) AS 'Staff',
    COUNT(CASE WHEN title = 'Engineer' THEN title ELSE NULL END) AS 'Engineer',
    COUNT(CASE WHEN title = 'Senior Staff' THEN title ELSE NULL END) AS 'Senior Staff',
    COUNT(CASE WHEN title = 'Assistant Engineer' THEN title ELSE NULL END) AS 'Assistant Engineer',
    COUNT(CASE WHEN title = 'Technique Leader' THEN title ELSE NULL END) AS 'Technique Leader',
    COUNT(CASE WHEN title = 'Manager' THEN title ELSE NULL END) AS 'Manager'
FROM departments
JOIN dept_emp USING(dept_no)
JOIN titles USING(emp_no)
GROUP BY dept_name
ORDER BY dept_name;


-- In this query, I filter in my JOINs for current employees who currently hold each title.
SELECT
    dept_name,
    COUNT(CASE WHEN title = 'Senior Engineer' THEN title ELSE NULL END) AS 'Senior Engineer',
    COUNT(CASE WHEN title = 'Staff' THEN title ELSE NULL END) AS 'Staff',
    COUNT(CASE WHEN title = 'Engineer' THEN title ELSE NULL END) AS 'Engineer',
    COUNT(CASE WHEN title = 'Senior Staff' THEN title ELSE NULL END) AS 'Senior Staff',
    COUNT(CASE WHEN title = 'Assistant Engineer' THEN title ELSE NULL END) AS 'Assistant Engineer',
    COUNT(CASE WHEN title = 'Technique Leader' THEN title ELSE NULL END) AS 'Technique Leader',
    COUNT(CASE WHEN title = 'Manager' THEN title ELSE NULL END) AS 'Manager'
FROM departments
JOIN dept_emp
    ON departments.dept_no = dept_emp.dept_no AND dept_emp.to_date > CURDATE()
JOIN titles
    ON dept_emp.emp_no = titles.emp_no AND titles.to_date > CURDATE()
GROUP BY dept_name
ORDER BY dept_name;
```

## Exercises

**Exercise Goals**

- Use CASE statements or IF() function to explore information in the employees database

Create a file named `case_exercises.sql` and craft queries to return the results for the following criteria:

1. Write a query that returns all employees, their department number, their
   start date, their end date, and a new column 'is_current_employee' that is a
   1 if the employee is still with the company and 0 if not. DO NOT WORRY ABOUT DUPLICATE EMPLOYEES. 
   
1. Write a query that returns all employee names (previous and current), and a
   new column 'alpha_group' that returns 'A-H', 'I-Q', or 'R-Z' depending on the
   first letter of their last name.
1. How many employees (current or previous) were born in each decade?
1. What is the current average salary for each of the following department
   groups: R&D, Sales & Marketing, Prod & QM, Finance & HR, Customer Service?
   
**BONUS**

Remove duplicate employees from exercise 1. 
