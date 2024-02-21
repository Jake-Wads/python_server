# Statistics

> There are three types of lies - lies, damn lies, and statistics   
> *- Benjamin Disraeli*

In this section we will review some basic descriptive statistics, talk about different probability distributions, and give an introduction to hypothesis testing.

## Goals

- Build on top of the statistics knowledge from the khan academy prework
- Understand how to use the uniform, binomial, poisson, and normal distributions to model real-world scenarios
- Understand in general how hypothesis testing is performed 
- Know when to use a t-test, correlation test, and $\chi^2$ test
- Write python code that simulates experiments in order to calculate an experimental probability
- Use various statistical distributions in python through `scipy.stats`
- Perform hypothesis testing in python code

## A Note on Visualizations, [the `viz` module](./viz.py)

Throughout the statistics curriculum you will see a module named `viz` imported in the code examples. This module contains some complex matplotlib plotting code, and is available for reference [here][1]. The intent of putting the code in a seperate module is to not distract from the lesson at hand.

[1]: viz.py

## Descriptive Statistics

Before we move on to more advanced concepts, we'll review some descriptive statistics terminology.

Descriptive statistics, as the name implies, let us *describe* a set of data.

We will discuss two main categories of descriptive statistics, measures of central tendancy, and measures of spread. The measures we will discuss focus on a single variable, for example, age or height. These measures do **not** measure multiple variables at the same time, or the interaction/relationship between variables.

### Measures of Central Tendency

All of the measures of central tendancy allow us to describe where the middle, or most mass of a data set is.

- **mean**: the average value, i.e. the sum of all the values divided by the number of values.

    $$ \frac{\sum_{i=1}^n x_i}{n} $$
    
    The mean can be subject to influence by large outlier points.

- **expected value**: similar to the average, except that each value is weighted by its probability

    $$ E[X] = \sum_{i=1}^n x_i p_i $$

- **median**: The center, or middle value. When there are an even number of data points, the average of the two middle points.

- **mode**: the most frequently occuring value

- **bi-modal**: when two values tie for the mode

- **trimmed mean**: The average after removing a certain percentage of outliers. Less sensitive to outliers than the mean.

### Measures of Spread

The measures of spread allow us to describe how spread out a data set is. These measures can give us an idea of the shape of the data by describing how far points tend to be from the middle.

- **Min**: smallest value

- **Max**: largest value

- **Range**: The difference between the max and the min

- **Mean Absolute Deviation**: The average of deviations from a central point, usually the mean. People often think and talk in terms of mean absolute deviation. For example, "we sell 100 units a day ± 10%". This measure of spread is the most common measure of spread/variance in conversational language.

- **Quantile**: The cut points that divide a probability distribution into equally sized continuous intervals. To divide our distribution into `n` equally sized intervals, there are `n-1` quantiles. 
    - To divide a distribution into 2 equally sized intervals, the median is the quantile. This is because the median is the middle of the range of values. Half of the values are below the median, and the other half of the values are above the median.
    - To create two evenly sized intervals from the distrubtion `[1, 2, 3, 4, 5, 6]`, the median is 3.5. The first half of values are between 1 and 3.5, and the second half of the values are between 3.5 and the max.

- **Quartile**: The cut points on a distrubtion to subdivide it into 4 equally sized intervals are called the quartiles. To create 4 equally sized quarters, we need 3 "cut points" called quartiles. The quartiles are commonly abbreviated as Q1, Q2, and Q3. 
    - Our quartiles Q1, Q2, and Q3 are numbers that create boundries for our 4 quarters. The quartiles split the distribution into 4 different intervals. 
        - 25% of the observations are between the min and Q1.
        - 50% of the observations are between the min and Q2.
        - 75% of the observations are between the min and Q3. 
    - How to use the quartiles to subdivide our distribution into four evenly sized quarters.
        - The first quarter contains values between the min and Q1. 
        - The second quarter contains values between Q1 and Q2.
        - The third quarter contains values between Q2 and Q3.
        - The fourth quarter contains values between Q3 and the max.
    - Consider `x = np.array([1, 2, 3, 4, 5, 6, 7, 8])`.
        - Q1 is `2.5` calculated by `np.quantile(x, 0.25)`
        - Q2 is `4.5` calculated by `np.quantile(x, 0.5)`
        - Q3 is `6.5`, calculated by `np.quantile(x, 0.75)`

- **Percentile**: A quantile cut into 100 equally sized intervals

    The percentile can be interpreted as the point where a percentage of values
    fall below it.

    For example, the 75% of the values fall below the 75th percentile.

- **IQR**: The Interquartile Range, Q3-Q1 (75th percentile - 25th percentile)

- **Variance**: The average squared distance between each point and the mean

    $$ \frac{1}{n}\sum(x_i-\mu)^2 $$

    We may divide by n-1 if sample is small to correct for a bias

    Note that the units of the variance are the units of the variable being
    measured squared.

- **Standard Deviation**: The square root of the variance

    $$ \sqrt{\frac{1}{n}\sum(x_i-\mu)^2} $$

    Measures the absolute variability, so the units can be compared to the original values

- **Skew**

    - Symmetric
    - Left-skewed: A set of data values in which the mean is generally less than the median. The left tail of the distribution is longer than the right tail of the distribution.
    - Right-skewed: A set of data values in which the mean is generally greater than the median. The right tail of the distribution is longer than the left tail of the distribution.
