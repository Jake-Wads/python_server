import pandas as pd
from sklearn.model_selection import train_test_split

def clean_data(df):
    '''
    This function will drop any duplicate observations, 
    drop ['deck', 'embarked', 'class', 'age'], fill missing embark_town with 'Southampton'
    and create dummy vars from sex and embark_town. 
    '''
    df = df.drop_duplicates()
    df = df.drop(columns=['deck', 'embarked', 'class', 'age'])
    df['embark_town'] = df.embark_town.fillna(value='Southampton')
    return df

def split_data(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames; stratify on survived.
    return train, validate, test DataFrames.
    '''
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.survived)
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.survived)
    return train, validate, test


def prep_titanic_data(df):
    '''
    This function takes in a df and will drop any duplicate observations, 
    drop ['deck', 'embarked', 'class', 'age'], fill missing embark_town with 'Southampton'
    create dummy vars from sex and embark_town, and perform a train, validate, test split. 
    Returns train, validate, and test DataFrames
    '''
    df = clean_data(df)
    train, validate, test = split_data(df)
    return train, validate, test


# from pandas import DataFrame
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split

# def handle_missing_values(df):
#     return df.assign(
#         embark_town=df.embark_town.fillna('Other'),
#         embarked=df.embarked.fillna('O'),
#     )

# def remove_columns(df):
#     return df.drop(columns=['deck'])

# def encode_embarked(df):
#     encoder = LabelEncoder()
#     encoder.fit(df.embarked)
#     return df.assign(embarked_encode = encoder.transform(df.embarked))

# def prep_titanic_data(df):
#     df = df\
#         .pipe(handle_missing_values)\
#         .pipe(remove_columns)\
#         .pipe(encode_embarked)
#     return df

# def train_validate_test_split(df, seed=123):
#     train_and_validate, test = train_test_split(
#         df, test_size=0.2, random_state=seed, stratify=df.survived
#     )
#     train, validate = train_test_split(
#         train_and_validate,
#         test_size=0.3,
#         random_state=seed,
#         stratify=train_and_validate.survived,
#     )
#     return train, validate, test