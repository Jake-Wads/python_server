# Evaluating Model Performance

>  An ML model is some approximation of reality, like a model airplane is an approximation of an aircraft.
>
>  And we will evaluate the performance of our models by using the power of *arithmetic!* 

### Key Terms and Fundamental Concepts

- Target - The thing we're trying to predict, the *dependent variable*. 

- Prediction - a forecast, root is from Latin *praedictiōn-* (stem of *praedictiō*) a **foretelling**.

- Model - The approximation of reality we use to generate predictions.

- Baseline or Baseline Model -  the best existing model/guess/prediction *so far*.

  - Our common baseline for classification is predicting using the most common class every single time.
  - It's also common to use "last year's model" as a baseline to beat. 
  - Your baseline is the business's best model, so far. And that model could be composed of one (or more) of the following:
    - Domain knowledge
    - Probability or other statistical analysis
    - Prior experience or folklore like stock brokers saying "Sell in May and go away."
    - A competitor's estimate or what's most common in the industry for that scenario
    - A previously produced machine learning model
  - Examples of baseline models:
    - Baseline for Titanic dataset is predicting "not survived" since 499 survived vs. 817 "not survived"
    - Telco baseline model, predict "not churn" since 1869 churned vs. 5174 "not churned".
    - Always predicting "heads" on flipping a coin (assuming it's fair)
    - Villagers believing that someone will only cry wolf if there's actually a wolf.

- What defines a *positive* or a *negative*? That's arbitrary, which means it's up to us to decide.

  - If we're predicting if it's going to rain, then "It will rain" is the positive prediction.

  - If we're focused on predicting churn, then "churn" will be our positive prediction.

  - If we're making a human face detector, the positive case would be "this is an image of a person's face"

  - If we're building an "unlock with your face" feature, the positive case is predicting if the face is yours.

    


## Evaluation metrics

To evaluate model performance, we count and compare the number and ratio of True Positives, True Negatives, False Positives (Type I Errors), and False Negatives (Type II Errors) between our model predictions and the actual outcomes. Different metrics mean different things. For much more detail, see `https://en.wikipedia.org/wiki/Sensitivity_and_specificity`

### Accuracy

- The total number correct predictions / total observations.
- `(TP + TN) / (TP + TN + FP + FN)`
- Count of (True Positives plus True Negatives) divided by the total number of observations.

### Recall is the True Positive Rate (AKA Sensitivity)

- `TP / (TP + FN)`
- % of acually positive cases that were predicted as positive
- Optimize for recall when missing actual positive cases is *expensive* or deadly
- Use recall when false negatives cost more than false positives.
- Example: Predicting the presence of cancer. 
  - False negative means aggressive cancer growth over time
  - False positive would mean treatment and scans, but we may discover that original false positive later.

### Precision is the Positive Predictive Value 

- `TP / (TP + FP)`
- % of positive predictions that are correct
- Optimize for precision when false positives are more expensive than false negatives.
- Use precision when false positives are more costly than false negatives. 

### Specificity is the True Negative Rate

- The percentage of predicting true negative out of all actual negatives.
- `TN / (TN + FP)`

### A Confusion Matrix clarfies our model's predictions
|                        |                 Predicted Negative |                         Predicted Positive |
| :--------------------- | ------------------------------: | --------------------------------------: |
| **Actual Negative** |                   True Negative | False Positive, a Type I Error |
| **Actual Positive** | False Negative, a Type II Error |                           True Positive |