# Data Reshaping + Tidy Data

- [Data Reshaping](#Data-Reshaping)
    - [Melt Example](#Melt-Example)
    - [Pivot Table Example](#Pivot-Table-Example)
- [Tidy Data](#Tidy-Data)
    - [One Column with Multiple Variables](#One-Column-with-Multiple-Variables)
    - [One Variable in Multiple Columns](#One-Variable-in-Multiple-Columns)
    - [Multiple vars in 2 columns](#Multiple-vars-in-2-columns)
    - [Another gnarly example](#Another-gnarly-example)
    - [A More Complex Example](#A-More-Complex-Example)

```python
import pandas as pd
import numpy as np
```

## Data Reshaping

- **long** data has many rows and few columns
- **wide** data has many columns
- a **melt** takes the data from wide to long
- a **spread**, or **pivot** takes the data from long to wide
- a **transpose** rotates the dataframe 90 degrees


### Melt Example

```python
np.random.seed(123)

# simple data for demonstration
df = pd.DataFrame({
    'a': np.random.randint(1, 11, 3),
    'b': np.random.randint(1, 11, 3),
    'c': np.random.randint(1, 11, 3),
    'x': np.random.randint(1, 11, 3),
    'y': np.random.randint(1, 11, 3),
    'z': np.random.randint(1, 11, 3),    
})
df.head()
```

Different ways of using `.melt`:

```python
# df.melt()
# df.melt(id_vars='a')
# df.melt(id_vars='x')
# df.melt(id_vars=['a', 'b'])
# df.melt(value_vars=['x', 'y', 'z'])
# df.melt(id_vars=['a', 'b'], value_vars=['x', 'y'], var_name='foo', value_name='bar')
```

### Pivot Table Example

```python
np.random.seed(123)
df = pd.DataFrame({
    'group': np.random.choice(['A', 'B', 'C'], 20),
    'subgroup': np.random.choice(['one', 'two'], 20),
    'x': np.random.randn(20),
})
df.head()
```

```python
df.pivot_table('x', 'subgroup', 'group')
```

## Tidy Data

Tidy Data Characteristics:

- data is tabular, i.e. made up of rows and columns
- there is one value per cell
- each variable is a column
- each observation is a row

General Ideas

- If the units are the same, maybe they should be in the same column
- If one column has measurements of different units, it should be spread out
- Should you be able to groupby some of the columns? combine them
- Can I pass this data to seaborn?
- Can we ask interesting questions and answer them with a group by? I.e. generally we **don't** want to be taking row or column averages.

For the rest of this lesson, we'll look at data that is **not** tidy.


### One Column with Multiple Variables

```python
df = pd.DataFrame({
    'name': ['Sally', 'Jane', 'Billy', 'Suzy'],
    'pet': ['dog: max', 'dog: buddy', 'cat: grizabella', 'hamster: fred']
})
df
```

### One Variable in Multiple Columns

```python
np.random.seed(123)

df = pd.DataFrame(
    np.random.uniform(60, 100, (4, 4)),
    columns=['Sally', 'Jane', 'Billy', 'Suzy'],
    index = pd.Index(['spelling', 'math', 'reading', 'nuclear physics'], name='subject')
).round(1).reset_index()
df
```

- what is the average spelling grade?
- What is Jane's average grade?

Sometimes it is desirable to "untidy" the data for quick analysis / visualization. E.g. spread subject out to columns, students as rows.


### Multiple vars in 2 columns

- "incorrect melt"

```python
df = pd.read_csv('./tidy_data/gapminder1.csv')
df.head()
```

### Another gnarly example

```python
df = pd.read_csv('tidy_data/gapminder2.csv')
df.head()
```

```python
df = df.melt(id_vars='country')
df['year'] = df.variable.str[-4:]
df['measure'] = df.variable.str[:-5]
df = df.drop(columns=['variable'])
df = df.pivot_table('value', ['country', 'year'], 'measure').reset_index()
df.columns.name = ''
df
```

### A More Complex Example

```python
sales = pd.read_csv('./tidy_data/sales.csv')
sales
```

```python
sales_melt = sales.melt(id_vars='Product', var_name='year_and_measure')

year_and_measure_df = sales_melt.year_and_measure.str.split(' ', expand=True)
year_and_measure_df.columns = ['year', 'measure']

sales2 = pd.concat([sales_melt, year_and_measure_df], axis=1).drop(columns='year_and_measure')

sales_tidy = sales2.pivot_table(index=['Product', 'year'], columns='measure', values='value')

sales_tidy.columns.name = ''
sales_tidy.reset_index(inplace=True)
sales_tidy
```
