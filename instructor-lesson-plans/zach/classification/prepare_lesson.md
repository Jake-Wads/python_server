```python
import pandas as pd
import numpy as np
import sklearn.impute
import sklearn.model_selection
import sklearn.preprocessing

import acquire

df = acquire.get_titanic_data()
print('%d rows by %d columns' % df.shape)
df.head()
```

## All Together


How many missing values do we have?

```python
df.isna().sum()
```

Is `embarked` the same as `embarked_town`?

```python
pd.crosstab(df.embark_town, df.embarked)
```

Takeaway: drop one (`embarked`)

```python
df = df.drop(columns='embarked')
```

What's the difference between `class` and `pclass`?

```python
pd.crosstab(df['class'], df.pclass)
```

Takeaway: drop `class`

```python
df = df.drop(columns='class')
```

Data Prep

1. deck -- drop
1. age -- fill with mean
1. class -- already done for us with `pclass`
1. embark_town -- fill w/ most frequent (`.value_counts` + `.fillna`)
1. embark_town -- one-hot encode
1. age -- fill with mean of class + sex

```python
df = df.drop(columns=['deck'])
```

```python
train, test = sklearn.model_selection.train_test_split(df, random_state=123, train_size=.8)
```

```python
imputer = sklearn.impute.SimpleImputer(strategy='mean')
imputer.fit(train[['age']])
train.age = imputer.transform(train[['age']])
test.age = imputer.transform(test[['age']])
```

```python
train.embark_town.value_counts()
```

```python
train.embark_town = train.embark_town.fillna('Southampton')
test.embark_town = test.embark_town.fillna('Southampton')
```

```python
encoder = sklearn.preprocessing.OneHotEncoder()
encoder.fit(train[['embark_town']])

assert (encoder.transform(train[['embark_town']]).sum(axis=1) == 1).all()

m = encoder.transform(train[['embark_town']]).todense()
pd.concat([
    train[['embark_town']],
    pd.DataFrame(m, columns=encoder.categories_[0], index=train.index),
], axis=1)
```

```python
m = encoder.transform(train[['embark_town']]).todense()
cols = ['embark_town_' + c for c in encoder.categories_[0]]
train = pd.concat([
    train,
    pd.DataFrame(m, columns=cols, index=train.index),
], axis=1).drop(columns='embark_town')

m = encoder.transform(test[['embark_town']]).todense()
cols = ['embark_town_' + c for c in encoder.categories_[0]]
test = pd.concat([
    test,
    pd.DataFrame(m, columns=cols, index=test.index),
], axis=1).drop(columns='embark_town')
```

```python
train
```

```python
age_by_sex_by_class = (
    train.groupby(['sex', 'pclass'], as_index=False)
    .age.mean()
    .rename(columns={'age': 'age_imputed'})
)
train = (
    pd.merge(age_by_sex_by_class, train, on=['sex', 'pclass'])
    .assign(age=lambda df: np.where(df.age.isna(), df.age_imputed, df.age))
    .drop(columns='age_imputed')
)
test = (
    pd.merge(age_by_sex_by_class, test, on=['sex', 'pclass'])
    .assign(age=lambda df: np.where(df.age.isna(), df.age_imputed, df.age))
    .drop(columns='age_imputed')
)
```

```python
def encode_embark_town(train, test):
    encoder = sklearn.preprocessing.OneHotEncoder()
    encoder.fit(train[['embark_town']])
    
    m = encoder.transform(train[['embark_town']]).todense()
    cols = ['embark_town_' + c for c in encoder.categories_[0]]
    train = pd.concat([
        train,
        pd.DataFrame(m, columns=cols, index=train.index),
    ], axis=1).drop(columns='embark_town')

    m = encoder.transform(test[['embark_town']]).todense()
    cols = ['embark_town_' + c for c in encoder.categories_[0]]
    test = pd.concat([
        test,
        pd.DataFrame(m, columns=cols, index=test.index),
    ], axis=1).drop(columns='embark_town')
    
    return train, test

def impute_age(train, test):
    age_by_sex_by_class = (
        train.groupby(['sex', 'pclass'], as_index=False)
        .age.mean()
        .rename(columns={'age': 'age_imputed'})
    )
    train = (
        pd.merge(age_by_sex_by_class, train, on=['sex', 'pclass'])
        .assign(age=lambda df: np.where(df.age.isna(), df.age_imputed, df.age))
        .drop(columns='age_imputed')
    )
    test = (
        pd.merge(age_by_sex_by_class, test, on=['sex', 'pclass'])
        .assign(age=lambda df: np.where(df.age.isna(), df.age_imputed, df.age))
        .drop(columns='age_imputed')
    )
    return train, test

def impute_age(train, test):
    imputer = sklearn.impute.SimpleImputer(strategy='mean')
    imputer.fit(train[['age']])
    train.age = imputer.transform(train[['age']])
    test.age = imputer.transform(test[['age']])
    return train, test

def impute_embark_town(train, test):
    train.embark_town.fillna('Southampton')
    test.embark_town.fillna('Southampton')
    return train, test

def prep_titanic(df):
    df = df.drop(columns=['deck', 'class', 'embarked'])
    train, test = sklearn.model_selection.train_test_split(df)
    train, test = impute_age(train, test)
    train, test = impute_embark_town(train, test)
    train, test = encode_embark_town(train, test)
    return train, test
```
