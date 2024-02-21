import numpy as np
import pandas as pd
from pandas import DataFrame, Series
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

import env


db = 'saas_llc'
path = 'data/saas_llc/'
files = ['customer_churn.csv', 'customer_invoice.csv', 'customer_mrr.csv', 'customer_signup.csv', 'customer.csv']
sql_table_names = ['churn', 'invoice', 'mrr', 'signup', 'customer_details']


def run_sql(db, tbl, insert_cols, df):
    '''
    This function open a connection to our mysql server to the named database (db) 
    with credentials stored in env.py 
    It will run a 'drop table if exists' for the sql table name passed (tbl)
    It will then (re)create the table with the columns and their types stored in the insert_cols string variable
    that is passed. 
    It will then insert the values from the dataframe passed (df). 
    '''
    url = 'mysql+pymysql://{}:{}@{}/{}'.format(env.user, env.password, env.host, db)
    dbc = create_engine(url)

    sql_drop = f'''DROP TABLE IF EXISTS {tbl};'''
    sql_create = f'''CREATE TABLE {tbl}({insert_cols});'''
    
    dbc.execute(sql_drop)
    dbc.execute(sql_create)

    df.to_sql(tbl, dbc, if_exists='replace', index=False)
    

def get_column_types(df):
    '''
    This function will get the column types of the dataframe passed (df)
    and it will return a string used to create the new table in sql.
    the string is each column name for the sql table followed by its sql datatype. 
    If the dataframe datatype is int64, it will add 'INT(64)' as the sql datatype. 
    If the dataframe datatype is float64, it will add 'DECIMAL(30,10)' as the sql datatype. 
    If the dataframe datatype is any other (like object), it will add 'VARCHAR(64)' as the sql datatype. 
    '''
    col_types = []
    for col in df.columns:
        if df[col].dtype == 'int64':
            col_types.append(f'{col} INT(64)')
        elif df[col].dtype == 'float64':
            col_types.append(f'{col} DECIMAL(30, 10)')
        else:
            col_types.append(f'{col} VARCHAR(64)')

    # using list comprehension, turn list of colnames and types to single string for insert statement. 
    insert_cols = ', '.join([str(col) for col in col_types]) 
    return insert_cols

def generate_tables():
    '''
    This function will read each the csv from the list of files in to a dataframe, set the sql table name (tbl)
    to be the associated item from the list of tables names (sql_table_names),
    run the get_column_types() function to generate a string for the creation of the sql table, 
    run the run_sql() function to drop, create and insert values into the sql table (tbl). 
    '''
    for i in range(len(files)):
        df = pd.read_csv(path+files[i])

        # Many of the csv's from this group of datasets begin with an appended column that was 
        # likely generated from an index with the file was written to a csv.
        # this will remove that column 'Unnamed: 0' from any of the dataframes where it exists. 
        if df.columns[0] == 'Unnamed: 0':
            df.drop(columns=['Unnamed: 0'], inplace=True)

        # column names are dates with dashes for the customer_mrr csv, so we are making the column names
        # acceptable for sql by removing the dashes and beginning the column names with d_ to 
        # indicate date. 
        if files[i] == 'customer_mrr.csv':
            df.columns = df.columns.str.replace('-','', regex=False)
            df.columns = df.columns.str.replace('^2', 'd_2', regex=True)
    
        # set sql table name
        tbl = sql_table_names[i]
    
        # to get insert_cols 
        insert_cols = get_column_types(df)
    
        # create table and insert rows 
        run_sql(db, tbl, insert_cols, df)

# to run:
# 
# import generate_saas_llc
# generate_saas_llc.generate_tables()
