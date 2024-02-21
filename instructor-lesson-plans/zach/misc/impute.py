import numpy as np
import pandas as pd

# TODO: refactor to allow a list of strings for group and join averages to the
# train and test splits with pd.merge


def impute_by_group_agg(
    train: pd.DataFrame, test: pd.DataFrame, x: str, group: str, aggfunc="mean"
):
    """
    Fills missing values in column ``x`` with the average x value by ``group``.

    The average ``x`` value by ``group`` will be calculated based on the train
    dataset, and then used to fill in missing values on both the train and the
    test datasets.

    >>> train = pd.DataFrame({'g': ['a', 'a', 'b', 'b'], 'x': [1, np.nan, 2, np.nan]})
    >>> train
       g    x
    0  a  1.0
    1  a  NaN
    2  b  2.0
    3  b  NaN
    >>> test = pd.DataFrame({'g': ['a', 'b'], 'x': [np.nan, 3]})
    >>> test
       g    x
    0  a  NaN
    1  b  3.0
    >>> train, test = impute_by_group_agg(train, test, 'x', 'g')
    >>> train
       g    x
    0  a  1.0
    1  a  1.0
    2  b  2.0
    3  b  2.0
    >>> test
       g    x
    0  a  1.0
    1  b  3.0
    """

    group_avg_lookup = train.groupby(group)[x].agg(aggfunc)

    train[x] = train[x].fillna(train[group].map(group_avg_lookup))
    test[x] = test[x].fillna(test[group].map(group_avg_lookup))
    return train, test
