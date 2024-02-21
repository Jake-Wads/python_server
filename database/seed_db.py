# TODO: world, sakila, and employees databases?
# Sakila: https://dev.mysql.com/doc/sakila/en/sakila-installation.html
# Employees: https://github.com/datacharmer/test_db
# World: https://dev.mysql.com/doc/world-setup/en/world-setup-installation.html

import warnings
from os import system, chdir
from subprocess import run
import pandas as pd
from pandas import DataFrame, Series
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from tqdm import tqdm

from util import log, get_connection, partition, get_mysql_command

# https://stackoverflow.com/questions/39494056/progress-bar-for-pandas-dataframe-to-sql
def insert_with_progress(df, conn, table_name, chunksize=1000, **kwargs):
    with tqdm(total=len(df)) as pbar:
        for i, cdf in enumerate(partition(df, chunksize)):
            replace = "replace" if i == 0 else "append"
            cdf.to_sql(con=conn, name=table_name, if_exists=replace, **kwargs)
            pbar.update(chunksize)


DATABASES = [
    'titanic_db', 'elo_db', 'iris_db', 'chipotle', 'fruits_db', 'telco_churn',
    'join_example_db', 'albums_db', 'tsa_item_demand', 'mall_customers',
    'svi_db', 'zillow', 'numbers'
]


def create_databases():
    log('<<<<< Ensure Databases Are Created >>>>>')
    dbc = get_connection('')
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for db in DATABASES:
            dbc.execute(f'CREATE DATABASE IF NOT EXISTS {db}')


def seed_world_db():
    log('<<<<< World DB >>>>>')
    from env import user, host, password
    download = 'wget http://downloads.mysql.com/docs/world.sql.gz'
    log(download)
    system(download)
    unzip = 'gunzip -f world.sql.gz'
    log(unzip)
    system(unzip)
    seed_db = 'mysql --host={} --user={} -p{} < world.sql'.format(host, user, password)
    log(seed_db)
    system(seed_db)
    log('Finished World DB')


def seed_employees_db():
    log('<<<<< Employees DB >>>>>')
    from env import host, password, user
    git_clone = 'git clone --depth=1 https://github.com/datacharmer/test_db employees_db'
    log(git_clone)
    system(git_clone)
    chdir('employees_db')
    seed_db = 'mysql --host={} --user={} -p{} < employees.sql'.format(host, user, password)
    log(seed_db)
    system(seed_db)
    log('Finished Employees DB')


def seed_numbers_db():
    log('<<<<< Numbers DB >>>>>')
    log('- getting database connection')
    dbc = get_connection('numbers')
    log('- creating & seeding table')
    queries = [
        'DROP TABLE IF EXISTS numbers',
        'DROP TABLE IF EXISTS numbers_with_groups',
        'DROP TABLE IF EXISTS numbers_with_more_groups',
        'CREATE TABLE numbers(n INT)',
        'INSERT INTO numbers(n) VALUES (1),(2),(3),(4),(5),(6),(7),(8),(9),(10)',
        'CREATE TABLE numbers_with_groups(n INT NOT NULL, category CHAR(1) NOT NULL)',
        ('INSERT INTO numbers_with_groups(n, category) VALUES '
         "(1, 'a'), (2, 'b'), (3, 'c'), (4, 'a'), (5, 'b'), (6, 'c'), "
         "(7, 'a'), (8, 'b'), (9, 'c'), (10, 'a')"),
        ('CREATE TABLE numbers_with_more_groups(n INT NOT NULL, '
            'category CHAR(1) NOT NULL, supergroup CHAR(3))'),
        ('INSERT INTO numbers_with_more_groups(n, category, supergroup) VALUES '
         "(1, 'a', 'one'), (2, 'b', 'two'), (3, 'c', 'one'), (4, 'a', 'two'), (5, 'b', 'one'),"
         "(6, 'c', 'two'), (7, 'a', 'one'), (8, 'b', 'two'), (9, 'c', 'one'), (10, 'a', 'two')")
    ]
    for query in tqdm(queries):
        dbc.execute(query)
    log('Finished Numbers DB')


