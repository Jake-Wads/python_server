import pandas as pd
import numpy as np

import env

def get_db_url(db):
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'

def get_data_from_mysql(db_name):
    query = '''
    select trxn.parcelid
    , props.calculatedfinishedsquarefeet
    , props.bedroomcnt
    , props.bathroomcnt
    , props.taxvaluedollarcnt
    from zillow.predictions_2017 trxn
    left join zillow.properties_2017 props using(parcelid)
    where props.unitcnt = 1
    group by trxn.parcelid
    , props.calculatedfinishedsquarefeet
    , props.bedroomcnt
    , props.bathroomcnt 
    , props.taxvaluedollarcnt
    having month(max(trxn.transactiondate)) in (5,6) AND year(max(trxn.transactiondate)) = 2017;    
    '''
    df = pd.read_sql(query, get_db_url(db_name))
    return df

def clean_data(df):
    df.dropna(inplace=True)
    return df.drop(columns=['parcelid'])

def wrangle_zillow(db_name):
    df = get_data_from_mysql(db_name)
    df = clean_data(df)
    return df