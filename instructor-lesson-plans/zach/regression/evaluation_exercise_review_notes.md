# Regression Evaluation

```python
import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydataset
import scipy.stats as stats
import sklearn.metrics
from statsmodels.formula.api import ols
```

Punchline: is our model better than the model that just predicts the average?

The best model we can make with no additional information: $\hat{y} = \bar{y}$


## Setup / Functions

```python
def residuals(actual, predicted):
    return predicted - actual

def sse(actual, predicted):
    return (residuals(actual, predicted) ** 2).sum()

def mse(actual, predicted):
    n = actual.shape[0]
    return sse(actual, predicted) / n

def rmse(actual, predicted):
    return math.sqrt(mse(actual, predicted))

def ess(actual, predicted):
    return ((predicted - actual.mean()) ** 2).sum()

def tss(actual):
    return ((actual - actual.mean()) ** 2).sum()
```

```python
def r2_score(actual, predicted):
    return ess(actual, predicted) / tss(actual)
```

```python
def plot_residuals(actual, predicted):
    residuals = actual - predicted
    plt.hlines(0, actual.min(), actual.max(), ls=':')
    plt.scatter(actual, residuals)
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title('Actual vs Residual')
    return plt.gca()

def regression_errors(actual, predicted):
    return {
        'sse': sse(actual, predicted),
        'ess': ess(actual, predicted),
        'tss': tss(actual),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
    }

def baseline_mean_errors(actual):
    predicted = actual.mean()
    return {
        'sse': sse(actual, predicted),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
    }

def better_than_baseline(actual, predicted):
    sse_baseline = sse(actual, actual.mean())
    sse_model = sse(actual, predicted)
    return sse_model < sse_baseline

def model_significance(ols_model):
    return {
        'r^2 -- variance explained': ols_model.rsquared,
        'p-value -- P(data|model == baseline)': ols_model.f_pvalue,
    }
```

## Using the Functions


### Tips

```python
tips = pydataset.data('tips')
```

```python
model = ols('tip ~ total_bill', tips).fit()
```

```python
actual = tips.tip
predicted = model.predict(tips.total_bill)
```

```python
plot_residuals(actual, predicted)
```

```python
regression_errors(actual, predicted)
```

```python
better_than_baseline(actual, predicted)
```

```python
model_significance(model)
```

```python
r2 = r2_score(actual, predicted)
r2
```

```python
tips.corr().loc['total_bill', 'tip'] ** 2
```

```python
# also sklearn.metrics.explained_variance_score
sklearn_r2 = sklearn.metrics.r2_score(actual, predicted)

r2 == sklearn_r2
```

```python
np.isclose(r2, sklearn_r2)
```

### mpg


## Visualizing Residuals

```python
def plot_residuals(actual, predicted):
    residuals = actual - predicted

    fig, axs = plt.subplots(2, 2, figsize=(12, 12))
    axs[0, 0].hist(residuals, bins=20, ec='black', fc='white')
    axs[0, 0].set(title="Distribution of Residuals")

    axs[0, 1].scatter(actual, predicted, marker='.', c='firebrick')
    axs[0, 1].plot([actual.min(), actual.max()], [actual.min(), actual.max()], ls=':', color='black')
    axs[0, 1].set(title="Actual vs Predicted", xlabel="$y$", ylabel=r"$\hat{y}$")

    axs[1, 0].scatter(actual, residuals, marker='.', c='firebrick')
    axs[1, 0].hlines(0, actual.min(), actual.max(), ls=':', color='black')
    axs[1, 0].set(title="Actual vs Residuals", xlabel="$y$", ylabel=r"$y - \hat{y}$")

    axs[1, 1].scatter(predicted, residuals, marker='.', c='firebrick')
    axs[1, 1].hlines(0, actual.min(), actual.max(), ls=':', color='black')
    axs[1, 1].set(
        title="Predicted vs Residuals", xlabel=r"$\hat{y}$", ylabel=r"$y - \hat{y}$"
    )

    return fig, axs
```

```python
plot_residuals(actual, predicted)
```
