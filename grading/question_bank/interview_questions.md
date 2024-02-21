1. If you wanted to predict whether or not a customer will churn, what is the name of the type of machine learning algorithms you would you use? 


1. What is feature engineering?  Give an example. 

1. What is the difference between a regression and a classification problem?  
    - Think continuous vs. discrete target variables

1. What evaluation approaches would you work to gauge the effectiveness of a machine learning model?
    - Split the dataset into training and test sets
    - Use cross-validation techniques to further segment the dataset into composite sets of training and test sets within the data. 
    - Implement a choice selection of performance metrics: here is a fairly comprehensive list. You could use measures such as the F1 score, the accuracy, and the confusion matrix. What’s important here is to demonstrate that you understand the nuances of how a model is measured and how to choose the right performance measures for the right situations.

1. How is KNN different from k-means clustering?
    - K-Nearest Neighbors: supervised classification algorithm, so you need labeled data you want to classify an unlabeled point into (thus the nearest neighbor part)
    - K-means: unsupervised clustering algorithm.  Need a set of unlabeled points and a threshold and the algorithm will take unlabeled points and gradually learn how to cluster them into groups by computing the mean of the distance between different points.

1. How do you handle missing or corrupted data in a dataset?
    - drop those rows or columns, or decide to replace them with another value.
    - In Pandas, there are two very useful methods: isnull() and dropna() that will help you find columns of data with missing or corrupted data and drop those values. If you want to fill the invalid values with a placeholder value (for example, 0), you could use the fillna() method.

1. How is a decision tree pruned?
    - Reduced error pruning is perhaps the simplest version: replace each node. If it doesn’t decrease predictive accuracy, keep it pruned. 

1. A model performs at 99% accuracy.  Under what conditions could this metric be entirely misleading?
    - If you wanted to detect fraud in a massive dataset with a sample of millions, a more accurate model would most likely predict no fraud at all if only a vast minority of cases were fraud. However, this would be useless for a predictive model — a model designed to find fraud that asserted there was no fraud at all! Questions like this help you demonstrate that you understand model accuracy isn’t the be-all and end-all of model performance.

1. What’s the F1 score? How would you use it?
    - It is a measure of a model’s performance. It is a weighted average of the precision and recall of a model, with results tending to 1 being the best, and those tending to 0 being the worst. You would use it in classification tests where true negatives don’t matter much.

1. How would you handle an imbalanced dataset?
    - An imbalanced dataset is when you have, for example, a classification test and 90% of the data is in one class. That leads to problems: an accuracy of 90% can be skewed if you have no predictive power on the other category of data! Here are a few tactics to get over the hump:
        - 1- Collect more data to even the imbalances in the dataset.
        - 2- Resample the dataset to correct for imbalances.
        - 3- Try a different algorithm altogether on your dataset.


1. Explain A/B Testing-use cases, goals, method
    - It is a statistical hypothesis testing for a randomized experiment with two variables A and B.
    - The goal of A/B Testing is to identify any changes to the web page to maximize or increase the outcome of an interest. 
    - method for figuring out the best online promotional and marketing strategies for your business. 
    - It can be used to test website copy, sales emails, to search ads
    - An example of this could be identifying the click-through rate for a banner ad.
    
1. Explain what is overfitting, how you would control for it, andyou can identify whether you have overfit. 
    - Overfitting is finding spurious results that are due to chance and cannot be reproduced by subsequent studies. 
    - reduce risk of overfitting by: 
        - Keep the model simpler: reduce variance by taking into account fewer variables and parameters, thereby removing some of the noise in the training data.
        - Use cross-validation techniques such as k-folds cross-validation.
        - Use regularization techniques such as LASSO that penalize certain model parameters if they’re likely to cause overfitting.
    - example:  a regression model that hits each sample data point. a decision tree that runs down to the find sample observation.  
    - example: We frequently see newspaper reports about studies that overturn the previous findings, like eggs are no longer bad for your health, or saturated fat is not linked to heart disease. The problem, in our opinion is that many researchers, especially in social sciences or medicine, too frequently commit the cardinal sin of Data Mining - Overfitting the data. 
    - The researchers test too many hypotheses without proper statistical control, until they happen to find something interesting and report it.  Not surprisingly, next time the effect, which was (at least partly) due to chance, will be much smaller or absent. 
    - identify: results are not repeatable.  in-sample metrics are significantly different from out-of-sample metrics.  

