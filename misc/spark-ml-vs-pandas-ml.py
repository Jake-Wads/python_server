import pandas as pd
from pydataset import data

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark import ml

spark = SparkSession.builder.getOrCreate()

df = spark.createDataFrame(data("voteincome"))

df.count()

train, test = df.randomSplit([0.8, 0.2], 123)

rf = ml.feature.RFormula(formula="vote ~ income + education + age + female")
rf = rf.fit(train)

lr = ml.classification.LogisticRegression()
lr = lr.fit(rf.transform(train))

(
    lr.transform(rf.transform(train))
    .select("label", "rawPrediction", "probability", "prediction")
    .show()
)

lr.summary.accuracy

spark_lr_coefs = pd.Series(
    dict(zip(["income", "education", "age", "female"], lr.coefficients))
)

X, y = train.toPandas().rformula("vote ~ income + education + age + female")

from sklearn.linear_model import LogisticRegression

sklearn_lr_coefs = pd.Series(
    dict(
        zip(
            ["income", "education", "age", "female"],
            LogisticRegression().fit(X, y).coef_[0],
        )
    )
)

pd.DataFrame(
    {
        "spark_lr": spark_lr_coefs.sort_index(),
        "sklearn_lr": sklearn_lr_coefs.sort_index(),
    }
)
