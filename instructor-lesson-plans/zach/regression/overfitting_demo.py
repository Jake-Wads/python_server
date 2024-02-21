"""
Generates the visual of an overfit polynomial regression model.
"""

import numpy as np
import matplotlib.pyplot as plt
import sklearn.preprocessing
import sklearn.model_selection
import sklearn.linear_model
from sklearn.metrics import mean_squared_error


def main():
    plt.rc("font", size=15)
    plt.figure(figsize=(16, 9))
    np.random.seed(12)

    x = np.random.uniform(size=15)
    y = np.random.uniform(size=15)
    x = x.reshape(-1, 1)

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y)

    plt.scatter(x_train, y_train, label="train")
    plt.scatter(x_test, y_test, label="test")

    degree = 8
    poly = sklearn.preprocessing.PolynomialFeatures(degree=degree, include_bias=False)
    poly.fit(x_train)
    x_poly = poly.transform(x_train)
    model = sklearn.linear_model.LinearRegression().fit(x_poly, y_train)
    x0 = np.linspace(x.min(), x.max()).reshape(-1, 1)

    plt.plot(x0, model.predict(poly.transform(x0)), label="polynomial model, degree=8")

    plt.gca().set(title="Example of Overfitting", xlabel="x", ylabel="y")
    plt.text(
        0,
        3,
        "The model fits the training data too perfectly,\nand does not generalize (misses the test data points).",
        va="top",
        ha="left",
    )
    plt.legend(loc="upper right")

    eq = " + ".join(
        reversed(
            [
                f'{coef:.1f}{x.replace("0", "")}'
                for coef, x in zip(model.coef_, poly.get_feature_names())
            ]
        )
    )
    plt.text(
        -0.025,
        -2.1,
        r"$\hat{y} = " + f"{eq} + {model.intercept_:.1f}$",
        size=13,
        ha="left",
        va="bottom",
    )
    return plt.gcf()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--save", help='filepath to save viz to')
    args = parser.parse_args()

    fig = main()

    if args.save is not None:
        fig.savefig(args.save)
    else:
        fig.show()
