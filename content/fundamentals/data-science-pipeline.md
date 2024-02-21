# Data Science Pipeline

![DataToAction_v2.jpg](DataToAction_v2.jpg)

## **Planning**

Business stakeholders and end users often ask more general questions that are very hard to answer directly or extremely specific questions that are not going to achieve their underlying goal. This leads to miscommunication, time spent on work that is ultimately thrown away, or inadequate understanding of the underlying problem being investigated. As you gain experience with the data and domain, you gain a better understanding of problems and can ask more informative & specialized questions. Even then, however, it is important to work through this planning stage, as it is all too easy to get lost down a rabbit hole when working on a data science project.

**The goal** of this stage is to clearly define your goal(s), measures of success, and plans on how to achieve that.

**The deliverable** is documentation of your goal, your measure of success, and how you plan on getting there. If you haven't clearly defined success, you will not know when you have achieved it.

**How to get there:** You can get there by answering questions about the final product & formulating or identifying any initial hypotheses (from you or others).

Common questions include:

- What will the end product look like?
- What format will it be in?
- Who will it be delivered to?
- How will it be used?
- How will I know I'm done?
- What is my MVP?
- How will I know it's good enough?

Formulating hypotheses

- Is attribute V1 related to attribute V2?
- Is the mean of target variable Y for subset A significantly different from that of subset B?
- ...

## **Acquisition**

**AKA** Data Gathering, Data Import, Data Wrangling (Acquisition + Prep)

**The goal** is to create a path from original data sources to the environment in which you will work with the data. You will gather data from sources in order to prepare and clean it in the next step. Many data scientists agree that this stage, along with the preparation stage, is where you will spend a majority of your time.

**The deliverable** is a file, acquire.py, that contains the function(s) needed to reproduce the acquisition of data.

**How to get there:**

- If the data source is SQL, you may need to do some clean-up, integration, aggregation or other manipulation of data in the SQL environment before reading the data into your python environment.
- Using the Python library pandas, acquire the data into a dataframe using a function that reads from your source type, such as pandas.read_csv for acquiring data from a csv.
- You may use Spark and/or Hive when acquiring data from a distributed environment, such as HDFS.
- Examples of source types include RDBMS, NoSQL, HDFS, Cloud Files (S3, google drive), static local flat files (csv, txt, xlsx).

## **Preparation**

**AKA** Data Tidying, Data Cleansing, Data Wrangling (Acquisition + Prep)

**The goal** is to transform the data into a shape where it can be easily explored, analyzed and visualized. To achieve this, the data is split into 3 samples (train, validate, and test). The data is split this way so we end up with one large sample to explore and train our models, a smaller sample to evaluate and develop our models, and a final sample to test our final model once it has been chosen. This final test helps us understand how accurately our final model predicts data that was not used in its development.

**The deliverable** is a file, prep.py, that contains the function(s) needed to reproduce the preparation of the data. The resulting dataframes should be split into 3 samples (Train, Validate, Test) as described above. Splits should contain roughly a 70%:20%:10% split. This can vary depending on the amount of available data.  

- The train dataset is explored during exploration, and used to build and evaluate predictive models during modeling.
- The validate dataset is used to evaluate and fine tune models during modeling. After all models are evaluated, a best model is chosen.
- The test dataset is used as a final evaluation of the best model, to help us understand how accurate the model is when predicting on data not used to train or tune the model.


**How to get there:**

- Python libraries: pandas, matplotlib, seaborn, scikit-learn.
- Use pandas to perform tasks such as handling null values, outliers, normalizing text, binning of data, changing data types, etc.
- Use matplotlib or seaborn to plot distributions of numeric attributes and the target.
- Use scikit-learn to split the data into train, validate, and test samples.

## **Exploration and Pre-processing**

**AKA** Exploratory Analysis/visualization, Feature Engineering, Feature Selection

**The goal** is to discover features that have the largest impact on the target variable, i.e. provide the most information gain, drive the outcome.

**The deliverable** is a file, preprocess.py, that contains the function(s) needed to reproduce the pre-processing of the data. The dataframe resulting from these functions should be one that is pre-processed, i.e. ready to be used in modeling. This means that attributes are reduced to features, features are in a numeric form, there are no missing values, and continuous and/or ordered values are scaled to be unitless.

**How to get there:**

- Use python libraries: pandas, statsmodels, scipy, numpy, matplotlib, seaborn, scikit-learn.
- Perform statistical testing to understand correlations, significant differences in variables, variable interdependencies, etc.
- Create visualizations that demonstrate relationships across and within attributes and target.
- Use domain knowledge and/or information gained through exploration to construct new features.
- Remove features that are noisy, provide no valuable or new information, or are redundant.
- Use scikit-learn's preprocessing algorithms (feature selection, feature engineering, dummy variables, binning, clustering, e.g.) to turn attributes into features.

## **Modeling**

**The goal** is to create a robust and generalizable model that is a mapping between features and a target outcome.

**The deliverable** is a file, model.py, that contains functions for training the model (fit), predicting the target on new data, and evaluating results.

**How to get there:**

- Python libraries: scikit-learn
- Identify regression, classification, cross validataion, and/or other algorithms that are most appropriate.
- Modeling Process:
    - Use data from train to train your model.
    - Evaluate the model by predicting the target variable in the train and validate data sets.
    - Evaluate as many models as necessary and choose the best model as the final model.
    - Evaluate the final model, using test data, to see how the final model performs on data that was not used in its development.

## **Delivery**

**The goal** is to enable others to use what you have learned or developed through all the previous stages.

**The deliverable** could be of various types:

- A pipeline.py file that takes new observations from acquisition to prediction using the previously built functions.
- A fully deployed model.
- A reproducible report and/or presentation with recommendations of actions to take based on original project goals.
- Predictions made on a specific set of observations.
- A dashboard for observing/monitoring the key drivers, or features, of the target variable.

**How to get there:**

- Python sklearn's pipeline method.
- Tableau for creating a report, presentation, story, or dashboard.
- Jupyter notebook for creating a report or a framework to reproduce your research, e.g.
- Flask to build a web server that provides a gateway to our model's predictions.
