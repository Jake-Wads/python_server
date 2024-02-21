# # Machine Learning with Spark

import numpy as np
from pydataset import data
import pyspark
import pyspark.ml
from pyspark.sql.functions import *

spark = pyspark.sql.SparkSession.builder.getOrCreate()

df = spark.createDataFrame(data('tips'))

train, test = df.randomSplit([0.8, 0.2], seed=123)


def shape(df: pyspark.sql.DataFrame):
    return df.count(), len(df.columns)


shape(train)
shape(test)

# ## Regression
#
# We'll first demonstrate a regression problem: predicting the tip amount.

train.show(5)

# `pyspark.ml.feature.RFormula`
#
# - `tip ~ total_bill`: predict tip based on total bill
# - `tip ~ total_bill + size`: predict tip based on total bill and size
# - `tip ~ .`: predict tip based on all the other features in the dataset

# nb: spark's rformula does encoding
rf = pyspark.ml.feature.RFormula(formula="tip ~ total_bill + size").fit(train)

rf.transform(train).show(5)

# `features` and `labels` columns are the shape/name required for `pyspark.ml`

train_input = rf.transform(train).select('features', 'label')
train_input.show(5)

# Create, fit, and use the model.
#
# **Note**: unlike `sklearn`, each step produces a new object!

lr = pyspark.ml.regression.LinearRegression()
lr

print(lr.explainParams())

lr_fit = lr.fit(train_input)
lr_fit.transform(train_input).show(5)

# Weird error messages with nulls!
tips = data('tips')
tips.loc[np.random.choice(tips.index), 'total_bill'] = np.nan
tips_transformed = rf.transform(spark.createDataFrame(tips))
lr.fit(
    tips_transformed
).transform(
    tips_transformed
)

# Training results:

lr_fit.summary

lr_fit.summary.r2, lr_fit.summary.rootMeanSquaredError

[x for x in dir(lr_fit.summary) if not x.startswith('_')]

# How do we do on the test data?

test_input = rf.transform(test)
lr_fit.transform(test_input).show(4)

evaluator = pyspark.ml.evaluation.RegressionEvaluator()
rmse = evaluator.evaluate(lr_fit.transform(test_input))
rmse

# ## Classification
#
# Preprocess the training data

rf = pyspark.ml.feature.RFormula(formula='time ~ total_bill + size').fit(train)
train_input = rf.transform(train)
train_input.show(50)

# Create and fit the model

lr = pyspark.ml.classification.LogisticRegression()

# +
# print(lr.explainParams())
# -

lr_fit = lr.fit(train_input)

# Model Evaluation

[x for x in dir(lr_fit.summary) if not x.startswith('_')]

# area under TPR (recall) vs FPR (FP / (FP + TN)) curve
# https://en.wikipedia.org/wiki/Receiver_operating_characteristic
lr_fit.summary.areaUnderROC

evaluator = pyspark.ml.evaluation.BinaryClassificationEvaluator()
test_auc = evaluator.evaluate(lr_fit.transform(rf.transform(test)))
test_auc

test_input = rf.transform(test)

# confusion matrix for the test data
(lr_fit.transform(test_input)
 .select('time', 'total_bill', 'size', 'label', 'probability', 'prediction')
 .groupby('prediction') # predicted == rows
 .pivot('label') # actual values are columns
 .count()
 .show())

# +
# Many other preprocessing steps
dir(pyspark.ml.feature)
