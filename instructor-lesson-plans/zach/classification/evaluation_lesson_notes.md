# Evaluation


## Examples

- Fraud Detection
    - we want to catch all the actual cases as fraud
    - better to flag a real transaction and have a human review it than to not flag it
    - a false negative is more costly than a false positive
    - optimize for recall
- Spam detection
    - it's bad to put a real email in spam
    - we should be very sure about our positive predictions, favor precision
    - a false positive is more costly than a false negative
- iPhone face id
    - better to reject the actual user than to accept a different person
    - a false positive is more costly than a false negative
- Google's interview process
    - google has explicitly stated they are okay with their interview process
      rejecting people that might actually be qualified to avoid hiring someone
      who isn't qualified

## Plan

- work through curriculum examples

## The Confusion Matrix

A **confusion matrix** is a cross-tabulation of our model's predictions against the actual values.

As a simple example, imagine we are predicting whether or not someone likes coffee. Our data and predictions might look like this:

```python
import pandas as pd

df = pd.DataFrame({
    'actual': ['coffee', 'no coffee', 'no coffee', 'coffee', 'coffee', 'coffee', 'no coffee', 'coffee'],
    'prediction': ['no coffee', 'no coffee', 'coffee', 'coffee', 'coffee', 'coffee', 'no coffee', 'no coffee'],
})
df
```

And the confusion matrix would look like this:

```python
pd.crosstab(df.prediction, df.actual)
```

The four cells represent the 4 possible outcomes of our classification task:

- There are 3 **True Positives**, that is for 4 people they really do like coffee and we predicted they do
- There is 1 **False Positive**, where we predicted the person likes coffee but they really don't
- There are 2 **False Negatives**, where we predicted those people don't like coffee, but they really do
- There are 2 **True Negatives**, where we predicted the people don't like cofee and they really don't

!!!note "Positives and Negatives"
    Here we are treating liking coffee as the positive case and not liking coffee as the negative case. This choice is arbitrary and we could have chosen not liking coffee as the positive case and liking cofee as the negative case.

    Either way, when discussing classification model performance, you'll see one outcome classified as positive and the other as negative.


## Baseline

For a classification problem, a common choice for the baseline model is a model that simply predicts the most common class every single time.

```python
df.actual.value_counts()
```

In our example, there are 5 coffee drinkers and 3 non-coffee drinkers, so our baseline model would be to predict that someone likes coffee every single time.

```python
df['baseline_prediction'] = 'coffee'
```

## Common Evaluation Metrics

Now that we have introduced the idea of a confusion matrix, we can discuss some metrics that are derived from it.

### Accuracy

Accuracy is the number of times we predicted correctly divided by the total number of observations. Put another way:

$$ \frac{\text{TP + TN}}{\text{TP + TN + FP + FN}} $$

In our example above, this would be

$$ \frac{3 + 2}{3 + 2 + 1 + 2} = \frac{5}{8} = 0.625 $$

So our model's overall accuracy is 62.5%.

Accuracy is a good, easy to understand metric, but can fail to capture the whole picture when the classes in the original dataset are not evenly distributed or when differing outcomes have differeng costs.


### Precision

!!!note "Positives and Negatives"
    While the overall accuracy will remain the same no matter which outcome we designate as the positive and the negative, because of their definition, precision and recall **are** affected by these choices.

Precision is the percentage of positive predictions that we made that are correct. Precision tells us how good our model's positive predictions are, and does not take into account false negatives or true negatives. More formally:

$$ \frac{\text{TP}}{\text{TP + FP}} $$

In our example:

$$ \frac{3}{3 + 1} = 0.75 $$

That is, 75% of the time that we predicted someone likes coffee, we were right.

We might choose to optimize for precision when the cost of acting on a positive prediction is high. With precision as a metric, false negatives are "free", but false positives are costly. For example we might optimize for precision when predicting whether or not an email message is spam, as it is better to send a spam message to a user's inbox than it is to send a real message to the spam folder.


