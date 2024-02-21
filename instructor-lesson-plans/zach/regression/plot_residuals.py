"""
Fancy viz with 4 subplots for differing ways of visualizing residuals
"""
import matplotlib.pyplot as plt


def plot_residuals(actual, predicted):
    residuals = actual - predicted

    fig, axs = plt.subplots(2, 2, figsze=(12, 12))
    axs[0, 0].hist(residuals)
    axs[0, 0].set(title="Distribution of Residuals")

    axs[0, 1].scatter(actual, predicted)
    axs[0, 1].set(title="Actual vs Predicted", xlabel="$y$", ylabel=r"$\hat{y}$")

    axs[1, 0].scatter(actual, residuals)
    axs[1, 0].set(title="Actual vs Residuals", xlabel="$y$", ylabel=r"$y - \hat{y}$")

    axs[1, 1].scatter(predicted, residuals)
    axs[1, 1].set(
        title="Predicted vs Residuals", xlabel=r"$\hat{y}$", ylabel=r"$y - \hat{y}$"
    )

    return fig, axs