1. What is a spurious correlation? 

1. Give an example of how you would use experimental design to answer a question about user behavior. 
    - Step 1: Formulate the Research Question: What are the effects of page load times on user satisfaction ratings? 
    - Step 2: Identify variables: We identify the cause & effect. Independent variable -page load time, Dependent variable- user satisfaction rating 
    - Step 3: Generate Hypothesis: Lower page download time will have more effect on the user satisfaction rating for a web page. Here the factor we analyze is page load time. 
    - Step 4: Determine Experimental Design. We consider experimental complexity i.e vary one factor at a time or multiple factors at one time in which case we use factorial design (2^k design). A design is also selected based on the type of objective (Comparative, Screening, Response surface) & number of factors. Here we also identify within-participants, between-participants, and mixed model.For e.g.: There are two versions of a page, one with Buy button (call to action) on left and the other version has this button on the right. Within-participants design - both user groups see both versions. Between-participants design - one group of users see version A & the other user group version B. 
    - Step 5: Develop experimental task & procedure: Detailed description of steps involved in the experiment, tools used to measure user behavior, goals and success metrics should be defined. Collect qualitative data about user engagement to allow statistical analysis. 
    - Step 6: Determine Manipulation & Measurements:  
        - Manipulation: One level of factor will be controlled and the other will be manipulated. 
        - Measures:
            - Latency- time between a prompt and occurrence of behavior (how long it takes for a user to click buy after being presented with products).
            - Frequency- number of times a behavior occurs (number of times the user clicks on a given page within a time)
            - Duration-length of time a specific behavior lasts(time taken to add all products)
            - Intensity-force with which a behavior occurs ( how quickly the user purchased a product)
    - Step 7: Analyze results: Identify user behavior data and support the hypothesis or contradict according to the observations made for e.g. how majority of users satisfaction ratings compared with page load times. 

1. What are the most important python libraries for data science?

1. What is the difference between “long” and “wide” format data?

1. How would you know if you have a normal distribution? (Properties of Nornal Distribution:)
    - Unimodal -one mode
    - Symmetrical -left and right halves are mirror images
    - Bell-shaped -maximum height (mode) at the mean
    - Mean, Mode, and Median are all located in the center
    - Asymptotic

1. What can you infer about probabilities knowing you have a normal distribution? 

1. Which data scientist do you admire the most? Which startups?

1. What is your favorite ML algorithm? Why? Explain it to me in less than a minute.
    - This type of question tests your understanding of how to communicate complex and technical nuances with poise and the ability to summarize quickly and efficiently. Make sure you have a choice and make sure you can explain different algorithms so simply and effectively that a five-year-old could grasp the basics!

1. What’s the difference between Type I and Type II error?
    - Type I error is a false positive, while Type II error is a false negative. Briefly stated, Type I error means claiming something has happened when it hasn’t, while Type II error means that you claim nothing is happening when in fact something is.
    - A clever way to think about this is to think of Type I error as telling a man he is pregnant, while Type II error means you tell a pregnant woman she isn’t carrying a baby.

[bayes: quiz show 1 stopped here]

1. What is the difference between supervised and unsupervised machine learning?

1. If you could spend the next week doing data science on the project of your choice, what would you do? 

1. How do you rest your brain from looking at a computer screen?

1. How do you start a project?

