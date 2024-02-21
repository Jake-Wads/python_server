# Basic Statements

**Lesson Goals**

- Use the `SELECT` statement to **read** data
- Introduce the `WHERE` clause
- Understand MySQL operators

---

Thus far we have seen SQL commands that let us explore the *structure* of our databases, and now we will learn another set of commands to look at the *data* in our databases.

SQL queries are often called [*CRUD*](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations, meaning "Create, Read, Update, and Delete". CRUD is the basic building block for working with data in any system, whether it is a database, a web API, a cache server, etc. Our focus will be on the R, reading data.


### SQL Quotes

Notice that all our string values are enclosed in single quotes (`'`), this is the SQL standard. Some versions of MySQL will allow you to use double quotes for strings, but for this course, and in general for [compatibility with other database management systems][other-dbms-compat], we will stick with single quotes.

If you need to put a single quote in a string, you can escape it, (`\'`) or you can use two single quotes in a row (`''`).

[other-dbms-compat]: http://stackoverflow.com/questions/11321491/when-to-use-single-quotes-double-quotes-and-backticks-in-mysql

## Select

We use [`SELECT`](http://dev.mysql.com/doc/refman/5.7/en/select.html) to find and return rows from a table. `SELECT` is a deceptively powerful statement and we will be learning a lot more about its capabilities in the later sections, but for right now let's focus on its basic syntax:

```sql
SELECT column1[, column2[, ...]] FROM table_name;
```

Here the square brackets indicate optional parts of the command.

For example, to select the fruits and their quantity in our fruits database, we would write (after logging in to the database server):

```sql
USE fruits_db;

SELECT name, quantity FROM fruits;
```

Running this query looks like this:

    mysql> SELECT name, quantity FROM fruits;
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

We can see the output is formatted as tabular data, with the columns defined by their names, and each row containing one record.

If we want to retrieve all of the available columns for a database table, we can use the wildcard `*`.

```sql
SELECT * FROM fruits;
```

This produces a similar result, containing all the possible rows:

    mysql> SELECT * FROM fruits;
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

Here we can see our `id` column has been auto incrementing for us on each insert.


### Where Clause

As we can see, `SELECT` will return all the rows in our table. If we want to change what data is being returned, we need to narrow down our selection. We can do this by using a `WHERE` clause. `WHERE` allows you to specify a condition that must be true for a given row to be displayed. The basic syntax looks like:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column_name = 'value';
```

For example, if we just wanted to view the dragonfruit record, we could write:

```sql
SELECT * FROM fruits WHERE name = 'dragonfruit';
```

We should now see the following results returned:

    mysql> SELECT * FROM fruits WHERE name = 'dragonfruit';
    +----+-------------+----------+
    | id | name        | quantity |
    +----+-------------+----------+
    |  4 | dragonfruit |        1 |
    +----+-------------+----------+
    1 row in set (0.06 sec)

Also remember, the guaranteed fastest and most precise way to find a single record in a table is to use the table's primary key:

```sql
SELECT * FROM fruits WHERE id = 5;
```

Whenever we query using the primary key, we will always get a single row:

    mysql> SELECT * FROM fruits WHERE name = 'dragonfruit';
    +----+-------------+----------+
    | id | name        | quantity |
    +----+-------------+----------+
    |  4 | dragonfruit |        1 |
    +----+-------------+----------+
    1 row in set (0.06 sec)


#### Operators

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

All of the following operators can be used as part of a `WHERE` clause. To illustrate the use of these operators, we can also use them with a `SELECT`.

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

Recalling our previous discussion of data types, we notice that MySQL represents true and false with `1` and `0`, respectively.

Here we used a `SELECT` to demonstrate how MySQL handles the various comparison operators, but most commonly, you will see these in a `WHERE` clause, as in the examples in the rest of this module.

## Aliases

Aliases allow us to temporarily rename a column, table, or miscellaneous pieces of our query. We use aliases with the `AS` keyword. Here is a simple example:

    mysql> SELECT 1 + 1 AS two;
    +-----+
    | two |
    +-----+
    |   2 |
    +-----+
    1 row in set (0.05 sec)

    mysql>

For example, if we wanted to view the rows in the fruits table where our inventory is low, we might write a query like the following:

    mysql> SELECT id, name AS low_quantity_fruit, quantity AS inventory FROM fruits WHERE quantity < 4;
    +----+--------------------+-----------+
    | id | low_quantity_fruit | inventory |
    +----+--------------------+-----------+
    |  1 | apple              |         3 |
    |  4 | dragonfruit        |         1 |
    |  5 | elderberry         |         2 |
    +----+--------------------+-----------+
    3 rows in set (0.06 sec)

    mysql>

Notice here we kept the `id` column as is, but gave aliases to the other two columns.


### Miscellaneous Output

Sometimes it may be useful to output arbitrary data from our SQL scripts. We can do this by selecting an arbitrary string and giving it a name like so:

```sql
SELECT 'I am output!' AS 'Info';
```

This gives us a table output like before.

    +----------------+
    | Info           |
    +----------------+
    | I am a output! |
    +----------------+
    1 row in set (0.00 sec)


## Command Line SQL Scripts

Creating even a simple table is several lines long, and if a single typo is made it can be frustrating to have to recall the previous command and step through it character by character to find the typo. To simplify this, we can create our SQL commands in a script file and then instruct the MySQL command line client to run those commands. In order to do so we create a file in with the extension `.sql`. The script can contain as many SQL queries as you need, each ending with `;` or `\G`. To run the script, use the following command:

    mysql -u USERNAME -p -h DB_HOST -t < filename.sql

!!!warning "Placeholders"
    Note that `USERNAME` and `DB_HOST` in the command above are placeholders,
    and you will need to replace them with the actual values.

The `-u`, `-p`, and `-h` options specify the database username, the user's password, and the host we wish to connect to, respectively.

The `< filename.sql` tells the MySQL command line client to read in the specified file and execute all the SQL queries in it. The option `-t` makes MySQL output data in tables just like when we interact with it directly.

You can add comments in your SQL script with two dashes: `--`. Everything on a line after `--` is a comment and will not be executed.

For example, if we have the following SQL code in a file named `example.sql`:

```sql
USE fruits_db;

SELECT 'SELECTING all fruits' AS 'INFO';

SELECT * FROM fruits;

SELECT 'SELECTing the first 3 fruits' AS 'INFO';

SELECT * FROM fruits WHERE id <= 3;

SELECT 'ALL DONE!' as 'INFO';
```

We could run it by issuing the following command (you'll need to replace the
username and host with values that work for you):

```
mysql --user=codeup --host=123.123.123.123 -p -t < example.sql
```

Which will produce the following output:

    +----------------------+
    | INFO                 |
    +----------------------+
    | SELECTING all fruits |
    +----------------------+
    +----+-------------+----------+
    | id | name        | quantity |
    +----+-------------+----------+
    |  1 | apple       |        3 |
    |  2 | banana      |        4 |
    |  3 | cantelope   |       16 |
    |  4 | dragonfruit |        1 |
    |  5 | elderberry  |        2 |
    +----+-------------+----------+
    +------------------------------+
    | INFO                         |
    +------------------------------+
    | SELECTing the first 3 fruits |
    +------------------------------+
    +----+-----------+----------+
    | id | name      | quantity |
    +----+-----------+----------+
    |  1 | apple     |        3 |
    |  2 | banana    |        4 |
    |  3 | cantelope |       16 |
    +----+-----------+----------+
    +-----------+
    | INFO      |
    +-----------+
    | ALL DONE! |
    +-----------+

## Exercises

1. Create a new file called `select_exercises.sql`. Do your work for this exercise in that file.

1. Use the `albums_db` database.

1. Explore the structure of the `albums` table.

1. Write queries to find the following information.

    - The name of all albums by Pink Floyd
    - The year Sgt. Pepper's Lonely Hearts Club Band was released
    - The genre for the album Nevermind
    - Which albums were released in the 1990s
    - Which albums had less than 20 million certified sales
    - All the albums with a genre of "Rock". Why do these query results not include albums with a genre of "Hard rock" or "Progressive rock"?