def seed_titanic_db():
    log('<<<<< Titanic Data >>>>>')
    log('- loading from seaborn')
    import seaborn as sns
    titanic = sns.load_dataset('titanic')
    log('- creating database connection')
    dbc = get_connection('titanic_db')
    log('- creating table & seeding')
    # Drop constructed features
    titanic.drop(columns=['adult_male', 'who', 'alive'], inplace=True)
    insert_with_progress(titanic, dbc, 'passengers',
                         500, index_label='passenger_id')
    log('- adding passenger_id as primary key')
    dbc.execute('ALTER TABLE passengers ADD PRIMARY KEY (passenger_id)')
    log('Finished Titanic Data')


def seed_iris_db():
    log('<<<<< Iris Data >>>>>')
    log('- importing module')
    from generate_iris_sql import get_iris_sql
    log('- running sql')
    sql = get_iris_sql()
    cmd = get_mysql_command()
    run(cmd, input=sql, encoding='utf8')
    log('Finished Iris Data')


def seed_chipotle_db():
    log('<<<<< Chipotle Data >>>>>')
    log('- importing module')
    from generate_chipotle_sql import get_sql
    log('- creating database connection')
    dbc = get_connection('chipotle')
    log('- running sql')
    dbc.execute(get_sql())
    log('Finished Chipotle Data')


def seed_fruit_db():
    log('<<<<< Fruit Data >>>>>')
    log('- reading file')
    with open('./fruits_db_migration_and_seed.sql') as f:
        sql = f.read()
    log('- creating database connection')
    dbc = get_connection('fruits_db')
    log('- running sql')
    dbc.execute(sql)
    log('Finished Fruit Data')


def seed_join_example_db():
    log('<<<<< Join Example DB >>>>>')
    log('- reading file')
    with open('./join_example_db.sql') as f:
        sql = f.read()
    log('- creating database connection')
    dbc = get_connection('join_example_db')
    log('- running sql')
    dbc.execute(sql)
    log('Finished Join Example DB')


def seed_albums_db():
    log('<<<<< Albums Example DB >>>>>')
    log('- reading files')
    with open('./albums_migration.sql') as migration, open('./albums_seeder.sql') as seed:
        sql = migration.read() + seed.read()
    log('- creating database connection')
    dbc = get_connection('albums_db')
    log('- running sql')
    dbc.execute(sql)
    log('Finished Albums Example DB')


def seed_tsa_store_item_demand():
    log('<<<<< TSA Store Item Demand >>>>>')
    log('- importing module')
    from tsa_store_item_demand import get_db_structure, get_stores_sql, get_items_sql, get_sales_sql
    log('- creating database connection')
    dbc = get_connection('tsa_item_demand')
    log('- creating db structure')
    dbc.execute(get_db_structure())
    log('- inserting stores')
    dbc.execute(get_stores_sql())
    log('- inserting items')
    dbc.execute(get_items_sql())
    log('- inserting sales (batch size: 10,000)')
    for stmt in tqdm(get_sales_sql(10_000)):
        dbc.execute(stmt)
    log('Finished TSA Store Item Demand')


def seed_mall_customers():
    log('<<<<< Mall Customers Data >>>>>')
    log('- reading csv')
    df = pd.read_csv('./data/Mall_Customers.csv')
    df.columns = ['customer_id', 'gender',
                  'age', 'annual_income', 'spending_score']
    log('- creating db connection')
    dbc = get_connection('mall_customers')
    log('- inserting data')
    df.to_sql('customers', dbc, if_exists='replace', index=False)
    log('- adding customer_id as primary key')
    dbc.execute('ALTER TABLE customers ADD PRIMARY KEY (customer_id)')
    log('Finished Mall Customers Data')