1. What is Bayes’ Theorem? How is it useful in a machine learning context?
    - Bayes’ Theorem gives you the posterior probability of an event given what is known as prior knowledge.
    - Mathematically, it’s expressed as the true positive rate of a condition sample divided by the sum of the false positive rate of the population and the true positive rate of a condition.
    - Say you had a 60% chance of actually having the flu after a flu test, but out of people who had the flu, the test will be false 50% of the time, and the overall population only has a 5% chance of having the flu. Would you actually have a 60% chance of having the flu after having a positive test?
    - Bayes’ Theorem says no. It says that you have a (.6 * 0.05) (True Positive Rate of a Condition Sample) / (.6*0.05)(True Positive Rate of a Condition Sample) + (.5*0.95) (False Positive Rate of a Population)  = 0.0594 or 5.94% chance of getting a flu.

1. Why is “Naive” Bayes naive?
    - It implies absolute independence of features — a condition probably never met in real life.


1. Draw a confusion matrix and label/explain all the parts. 
    - accuracy: what percent of your predictions were correct? 
    - precision: what percent of the positive predictions did you catch? 
    - recall: what percent of the positive cases did you catch? 
    - sensitivity == recall
    - specificity == ~precision
    - TN
    - FN
    - TP
    - FP

1. Draw and describe a ROC curve. What does ROC stand for?  
    - ROC: receiver operator characteristic
    - ROC curve represents a relation between sensitivity (RECALL) and specificity(NOT PRECISION) and is commonly used to measure the performance of binary classifiers.

1. What is statisitical power? 
    - the likelihood that a study will detect an effect when the effect is present. The higher the statistical power,the less likely you are to make a Type II error (concluding there is no effect when, in fact, there is). 

1. What could be happening if a model appeared to perform well when training/testing but when deployed results were drastically different? 

1. What is RCA, root cause analysis?

1. What is bootstrapping?

1. What is jackknifing?

1. What is cross validation?

1. What cross-validation technique would you use on a time series dataset?
    - Instead of using standard k-folds cross-validation, you have to pay attention to the fact that a time series is not randomly distributed data — it is inherently ordered by chronological order. You’ll want to do something like forward chaining where you’ll be able to model on past data then look at forward-facing data.
    - example: 
        - fold 1 : training [1], test [2]
        - fold 2 : training [1 2], test [3]
        - fold 3 : training [1 2 3], test [4]
        - fold 4 : training [1 2 3 4], test [5]
        - fold 5 : training [1 2 3 4 5], test [6]


1. What is bagging?

1. What is boosting?

1. What are ensemble models? 

1. Is it better to have too many false positives or too many false negatives?
    - It depends on the question as well as on the domain for which we are trying to solve the question. 
    - In medical testing, false negatives may provide a falsely reassuring message to patients and physicians that disease is absent, when it is actually present. This sometimes leads to inappropriate or inadequate treatment of both the patient and their disease. So, it is desired to have too many false positive. 
    - For spam filtering, a false positive occurs when spam filtering or spam blocking techniques wrongly classify a legitimate email message as spam and, as a result, interferes with its delivery. While most anti-spam tactics can block or filter a high percentage of unwanted emails, doing so without creating significant false-positive results is a much more demanding task. So, we prefer too many false negatives over many false positives. 

1. What is selection bias? 
    - when the researcher decides who is going to be studied. 
    - Sampling bias: non-random sample of a population where some members are less likely to be included than others resulting in a biased sample.
    - Time interval: A trial may be terminated early leaving a specific group of members out
    - Data: When specific subsets of data are chosen to support a conclusion or rejection of bad data on arbitrary grounds, instead of according to previously stated or generally agreed criteria.
    - Attrition: caused by attrition (loss of participants) discounting trial subjects/tests that did not run to completion.

1. How would you validate a regression model?
    - $R^{2}$
    - RMSE
    - MSE
    - MAE
    - Residual plot

1. What is Machine Learning?

1. Name some common classification algorithms.

1. How can you identify outliers?
    - IQR
    - box-plots
    - Z-Score