### Recall

Recall is the percentage of positive cases that we accurately predicted. Recall tells us how well our model does at "capturing" the actually positve cases. Recall does not take into account false positives or false negatives.

$$ \frac{TP}{TP + FN} $$

In our example:

$$ \frac{3}{3 + 2} = 0.6 $$

We predicted 60% of the people that like coffee correctly.

We might choose to optimize for recall when the cost of missing out on a positive case is high, or when it is better to act on a predicted positive than not to. With recall as a metric, false positives are "free", but false negatives are costly. For example, we might optimize for recall when trying to flag fradulent bank transactions, as it is better to flag is non-fraudulent transaction for review than it is to miss out on an actually fraudulent transaction.


### Other Metrics

While the metrics above are some of the most common, they are not by far an exhaustive list. Here is an overview of several other common metrics:

- **Misclassification Rate**: 1 - accuracy; how often does the model get it wrong?
- **Sensitivity**: aka *True Positive Rate*; how good is our model when the actual value is positive? recall for the positive class
- **Specificity**: How good is our model when the actual value is negative? Recall for the negative class
- **False positive rate**: How likely is it we get a false positive when the actual value is negative?
- **F1 Score**: the harmonic mean of precision and recall
- **Area Under ROC Curve**: A way to measure overall model performance for models that predict not just a class, but a probability as well.


## Evaluation

Now we will put the metrics we've discussed into practice with python code.

First we can calculate accuracy.
Accuracy is simply the number of times where we got the prediction right:

```python
model_accuracy = (df.prediction == df.actual).mean()
baseline_accuracy = (df.baseline_prediction == df.actual).mean()

print(f'   model accuracy: {model_accuracy:.2%}')
print(f'baseline accuracy: {baseline_accuracy:.2%}')
```

Recall is how well we do on actually positive cases. Here we'll define positive as preferring coffe.

First we'll subset the dataframe so that we are only looking at the rows where we have the positive case.
Then we'll evaluate how well our model's predictions do.

```python
subset = df[df.actual == 'coffee']

model_recall = (subset.prediction == subset.actual).mean()
baseline_recall = (subset.baseline_prediction == subset.actual).mean()

print(f'   model recall: {model_recall:.2%}')
print(f'baseline recall: {baseline_recall:.2%}')
```

Notice here that our baseline model has 100% recall.
This is because the baseline is to always predict the person prefers coffee, so we'll never miss an actually positive case.

Next we'll calculate precision.
Precision is based on just the times that the model predicts the positive class.
Because the predictions for our model and the baseline differ, we'll need to create 2 seperate subsets here.

```python
subset = df[df.prediction == 'coffee']
model_precision = (subset.prediction == subset.actual).mean()

subset = df[df.baseline_prediction == 'coffee']
baseline_precision = (subset.baseline_prediction == subset.actual).mean()

print(f'model precision: {model_precision:.2%}')
print(f'baseline precision: {baseline_precision:.2%}')
```

Notice that the baseline model's precision is the same as it's accuracy. This is because the baseline model always predicts the positive case, so the subset of the data used for the precision calculation is the entire dataset.


## Multi-Class Classification

All of the above metrics can be applied to a multi-class classfication problems as well.
Overall, we treat the multiclass classification performance evaluation as a sequence of binary classification performance evaluations, one for each class.
This approach is sometimes referred to as **one-vs-rest**.

The steps for doing so are:

1. Look at one class individually. Treat correctly identifying the class as the positive case.
1. Compute performance metrics for this class.
1. Repeat for every other classes.
1. Average the performance metrics together.

The average calculation can be performed by simply averaging all the metrics together and dividing by the number of data points (a **macro average**), or by a weighted average.
For the weighted average, we weight each metric by the number of data points in the class and divide by the total number of data points.
This process is referred to as a **micro average**.

One way to think about this is that the macro average weighs each class equally, while the micro average weighs each observation equally.
