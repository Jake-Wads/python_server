# Interview Question of the Day

## Summary and Rationale

The idea is to have students ask each-other (inter-review) interview questions so that students.

When prompting the entire class to answer, the majority of students class is not actively engaged. The difference with students asking each-other questions is that it's more active and there are more "question + answer" pairings/connections than only between an instructor and the entire class (which can be one directional).

Some of the questions are 'easy' or conversational, and it's OK if the pairings ask/answer a few in bunches.

Some of the questions are challenging and require more depth and demonstration of explanatory depth.

Aim for 5-20 minutes per pairing, depending
Swap partners at least once


## Interview Questions


Tell me a little about yourself. (elevator pitch in 1 minute or 1-3 sentences)

What led you to your interest in data science?

If you could spend the next week doing data science on the project of your choice, what would you do?

What kinds of questions can data science methods answer?

What is Codeup?

What are some challenges you are run into while working collaboratively? 

What is a left join in SQL vs an outer join?

What are the most important python libraries for data science? 

Where would you expect the data to come from? How would you expect to access it?

What steps do you take to ensure that your work is accurate and correct?

What is the difference between “long” and “wide” format data?

How can you identify outliers?

What should you do when you find outliers? 

What are some ways to handle missing values in a dataset you are trying to model? 

What are your personal "best practices" for making sense of data? 

Tell me about your analytical abilities, specifically statistical analysis, before Codeup?

How could you represent 5 dimensions in a chart? 

Explain p-value. 

Explain Pearson R. 

Explain T-Test. 

Explain Chi Square Test. 

How would you know if you have a normal distribution, and what can you infer about properties of the data knowing that?  

What is a spurious correlation? 

What do you do when you have inconclusive data?	

Explain different kinds of Biases. Selection bias: when the researcher decides who is going to be studied. Sampling bias: non-random sample of a population where some members are less likely to be included than others resulting in a biased sample. Time interval: A trial may be terminated early leaving a specific group of members out. Data: When specific subsets of data are chosen to support a conclusion or rejection of bad data on arbitrary grounds, instead of according to previously stated or generally agreed criteria.. Attrition: caused by attrition (loss of participants) discounting trial subjects/tests that did not run to completion.

In any 15-minute interval, there is a 20% probability that you will see at least one shooting star. What is the proba­bility that you see at least one shooting star in the period of an hour? 
Answer: Probability of not seeing any shooting star in 15 minutes is = 1–P( Seeing one shooting star ) = 1–0.2 = 0.8. Probability of not seeing any shooting star in the period of one hour = (0.8)^4 = 0.4096. Probability of seeing at least one shooting star in the one hour = 1–P( Not seeing any star ) = 1–0.4096 = 0.5904

A jar has 1000 coins, of which 999 are fair and 1 is double headed. Pick a coin at random, and toss it 10 times. Given that you see 10 heads, what is the probability that the next toss of that coin is also a head? 
Answer: First, I picked the coin, so I’d just look at both sides of the coin :D. But if I can’t examine the coin…  the prior odds that you picked the double-headed coin are 1/999. after seeing ten heads, the posterior odds that you picked the double-headed coin are (2^10)/999 - let's approximate this as 1. (Bayes' theorem usually gets expressed in terms of probabilities, but it's so much simpler in terms of odds.) so it's roughly equally likely that you have the double-headed coin or any non-double-headed coin; the probability of flipping an eleventh head is then approximate (1/2)(1) + (1/2)(1/2) = 3/4. At around 15 prior heads, you are pretty much guaranteed a head flip. 

What is your favorite ML algorithm? Why? Explain it to me in less than a minute.
This type of question tests your understanding of how to communicate complex and technical nuances with poise and the ability to summarize quickly and efficiently. Make sure you have a choice and make sure you can explain different algorithms so simply and effectively that a five-year-old could grasp the basics!

What is the difference between supervised and unsupervised machine learning? Supervised: 1. Input data is labeled, 2. Uses training dataset, 3. Used for prediction. Unsupervised: 1. Input data is unlabeled, 2. Uses the input data set, 3. Used for analysis

