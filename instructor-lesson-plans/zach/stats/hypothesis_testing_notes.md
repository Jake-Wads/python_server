## Prereqs

- notation, hat, bar
- sample vs population?
    - statistic vs parameter
- mean vs proportion

## Explanation

0. We are 95% confident the random variable for a normal distribution (TODO:
   fill in with a real example) will fall within which two values? Store this
   thought in your head for later
1. Scratch off tickets, calculate P(win) or how many students win
2. Imagine we do this for every data science (and webdev) class, the
   distribution of our calculation of P(win) (or the number of students that
   win) will be normally distributed
3. Assuming the win rate is what they say it is, what is the likelihood that we
   observed the win rate that we calculated?

1 is our data. 2 is the central limit theorem and the concept of a sampling
distribution here we could also talk about confidence intervals for sample
statistics. 3 is the p value for a 1 sample t-test

```python
import math
import numpy as np
import matplotlib.pyplot as plt

n = 100
nsims = 10_000
expected_value = 1/4 * n

# let x = classrooms (matrix elements before the sum are individual students)

x = np.random.choice([0, 1], (nsims, n), p=[.75, .25]).sum(axis=1)
x = pd.Series(x)
x.value_counts(bins=np.arange(0, 51)).sort_index().plot.bar(width=1, fc='white')
sd = ((math.sqrt(n * .25 * .75)) / math.sqrt(n))
plt.vlines([expected_value - sd, expected_value + sd], 0, 1000, ls=':')
plt.grid(False)

[expected_value - sd, expected_value + sd]

```

## Simulation Based Approach

- scenario: P(win scratch off) = .25
- imagine 1000 people have played this game
- we model win with true and lose with false
    - because of this, we can take the mean of a series to measure the
      likelihood of winning

```python
s = pd.Series([True] * 250 + [False] * 750)
print('The actual probability of winning is %.2f' % s.mean())
s.value_counts().plot.bar()
```

- surveying everyone who has played is impractical
- If we were to take a random sample of size, say 50, we probably won't see
  exactly .25

```
n = 50
s.sample(50, random_state=70).mean()
```

- in fact, we'd calculate different win rates depending on which individuals
  came up in our sample of 50 individuals

```python
[s.sample(n, random_state=seed).mean() for seed in range(100, 104)]
```

- if we repeated the sampling a whole bunch of times, we'd see that the
  calculated probabilities of winning form a normal distribution
- CLT: sample means are normally distributed even if the underlying random var
  isn't

```python
sample_means = pd.Series([s.sample(n, random_state=seed).mean() for seed in range(1000)])
sample_means.plot.hist(bins=19)
```

- the mean of the distribution of the sample means will be the "true" mean
- the standard deviation of the sample means is $\sqrt{\frac{pq}{n}}$, aka the
  standard error

```python
se = math.sqrt((.25 * .75) / 50)
```

Let's compare our calculated standard error (i.e. the standard deviation of the
sample means) to the experimental value:

```
print('SE:                 %.4f' % se)
print('sample_means.std(): %.4f' % sample_means.std())
```

```python
stats.norm(.25, math.sqrt((.25 * .75) / 50)).cdf(.13)
```

## misc

### Visualizing when a sample proportion will be normally distributed

The sampling distribution of the sample proportion will be normally distributed
when $n \times p \times q >= 10$

```python

df = pd.DataFrame(
    [dict(n=n, p=p, npq=n*p*(1 - p)) for n in range(2, 200) for p in np.arange(0, 1, .01)]
).assign(normal=lambda df: df.npq >= 10)
for group, data in df.groupby('normal'):
    plt.scatter(data.p, data.n, label=group)
plt.xlabel('p')
plt.ylabel('n')
plt.xticks(
    np.arange( 0, 1.1, .05),
    [round(x, 1) if i % 2 == 0 else '' for i, x in enumerate(np.arange(0, 1.1, .05))],
)

df = pd.DataFrame(
    [dict(n=n, p=p, npq=n*p*(1 - p)) for n in range(10, 210, 10) for p in [.25, .4, .5, .6, .75]]
).assign(normal=lambda df: df.npq >= 10)
for group, data in df.groupby('p'):
    plt.scatter(data.n, data.npq, label=round(group, 1))
plt.legend()

```
