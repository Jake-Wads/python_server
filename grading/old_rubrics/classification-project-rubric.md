# Classification Project Rubric

## 5 CSV File Predicting Churn

- contains the 3 columns specified

## 10 Google Slide

- explains how the model works
- metrics on model accuracy are present
- the link to the google slide is in the project `README`
- slide is appropriate for the audience and able to be to be consumed quickly

## 10 Python Script

- runs without errors
- how to use it is documented
- the script performs the preparation necessary

## 25 Notebook

### 5 Overall

- The notebook has a good title
- Documentation (e.g. clear sections, explanations, interpretations)
- Code Style (e.g. good function and variable names, consistent style)

### 1 Acquisition

- The data is acquired from the `telco_churn` database
- a `peekatdata` function is present and used to look at the recently acquired
  data

### 4 Preparation

- the missing values are explored and handled
- the requested columns are created/transformed
    - `churn`
    - `tenure_year`
    - `phone_id`
    - `household_type_id`
    - `streaming_services`
    - `online_security_backup`
- the data is split into training and test
- any non-numeric variables that are going to be used are encoded
- `monthly_charges` and `total_charges` are scaled

### 10 Exploration

- rate of churn vs tenure is visualized
- is there a price threshold for specific services where the likelihood of churn
  increases?
- is churn comparable for month-to-month customers after the 12th month and
  1-year customers after the 12th month?
- a t-test is performed to compare the monthly charges for cutomers who have
  churned and not churned, controlling for different services
- the correlation between monthly charges and internet service type is
  investigated.
- the correlation between monthly charges, internet service, and phone service
  type is investigated.
- the distribution of each feature is visualized
- the relationship between each feature and churn is visualized
- various different types of plots are used
- conclusions are drawn

### 5 Modeling

- feature selection is performed
- at least 4 different models are fit and evaluated
- the best model is selected and run on the test data set
