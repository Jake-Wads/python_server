import pandas as pd
import numpy as np
from functools import partial

# recall = | actual positive -- TP / (TP + FN)
# precision = | predicted positive -- TP / (TP + FP)


def accuracy(actual, predicted):
    return (actual == predicted).mean()


def recall(actual, predicted, positive_class):
    return (actual == predicted)[actual == positive_class].mean()


def precision(actual, predicted, positive_class):
    return (actual == predicted)[predicted == positive_class].mean()


def evaluate_model(actual, predicted):
    output = {"accuracy": accuracy(actual, predicted)}
    for klass in actual.unique():
        output["recall_" + klass] = recall(actual, predicted, klass)
        output["precision_" + klass] = precision(actual, predicted, klass)
    return pd.Series(output)


def good_cat_precision(actual):
    if actual == "cat":
        return np.random.choice(["cat", "dog"], p=[0.35, 0.65])
    else:
        return np.random.choice(["cat", "dog"], p=[0.05, 0.95])


def good_defect_precision(actual):
    if actual == "Defect":
        return np.random.choice(["Defect", "No Defect"], p=[0.35, 0.65])
    else:
        return "No Defect" if np.random.uniform() < 0.99 else "Defect"


def get_rubber_duck_models():
    n = 200
    np.random.seed(123)
    df = pd.DataFrame(
        {"actual": np.random.choice(["Defect", "No Defect"], n, p=[0.1, 0.9])}
    )
    df["opposite"] = df.actual.apply(
        lambda s: "No Defect" if s == "Defect" else "Defect"
    )
    # good precision
    df["model1"] = df.actual.apply(good_defect_precision)
    # noise
    df["model2"] = np.random.choice(["Defect", "No Defect"], n)
    # good recall
    df["model3"] = np.where(
        df.actual == "Defect",
        np.random.choice(["Defect", "No Defect"], n, p=[0.9, 0.1]),
        np.random.choice(["Defect", "No Defect"], n, p=[0.5, 0.5]),
    )
    return df.drop(columns=["opposite"])


def get_dog_cat_models():
    n = 5000
    np.random.seed(123)
    df = pd.DataFrame({"actual": np.random.choice(["dog", "cat"], n, p=[0.65, 0.35])})
    df["opposite"] = df.actual.apply(lambda s: "dog" if s == "cat" else "cat")
    # ~ 80% accuracy
    df["model1"] = np.where(np.random.uniform(size=n) <= 0.8, df.actual, df.opposite)
    # good cat recall
    df["model2"] = np.where(
        df.actual == "dog",
        np.where(np.random.uniform(size=n) < 0.5, "dog", "cat"),
        np.where(np.random.uniform(size=n) < 0.90, "cat", "dog"),
    )
    # noise
    df["model3"] = np.random.choice(["dog", "cat"], n)
    # good cat precision
    df["model4"] = df.actual.apply(good_cat_precision)
    return df.drop(columns=["opposite"])


if __name__ == "__main__":
    import os

    get_dog_cat_models().to_csv("gives_you_paws.csv", index=False)
    get_rubber_duck_models().to_csv("c3.csv", index=False)
    os.system(
        "scp gives_you_paws.csv ds.codeup.com/srv/www/codeup.com/public/data/gives_you_paws.csv"
    )
    os.system("scp c3.csv ds.codeup.com/srv/www/codeup.com/public/data/c3.csv")
