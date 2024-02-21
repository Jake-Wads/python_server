import pandas as pd
from pandas import DataFrame, Series
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

# import seaborn as sns
# sns.load_dataset('titanic').to_csv('./data/titanic.csv')

def chunk(l, n=1):
    return (l[i:i+n] for i in range(0, len(l), n))

df: DataFrame = pd.read_csv('./data/titanic.csv').iloc[:, 1:]

user, host, password = ('zach', '162.243.162.52', '18ef255558c15d97566fd9eeec8ce012')

url = 'mysql://{}:{}@{}/titanic_db'.format(user, password, host)

dbc: Engine = create_engine(url)

df.to_sql('passengers', dbc, index_label='passenger_id', if_exists='replace')
dbc.execute('ALTER TABLE passengers ADD PRIMARY KEY (passenger_id)')

from datetime import datetime
print(datetime.now(), 'DONE!')