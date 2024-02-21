# K Nearest Neghbors

Make predictions based off of the closest observations.

Pros:

- Fast to train
- Intuitive
- can pick up on arbitrary patterns (unline logit or dtrees)
- one assumption: closer points are more similar

Cons:

- `k` is unknown
- Model parameter is the entire training dataset
- Prediction can be expensive (lazy)
- Because distance is used, scaling is important

## Plan

1. Demo KNN in a single dimension
2. Demo in 2 dimensions
3. See the need for scaling
4. Compare model performance on unscaled vs scaled data
5. How to choose `k` ? Visualize model performance

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import knn_lesson_util as util
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

plt.rc('axes', grid=True)
plt.rc('figure', figsize=(12, 8.5))
plt.rc('axes.spines', top=False, right=False)

train, test = knn_lesson_util.get_ice_cream_data()
train.head()
```

## Sinle Dim

```python
# util.plot_pints(train)
util.plot_pints(train, test, True)
```

## 2 Dim

```python
# note that there's not as much seperation in the y direction, and the units are v different
# util.plot_pints_and_sprinkles(train, test)
util.plot_pints_and_sprinkles(train, test, plot_test=True)
```

```python
X_train = train[['pints', 'n_sprinkles']]
X_test = test[['pints', 'n_sprinkles']]
y_train = train.flavor
y_test = test.flavor
```

```python
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train, y_train)
knn.score(X_test, y_test)
```

```python
util.plot_pints_and_sprinkles(train, test, plot_test=True, same_xy_scale=True)
```

```python
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn.fit(X_train_scaled, y_train)
knn.score(X_test_scaled, y_test)
```

```python
util.plot_k_vs_accuracy(X_train_scaled, y_train, X_test_scaled, y_test)
```

**beware, only 2 dims limitiations**

## More complex Example

```python
train, test = util.get_complex_data()

X_train = train[['pints', 'n_sprinkles']]
X_test = test[['pints', 'n_sprinkles']]
y_train = train.flavor
y_test = test.flavor

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

```python
util.plot_k_vs_accuracy(X_train_scaled, y_train, X_test_scaled, y_test)
```

```python
k = 15
knn = KNeighborsClassifier(n_neighbors=k).fit(X_train_scaled, y_train)

train['correct'] = knn.predict(X_train_scaled) == train.flavor
test['correct'] = knn.predict(X_test_scaled) == test.flavor
```

```python
util.plot_misses(train, test)
```
