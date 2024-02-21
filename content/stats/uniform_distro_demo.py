import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# generate a uniform distribution using random generator 

def generate_uniform_distro(number_of_experiments, minimum_outcome_value, maximum_outcome_value, bins):
    n = number_of_experiments
    start = minimum_outcome_value
    width = maximum_outcome_value - minimum_outcome_value
    data_uniform = uniform.rvs(size=n, loc=start, scale=width)
    ax = sns.distplot(data_uniform,
                      bins=100,
                      kde=True,
                      color='skyblue',
                      hist_kws={"linewidth": 15,'alpha':1})
    ax.set(xlabel='Uniform Distribution ', ylabel='Frequency')
    return plt.show()

# demonstrate a uniform distribution using a classic case (with perfect outcomes) 

def uniform_demo(possible_outcomes, experiments):
    outcomes = []
    for i in range(1, possible_outcomes + 1):
        new_outcomes = np.ndarray.tolist(np.repeat(i, experiments/possible_outcomes))
        outcomes = outcomes + new_outcomes

    # build plot
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(13,4))

    labels = list(dict.fromkeys(outcomes)) 
    x = np.array(list(range(min(labels), max(labels)+1)))  # the label locations
    width = 0.35  # the width of the bars
    hist_range = (min(labels)-0.5,max(labels)+0.5)
    xlabel = 'Outcome of x: X~U[1,6]'
    ylabel = 'Number of outcomes of x'
    
    ## plot 1: 
    #    ax1.hist(outcomes, bins=mybins, density=False, facecolor='green')

    
    ax1.hist(outcomes, bins=6, density=False, range=hist_range, align='mid', facecolor='skyblue')

    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.set_title('Uniform Distribution Histogram')    
    
    ax1.annotate('A die was rolled 600 times.\nEach side (x) showed up 100 times.\nTherefore,\n     P(x) = 100/600 = 1/6',
            xy=(1, 50), xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            fontsize=12,
            color='black',
            ha='left', va='bottom')
    
    ## plot 2:

    ax2.hist(outcomes, bins=6, density=True, range=hist_range, align='mid', facecolor='skyblue') 
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel(ylabel)
    ax2.set_title('Probability Mass Function: Probability of rolling each side')

    ax2.annotate('Probability of rolling each number is 1/6.\n     P(x) = 1/6 = .167\nTotal Area Under the Curve:\n     AUC = 6 * (1/6) = 1',
            xy=(.8,.08), xytext=(3, 3),  # 3 points vertical offset
            textcoords="offset points",
            fontsize=12,
            color='black',
            ha='left', va='bottom')
    
    return plt.show()