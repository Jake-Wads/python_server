<style>li { line-height: 1; }</style>
Regression Project
------------------

5 points Overall

- 1 point: The notebook has a good title, either in the filename, or as a
  heading at the top of the file
- 2 points: the code / thought process is well documented
- 2 points: the code follows a good, consistent style (good variable names)

6 points Planning

- 1 point: the goal of the project is clearly stated
- 1 point: the end deliverable of the project is clearly stated
- 2 point: at least 3 hypotheses for the project are present
- 2 points: a data dictionary is present

2 points Acquisition

- 1 point: data set is created with the specified columns
- 1 point: an overview of the data (e.g. `.head`, `.describe`, etc) is performed

4 points Preparation

- 1 point: the number / percentage of missing values in each column is present
- 1 point: the missing values in the dataset are handled (either filled or dropped)
- 2 point: the distribution of each independent variable is visualized

5 points Exploration

- 1 point: a plot of each independent var vs the dependent var is present
- 1 point: the correlations between each variable are explored
- 1 point: a t-test is performed to compare logerror for houses with 3 bedrooms
  vs 5+ bedrooms
- 1 point: the results of the t-test are interpreted
- 1 point: another t test is performed, dividing the data set up in some
  different way

3 points: Feature Engineering

- 1 point: a new feature is constructed based on 2+ existing variables
- 1 point: a OLS model is created
- 1 point: conculsions are drawn / the OLS model is summarized

7 points: Modeling

- 1 point: an `sklearn` `LinearRegression` model is created and fitted on the train
  data set
- 1 point: the model is evaluated on the training data using $r^2$ and mean
  squared error or mean absolute error
- 1 point: the model's residuals are plotted
- 2 points: at least 2 other LinearRegression models are created and their
  performance is measured on the training data set
- 2 points: the best model is used to predict the test data, and it's performace
  is measured


Instructor notes:

- a data error was added to the table with a date occurring in 2018. If the student doesn't filter for the year (due to the name of the table, assuming all years are 2017), this record will incorrectly show up in their data. 

INSERT INTO `zillow`.`predictions_2017`
(`id`,
`parcelid`,
`logerror`,
`transactiondate`)
VALUES
(77613, 13083743, -0.197754626087,  '2018-05-25');

- only single unit props
- 13,289 properties
(tax rates = tax amount / tax value). 

- The last transaction for each parcel whose last transaction occurred during may or june of 2017
- only single unit properties
- you will use square feet of the home, number of bedrooms, and number of bathrooms to estimate the properties assessed value, 'taxvaluedollarcnt'. 
- only 1 observation per parcel id
- are you using the best field for square feet of home, number of bedrooms and number of bathrooms?  This will require a bit of exploration of the data within the SQL table. 
- 
