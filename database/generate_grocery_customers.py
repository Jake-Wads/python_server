import pandas as pd
from pandas import DataFrame, Series
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from env import user, host, password

file = "./data/customers.csv"

df = pd.read_csv(file)
url = 'mysql://{}:{}@{}/grocery_db'.format(user, password, host)

dbc = create_engine(url)

df.to_sql('grocery_customers', dbc, index_label='customer_id', if_exists='replace')

from datetime import datetime
print(datetime.now(), 'DONE!')