# MySQL Functions

MySQL has several built in functions that we can use in our queries. There is also the ability to create user defined functions; however, this is a more advanced topic and outside of the scope of this course.

## Using MySQL Functions

There are several types of functions available in MySQL. While we will only be covering a few, you can view the entire list in the [Function and Operator Reference in the MySQL documentation](https://dev.mysql.com/doc/refman/5.7/en/functions.html).



## Numerical Functions

MySQL provides a handful of functions for common mathematical operations on sequences.  Some of the most common are:

- `AVG`: the mean
- `MIN`: for finding the minimum value
- `MAX`: for finding the maximum value

```sql
SELECT MIN(emp_no) from employees;
```

    +-------------+
    | MIN(emp_no) |
    +-------------+
    | 10001       |
    +-------------+

We will use these functions more in the next lesson when we introduce `GROUP BY`.


## String Functions

For a full list of available functions, see the [MySQL documentation on string functions](https://dev.mysql.com/doc/refman/5.7/en/string-functions.html).

### CONCAT

The [`CONCAT()` function](http://dev.mysql.com/doc/refman/5.7/en/string-functions.html#function_concat) takes in any number of strings or column names and will concatenate them all together.

```sql
SELECT CONCAT('Hello ', 'Codeup', '!');
```

Our results will look like:

    +---------------------------------+
    | CONCAT('Hello ', 'Codeup', '!') |
    +---------------------------------+
    | Hello Codeup!                   |
    +---------------------------------+


### SUBSTR

We can extract part of a string with the `SUBSTR` function.

```
SUBSTR(string, start_index, length)
```

We need to supply the string we wish to manipulate, the starting index, i.e., which character to start from, and the length, or the number of characters to extract.

```sql
SELECT SUBSTR('abcdefg', 2, 4);
```

    +-------------------------+
    | SUBSTR('abcdefg', 2, 4) |
    +-------------------------+
    | bcde                    |
    +-------------------------+
    1 row in set (0.05 sec)

Here we started from the second character, `b`, and extracted 4 letters, leaving us with `bcde`.

!!!warning "String Indexes in MySQL"
    In MySQL, the first character in a string is at index 1. This is notably different from other programming languages, like Python, where indexes start from 0.

### Case Conversion

We can use the `UPPER` and `LOWER` functions to convert to upper or lower case.

```sql
SELECT UPPER('abcde'), LOWER('ABCDE');
```

    +----------------+----------------+
    | UPPER('abcde') | LOWER('ABCDE') |
    +----------------+----------------+
    | ABCDE          | abcde          |
    +----------------+----------------+
    1 row in set (0.09 sec)

### Replace

The `REPLACE` function lets us manipulate strings by replacing substrings. The general form looks like this:

```sql
REPLACE(subject, search, replacement)
```

```sql
SELECT REPLACE('abcdefg', 'abc', '123');
```

    +----------------------------------+
    | REPLACE('abcdefg', 'abc', '123') |
    +----------------------------------+
    | 123defg                          |
    +----------------------------------+
    1 row in set (0.05 sec)

## Date and Time Functions

MySQL offers a wide range of [date and time functions](http://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html).  One of the most commonly used is `NOW()` or its synonymous alias `CURRENT_TIMESTAMP()`.

### NOW

The [`NOW()` function](http://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html#function_now) returns the current time in `YYYY-MM-DD HH:MM:SS` format.

```sql
SELECT NOW();
```

### CURDATE

The [`CURDATE()` function](http://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html#function_current-date) returns just the current date with no time information  in `YYYY-MM-DD` format.

```sql
SELECT CURDATE();
```

### CURTIME

The [function `CURTIME()`](http://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html#function_current-time) returns the time formatted as `HH:MM:SS`.

```sql
SELECT CURTIME();
```

### UNIX_TIMESTAMP() & UNIX_TIMESTAMP(date)

The [`UNIX_TIMESTAMP()` function](http://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html#function_unix-timestamp) is used to represent time as an integer. It will return the number of seconds since midnight January 1st, 1970. If you pass a date time value to `UNIX_TIMESTAMP()`, it will give you the number of seconds from the [unix epoch](https://en.wikipedia.org/wiki/Unix_time) to that date.

```sql
SELECT CONCAT(
    'Teaching people to code for ',
    UNIX_TIMESTAMP() - UNIX_TIMESTAMP('2014-02-04'),
    ' seconds'
);
```


## Casting

While not technically a function call, casting is a related concept. Casting lets us convert one type to another. For the most part, we can simply treat a number as a string, or a string as a number, and MySQL will figure out what to do:

```sql
SELECT
    1 + '4',
    '3' - 1,
    CONCAT('Here is a number: ', 123);
```

    +---------+---------+-----------------------------------+
    | 1 + '4' | '3' - 1 | CONCAT('Here is a number: ', 123) |
    +---------+---------+-----------------------------------+
    |       5 |       2 | Here is a number: 123             |
    +---------+---------+-----------------------------------+
    1 row in set (0.06 sec)

There is also an explicit `CAST` function should the need arise:

```sql
SELECT
    CAST(123 as CHAR),
    CAST('123' as UNSIGNED);
```

## Further Reading
- [MySQL Mathematical Functions](https://dev.mysql.com/doc/refman/5.7/en/mathematical-functions.html).
- [MySQL Regular Expression Syntax](https://dev.mysql.com/doc/refman/5.7/en/regexp.html#regexp-syntax)


## Exercises

**Exercise Goals**

1. You may choose to copy the order by exercises and save it as `functions_exercises.sql`, to save time as you will be editing the queries to answer your functions exercises. 

1. Write a query to find all employees whose last name starts **and** ends with `'E'`. Use `concat()` to combine their first and last name together as a single column named `full_name`.  

1. Convert the names produced in your last query to all uppercase.  

1. Use a function to determine how many results were returned from your previous query. 

1. Find all employees hired in the 90s **and** born on Christmas. Use [`datediff()`](https://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html#function_datediff) function to find how many days they have been working at the company (_**Hint:** You will also need to use `NOW()` or `CURDATE()`_),  

1. Find the smallest and largest current salary from the `salaries` table.  

1. Use your knowledge of built in SQL functions to generate a username for all of the employees. A username should be all lowercase, and consist of the first character of the employees first name, the first 4 characters of the employees last name, an underscore, the month the employee was born, and the last two digits of the year that they were born. Below is an example of what the first 10 rows will look like:

        +------------+------------+-----------+------------+
        | username   | first_name | last_name | birth_date |
        +------------+------------+-----------+------------+
        | gface_0953 | Georgi     | Facello   | 1953-09-02 |
        | bsimm_0664 | Bezalel    | Simmel    | 1964-06-02 |
        | pbamf_1259 | Parto      | Bamford   | 1959-12-03 |
        | ckobl_0554 | Chirstian  | Koblick   | 1954-05-01 |
        | kmali_0155 | Kyoichi    | Maliniak  | 1955-01-21 |
        | apreu_0453 | Anneke     | Preusig   | 1953-04-20 |
        | tziel_0557 | Tzvetan    | Zielinski | 1957-05-23 |
        | skall_0258 | Saniya     | Kalloufi  | 1958-02-19 |
        | speac_0452 | Sumant     | Peac      | 1952-04-19 |
        | dpive_0663 | Duangkaew  | Piveteau  | 1963-06-01 |
        +------------+------------+-----------+------------+
        10 rows in set (0.05 sec)
