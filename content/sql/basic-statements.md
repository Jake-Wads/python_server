# Basic Statements

**Lesson Goals**

- Understand how to **read** data with `SELECT` and `FROM`
- Understand `DISTINCT` and aliases. 
- Understand MySQL operators.
- Understand the `WHERE` clause.
- Understand operators.

---

Thus far we have seen SQL commands that let us explore the *structure* of our databases, and now we will learn another set of commands to look at the *data* in our databases.

SQL queries are often called [*CRUD*](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations, meaning "Create, Read, Update, and Delete". CRUD is the basic building block for working with data in any system, whether it is a database, a web API, a cache server, etc. Our focus will be on the 'R', reading data.


## SQL Quotes

Notice that all our string values are enclosed in single quotes (`'`), this is the SQL standard. Some versions of MySQL will allow you to use double quotes for strings, but for this course, and in general for [compatibility with other database management systems][other-dbms-compat], we will stick with single quotes.

If you need to put a single quote in a string, you can escape it, (`\'`) or you can use two single quotes in a row (`''`).

[other-dbms-compat]: http://stackoverflow.com/questions/11321491/when-to-use-single-quotes-double-quotes-and-backticks-in-mysql

## SQL Comments

We can and should annotate our code by using human-readable comments for our colleagues or even for our forgetful future selves. This holds true for any programming language, but here we will view a few different ways we can include single- or multiple-line comments in our MySQL code, `#` or `--` for single-line comments and `/* This for multiple-line comments*/`
```sql
SELECT *
-- This is a single-line comment, space after dashes necessary.
FROM fruits;

SELECT
    name,
    quantity
/* 
This is a multiple-line
comment; it can go and go.
*/
FROM fruits;
```


## The Select Statement

We use [`SELECT`](http://dev.mysql.com/doc/refman/5.7/en/select.html) to find and return rows from a given column or columns in a table. `SELECT` is a powerful statement, and we will learn a lot more about its capabilities in the later sections of our curriculum, but for right now let's focus on its basic syntax:

```sql
-- The square brackets indicate optional parts of the command.
SELECT column1[, column2[, ...]] FROM table_name;
```

To retrieve all of the available columns from a database table, we can use the wildcard `*`.

```sql
USE fruits_db;

SELECT * FROM fruits;
```

This outputs tabular data containing all the columns and rows from our table:

    +----+-------------+----------+
    | id | name        | quantity |
    +----+-------------+----------+
    |  1 | apple       |        3 |
    |  2 | banana      |        4 |
    |  3 | cantelope   |       16 |
    |  4 | dragonfruit |        1 |
    |  5 | elderberry  |        2 |
    +----+-------------+----------+
    5 rows in set (0.06 sec)

We can see the output is formatted as tabular data, with the columns labeled by their names and each row containing one record. We can also see that our `id` column is auto incrementing.


To only select specific columns, we would write their column name in the select statement, with each column separated by a comma:

```sql
SELECT 
    name, 
    quantity 
FROM fruits;
```

Running this query looks like this:

    +-------------+----------+
    | name        | quantity |
    +-------------+----------+
    | apple       |        3 |
    | banana      |        4 |
    | cantelope   |       16 |
    | dragonfruit |        1 |
    | elderberry  |        2 |
    +-------------+----------+
    5 rows in set (0.05 sec)



### Distinct

As we can see, `SELECT` will return all the columns and rows in our table. If we want to change what data is being returned, we need to narrow down or filter our selection. One way we can do this is by adding the `DISTINCT` keyword to our `SELECT` statement; this will eliminate duplicate values from our output.

```sql
SELECT DISTINCT column1
FROM table_name;
```

### Miscellaneous Output

Sometimes it may be useful to output arbitrary data from our SQL scripts. We can do this by selecting an arbitrary string and giving it a name like so:

```sql
SELECT 'I am output!';
```

This gives us a table output like before; our column name is our input syntax and the output value is our string.

    +----------------+
    | I am a output! |
    +----------------+
    | I am a output! |
    +----------------+
    1 row in set (0.00 sec)


### Aliases

Aliases allow us to temporarily rename a column, table, or miscellaneous pieces of our query. If the alias name contains spaces, you must enclose the 'alias name' in quotes. Otherwise, quotes are not needed around your alias_name. *It is fine to use spaces in a column alias, but it is not good practice to use spaces in a table alias.*

Below is a simple example of using an alias in a `SELECT` statement with the `AS` keyword:

```sql
SELECT 'I am output!' as Info;
```

    +----------------+
    | Info           |
    +----------------+
    | I am a output! |
    +----------------+
    1 row in set (0.00 sec)


## The Where Clause

We can filter our data using the `WHERE` clause. `WHERE` allows you to specify a condition that must be true for a given row to be displayed. The statement selects all rows if there is no WHERE clause. The basic syntax looks like:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column_name = 'value';
```

For example, if we just wanted to view the dragonfruit record, we could write:

```sql
SELECT * 
FROM fruits 
WHERE name = 'dragonfruit';
```

We should now see the following results returned:

    +----+-------------+----------+
    | id | name        | quantity |
    +----+-------------+----------+
    |  4 | dragonfruit |        1 |
    +----+-------------+----------+
    1 row in set (0.06 sec)

Also remember, the guaranteed fastest and most precise way to find a single record in a table is to use the table's primary key because it is by nature a unique value:

```sql
SELECT * 
FROM fruits 
WHERE id = 5;
```

Whenever we query using the primary key, we will always get a single row, as each primary key is unique:

    +----+-------------+----------+
    | id | name        | quantity |
    +----+-------------+----------+
    |  4 | dragonfruit |        1 |
    +----+-------------+----------+
    1 row in set (0.06 sec)



## Operators

Most [MySQL operators](https://dev.mysql.com/doc/refman/5.7/en/non-typed-operators.html) should look pretty familiar to you, although there are a couple of new ones:

| Operator                    | Description                                                     |
| ---                         | ---                                                             |
| `=`                         | Equal                                                           |
| `!=` or `<>`                | Not equal                                                       |
| `<`                         | Less than                                                       |
| `>`                         | Greater than                                                    |
| `<=`                        | Less than or equal to                                           |
| `>=`                        | Greater than or equal to                                        |
| `BETWEEN value1 AND value2` | Greater than or equal to value1 and less than or equal to value2|

All of the following operators can be used in the `SELECT` statement or in the `WHERE` clause. Here is a demo in the `SELECT` statement.

```sql
SELECT
    2 = 2,
    1 = 2,
    1 < 2,
    2 <= 3,
    2 BETWEEN 1 AND 3,
    2 != 2,
    1 > 2;
```

    +-------+-------+-------+--------+-------------------+--------+-------+
    | 2 = 2 | 1 = 2 | 1 < 2 | 2 <= 3 | 2 BETWEEN 1 AND 3 | 2 != 2 | 1 > 2 |
    +-------+-------+-------+--------+-------------------+--------+-------+
    |     1 |     0 |     1 |      1 |                 1 |      0 |     0 |
    +-------+-------+-------+--------+-------------------+--------+-------+
    1 row in set (0.09 sec)

Recalling our previous discussion of data types, we notice that MySQL represents true and false with `1` and `0`, respectively. Our output above returns `1` if our expression evaluates to True and `0` if it evalutes to False.

Here we used a `SELECT` to demonstrate how MySQL handles the various comparison operators, but most commonly, you will see these in a `WHERE` clause as a part of filtering data, as in the examples in the rest of this module.

For example, if we wanted to view the rows in the fruits table where our inventory is low, we might write a query like the following:

```mysql
SELECT 
    id,
    name AS low_quantity_fruit,
    quantity AS inventory
FROM fruits
WHERE quantity < 4;
```

    +----+--------------------+-----------+
    | id | low_quantity_fruit | inventory |
    +----+--------------------+-----------+
    |  1 | apple              |         3 |
    |  4 | dragonfruit        |         1 |
    |  5 | elderberry         |         2 |
    +----+--------------------+-----------+
    3 rows in set (0.06 sec)

Notice above we kept the id column as is, but gave aliases to the other two columns.


## Exercises

Create a new file called `basic_statement_exercises.sql` and save your work there. *You should be testing your code in MySQL Workbench as you go.*

1. Use the `albums_db` database.

1. What is the primary key for the `albums` table?

1. What does the column named 'name' represent? 

1. What do you think the sales column represents? 

1. Find the name of all albums by Pink Floyd.
    
1. What is the year Sgt. Pepper's Lonely Hearts Club Band was released?
    
1. What is the genre for the album Nevermind?
    
1. Which albums were released in the 1990s?
    
1. Which albums had less than 20 million certified sales? Rename this column as low_selling_albums. 
    