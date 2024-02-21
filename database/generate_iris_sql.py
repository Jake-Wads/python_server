import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from pydataset import data

df: DataFrame = data('iris')

df.columns = [col.lower().replace('.', '_') for col in df]

lookup_species = {species: i + 1 for i, species in enumerate(df.species.unique())}

def to_sql(row: Series) -> str:
    species_id = lookup_species[row.species]
    return f'({row.sepal_length}, {row.sepal_width}, {row.petal_length}, {row.petal_width}, {species_id})'

measurement_values = ', '.join([to_sql(row) for _, row in df.iterrows()])

species_values = ', '.join([f"({id}, '{name}')" for name, id in lookup_species.items()])

sql = f'''
DROP DATABASE IF EXISTS iris_db;
CREATE DATABASE iris_db;
USE iris_db;

CREATE TABLE species(
    species_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    species_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (species_id)
);

CREATE TABLE measurements(
    measurement_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    sepal_length DECIMAL(3, 1) NOT NULL,
    sepal_width DECIMAL(3, 1) NOT NULL,
    petal_length DECIMAL(3, 1) NOT NULL,
    petal_width DECIMAL(3, 1) NOT NULL,
    species_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (measurement_id),
    FOREIGN KEY (species_id) REFERENCES species(species_id)
);

INSERT INTO species(species_id, species_name) VALUES {species_values};

INSERT INTO measurements(sepal_length, sepal_width, petal_length, petal_width, species_id) VALUES
{measurement_values};
'''

def get_iris_sql():
    return sql

if __name__ == '__main__':
    print(get_iris_sql())
