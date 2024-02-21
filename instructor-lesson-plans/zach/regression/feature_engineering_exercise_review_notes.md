```python
import pydataset
import sklearn.feature_selection
import sklearn.metrics
import sklearn.linear_model
```

```python
tips = pydataset.data('tips')
tips['tip_percentage'] = tips.tip / tips.total_bill
tips['price_per_person'] = tips.total_bill / tips['size']
tips.head()

X = tips[['total_bill', 'tip_percentage', 'price_per_person', 'size']]
y = tips.tip
```

```python
kbest = sklearn.feature_selection.SelectKBest(sklearn.feature_selection.f_regression, k=2)
kbest.fit(X, y)
X.columns[kbest.get_support()]
```

```python
lm = sklearn.linear_model.LinearRegression()
rfe = sklearn.feature_selection.RFE(lm, 2)
rfe.fit(X, y)
X.columns[rfe.support_]
```

```python
def kbest(X, y, k):
    kbest = sklearn.feature_selection.SelectKBest(
        sklearn.feature_selection.f_regression,
        k=k
    )
    kbest.fit(X, y)
    return X.columns[kbest.get_support()]

def rfe(X, y, k):
    lm = sklearn.linear_model.LinearRegression()
    selector = sklearn.feature_selection.RFE(lm, k)
    selector.fit(X, y)
    return X.columns[selector.support_]
```

```python
rfe(X, y, 3)
```

```python
kbest(X, y, 3)
```

```python
swiss = pydataset.data('swiss')

X = swiss.drop(columns='Fertility')
y = swiss.Fertility
```

```python
rfe(X, y, 3)
```

```python
kbest(X, y, 3)
```
