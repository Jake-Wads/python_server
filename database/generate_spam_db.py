import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from env import user, host, password

import re
import unicodedata
import pandas as pd
import nltk

df = pd.read_csv('./data/spam_clean.csv')

url = 'mysql://{}:{}@{}/spam_db'.format(user, password, host)\

dbc = create_engine(url)

df.to_sql('spam', dbc, index_label='id', if_exists='replace')

from datetime import datetime
print(datetime.now(), 'DONE!')

# TODO: this does not create the database automatically