def seed_telco_churn():
    log('<<<<< Telco Customer Churn >>>>>')
    log('- importing data frames')
    from normalize_telco_churn import customers, internet_service_types, payment_types, contract_types
    log('- creating database connection')
    dbc = get_connection('telco_churn')
    log('- dropping customers')
    dbc.execute('DROP TABLE IF EXISTS customers')
    log('- seeding lookup tables')
    internet_service_types.to_sql(
        'internet_service_types', dbc, index=False, if_exists='replace')
    payment_types.to_sql('payment_types', dbc,
                         index=False, if_exists='replace')
    contract_types.to_sql('contract_types', dbc,
                          index=False, if_exists='replace')
    log('- seeding customers')
    insert_with_progress(customers, dbc, 'customers',
                         chunksize=1000, index=False)
    log('- adding primary keys')
    statements = [
        'ALTER TABLE customers MODIFY customer_id CHAR(10)',
        'ALTER TABLE customers ADD PRIMARY KEY (customer_id)',
        'ALTER TABLE internet_service_types ADD PRIMARY KEY (internet_service_type_id)',
        'ALTER TABLE payment_types ADD PRIMARY KEY (payment_type_id)',
        'ALTER TABLE contract_types ADD PRIMARY KEY (contract_type_id)',
    ]
    for stmt in tqdm(statements):
        dbc.execute(stmt)
    log('- adding foreign key constraints')
    statements = [
        'ALTER TABLE customers ADD FOREIGN KEY fk_internet_service(internet_service_type_id) REFERENCES internet_service_types(internet_service_type_id)',
        'ALTER TABLE customers ADD FOREIGN KEY fk_payment(payment_type_id) REFERENCES payment_types(payment_type_id)',
        'ALTER TABLE customers ADD FOREIGN KEY fk_contract(contract_type_id) REFERENCES contract_types(contract_type_id)',
    ]
    for stmt in tqdm(statements):
        dbc.execute(stmt)
    log('Finished Telco Customer Churn')


def seed_svi():
    log('<<<<< SVI Data >>>>>')
    log('- getting database connection')
    dbc = get_connection('svi_db')
    log('- reading Texas data')
    df = pd.read_csv('data/Texas.csv')
    log('- inserting Texas data')
    insert_with_progress(df, dbc, 'texas', 1000, index_label='id')
    log('- reading SVI2014_US.csv')
    df = pd.read_csv('./data/SVI2014_US.csv')
    log('- inserting SVI2014_US')
    insert_with_progress(df, dbc, 'svi2014_us', 2000, index_label='id')
    log('- reading SVI2016_US.csv')
    df = pd.read_csv('./data/SVI2016_US.csv')
    log('- inserting SVI2016_US')
    insert_with_progress(df, dbc, 'svi2016_us', 2000, index_label='id')
    log('- reading SVI2016_US_COUNTY.csv')
    df = pd.read_csv('./data/SVI2016_US_COUNTY.csv')
    log('- inserting SVI2016_US_COUNTY')
    insert_with_progress(df, dbc, 'svi2016_us_county', 2000, index_label='id')
    log('Finished SVI Data')


