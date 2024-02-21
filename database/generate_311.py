# add 311 migration + seed
# then add access to the create_users script 
# and add access to all existing users
# sort out the PySpark necessary to read + merge those tables for the lesson

import pandas as pd
from pandas import DataFrame, Series
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from env import user, host, password
from datetime import datetime

def generate_311():

    print("Writing 311 data to the database...")

    # The connection string needs to connect to something, so this is the default
    db = "mysql"
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'

    dbc = create_engine(url)

    db = "311_data"

    # Delete database if exists 311_data
    # Create database
    dbc.execute(f"""DROP DATABASE IF EXISTS {db};""")
    dbc.execute(f"""CREATE DATABASE {db};""")

    # Generate a new connection string to the fresh 311_data database
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'

    # Create the "source" table, which is the source of a 311 call
    file = "./data/source.csv"
    df = pd.read_csv(file)
    dbc = create_engine(url)
    df.to_sql('source', dbc, if_exists='replace')

    # Create the "dept" table, the table of city departments
    file = "./data/dept.csv"
    df = pd.read_csv(file)
    dbc = create_engine(url)
    df.to_sql('dept', dbc, if_exists='replace')


    # Create the "case" table, the table of 311 cases
    file = "./data/case.csv"
    df = pd.read_csv(file)
    dbc = create_engine(url)
    df.to_sql('cases', dbc, if_exists='replace')

    print("311 data written to the database")
    print("...")
    print("Optimizing Column Data Types...")

    dbc.execute("alter table source modify source_id CHAR(255);")
    dbc.execute("alter table source modify source_username CHAR(255);")
    dbc.execute("alter table cases drop column `index`;")
    dbc.execute("alter table cases modify case_closed CHAR(5);")
    dbc.execute("alter table cases modify case_id INT(11);")
    dbc.execute("alter table cases modify case_opened_date CHAR(32);")
    dbc.execute("alter table cases modify case_closed_date CHAR(32);")
    dbc.execute("alter table cases modify SLA_due_date CHAR(32);")
    dbc.execute("alter table cases modify case_late CHAR(3);")
    dbc.execute("alter table cases modify dept_division CHAR(255);")
    dbc.execute("alter table cases modify service_request_type CHAR(64);")
    dbc.execute("alter table cases modify case_status CHAR(6);")
    dbc.execute("alter table cases modify source_id CHAR(255); ")
    dbc.execute("alter table cases modify request_address CHAR(255);")
    dbc.execute("alter table dept drop column `index`;")
    dbc.execute("alter table dept modify dept_division CHAR(128);")
    dbc.execute("alter table dept modify dept_name CHAR(128);")
    dbc.execute("alter table dept modify standardized_dept_name CHAR(128);")
    dbc.execute("alter table dept modify dept_subject_to_SLA CHAR(128);")
    
    print(datetime.now(), 'DONE!')



if __name__ == '__main__':
    """Run this table creation if this script is executed from the command line"""
    generate_311()