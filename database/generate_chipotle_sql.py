import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

df: DataFrame = pd.read_csv('data/chipotle.tsv', sep='\t')

def format_row(row: Series) -> str:
    return (f'({row.order_id}, {row.quantity}, \'{row.item_name}\','
            f'\'{row.choice_description}\', \'{row.item_price}\')')

values = ', '.join([format_row(row) for _, row in df.iterrows()])

sql = f'''
DROP TABLE IF EXISTS orders;
CREATE TABLE orders(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    order_id INT UNSIGNED NOT NULL,
    quantity INT UNSIGNED NOT NULL,
    item_name VARCHAR(64) NOT NULL,
    choice_description TEXT,
    item_price VARCHAR(16) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO orders(order_id, quantity, item_name, choice_description, item_price)
VALUES {values};
'''

def get_sql():
    return sql

if __name__ == '__main__':
    print(get_sql())
