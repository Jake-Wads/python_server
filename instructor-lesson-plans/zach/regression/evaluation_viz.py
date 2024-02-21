"""
Module to generate a visualization of the relationships between the residuals,
SSE, ESS, and TSS.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def make_df():
    np.random.seed(2)

    df = pd.DataFrame({"y": np.random.normal(6, 1, 5)})

    df["x"] = df.y + np.random.uniform(0, 2, 5)

    slope, intercept, r, p, stderr = stats.linregress(df.x, df.y)
    print("p", p)

    df["yhat"] = slope * df.x + intercept
    df["residual"] = df.y - df.yhat
    df["ybar"] = df.y.mean()
    return df


def plot_residuals(df):
    plt.scatter(df.x, df.y, label="y")
    plt.plot(df.x, df.yhat, label=r"$\hat{y}$", marker="o", c="orange")

    # ybar
    plt.hlines(
        df.y.mean(), df.x.min(), df.x.max(), ls=":", label=r"$\bar{y}$", color="purple"
    )

    plt.vlines(
        x=df.x,
        ymin=df[["y", "yhat"]].min(axis=1),
        ymax=df[["y", "yhat"]].max(axis=1),
        ls=":",
        color="firebrick",
        label="residuals",
    )
    plt.title("Residuals = $y - \hat{y}$")
    plt.legend()
    return plt.gca()


def plot_sse(df):
    # y and yhat points
    plt.scatter(df.x, df.y, label="y")
    plt.plot(df.x, df.yhat, label=r"$\hat{y}$", ls=":", marker="o", c="orange")

    # ybar
    plt.hlines(
        df.y.mean(), df.x.min(), df.x.max(), ls=":", label=r"$\bar{y}$", color="purple"
    )

    ax = plt.gca()

    for i, row in df.iterrows():
        fn = min if row.residual > 0 else max
        xy = (row.x, fn(row.y, row.yhat))
        width = height = row.residual
        r = plt.Rectangle(xy, width, height, ls="--", color="black", fill=False)
        ax.add_patch(r)

    # plt.ylim(3.5, 8.5)
    # plt.xlim(4, 9)

    plt.title(r"SSE = $\sum (y - \hat{y})^2$")
    plt.legend()
    return plt.gca()


def plot_ess(df):
    # y and yhat points
    plt.plot(df.x, df.yhat, label=r"$\hat{y}$", ls="", marker="o", c="orange")

    # ybar
    plt.hlines(
        df.y.mean(), df.x.min(), df.x.max(), ls="-", label=r"$\bar{y}$", color="purple"
    )

    ax = plt.gca()

    for i, row in df.iterrows():
        ess = row.yhat - row.ybar
        fn = min if ess > 0 else max
        xy = (row.x, fn(row.yhat, row.ybar))
        width = height = ess
        r = plt.Rectangle(xy, width, height, fill=False, ls="--")
        ax.add_patch(r)

    # plt.xlim(2.5, 10.5)
    # plt.ylim(2.5, 10.5)
    plt.title(r"ESS = $\sum (\hat{y} - \bar{y})^2$")
    plt.legend()
    return plt.gca()


def plot_tss(df):
    # y and yhat points
    plt.scatter(df.x, df.y, label="y")

    # ybar
    plt.hlines(
        df.y.mean(), df.x.min(), df.x.max(), ls="-", label=r"$\bar{y}$", color="purple"
    )

    ax = plt.gca()
    for i, row in df.iterrows():
        tss = row.y - row.ybar
        fn = min if tss > 0 else max
        xy = (row.x, fn(row.y, row.ybar))
        width = height = tss
        r = plt.Rectangle(xy, width, height, fill=False, ls=":")
        ax.add_patch(r)

    # plt.xlim(2.5, 10.5)
    # plt.ylim(2.5, 10.5)
    plt.title(r"TSS = $\sum (y - \bar{y})^2$")
    plt.legend()
    return plt.gca()


def viz(df):
    plt.figure(figsize=(16, 16))
    plt.subplot(2, 2, 1)
    plot_residuals(df)
    plt.subplot(2, 2, 2)
    plot_sse(df)
    plt.subplot(2, 2, 3)
    plot_ess(df)
    plt.subplot(2, 2, 4)
    plot_tss(df)
    plt.show()


if __name__ == "__main__":
    df = make_df()
    viz(df)
    plt.savefig("evaluation_viz.png")
