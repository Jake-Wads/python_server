import pandas as pd
import matplotlib.pyplot as plt


def clustering_example1(iris: pd.DataFrame):
    """
    Expects the iris dataframe to have a cluster column.
    """
    fig, axs = plt.subplots(2, 2, figsize=(16, 9), sharex=True, sharey=True)

    iris.plot.scatter(
        y="petal_length", x="sepal_length", ax=axs[0, 1], title="Original Data"
    )

    for species, subset in iris.groupby("species_name"):
        axs[1, 0].scatter(subset.sepal_length, subset.petal_length, label=species)
    axs[1, 0].legend()
    axs[1, 0].set(title="Actual Species")

    # This is kinda gross and hacky, but we're doing it by hand so that the
    # colors match up with the actual species data
    axs[1, 1].scatter(
        iris.query("cluster == 0").sepal_length,
        iris.query("cluster == 0").petal_length,
        label=0,
    )
    axs[1, 1].scatter(
        iris.query("cluster == 2").sepal_length,
        iris.query("cluster == 2").petal_length,
        label=2,
    )
    axs[1, 1].scatter(
        iris.query("cluster == 1").sepal_length,
        iris.query("cluster == 1").petal_length,
        label=1,
    )
    axs[1, 1].legend()
    axs[1, 1].set(title="K-Means Clusters")

    axs[0, 0].text(
        (axs[0, 0].get_xlim()[1] + axs[0, 0].get_xlim()[0]) / 2,
        (axs[0, 0].get_ylim()[1] + axs[0, 0].get_ylim()[0]) / 2,
        "K-Means Clustering",
        size=24,
        ha="center",
        va="center",
    )
    axs[0, 0].set_axis_off()

    for ax in axs.ravel()[1:]:
        ax.set(xlabel="sepal_length", ylabel="petal_length")
