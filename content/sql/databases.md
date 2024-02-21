# MySQL Databases & Tables

**Lesson Goals**

- Understand the organizational structure of a MySQL server and how to navigate it
- Understand how to create, show, and describe tables
- Understand data types in MySQL
- Introduce primary keys

---

## Databases

The main organization structure of MySQL is a *database*. One MySQL server can have many different databases. In fact, our MySQL server came with three system databases already defined, one of which we have already seen (`mysql`).

### Listing Databases

To see a list of the databases in the MySQL server we can run the [`SHOW DATABASES`](http://dev.mysql.com/doc/refman/5.7/en/show-databases.html) command.

```sql
SHOW DATABASES;
```

This will give you output that looks similar to the following:

    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | employees          |
    | fruits_db          |
    | menagerie          |
    | mysql              |
    | performance_schema |
    | sakila             |
    | sys                |
    | world              |
    +--------------------+

Alternatively, the "Schemas" tab in MySQL Workbench lists all the databases.

### Selecting a Database

Since virtually all MySQL information is stored within a database, it can be convenient to switch to a particular database. Doing so ensures that your subsequent queries refer (by default) to tables and other objects within that database. The command to select a database is [`USE`](http://dev.mysql.com/doc/refman/5.7/en/use.html).

```sql
USE database_name;
```

### Showing Current Database

In order to determine what database you currently have selected you can use the following query:

```sql
SELECT database();
```

You should see the following output:

    +---------------+
    | database()    |
    +---------------+
    | database_name |
    +---------------+
    1 row in set (0.00 sec)

If the MySQL server responds with `NULL` as the database name, you likely do not have a database selected.

### Inspecting a Database

You can actually find out the query used to create a database with the [`SHOW CREATE` query](http://dev.mysql.com/doc/refman/5.7/en/show-create-database.html):

```sql
SHOW CREATE DATABASE database_name;
```

The output for this command looks like the following:

    +---------------+------------------------------------------------------------------------+
    | Database      |         Create Database                                                |
    +---------------+------------------------------------------------------------------------+
    | database_name | CREATE DATABASE `database_name` /*!40100 DEFAULT CHARACTER SET utf8 */ |
    +---------------+------------------------------------------------------------------------+
    1 row in set (0.00 sec)

The query has given us the exact SQL command necessary to recreate the database. This could be useful if we were trying to export or duplicate our database on a different server. While this information may not look like much now, we will be using a nearly identical command when it comes to tables as well.

### Database vs. Schema

You may notice the word "schema" being used in documentation in several places. Other RDBMS's use schemas as a second level of organization *within* databases and strictly separate databases from each other from the user's perspective. Understandably, this has lead to more than a bit of [confusion and debate](http://en.wikipedia.org/wiki/Comparison_of_relational_database_management_systems#Databases_vs_schemas_.28terminology.29) over the years.

Within MySQL, "database" and "schema" mean the same thing and can be used interchangeably.

Words like `SELECT`, `INSERT`, `CREATE` are reserved words in MySQL, and cannot be used for database, table, or column names. Refer to the MySQL documentation on [reserved words](https://dev.mysql.com/doc/refman/5.7/en/keywords.html) for a complete list.


## Tables

Data in databases is organized into tables. Tables look a lot like a spreadsheet; they break our data down into columns and store individual records in rows. Unlike a spreadsheet, however, a database table has a specific set of columns. Developers and database administrators define the column names and what kind of data they can contain.

### Showing Tables

If we need to see what tables are defined in a database (after switching to it), we can use the [`SHOW TABLES`](https://dev.mysql.com/doc/refman/5.7/en/show-tables.html) command.

```sql
SHOW TABLES;
```

### Referring to Tables in Other Databases

At times it may be necessary to refer to a table or object in a separate database. Or, if you have just connected to a MySQL server, you may not have any database selected. To do this, you can use the syntax `database_name.table_name`. We have used this style of query a couple times already! Refer back to the previous lessons and notice that most of our queries refer to the `mysql` database (e.g. `mysql.user`). That is because we had not selected a database at that point.


## Data types

MySQL, and most database systems, are statically typed. This means that when tables are created, the data type of each column must be specified. This is beneficial because we know ahead of time what kind of data is stored in each column.

Here is a brief overview of the most common data types:

### Numeric Types

The basic building block of any language is a numeric data type. MySQL supports a [variety of numeric types](https://dev.mysql.com/doc/refman/8.0/en/numeric-types.html), but the most common ones are listed below.

- `INT`: Any number *without* a decimal point. A so-called "counting number". Optionally can be `UNSIGNED`, which means that it can only hold positive values.
- `FLOAT`: A number *with* decimal values, but which can sometimes be less accurate. You can use `DOUBLE` instead to increase the precision.
- `DECIMAL(length, precision)`: A *precise* decimal number. Decimal columns must be defined with a *length* and a *precision*; length is the total number of digits that will be stored for a value, and precision is the number of digits after the decimal place. For example, a column defined as `DECIMAL(4,2)` would allow four digits total: two before the decimal point and two after. So the values `99.99`, `4.50`, and `-88.10` would be allowed, but not `100.00` or `7.134`. Decimal columns are perfect for storing monetary values.

#### Unsigned

When we are declaring our numeric columns, we can specify that the values are `UNSIGNED`. This allows us to store larger numbers in a column but only positive values. For example, a normal `INT` column can store numbers from `-2,147,483,648` to `2,147,483,647`, whereas an `INT UNSIGNED` column can store `0` to `4,294,967,295`.

#### Boolean

MySQL has no native support for boolean values. Instead, it uses a `TINYINT` data type that goes from `-128` to `127` and treats `0` as `False` and `1` as `True`. Other database management systems vary in how they handle boolean values.

### String Types

Like other languages, MySQL has [string types](https://dev.mysql.com/doc/refman/8.0/en/string-types.html), with a few caveats. Below are the most common string datatypes in MySQL and how to use them.

- `CHAR(length)` &mdash; A string with a fixed number of characters, where `length` can be from 1 to 255. If a string shorter than `length` is stored in a `CHAR` column, the value is padded with empty space to take up the full size. If you try to store a string longer than `length`, an error occurs. `CHAR` column types are ideal for values where you know the length and it is constant, such as a state abbreviation `CHAR(2)`, zip code `CHAR(5)`, or phone number `CHAR(10)`.
- `VARCHAR(length)` &mdash; For strings where the length could vary, up to some maximum number. `VARCHAR` columns are the most common data type you will encounter in database tables. Although `VARCHAR` lengths can go up to 65,535, if you need more than 255 characters, consider using `TEXT` instead.
- `TEXT` &mdash; A large block of characters that can be any length. It may be tempting to just throw everything in `TEXT` columns and not worry about length, but this is a very bad idea! There are some major technical limitations to `TEXT` and they can cause serious performance issues if they are abused. Only use `TEXT` columns for very large blocks of text, such as the full text of an article or the pages of a book.

We will use single quotes (`'`) to indicate string values.

### Date Types

Dates and times are deceptively complex data types. Thankfully MySQL includes several ways to [represent them](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-types.html).

- `DATE` &mdash; A date value without any time. Typically, MySQL displays dates as `YYYY-MM-DD`.
- `TIME` &mdash; A time down to the seconds. MySQL uses 24-hour times.
- `DATETIME` &mdash; A combined date and time value. `DATETIME` does not store any timezone information and will typically display information in the format `YYYY-MM-DD HH:MM:SS`.

### Null

The value `NULL` has special meaning in relational databases. In most languages, `null` behaves like `0` (many times, it secretly *is* `0`). In MySQL, `NULL` can be thought of as *the absence of value*. This has some interesting consequences. If we asked if `NULL != NULL`, the answer would be `NULL`. On the other hand, if we asked if `NULL = NULL`, the answer would **also** be `NULL`! In essence, you can think of this question as "does some unknown value equal some other unknown value?" to which MySQL responds "How should I know?!"

Since `NULL` values are complex, and because they can lead to inconsistent data, columns can specify that their values are `NOT NULL`. This will prevent `NULL` values from being stored in a particular column and lead to more predictable results.

## Creating Tables

Although you probably won't create many tables as a data scientist, it is good to be familiar with how the process works:

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

Notice how we allow for the `author_first_name` to be `NULL`, but `author_last_name` and `content` are both mandatory. However, this example is incomplete. We are missing a final key concept for our tables. Some might even say, that it is the *primary key* concept.

### Primary Keys

If we started working with our `quotes` table as is, there would be nothing to stop us from inserting duplicate values. At that point, we could have two or more records in the database with no way to distinguish between them. Primary keys solve this problem; a primary key is a guaranteed way to uniquely identify a single row in a table. A primary key is a special type of column with the following rules:

1. Each value must be unique.
1. Each value cannot be `NULL`.
1. There can only be one primary key in a table.

There is a lot of database theory that can go into creating and assigning primary keys. Most of the time, it is perfectly reasonable to let the database server manage your primary keys for you. Let's update our `quotes` table definition to have a primary key:

```sql
CREATE TABLE quotes (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    author_first_name VARCHAR(50),
    author_last_name  VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    PRIMARY KEY (id)
);
```

Let's break down our changes a bit. First, our new column `id` **is** a column just like the other four, but we have added some additional constraints to it. We have specified that the `id` is an `UNSIGNED` integer. That is because MySQL will assign IDs starting with `1`, so it does not make sense to allow negative values in our column. The last part of our column definition is `AUTO_INCREMENT`. This instructs MySQL to generate new values for this column when we insert new records into our table. Only one column per table may be `AUTO_INCREMENT` and it **must** be the primary key. Finally, at the end our table definition, we specify that the `PRIMARY KEY` for the table is `id`.

!!!note "Naming Conventions"
    It is common to see the primary key name include the name of the table. In our example above, we might have seen `quote_id` for the primary key name. In addition, database table names might be singular instead of plural, or written in ALL CAPS. Conventions vary by database, but tend to be internally consistent within the database itself.



## Quoting Identifiers

Although great care should be exercised to avoid using reserved words (words that have a special meaning in the SQL language) in your database or table names, there is a way around it. In SQL, you can use any word for a database name, even space characters, as long as you enclose the database name in back ticks (\`\`). You will see that in our output from `SHOW CREATE`, our database name was enclosed in back ticks as well. In practice, do not do this. Using a reserved word as a table name is never worth the trouble it takes to do so; the same goes for names with spaces in them.

---

## Exercises

0. Open MySQL Workbench and login to the database server
1. Save your work in a file named `db_tables_exercises.sql`
1. List all the databases
1. Write the SQL code necessary to use the `albums_db` database
1. Show the currently selected database
1. List all tables in the database
1. Write the SQL code to switch to the `employees` database
1. Show the currently selected database
1. List all tables in the database
1. Explore the `employees` table. What different data types are present in this table?
1. Which table(s) do you think contain a numeric type column? (Write this question and your answer in a comment)
1. Which table(s) do you think contain a string type column? (Write this question and your answer in a comment)
1. Which table(s) do you think contain a date type column? (Write this question and your answer in a comment)
1. What is the relationship between the `employees` and the `departments` tables? (Write this question and your answer in a comment)
1. Show the SQL code that created the `dept_manager` table. Write the SQL it takes to show this as your exercise solution.
