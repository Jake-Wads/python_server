# Splitting Time Series Data

- Use the last "unit" of data as the testing set, the rest as the training set

    For example if we have 4 years worth of data, the first 3 will be the
    training set and the last 3 will be the test set.

- Cross Validation

    The way we do cross validation with time series data is by taking a
    historical set of data, then predicting the closest future time set.

    `sklearn.model_selection.TimeSeriesSplit`: will give us back multiple
    overlapping splits that can be used for this purpose.

    ```python
    import numpy as np
    from sklearn.model_selection import TimeSeriesSplit
    x = np.arange(10).reshape(-1, 1)
    list(TimeSeriesSplit(n_splits=4).split(x))
    ```

        [(array([0, 1]), array([2, 3])),
         (array([0, 1, 2, 3]), array([4, 5])),
         (array([0, 1, 2, 3, 4, 5]), array([6, 7])),
         (array([0, 1, 2, 3, 4, 5, 6, 7]), array([8, 9]))]

    This gives us back the indices of the train and test sets, so it could be
    used like this:

    ```python
    for itrain, itest in TimeSeriesSplit(n_splits=4).split(df):
        train = df[itrain]
        test = df[itest]
        ...
    ```

