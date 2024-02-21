# Logistic Regression

0. Validate Split
1. What is logistic regression?

    $$ \frac{1}{1 + e^{-\sum{\beta_ix_i}}} $$
    
    * putting our ols formula into a transformation such that the outcome is a
    number between 0 and 1
    * Pros: fast to train and predict, probabilities, more interpretable than
    some models
    * Cons: not as interpretable as, e.g. dtrees; assumes feature independence
    * Good choice for a baseline to compare other models against

2. Analyzing our model
3. Choosing the best threshold

## Simple Example

Using just one predictor

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
import logistic_regression_util
plt.ion()
plt.style.use('ggplot')
```

```python
df = logistic_regression_util.get_macbook_data()
df.head()
```

```python
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 8.5))
df.query('macbook == 1').coolness.plot.hist(ax=ax1, bins=15, alpha=.8, title='macbook')
df.query('macbook == 0').coolness.plot.hist(ax=ax2, bins=15, alpha=.8, title='no macbook')
ax2.set(xlabel='coolness')
fig.tight_layout()
df.groupby('macbook').mean()
```

```python
model = smf.logit('macbook ~ coolness', df).fit()
df['prediction'] = model.predict(df)
```

```python
df.plot.scatter(y='macbook', x='coolness', label='Actual')
```

```python
ax = df.plot.scatter(y='macbook', x='coolness')
df.set_index('coolness').sort_index().prediction.plot(ax=ax)
ax.set(ylabel='P(macbook)')
plt.tight_layout()
```

We define a **threshold** for predicting the positive class. If the predicted
probability is above the threshold, then we predict 1, else 0.

- default .5
- threshold == 1, always predict negative (perfect precision)
- threshold == 0, always predict positive (perfect recall)

```python
df['yhat'] = (df.prediction > .5).astype(int)
df.head()
```

```python
# evaluate...
```

## Mini Exercise

1. Load the titanic dataset that you've put together from previous lessons.
2. Split your data into train and test datasets. Further split your training
data into train and validate sets.
3. Fit a logistic regression model on your training data using sklearn's
linear_model.LogisticRegression class. Use fare and pclass as the
predictors.
4. Use the model's `.predict` method. What is the output?
5. Use the model's `.predict_proba` method. What is the output? Why do you
think it is shaped like this?
6. Evaluate your model's predictions on the validate data set. How accurate
is the mode? How does changing the threshold affect this?


## More Complex Example

train-test-validate split

```python
df = sns.load_dataset('titanic')[['survived', 'age', 'pclass', 'sex']].dropna()
train, test = train_test_split(df, random_state=14, train_size=.85)
train, validate = train_test_split(train, random_state=14, train_size=.85)
print('   train: %d rows x %d columns' % train.shape)
print('validate: %d rows x %d columns' % validate.shape)
print('    test: %d rows x %d columns' % test.shape)
```

```python
model = smf.logit('survived ~ age + pclass + sex', train).fit()
model.summary()
```

```python
dataset = validate
t = .5
probs = model.predict(dataset)
y = dataset.survived
yhat = (probs > t).astype(int)

precision_score(y, yhat, average=None), recall_score(y, yhat, average=None), accuracy_score(y, yhat)
```

```python
plt.figure(figsize=(12, 8.5))
logistic_regression_util.plot_true_by_probs(y, probs)
```

```python
logistic_regression_util.plot_true_by_probs(y, probs, subplots=True)
```

```python
plt.style.use('ggplot')
logistic_regression_util.plot_metrics_by_thresholds(y, probs)
```
