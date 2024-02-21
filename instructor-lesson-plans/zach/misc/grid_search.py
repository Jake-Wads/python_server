from typing import List, Tuple, Dict, Union
from zgulde.ds_imports import *


def cv_results_to_df(grid: GridSearchCV) -> pd.DataFrame:
    results = grid.cv_results_
    params_and_scores = zip(results["params"], results["mean_test_score"])
    df = pd.DataFrame([dict(**p, score=s) for p, s in params_and_scores])
    df["model"] = grid.best_estimator_.__class__.__name__
    return df


GridCandidates = List[
    Tuple[sklearn.base.BaseEstimator, Dict[str, List[Union[str, int]]]]
]


def multi_grid_search(models: GridCandidates, X, y, cv=4) -> pd.DataFrame:
    return pd.concat(
        [
            cv_results_to_df(GridSearchCV(model, params, cv=cv).fit(X, y))
            for model, params in models
        ]
    )


def inspect_coefs(lm, X):
    return pd.Series(dict(zip(X.columns, lm.coefs_))).sort_values()


def inspect_feature_importances(tree, X):
    return pd.Series(dict(zip(X.columns, tree.feature_importances_))).sort_values()


classification_models = [
    (DecisionTreeClassifier(), {"max_depth": range(1, 11)}),
    (KNeighborsClassifier(), {"n_neighbors": range(1, 21)}),
    (LogisticRegression(), {"C": [0.01, 0.1, 1, 10, 100, 1000], "solver": ["lbfgs"]}),
    (SVC(), {"kernel": ["rbf", "linear"]}),
    (SVC(), {"kernel": ["poly"], "degree": [2]}),
]

regression_models = [
    (DecisionTreeRegressor(), {"max_depth": range(1, 11)}),
    (KNeighborsRegressor(), {"n_neighbors": range(1, 11)}),
    (LinearRegression(), {}),
    (Ridge(), {"alpha": [0.01, 0.1, 1, 10, 100, 1000]}),
    (SVR(), {"kernel": ["rbf", "linear"]}),
    (SVR(), {"kernel": ["poly"], "degree": [2]}),
]

X, y = data("voteincome").rformula("vote ~ age + income + education")
results = multi_grid_search(classification_models, X, y)
results.sort_values(by="score")

X, y = mpg.rformula("hwy ~ displ + cyl")
results = multi_grid_search(regression_models, X, y)
results.sort_values(by="score")

r2_score(y, np.repeat(y.mean(), y.size))

grid = GridSearchCV(SVC(), {"kernel": ["rbf", "poly", "linear"]})
grid.fit(X, y)

# X, y = iris.drop(columns='species'), iris.species.astype('category').cat.codes

# # X, y = mpg[['hwy', 'cty', 'displ']], mpg.cyl

# X_train, X_test, y_train, y_test = train_test_split(X, y)

# params = {'n_neighbors': range(1, 21), 'p': [1, 2]}
# grid = GridSearchCV(KNeighborsClassifier(), params, cv=4)
# grid.fit(X, y)
# results = cv_results_to_df(grid)

# plot_scatter_by_group(results, y='score', x='n_neighbors', g='p')
# sns.boxplot(data=results, y='score', x='p')

# # List[Tuple[sklearn.base.BaseEstimator, Dict[str, list]]]

# # results = []
# # for model, params in models:
# #     grid = GridSearchCV(model(), params, cv=5).fit(X, y)
# #     params, scores = grid.cv_results_['params'], grid.cv_results_['mean_test_score']
# #     for p, s in zip(params, scores):
# #         p['score'] = s
# #         p['model'] = model.__name__
# #     results.extend(params)

# results = []
# for model, params in models:
#     grid = GridSearchCV(model(), params, cv=5).fit(X, y)
#     params, scores = grid.cv_results_['params'], grid.cv_results_['mean_test_score']
#     for p, s in zip(params, scores):
#         results.extend([{
#             'score': s, 'model': model.__name__, 'params': p
#         }])

# pd.DataFrame(results).sort_values(by='score')

# partial(LogisticRegression, solver='lbfgs', multi_class='auto')
