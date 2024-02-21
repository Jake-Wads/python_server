# Miscellaneous Notes

1. [Better Looking Decision Trees](#Better-Looking-Decision-Trees)
1. [Better Confusion Matrix](#Better-Confusion-Matrix)
1. [Visual Classifier Evaluation](#Visual-Classifier-Evaluation)

## Better Looking Decision Trees

First some setup:

```python
import seaborn as sns
import pandas as pd

from sklearn.model_selection import train_test_split

from acquire import get_iris_data

iris = get_iris_data()\
    .drop(columns=['measurement_id', 'species_id'])\
    .rename(columns={'species_name': 'species'})

iris.head()
```

Do the train-test split. For the sake of demonstration, we'll just use two features from the iris data set.

```python
X, y = iris[['sepal_length', 'sepal_width']], iris.species

X_train, X_test, y_train, y_test = train_test_split(X, y)
```

We'll make a simple decision tree model.

```python
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=2)
tree.fit(X_train, y_train)
```

Visualize the decision tree.

```python
import graphviz
from sklearn.tree import export_graphviz

feature_names = X_train.columns
class_names = sorted(y_train.unique())

dot = export_graphviz(
    tree,
    out_file=None,
    feature_names=feature_names,
    class_names=class_names, # target value names
    special_characters=True,
    filled=True,             # fill nodes w/ informative colors
    impurity=False,          # show impurity at each node
    leaves_parallel=True,    # all leaves at the bottom
    proportion=True,         # show percentages instead of numbers at each leaf
    rotate=True,             # left to right instead of top-bottom
    rounded=True,            # rounded boxes and sans-serif font
)

graph = graphviz.Source(dot, filename='iris_decision_tree', format='png')
graph.view(cleanup=True)
```

Here is my decision tree:

![](iris_decision_tree.png)


## Better Confusion Matrix

```python
from sklearn.metrics import confusion_matrix

predictions = tree.predict(X_train)

confusion_matrix(y_train, predictions)
```

```python
train = X_train.assign(actual=y_train, predicted=predictions)
```

```python
train.head()
```

```python
cm = pd.crosstab(train.actual, train.predicted)

sns.heatmap(cm, annot=True, cmap='Greens')
```

## Visual Classifier Evaluation

```python
train['correct'] = train.actual == train.predicted

train.head()
```

```python
sns.relplot(data=train, x='sepal_length', y='sepal_width', style='correct', hue='actual')
```
