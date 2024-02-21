# Tables

**Lesson Goals**

- Understand what a table is
- Understand data types in MySQL
- Understand how to create, show, describe and drop tables
- Introduce primary keys
- Understand how to use external sql scripts

---

Data in databases is organized into tables. Tables look a lot like a spreadsheet; they break our data down into columns and store individual records in rows. Unlike a spreadsheet however, a database table has a specific set of columns and it is up to developers and database administrators to define what those columns are named and what kind of data they can contain.

## Data types

MySQL, and most database systems, are statically typed. This means that when tables are created, the data type of each column must be specified. This is beneficial in that we will know ahead of time what kind of data is stored in each column.

Here we will give a brief overview of the most common data types:

### Numeric Types

The basic building block of any language is a numeric data type. MySQL supports a [variety of numeric types](https://dev.mysql.com/doc/refman/8.0/en/numeric-types.html), but the most common ones are listed below.

- `INT`: Any number *without* a decimal point. A so-called "counting number". Optionally can be `UNSIGNED`, which means that it can only hold positive values.
- `FLOAT`: A number *with* decimal values, but which can sometimes be less accurate. You can use `DOUBLE` instead to increase the precision.
- `DECIMAL(length, precision)`: A *precise* decimal number. Decimal columns must be defined with a *length* and a *precision*; length is the total number of digits that will be stored for a value, and precision is the number of digits after the decimal place. For example, a column defined as `DECIMAL(4,2)` would allow four digits total: two before the decimal point and two after. So the values `99.99`, `4.50`, and `-88.10` would be allowed, but not `100.00` or `7.134`. Decimal columns are perfect for storing monetary values.

#### Unsigned

When we are declaring our numeric columns, we can specify that the values are `UNSIGNED`. This allows us to potentially store larger numbers in a column but only positive values. For example, a normal `INT` column can store numbers from `-2,147,483,648` to `2,147,483,647`, whereas an `INT UNSIGNED` column can store `0` to `4,294,967,295`.

#### Boolean

MySQL has no native support for boolean values. Instead, it uses a `TINYINT` data type that goes from `-128` to `127` and treats `0` as `false` and `1` as `true`. Other database management systems will vary in how they handle boolean values.

### String Types

Like our other languages, MySQL also has [string types](https://dev.mysql.com/doc/refman/8.0/en/string-types.html), although with a few caveats. Below are the most common string datatypes in MySQL and how to use them.

- `CHAR(length)` &mdash; A string with a fixed number of characters, where `length` can be from 1 to 255. If a string shorter than `length` is stored in a `CHAR` column then the value is padded with empty space to take up the full size. If you try to store a string longer than `length`, then an error occurs. `CHAR` column types are ideal for values where you know the length and it is constant, like a state abbreviation `CHAR(2)`, zip code `CHAR(5)`, or phone number `CHAR(10)`.
- `VARCHAR(length)` &mdash; For strings where the length could vary up to some maximum number. `VARCHAR` columns are probably the most common type of column you will use in your database tables. Although `VARCHAR` lengths can go up to 65,535, if you need more than 255 characters consider using `TEXT` instead.
- `TEXT` &mdash; A large block of characters than can be any length. It may be tempting to just throw everything in `TEXT` columns and not worry about lengths, but this is a very bad idea! There are some major technical limitations to `TEXT` and they can cause serious performance issues if they are abused. Only use `TEXT` columns for very large blocks of text, like the full text of an article, or the pages of a book.

We will use single quotes (`'`) to indicate string values.

### Date Types

Dates and times are deceptively complex data types. Thankfully MySQL includes several ways of [representing them](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-types.html).

- `DATE` &mdash; A date value without any time. Typically MySQL displays dates as `YYYY-MM-DD`.
- `TIME` &mdash; A time down to the seconds. MySQL uses 24-hour times.
- `DATETIME` &mdash; A combined date and time value. `DATETIME` does not store any timezone information and will typically display information in the format `YYYY-MM-DD HH:MM:SS`.

### Null

The value `NULL` has special meaning in relational databases. In most languages `null` behaves like `0` (many times, it secretly *is* `0`). In MySQL, `NULL` can be thought of as *the absence of value*. This has some interesting consequences. If we asked whether `NULL != NULL` the answer would be `NULL`. On the other hand, if we asked if `NULL = NULL` the answer would **also** be `NULL`! In essence, you can think of this question as "does some unknown value equal some other unknown value?" to which MySQL responds "How should I know?!"

Since `NULL` values are complex, and because they can lead to inconsistent data, columns can specify that their values are `NOT NULL`. This will prevent `NULL` from being stored in a particular column and lead to more predictable results.

## Creating Tables

Although you probably won't be creating tables often as a data scientist, it is good to be familiar with how the process works:

```sql
CREATE TABLE table_name (
    column1_name data_type,
    column2_name data_type,
    ...
);
```

For example, if we wanted to create a table for storing famous quotes it might look like:

```sql
CREATE TABLE quotes (
    author_first_name VARCHAR(50),
    author_last_name  VARCHAR(100) NOT NULL,
    content TEXT NOT NULL
);
```

Notice we allow for the `author_first_name` to be `NULL`, but that `author_last_name` and `content` are both mandatory. However, this example is not yet complete. We are missing a final key concept for our tables. Some might even say, that it was the *primary key* concept.

### Primary Keys

If we were to start working with our `quotes` table as is, there would be nothing to stop us from inserting multiple duplicate values. At that point we could have two or more records in the database with no way to distinguish between them. Primary keys solve this problem; a primary key is a guaranteed way to uniquely identify a single row in a table. A primary key is a special type of column with the following rules:

1. Each value must be unique.
1. They cannot be `NULL`.
1. There can only be one primary key in a table.

There is a lot of database theory that can go into creating and assigning primary keys. Practically speaking though, this is usually not a problem you want to burden yourself with. Most of the time, it is perfectly reasonable to let the database server manage your primary key values for you. Let's update our `quotes` table definition to have a primary key:

```sql
CREATE TABLE quotes (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    author_first_name VARCHAR(50),
    author_last_name  VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    PRIMARY KEY (id)
);
```

Let's break down our changes a bit. First, our new column `id` **is** a column just like the other four, but we have added some additional constraints to it. We have specified that the `id` is an `UNSIGNED` integer. That is because MySQL will assign IDs starting with `1`, so it does not make sense to allow negative values in our column. The last part of our column definition is `AUTO_INCREMENT`. This is what instructs MySQL to generate a new values for this column when we try to insert records into our table. Only one column per table may be `AUTO_INCREMENT` and it **must** be the primary key. Finally, at the end our table definition, we specify that the `PRIMARY KEY` for the table is `id`.

!!!note "Naming Conventions"
    It is common to see the primary key named with the name of the table as well, in our example above, we might have seen `quote_id` for the primary key name. In addition, database table names might be singular instead of plural, or written in ALL CAPS. Conventions vary by database, but tend to be internally consistent within the database itself.

## Showing Tables

If we need to see what tables are defined in a database (after switching to it), we can use the [`SHOW TABLES`](https://dev.mysql.com/doc/refman/5.7/en/show-tables.html) command.

```sql
SHOW TABLES;
```

## Getting Information about Existing Tables

Once you have access to a database, there are 2 primary ways to explore the table structure. Of course you might start with `SHOW TABLES`, but to explore the structure of a single table you can use `DESCRIBE` or `SHOW CREATE`.

The command to show the structure of a table is [`DESCRIBE`](https://dev.mysql.com/doc/refman/5.7/en/explain.html).

```sql
DESCRIBE quotes;
```

This give us:

    +-------------------+------------------+------+-----+---------+----------------+
    | Field             | Type             | Null | Key | Default | Extra          |
    +-------------------+------------------+------+-----+---------+----------------+
    | id                | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
    | author_first_name | varchar(50)      | YES  |     | NULL    |                |
    | author_last_name  | varchar(100)     | NO   |     | NULL    |                |
    | content           | text             | NO   |     | NULL    |                |
    +-------------------+------------------+------+-----+---------+----------------+
    4 rows in set (0.00 sec)

MySQL uses `EXPLAIN` and `DESCRIBE` interchangeably. By convention we use `DESCRIBE` when we want to inspect a table, and `EXPLAIN` when we want to analyze a query.

MySQL can also display the original command used to create a table by using [`SHOW CREATE TABLE`](https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html).

```sql
SHOW CREATE TABLE quotes;
```

    *************************** 1. row ***************************
            Table: quotes
    Create Table: CREATE TABLE `quotes` (
        'id' int(10) unsigned NOT NULL AUTO_INCREMENT,
        'author_first_name' varchar(50) DEFAULT NULL,
        'author_last_name' varchar(100) NOT NULL,
        'content' text NOT NULL,
        PRIMARY KEY ('id')
    )
    1 row in set (0.00 sec)

## Exercises

0. Open MySQL Workbench and login to the database server
1. Save your work in a file named `tables_exercises.sql`
1. Use the `employees` database. Write the SQL code necessary to do this.
1. List all the tables in the database. Write the SQL code necessary to accomplish this.
1. Explore the `employees` table. What different data types are present on this table?
1. Which table(s) do you think contain a numeric type column? (Write this question and your answer in a comment)
1. Which table(s) do you think contain a string type column? (Write this question and your answer in a comment)
1. Which table(s) do you think contain a date type column? (Write this question and your answer in a comment)
1. What is the relationship between the `employees` and the `departments` tables? (Write this question and your answer in a comment)
1. Show the SQL that created the `dept_manager` table. Write the SQL it takes to show this as your exercise solution.
