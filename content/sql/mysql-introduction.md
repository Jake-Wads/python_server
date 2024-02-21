# Introduction to MySQL

**Lesson Goals**

- Introduce Databases as a concept
- Introduce SQL
- Explain how to access our MySQL database from the command line
- Explain how to get different formats for query results

---

MySQL is a Relational Database Management System, or RDBMS. This means data is stored in tables and there are relationships between data in different tables. This is much like having multiple spreadsheets and having the data from one sheet use data from another. Unlike spreadsheet programs like Excel or Numbers, relational databases like MySQL are able to manipulate millions of rows rapidly and effectively. Relational databases are the most common way to permanently store data, with MySQL as one of the most popular and common.

While we will be focusing on MySQL, other common database management systems (for example, Oracle or Microsoft SQL Server) will behave very similarly, and the SQL language is almost the same across all relational databases. It is common to hear talk of different "dialects" of SQL. This is because the language fundamentals are shared among RDBMS's, but some of the specifics or usage patterns might be different.

## Vocabulary

- **RDBMS**: The software that manages the data, i.e. handles its storage and retrieval. Runs the database server
- **Database**: Sometimes used interchangeably with a DBMS; The actual location of the data stored on disk; You won't interact with this directly, but rather, through the DBMS.
- **Database Client**: A program that can be used to connect to a database. Each database usually comes with an officially sanctioned command line client, and there are many different GUI database clients as well.
- **Database Server**: A computer that runs the DBMS and stores the data, typically either on-premises or in the cloud.
- **DDL**: Data definition language; commands that change the structure of the database or the DBMS itself, or change the structure of tables in the database. We will not be focusing on this part of SQL.
- **DML**: Data manipulation language; used to insert, update, delete, and retrieve information from databases. We will be focusing on the the retrieval part of this.

## Queries

We use the Structured Query Language (SQL) to interact with MySQL. SQL is made up of statements and commands sent to the server individually, with results sent back to the client. We often think of these statements as asking questions of the server; as in "who are the users named 'jason'?", "how many clients does this seller have?", "what movies were sold between May 5 and October 20?", etc. Because of this, these statements are generally called *queries*. SQL commands fall into several different categories, such as DDL and DML. Our focus will be on the retrieval part of the data manipulation language (DML).

Most of our output from MySQL will be formatted in a table. Something similar to:

    +----+----------+----------+----------+
    | id | Column 1 | Column 2 | Column 3 |
    +---------------+----------+----------+
    |  1 | Value A  | Value B  | Value C  |
    |  2 | Value D  | Value E  | Value F  |
    |  3 | Value G  | Value H  | Value I  |
    |  4 | Value J  | Value K  | Value L  |
    +----+----------+----------+----------+

## Ways to Connect to a MySQL Server

- [Sequel Workbench](https://www.mysql.com/products/workbench/) has lots of features and is a powerful MySQL Client.
- You can also use the MySQL Client from your Terminal. 
- How to connect to a SQL server through the terminal:
    - The abstract pattern is `mysql -h HOST -u USERNAME -p` then type in your password when prompted.
    - For a concrete example, imagine the host is `data.codeup.com`, your username is `example_user_1`, and the password `supersecurepassword2`.
        - `mysql -h data.codeup.com -u example_user_1 -p` and then you type in `supersecurepassword2` when prompted from the terminal.
        - For the avoidance of doubt, `example_user_1` is not a real live user.
        - To connect, you'll use the `host`, `user`, and `password` provided by your MySQL Administrator.

## SQL GUI Client

We will primarily be using [MySQL Workbench](https://www.mysql.com/products/workbench/) to interact with our database server, run queries, and see their results. Other clients exist, with similar functionality.

## Exercises

**From the command line:**

- Connect to the MySQL server from your terminal. Use `mysql -h ip.of.your.host -u your_username -p` then type in your MySQL password when prompted.
- Once connected to the MySQL server, run the following commands:
    - `SHOW DATABASES;`
    - `SELECT user, host FROM mysql.user;`
- Type `exit` to exit.

**From a GUI client:**

0. Open MySQL Workbench

1. Choose Standard for the connection type (i.e. not "Socket" or "SSH")

1. Name the connection "Codeup DB Server"

1. Enter the MySQL Host, Username, and Password provided by your instructors

1. Leave the Database, Port, and SSH Host blank

1. Click the "Test Connection" button to ensure that everything works as expected

1. Explore the UI of MySQL Workbench

    - How can you choose a database?
    - Select a database, and view the details of several tables
    - Explore the Structure, Content, and Query Icons
    - Where is the menu item for executing a database query?
    - What is the keyboard shortcut for executing all of the queries? The current query?

1. Once you are somewhat comfortable with the UI, run the database queries below. You are not expected to understand the syntax for these queries yet, just use them to see what query output looks like.

    ```sql
    SELECT * FROM mysql.user;
    SELECT user, host FROM mysql.user;
    SELECT * FROM mysql.help_topic;
    SELECT help_topic_id, help_category_id, url FROM mysql.help_topic;
    ```
    
1. Save the query as `mysql_introduction.sql`. 

**Running `.sql` scripts from the terminal**

In the abstract, `mysql -u USERNAME -p -h DB_HOST -t < filename.sql` will attempt to run a .sql file named
  `filename.sql` as your provided username on the specified MySQL server.
  
   - `DB_HOST`, `USERNAME`, and `filename.sql` are generic placeholders.

For example, `mysql -u codeup -h 123.123.123.123 -p -t < example.sql` attempts
  to run `example.sql` from the current working directory on the MySQL server at
  123.123.123.123.

1. Using the host name of the DS MySQL server (`data.codeup.com`) and your login credentials, run
  `mysql_introduction.sql` and observe the results delivered to your terminal.


**Set up a git respository for SQL module**

Using the [repo setup directions](https://ds.codeup.com/fundamentals/git/), setup a new local and remote repository for the SQL module. The local version of your repo should live inside of `~/codeup-data-science`. This repo should be named `database-exercises`.

1. Ensure that your repo is setup properly. `cd ~/codeup-data-science/database-exercises`. Type `git status`. You should see confirmation that you're in a repository and running `pwd` from this folder should show `~/codeup-data-science/database-exercises`.
1. In your new local repository, create a `README.md` file that explains the contents of the repository.
1. Add and commit your README.
1. Push your work to GitHub.

1. Also add, commit, push to GitHub the `mysql_introduction.sql` file you created earlier.

