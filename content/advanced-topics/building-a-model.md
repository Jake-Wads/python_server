# Building A Model

We'll build a python module that defines a single function to interact with our
trained model.

!!!note "Libraries"
    Make sure to install `sklearn` and `pandas` into your virtual environment.

```python
from time import strftime

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def log(msg):
    print('[{} model.py] {}'.format(strftime('%Y-%m-%d %H:%M:%S'), msg))

df = pd.read_csv('./spam_clean.csv')

tfidf = TfidfVectorizer()

X = tfidf.fit_transform(df.text)
y = df.label

log('Training model')
lm = LogisticRegression(solver='saga').fit(X, y)

log('Finished training model')
log('Accuracy: {:.2%}'.format(accuracy_score(y, lm.predict(X))))
log('Classification Report')
print(classification_report(y, lm.predict(X)))
log('All done')

def predict(msg):
    return lm.predict(tfidf.transform([msg]))[0]
```

When we import the `predict` function from this module, we'll not only get our
prediction function, but also will load the dataset and train our model.

## Exercise

1. Copy the `model.py` file from the curriculum to your project

1. Copy the `spam_clean.csv` file over to your project

1. Activate your virtual environment (if it's not already)

1. Install any necessary dependencies to your virtual environment (`sklearn` and
   `pandas`)

1. Fire up a python interpreter and ensure your `predict` function works

    ```
    python
    ```

    ```
    >>> from model import predict
    >>> predict('free cash')
    'spam'
    ```

1. Update your `requirements.txt` file

    ```
    pip freeze > requirements.txt
    ```

1. Add, commit, and push your work to GitHub