1. What should you do when you find outliers?
    - ask why there is an outlier:  why is it different?  (data integrity? one-off event?)
    - you can remove the observations with the outliers, create bins for the variable, replace the outlier with the max value, do nothing, ... 

1. What is a recommendation engine? How does it work?
    - Netflix: "Other Movies you might enjoy" or Amazon - Customers who bought X also bought Y.
    - Two methods: collaborative or content-based filtering. 
    - Collaborative filtering methods build a model based on users past behavior (items previously purchased, movies viewed and rated, etc) and use decisions made by current and other users. This model is then used to predict items (or ratings for items) that the user may be interested in. 
    - Content-based filtering methods use features of an item to recommend additional items with similar properties. These approaches are often combined in Hybrid Recommender Systems. 
    - Here is a comparison of these 2 approaches used in two popular music recommender systems - Last.fm and Pandora Radio. (example from Recommender System entry)
        - Last.fm creates a "station" of recommended songs by observing what bands and individual tracks the user has listened to on a regular basis and comparing those against the listening behavior of other users. Last.fm will play tracks that do not appear in the user's library, but are often played by other users with similar interests. As this approach leverages the behavior of users, it is an example of a collaborative filtering technique.
        - Pandora uses the properties of a song or artist (a subset of the 400 attributes provided by the Music Genome Project) in order to seed a "station" that plays music with similar properties. User feedback is used to refine the station's results, deemphasizing certain attributes when a user "dislikes" a particular song and emphasizing other attributes when a user "likes" a song. This is an example of a content-based approach.

1. Which tools do you use for visualization? How could you represent 5 dimensions in a chart
    - What’s important here is to define your views on how to properly visualize data and your personal preferences when it comes to tools. Popular tools include R’s ggplot, Python’s seaborn and matplotlib, and tools such as Plot.ly and Tableau.

1. Where do you usually source datasets?
    - Machine learning interview questions like these try to get at the heart of your machine learning interest. Somebody who is truly passionate about machine learning will have gone off and done side projects on their own, and have a good idea of what great datasets are out there. If you’re missing any, check out Quandl for economic and financial data, and Kaggle’s Datasets collection for another great list.

1. What are your favorite use cases of machine learning models?
    - Make sure that you have a few examples in mind and describe what resonated with you. It’s important that you demonstrate an interest in how machine learning is implemented.

1. Describe the data science pipeline.

1. What are the various types of data products or deliverables you might develop as a data scientist? 

1. What are some ways to handle missing values in a dataset you are trying to model?  

1. How would you identify the optimal k for your k-means algorithm? 
    - the elbow method

1. In any 15-minute interval, there is a 20% probability that you will see at least one shooting star. What is the proba­bility that you see at least one shooting star in the period of an hour?
    - Probability of not seeing any shooting star in 15 minutes is
        = 1–P( Seeing one shooting star ) = 1–0.2 = 0.8
    - Probability of not seeing any shooting star in the period of one hour = (0.8)^4 = 0.4096
    - Probability of seeing at least one shooting star in the one hour = 1–P( Not seeing any star ) = 1–0.4096 = 0.5904

1. A jar has 1000 coins, of which 999 are fair and 1 is double headed. Pick a coin at random, and toss it 10 times. Given that you see 10 heads, what is the probability that the next toss of that coin is also a head?

1. What is data science?  How is it different from other data professions? 
    - Data Science is a blend of various tools, algorithms, and machine learning principles with the goal to discover hidden patterns from the raw data. How is this different from what statisticians have been doing for years?
    - The answer lies in the difference between explaining and predicting, and in the difference in available data (i.e. sample sizes)
    - Data Analyst: Business administration, exploratory data analysis
    - Data Science: exploratory data analysis, ML and advanced algorithms, data product engineering

1. What are the differences between supervised and unsupervised machine learning? 
    - supervised:  input data is labeled, uses training dataset, used for prediction, enables classification & regression
    - unsupervised: input data is unlabeled, uses the input dataset, used for analysis, enables classification, density estimation and dimension reduction. 

