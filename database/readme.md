# Codeup Data Science Database

## Setup

1. Create and provision a VPS with [cods](https://github.com/zgulde/cods).
1. Run the `provision.sh` script to allow external access to the MySQL database.
1. Run the `seed_db.py` script to fill the database with data (alternatively,
   restore from a database backup).

## Usage

1. Run `create_users.py` to create user accounts for the data science
   students.
1. Run `db_connect.py` to open a REPL to the production mysql database. (This
   script assumes you have the `mysql` command line client installed locally.)