Give an example where you used machine learning to solve a business problem. (Capstone…)

Explain the “curse of dimensionality.” What types of algorithms are most affected by this? "As the number of features or dimensions grows, the amount of data we need to generalize accurately grows exponentially." as we add more dimensions we also increase the processing power we need to analyze the data, and we also increase the amount of training data required to make meaningful models. So, in general, you need X*d feature space, where X is your number of data points in training and d is the number of features or dimensions. Classification algorithms are highly affected by this.

What is Machine Learning? 

What are your favorite use cases of machine learning models? Make sure that you have a few examples in mind and describe what resonated with you. It’s important that you demonstrate an interest in how machine slearning is implemented.

What is feature engineering? Give an example. 

What is an One Hot Encoder? 

What is a dummy variable? 

What are some resampling methods and how do they work? The bootstrap method is a resampling technique used to estimate statistics on a population by sampling a dataset with replacement; Validation set approach is the most basic approach. It simply involves randomly dividing the dataset into two parts: a training set and a validation set or hold-out set. The model is fit on the training set and the fitted model is used to make predictions on the validation set; Leave-one-out cross-validation (LOOCV) is a better option than the validation set approach. Instead of splitting the dataset into two subsets, only one observation is used for validation and the rest is used to fit the model; k-fold cross-validation involves randomly dividing the set of observations into k groups or folds of approximately equal size. The first fold is treated as a validation set and the model is fit on the remaining folds. The procedure is then repeated k times, where a different group is treated as the validation set; Regularization methods effectively prevent overfitting. Overfitting occurs when a model performs well on the training set, but then performs poorly on the validation set; Shrinkage methods--Shrinking the estimated coefficients towards 0 can significantly improve the fit and reduce the variance of the coefficients. Here, we explore ridge regression and lasso; Ridge regression:  Traditional linear fitting involves minimizing the RSS (residual sum of squares). In ridge regression, a new parameter is added, and now the parameters will minimize; Lasso:  Similarly to ridge regression, lasso will minimizes:

What evaluation approaches would you work to gauge the effectiveness of a machine learning model? Split the dataset into training and test sets; Use cross-validation techniques to further segment the dataset into composite sets of training and test sets within the data; Implement a choice selection of performance metrics: here is a fairly comprehensive list. You could use measures such as the F1 score, the accuracy, and the confusion matrix. What’s important here is to demonstrate that you understand the nuances of how a model is measured and how to choose the right performance measures for the right situations.

A model performs at 99% accuracy. Under what conditions could this metric be entirely misleading? If you wanted to detect fraud in a massive dataset with a sample of millions, a more accurate model would most likely predict no fraud at all if only a vast minority of cases were fraud. However, this would be useless for a predictive model — a model designed to find fraud that asserted there was no fraud at all! Questions like this help you demonstrate that you understand model accuracy isn’t the be-all and end-all of model performance.

What’s the F1 score? How would you use it? It is a measure of a model’s performance. It is a weighted average of the precision and recall of a model, with results tending to 1 being the best, and those tending to 0 being the worst. You would use it in classification tests where true negatives don’t matter much.

Explain what is overfitting, how you would control for it, and you can identify whether you have overfit. 
Overfitting is finding spurious results that are due to chance and cannot be reproduced by subsequent studies.
reduce risk of overfitting by: Keep the model simpler: reduce variance by taking into account fewer variables and parameters, thereby removing some of the noise in the training data; Use cross-validation techniques such as k-folds cross-validation; Use regularization techniques such as LASSO that penalize certain model parameters if they’re likely to cause overfitting. Example: a regression model that hits each sample data point. a decision tree that runs down to the find sample observation. Identify it by finding results are not repeatable. in-sample metrics are significantly different from out-of-sample metrics.

