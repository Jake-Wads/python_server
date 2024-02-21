'''
Script to create database users for all the students and give them correct
permissions in the database.


Example usage for a new cohort

python create_users.py -u florence01 florence02 florence03 florence04 florence05 florence06 florence07 florence08 florence09 florence10 florence11 florence12 florence13 florence14 florence15 florence16 florence17 florence18 florence19 florence20 florence21 -f ./florence.csv
usage: python create_users.py -u user01 user02 user03 -f ./new_users.csv
'''

# TODO: admin user w/ all permissions
# TODO: remove a user

import warnings
from random import choice
from string import ascii_letters
from typing import List, NamedTuple
from sqlalchemy.engine import Engine
from sqlalchemy import text
from tqdm import tqdm
from util import get_connection, log


DATABASES = [
    '311_data',
    'albums_db',
    'chipotle',
    'curriculum_logs',
    'elo_db',
    'employees',
    'farmers_market',
    'fruits_db',
    'iris_db',
    'join_example_db',
    'grocery_db',
    'home_credit',
    'logs',
    'mall_customers',
    'numbers',
    'pizza',
    'quotes_db',
    'saas_llc',
    'sakila',
    'school_sample',
    'svi_db',
    'spam_db',
    'superstore_db',
    'telco_churn',
    'telco_normalized',
    'tidy_data',
    'titanic_db',
    'tsa_item_demand',
    'world',
    'zillow',
]


Credential = NamedTuple('Credentials', username=str, password=str)
Credentials = List[Credential]


DROP_USER = "DROP USER IF EXISTS {}@'%%'"
DROP_USER_DB = 'DROP DATABASE IF EXISTS {}'
CREATE_USER_QUERY = "CREATE USER {}@'%%' IDENTIFIED BY '{}'"
CREATE_USER_DB = 'CREATE DATABASE IF NOT EXISTS {}'
REVOKE_PERMISSIONS = "REVOKE ALL PRIVILEGES, GRANT OPTION FROM {}@'%%'"
GRANT_PERMISSIONS = "GRANT SELECT ON {} to {}@'%%'"
GRANT_USER_DB_PERMISSIONS = "GRANT ALL ON {}.* to {}@'%%'"


def mkpassword(length=32):
    'generate a random sequence of letters and numbers'
    letters = [*'0123456789', *ascii_letters]
    return ''.join([choice(letters) for _ in range(length)])


def create_user(dbc: Engine, username: str, password: str, with_user_db=True) -> None:
    'create a user and set appropriate permissions. Optionally create a database for the user'
    with dbc.connect() as conn:
        conn.execute(text(DROP_USER.format(username)))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            conn.execute(text(DROP_USER_DB.format(username)))
        conn.execute(text(CREATE_USER_QUERY.format(username, password)))
        conn.execute(text(REVOKE_PERMISSIONS.format(username)))
        for database in DATABASES:
            conn.execute(text(GRANT_PERMISSIONS.format(database + '.*', username)))
        conn.execute(text(GRANT_PERMISSIONS.format('mysql.help_topic', username)))
        conn.execute(text(GRANT_PERMISSIONS.format('mysql.user', username)))
        if with_user_db:
            conn.execute(text(CREATE_USER_DB.format(username)))
            conn.execute(text(GRANT_USER_DB_PERMISSIONS.format(username, username)))


def main(credentials: Credentials, credentials_filepath: str):
    'Open the database connection, create the users, and store credentials to a text file'
    log('Opening DB Connection')
    dbc = get_connection('')
    with open(credentials_filepath, 'a+') as credentials_file:
        for username, password in tqdm(credentials):
            create_user(dbc, username, password)
            credentials_file.write(f'{username}:{password}\n')
    log('All Done!')


if __name__ == '__main__':
    import argparse

    print("How to use this script: python create_users.py -u user01 user02 user03 -f new_users.csv")

    parser = argparse.ArgumentParser()
    parser.description = 'Add a user or users to the production data science database.'
    parser.add_argument('-u', '--usernames', required=True, nargs='+',
                        help='username(s) of the user(s) to create')
    parser.add_argument('-f', '--file', required=True,
                        help='file to store credentials in')

    args = parser.parse_args()

    credentials = [Credential(username, mkpassword()) for username in args.usernames]

    main(credentials, args.file)