1. What are the important skills to have in Python with regard to data analysis?
    - built-in data types especially lists, dictionaries, tuples, and sets.
    - N-dimensional NumPy Arrays.
    - Pandas dataframes.
    - Ability to perform element-wise vector and matrix operations on NumPy arrays.
    - Familiarity with Scikit-learn.
    - Ability to write efficient list comprehensions instead of traditional for loops.
    - Ability to write small, clean functions 

1. What is Deep Learning? What are some use cases? 
    - Deep learning is a subset of machine learning that is concerned with neural networks: how to use backpropagation and certain principles from neuroscience to more accurately model large sets of unlabelled or semi-structured data. In that sense deep learning represents an unsupervised learning algorithm that learns representations of data through the use of neural nets.

1. What are artificial neural networks?
Artificial Neural networks are a specific set of algorithms that have revolutionized machine learning. They are inspired by biological neural networks. Neural Networks can adapt to changing input so the network generates the best possible result without needing to redesign the output criteria.

1. What are the different Deep Learning Frameworks?
    - Pytorch
    - TensorFlow
    - Microsoft Cognitive Toolkit
    - Keras
    - Caffe
    - Chainer

1. What is an One Hot Encoder?
    - process by which categorical variables are converted into a form that could be provided to ML algorithms to do a better job in prediction.

1. What is a dummy variable?
    - a dummy variable is one that takes the value 0 or 1 to indicate the absence or presence of some categorical variable.

1. What are some resampling methods and how do they work? 

1. What is logistic regression? When might you use it?  Explain the difference between logistic regression and linear regression?  
    - Supervised ML Algorithm used to predict the binary outcome from a linear combination of predictor variables. For example, if you want to predict whether a particular political leader will win the election or not. In this case, the outcome of prediction is binary i.e. 0 or 1 (Win/Lose). The predictor variables here would be the amount of money spent for election campaigning of a particular candidate, the amount of time spent in campaigning, etc.
    - difference between the two:  

1. What is power analysis?

1. Explain P-value.
    - A metric that helps assess the statistical significance of an insight whether it is a real insight or just by chance

1. How can you deal with seasonality in time series modeling?

1. Explain curse of dimensionality.  What types of algorithms are most affected by this?

1. What assumption is made when performing a t-test?

1. What equipment, tools, training, or other team members would you need in order to be super effective at making sense of these problems (a specific problem named)?

1. Where would you expect the data to come from? How would you expect to access it?

1. Have you ever worked with a dataset that was too big to make sense of in Excel? If so, please describe. ... Too big for R or Pandas? If so, please describe.

1. What's the coolest thing you've found while making sense of data?
Give an example of a data problem you solved that took more than a few days to work through.

1. Give an example where you used machine learning to solve a business problem.

1. What are your personal "best practices" for making sense of data?

1. What are your personal "best practices" for validating the results of a data experiment?

1. What are your personal "best practices" for working collaboratively?

1. Tell me about yourself.

1. What is Codeup? Why did you choose Codeup vs. a more academic approach?

1. Why is data science for you?

1. Tell me about your analytical abilities, specifically statistical analysis, before Codeup?

1. Tell me about your programming skills before doing Codeup's data science program?

1. What makes you uniquely suited for a role in data science?

1. In your own words, how do you define Data Science?

1. Isn't data science another way to say applied statistics? Why or why not?

1. How would you say data science is similar and different than data analytics?

1. Tell me, where does "science" come in with the work you've been doing?

1. What do you do when you have inconclusive data 

1. How do you explain tenuous connections between variables?

1. What kinds of questions can data science methods answer?

Portfolio, projects, and pipeline
1. Walk me through your approach to the data science pipeline?

1. Will you please show me your portfolio of data science projects

1. Tell me about a data product that you've put in production.

1. What steps do you take to ensure that your work is accurate and correct?

1. What was your favorite project that you’ve worked to build? What about it makes it your favorite? The topic? The challenges in the data? The methodologies? 