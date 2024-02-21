import numpy as np
import pandas as pd
import pydataset
import sklearn.feature_selection
import sklearn.linear_model
from sklearn.model_selection import train_test_split

tips = pydataset.data('tips')
tips['tip_percentage'] = tips.tip / tips.total_bill
tips['price_per_person'] = tips.total_bill / tips['size']

X = tips[['total_bill', 'tip', 'size', 'price_per_person']]
y = tips.tip_percentage

lm = sklearn.linear_model.LinearRegression()
rfe = sklearn.feature_selection.RFE(lm, 2).fit(X, y)
kbest = sklearn.feature_selection.SelectKBest(sklearn.feature_selection.f_regression, k=2)
kbest.fit(X, y)

pd.concat([
    pd.Series(dict(zip(X.columns, kbest.pvalues_)), name='pvalue'),
    pd.Series(dict(zip(X.columns, kbest.scores_)), name='fscore'),
], axis=1)

X.columns[kbest.get_support()]

df = pydataset.data('swiss')

df['noise'] = np.random.uniform(0, 100, size=df.shape[0])

X = df.drop(columns='Fertility')
y = df.Fertility

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.9, random_state=123)

scores = {}

for n_features in range(1, len(X.columns) + 1):
    lm = sklearn.linear_model.LinearRegression()
    rfe = sklearn.feature_selection.RFE(lm, n_features)
    X_train_rfe = rfe.fit_transform(X_train, y_train)
    X_test_rfe = rfe.transform(X_test)
    lm.fit(X_train_rfe, y_train)
    scores[n_features] = lm.score(X_test_rfe, y_test)

pd.Series(scores).sort_index()