What’s the difference between Type I and Type II error? Type I error is a false positive, while Type II error is a false negative. Briefly stated, Type I error means claiming something has happened when it hasn’t, while Type II error means that you claim nothing is happening when in fact something is. A clever way to think about this is to think of Type I error as telling a man he is pregnant, while Type II error means you tell a pregnant woman she isn’t carrying a baby.

Draw and describe a ROC curve. What does ROC stand for? ROC: receiver operator characteristic. ROC curve represents a relation between sensitivity (RECALL) and specificity(NOT PRECISION) and is commonly used to measure the performance of binary classifiers.

What are your personal "best practices" for validating the results of a data experiment? I prefer to always employ cross validation if I have enough data. And I work to be able to explain the results. I’m not fond of using only black boxes for that reason, though I am okay using them for insight and then backing them up with other methods.

Draw a confusion matrix and label/explain all the parts.
accuracy: what percent of your predictions were correct?
precision: what percent of the positive predictions did you catch? == specificity the higher this number is, the more you were able to pinpoint all positives correctly. If this is a low score, you predicted a lot of positives where there were none. tp / (tp + fp)
recall: what percent of the positive cases did you catch? if this score is high, you didn’t miss a lot of positives. But as it gets lower, you are not predicting the positives that are actually there. tp / (tp + fn). == sensitivity
f1-score: The balanced harmonic mean of Recall and Precision, giving both metrics equal weight. The higher the F-Measure is, the better.
Support: number of occurrences of each class in where y is true.

What could be happening if a model appeared to perform well when training/testing but when deployed results were drastically different? You could have overfit the training data. Doing cross validation will help mitigate that risk.

Is it better to have too many false positives or too many false negatives? It depends on the question as well as on the domain for which we are trying to solve the question. In medical testing, false negatives may provide a falsely reassuring message to patients and physicians that disease is absent, when it is actually present. This sometimes leads to inappropriate or inadequate treatment of both the patient and their disease. So, it is desired to have too many false positives.For spam filtering, a false positive occurs when spam filtering or spam blocking techniques wrongly classify a legitimate email message as spam and, as a result, interferes with its delivery. While most anti-spam tactics can block or filter a high percentage of unwanted emails, doing so without creating significant false-positive results is a much more demanding task. So, we prefer too many false negatives over many false positives.

If you wanted to predict whether or not a customer will churn, what subset of machine learning algorithms would you use?

What is Logistic Regression? What is the difference between logistic regression and linear regression? Diagram it. 

How is a decision tree pruned? Reduced error pruning is perhaps the simplest version: replace each node. If it doesn’t decrease predictive accuracy, keep it pruned.

How would you handle an imbalanced dataset? An imbalanced dataset is when you have, for example, a classification test and 90% of the data is in one class. 1- Collect more data to even the imbalances in the dataset, 2- Resample the dataset to correct for imbalances, 3- Try a different algorithm altogether on your dataset.

Name some common classification algorithms. Logistic Regression, K-Nearest Neighbors, Decision Tree, Random Forest, Support Vector Machine (SVM), Naïve Bayes, Stochastic Gradient Descent

What was the RMSE and R^2 value of your regression project and what is the significance of those values?

How would you validate a regression model? R2, RMSE, MSE, MAE, Residual plot

What's the difference between K-means and K-Nearest Neighbor? K-Nearest Neighbors: supervised classification algorithm, so you need labeled data you want to classify an unlabeled point into (thus the nearest neighbor part) K-means: unsupervised clustering algorithm. Need a set of unlabeled points and a threshold and the algorithm will take unlabeled points and gradually learn how to cluster them into groups by computing the mean of the distance between different points.

How would you identify the optimal k for your k-means algorithm? the elbow method to find the number of clusters (k)

How can you deal with seasonality in time series modeling? Once seasonality is identified, it can be modeled. The model of seasonality can be removed from the time series. This process is called Seasonal Adjustment, or Deseasonalizing. A time series where the seasonal component has been removed is called seasonal stationary.
Are you familiar with cloud computing services such as AWS, Google Cloud, or Azure?