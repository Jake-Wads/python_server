import pandas as pd
from util import get_connection
from sqlalchemy.types import String

def main():
    url = 'https://gist.githubusercontent.com/zgulde/f45e9c11cd556d2ff4d2441c6b79ff94/raw/a836f5447fb21e274e2729201d76b940825ba02b/train.csv'
    df = pd.read_csv(url)
    df = df.dropna()
    df = df.drop(columns='Row ID')
    # Extract customers
    customers = df.groupby('Customer ID')['Customer Name'].unique().str[0]
    df = df.drop(columns='Customer Name')
    # Extract categories
    t = df.groupby(['Category', 'Sub-Category']).size()
    t = t.reset_index().drop(columns=0)
    subcategories = pd.Series(
        {cat: i + 1 for i, cat in enumerate(df['Sub-Category'].unique())}
    )
    t['Category ID'] = t['Sub-Category'].map(subcategories)
    subcategories = t[['Category ID', 'Category', 'Sub-Category']]
    subcategories = subcategories.set_index('Category ID')
    df['Category ID'] = df['Sub-Category'].map(subcategories['Sub-Category'].reset_index().set_index('Sub-Category')['Category ID'])
    df = df.drop(columns=['Category', 'Sub-Category'])
    # Extract products
    products = df.groupby('Product ID')['Product Name'].unique().str[0]
    df = df.drop(columns='Product Name')
    # Extract regions
    regions = pd.Series({region: i + 1 for i, region in enumerate(df.Region.unique())})
    df['Region ID'] = df['Region'].map(regions)
    regions.index.name = 'Region Name'
    regions = regions.rename('Region ID')
    regions = regions.reset_index().set_index('Region ID')
    df = df.drop(columns='Region')
    # PK
    df = df.set_index('Order ID')

    # Create Database
    dbc = get_connection('')
    dbc.execute('CREATE DATABASE IF NOT EXISTS superstore_db')

    # Clear out old tables
    dbc = get_connection('superstore_db')
    tables = ['orders', 'customers', 'categories', 'products', 'regions']
    for table in tables:
        dbc.execute(f'DROP TABLE IF EXISTS {table}')

    # Fill with data
    customers.to_sql('customers', dbc, if_exists='replace', dtype={
        'Customer ID': String(8),
    })
    dbc.execute('ALTER TABLE customers ADD PRIMARY KEY (`Customer ID`)')
    subcategories.to_sql('categories', dbc, if_exists='replace')
    dbc.execute('ALTER TABLE categories ADD PRIMARY KEY (`Category ID`)')
    products.to_sql('products', dbc, if_exists='replace', dtype={
        'Product ID': String(15)
    })
    dbc.execute('ALTER TABLE products ADD PRIMARY KEY (`Product ID`)')
    regions.to_sql('regions', dbc, if_exists='replace')
    dbc.execute('ALTER TABLE regions ADD PRIMARY KEY (`Region ID`)')
    df.to_sql('orders', dbc, if_exists='replace', dtype={
        'Customer ID': String(8),
        'Product ID': String(15),
        'Order ID': String(14),
    })

    # Add FK constraints
    preamble = 'ALTER TABLE orders ADD FOREIGN KEY'
    fks = [
        ('customers', 'Customer ID'),
        ('categories', 'Category ID'),
        ('products', 'Product ID'),
        ('regions', 'Region ID')
    ]
    for table, column in fks:
        stmt = f'{preamble} fk_{table}(`{column}`) REFERENCES {table}(`{column}`)'
        dbc.execute(stmt)

if __name__ == '__main__':
    main()
