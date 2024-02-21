# Statistics and ML Inter-Review

## Inter-Review

- Below is a sample from a dataset.

    |   hours_slept |   coffee_consumed |
    |--------------:|------------------:|
    |       5.54104 |           3.24496 |
    |       7.26644 |           3.02276 |
    |       6.81273 |           1.60564 |
    |       8.77158 |           3.48798 |
    |       6.14643 |           3.18676 |

    How would you visualize the relationship between cups of coffee consumed and
    hours slept? What is a good statistical test for this relationship?

- Give an example of messy data that you've seen.

- What is a baseline model?

## Inter-Review

- Below is a sample of a dataset:

    | hours per day | product |
    |--------------:|:--------|
    |          3.45 |       A |
    |          2.63 |       B |
    |          4.95 |       A |
    |          1.12 |       C |

    How would you visualize the relationship between `hours per day` and
    `product`? What statistical test would be appropriate here?

- When working on a data science project, how do you organize your code and
  notebooks?

- When is it appropriate to scale your data? What's your go-to scaler?

## Inter-Review

- Below is a sample of a dataset:

    | license    | active_in_last_30_days   |
    |:-----------|:-------------------------|
    | pro        | True                     |
    | enterprise | True                     |
    | free       | False                    |
    | enterprise | True                     |
    | free       | True                     |

    How would you visualize the relationship between `license` and
    `active_in_last_30_days`? What statistical test would be appropriate here?

- When and why should you split your data into train and test sets?

- What is the difference between linear and non-linear feature scaling? Give an
  example of each.

## Inter-Review

- Below is a sample from a dataset:

    | screen_size   |   memory_gb |
    |:--------------|------------:|
    | 14"           |           4 |
    | 15"           |           8 |
    | 14"           |           8 |
    | 16"           |          16 |
    | 15"           |           8 |
    | 14"           |          16 |
    | 16"           |           8 |

    What are two ways you could visualize the relationship between `screen_size`
    and `memory_gb`?

- What's an example of a metric you would use to determine how well your model
  performs?

- What does OLS stand for? What does this mean?


What is the difference between supervised and unsupervised machine learning? *

supervised: labeled data you can use to model the patterns for predicting those labels. Unsupervised: you are not modeling to predict labels. you are looking for patterns you don't know how to label yet. 

Name 3 different classification algorithms. *

Decision Tree, Random Forest, Support Vector Machine, Logistic Regression

Name 3 different regression algorithms. *
Linear Regression, Support Vector Regressor, Decision Tree Regressor

Which of the following are direct methods for identifying drivers of an outcome? (Select all that apply) *

What does it mean to "fit" a linear regression model to my data? *identify the parameters, or coefficients, for each feature and intercept that creates the line of best fit, i.e. the line that minimizes the sum of the squared errors. 

Why is logistic regression called "regression"? *
It uses the logit function, which is an s-shaped function, to predict values between 0 and 1. It is regressing to a continuous interval. 

Why is logistic regression a classification algorithm? *
Those predictions between 0 and 1 can be seen as probabilities in a binary classifier. 

If I wanted to see if customers using fiber are more or less likely to churn than customers using DSL, what type of test could I use? *

If I wanted to see if customers using fiber are more or less likely to churn than customers using DSL, what would be my null hypothesis? My alternative hypothesis? *

H_0: P(churn | fiber) == P(churn | DSL)
H_a: P(churn | fiber) != P(churn | DSL)  

I want to see if a customer's monthly spend is a predictor of churn. What kind of statistical test could I run to test this? *

I want to see if a customer's monthly spend is a predictor of churn. What is my null hypothesis? My alternative hypothesis? *
H_0: mean(monthly_spend) for customers who churn == mean(monthly_spend) for customers who do not churn. 
H_a: mean(monthly_spend) for customers who churn != mean(monthly_spend) for customers who do not churn. 


Match the following steps into the relative order of implementing these steps, indicated by the integer. Clearly not all steps are included, so the rank is relative but not absolute. *

Given the temperature data, compute the RMSE (rounded to the nearest int) for the baseline, where the baseline predicts each temperature to be the overall mean (rounded to 2 decimals). (temp = [98, 79, 86, 78, 73, 82]) *

19

Given the churn data, what should our baseline prediction be? (churn = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]) *
5 points
0

Given the churn data, and the baseline predictions you made based on the question above (where churn = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]), give the values of true positive, true negative, false positive, false negative, accuracy, sensitivity, and specificity in the format: [TP, TN, FP, FN, accuracy, sensitivity, specificity]. e.g. using completely random numbers, your answer would look like: [10, 100, 10, 50, 0.50, 0.25, 0.30], and be sure to include the brackets and follow those numeric formats (integer for first 4, x.xx for the last 3). *
[0, 8, 0, 3, 0.73, 0.00, 1.00]

Fill in the blanks: Ordinary linear regression works by finding the line or plane that minimizes the ______ __ _______ ______. That line is often referred to as the line of ____ _____. Separate the 2 answers by a comma, and please use all lower case. *
sum of squared errors, best fit



