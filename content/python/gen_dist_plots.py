import pandas as pd, numpy as np, matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import uniform, binom, norm, poisson
import seaborn as sns

mpl.rcParams['figure.figsize'] = [14, 10]

def do_binom_dist():
    n = 10_000

    plt.suptitle('Binomial Distribution')
    for i, p in enumerate([0.1, 0.5, 0.75, 0.9]):
        plt.subplot(2, 2, i + 1)
        x = binom.rvs(size=n, p=p, n=10)
        pd.Series(x).plot.hist(bins=range(11))
        plt.title(f'{n:,} samples from p={p}, n=10')
        plt.xlabel('Number of Successes in 10 trials')
        plt.ylabel('')

    plt.savefig('./binomial_distribution.png')
    plt.show()

def do_poisson_dist():
    n = 10_000

    plt.suptitle(f'Poisson Distribution, {n:,} simulations')
    all_bins = [[0, 7], [0, 21], [0, 21], [60, 140, 10]]
    for i, mu in enumerate([1, 5, 10, 100]):
        plt.subplot(2, 2, i + 1)
        x = poisson.rvs(size=n, mu=mu)
        bins = all_bins[i]
        pd.Series(x).plot.hist(bins=range(*bins))
        plt.title(f'$\mu$={mu}')
        plt.xlabel('Number of events')
        plt.ylabel('')

    plt.savefig('./poisson_distribution.png')
    plt.show()

def do_normal_dist():
    n = 10_000

    plt.suptitle(f'Normal Distribution, {n:,} simulations')
    colors = ['blue', 'red', 'green', 'orange']
    for i, vals in enumerate([(50, 10), (100, 20), (100, 40), (150, 50)]):
        mu, sigma = vals
        x = norm.rvs(size=n, loc=mu, scale=sigma)
        sns.distplot(x, color=colors[i], label=f'$\mu$={mu}, $\sigma$={sigma}')
        plt.ylabel('frequency')

    plt.legend()
    plt.savefig('./normal_distribution.png')
    plt.show()

def do_uniform_dist():
    n = 10_000

    plt.suptitle(f'Uniform Distribution, {n:,} simulations')
    x = uniform.rvs(size=n, loc=1, scale=6)
    pd.Series(x).plot.hist(bins=range(1, 7), align='left')
    plt.title('Rolling a dice')

    plt.savefig('./uniform_distribution.png')
    plt.show()


