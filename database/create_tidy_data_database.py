import os
import pandas as pd
import env

DB_URL = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/tidy_data'

for file in os.listdir('data/untidy-data'):
    if not file.endswith('.csv'):
        continue
    sql_table_name = file.replace('.csv', '')
    df = pd.read_csv(f'data/untidy-data/{file}')
    print(f'Columns: {list(df)}')
    print(f'Writing {file} to tidy_data.{sql_table_name}')
    df.to_sql(sql_table_name, DB_URL, index=False)