def seed_zillow():
    log('<<<<< Zillow Data >>>>>')
    log('- getting database connection')
    dbc = get_connection('zillow')

    log('- reading and seeding lookup tables')
    sheets = [
        'HeatingOrSystemTypeID', 'PropertyLandUseTypeID', 'StoryTypeID',
        'AirConditioningTypeID', 'ArchitecturalStyleTypeID',
        'TypeConstructionTypeID', 'BuildingClassTypeID'
    ]

    for sheet in tqdm(sheets):
        table_name = sheet.replace('ID', '').lower()
        id = sheet.lower()
        df = pd.read_excel(
            './data/zillow/zillow_data_dictionary.xlsx', sheet_name=sheet)
        df.columns = [col.lower() for col in df]
        df.to_sql(table_name, dbc, if_exists='replace', index=False)
        dbc.execute(f'ALTER TABLE {table_name} ADD PRIMARY KEY ({id})')

    log('- reading predictions_2016')
    df = pd.read_csv('./data/train_2016_v2.csv')
    log('- seeding predictions_2016 (batch size: 10,000)')
    insert_with_progress(df, dbc, 'predictions_2016', 10_000, index_label='id')

    log('- reading predictions_2017')
    df = pd.read_csv('./data/train_2017.csv')

    log('- seeding predictions_2017 (batch size: 10,000)')
    insert_with_progress(df, dbc, 'predictions_2017', 10_000, index_label='id')

    log('- reading properties_2016')
    df = pd.read_csv('./data/properties_2016.csv')
    # TODO: correct data types

    log('- seeding properties_2016 (batch size: 50,000)')
    insert_with_progress(df, dbc, 'properties_2016', 50_000, index_label='id')

    log('- reading properties_2017')
    df = pd.read_csv('./data/properties_2017.csv')

    log('- seeding properties_2017 (batch size: 50,000)')
    insert_with_progress(df, dbc, 'properties_2017', 50_000, index_label='id')

    log('Finished Zillow Data')

# WARNING: This one takes ~ 1.5 hours to run
def seed_elo_db():
    log('<<<<< Elo Data >>>>>')
    log('- reading in historical transactions')
    df: DataFrame = pd.read_csv('./data/historical_transactions.csv')
    batch_size = 10_000
    log(f'- inserting transactions, batch size: {batch_size}')
    dbc = get_connection('elo_db')
    insert_with_progress(df, dbc, 'transactions',
                         batch_size, index_label='transaction_id')
    log('Finished Elo Data')


def seed_all():
    seed_titanic_db()
    seed_iris_db()
    seed_chipotle_db()
    seed_fruit_db()
    seed_join_example_db()
    seed_albums_db()
    seed_tsa_store_item_demand()
    seed_mall_customers()
    seed_telco_churn()
    seed_svi()
    seed_zillow()  # ~ one hour
    seed_elo_db()  # this one takes a long time (~1.5 hours)


if __name__ == '__main__':
    from sys import exit
    import argparse

    seeders = dict(titanic=seed_titanic_db, iris=seed_iris_db, chipotle=seed_chipotle_db,
                   fruit=seed_fruit_db, join_example=seed_join_example_db, albums=seed_albums_db,
                   tsa=seed_tsa_store_item_demand, mall=seed_mall_customers, telco=seed_telco_churn,
                   svi=seed_svi, zillow=seed_zillow, elo=seed_elo_db, all=seed_all,
                   numbers=seed_numbers_db, employees=seed_employees_db, world=seed_world_db)

    parser = argparse.ArgumentParser()
    parser.description = 'Seed the production Data Science Database'
    parser.add_argument('seeders', metavar='SEEDER', nargs='*',
                        help='name of the seeder(s) to run')
    parser.add_argument('--list-seeders', action='store_true',
                        help='list the names of the seeders and exit')
    args = parser.parse_args()

    if args.list_seeders:
        for seeder in sorted(seeders.keys()):
            print(f'- {seeder}')
        print('choosing "all" will run all of the seeders')
        exit(0)

    if len(args.seeders) < 1:
        print('Error: at least one seeder is required (try --help)')
        exit(1)

    seeder_fns = []
    for seeder in args.seeders:
        fn = seeders.get(seeder)
        if fn is None:
            print('Invalid seeder: {}'.format(seeder))
            exit(1)
        seeder_fns.append(fn)

    try:
        log('Starting Up')
        log('-----------')
        create_databases()
        for fn in seeder_fns:
            fn()
        log('All Done!')
    except KeyboardInterrupt:
        log('Interrupted! Exiting...')
