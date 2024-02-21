# Simulation

1. Overview / context
2. Super simple example
3. Curriculum examples

## Stats Overview

- The point of our stats module isn't to make you an expert statistician, but to
  give you the stats knowledge you need to do data science
- The overview page lists a bunch of descriptive stats, it's probably worth
  reviewing to make sure everyone is on the same page.

## Simulation

NB. When demoing for students, I like to start with very small numbers that could
be calculated in their head. E.g. for the simulations start with a 5x2 matrix to
introduce the concept, then crank the number of simulations up to like a
10,000x2 matrix.

- Simulation is a way for us to calculate probabilities by blowing off statistics
    - i.e. we are calculating probabilities experimentally, as opposed to theoretically
    - This is a great way to check our work too. For example, if we came up with
      some calculated statistic based on a theoretical distribution, we could
      also try to arrive at that number through simulation and see if the
      numbers match
    - As the number of simulations goes up, our experimental probability gets
      more precise
- Key vocabulary: simulation vs trial vs n
    - one simulation can consist of multiple trials (NB think binomial distribution)
    - one simulation could be of multiple subjects
    - we have 2 numbers here, the number of trials or subjects within each
      simulation, and then also the number of simulations all together
    - example: How many heads do we get after flipping two coins?
        - here the number of trials (or n_subjects) is 2
        - we could simulate this many times (e.g. 10,000) and take the number of
          simulations where we got 2 heads divided by the total number of
          simulations as the experimental probability that we got 2 heads.
- How to do simulation with python (NB this is a way I think is good, but approaches vary here)
    1. Figure out a way to represent your data (e.g. heads is 1, tails is 0)
    1. Create a matrix of random numbers where rows represent simulations and
       columns represent trials (flipping 2 coins 10,000 times would be a 10,000
       x 2 matrix)
    1. apply some aggregate row wise to produce the results of each simulation
    1. apply an aggregation to the resulting 1-d data to get your overall result

### Example

NB. This is what I'd walk through first with the students before working through
the curriculum examples.

> What's the probability I get 2 or more heads after flipping 3 coins?

```python
# 1. Represent the data -- 1 will be heads, 0 will be tails

# 2. Create a matrix of random numbers

coin_flips = np.random.choice([0, 1], (20, 3))
print(coin_flips)

# Here the `(20, 3)` tuple tells numpy the shape of the matrix to generate Since
# we are flipping 3 coins we have 3 columns, and we are doing 20 simulations,
# we'll have 20 rows.

# 3. Apply an aggregate row-wise to produce the results of each simulation
# Since we've chosen 1 for heads, we can do a sum row-wise:

n_heads_in_each_simulation = coin_flips.sum(axis=1)
print(n_heads_in_each_simulation)

# And now n_heads_in_each_simulation is a 1-d array where each number represents
# the number of heads that came up in that simulation.
#
# We want to know how many times we have 2 or more heads, so we can convert
# n_heads_in_each_simulation to a boolean array that tells us whether each trial
# "succeeded"

sims_with_at_least_2_heads = n_heads_in_each_simulation >= 2
print(sims_with_at_least_2_heads)

# 4. Aggregate the resulting data to get our experimental probability
# Here we'll calculate the number of successful trials
n_successes = sims_with_at_least_2_heads.sum()
# we can take the sum of a boolean series to find the number of true values
print(n_successes)
# and divide by the number of simulations to get our experimental probability
print(n_successes / 20)

# Note that we just did the sum divided by the length, which is the definition
# of the mean.
print(sims_with_at_least_2_heads.mean())
# doing `.mean` on a boolean series will give the percentage of true values

# All the above could be done in a one-liner to get rid of the intermediate
# variables too. Here we'll bump the number of simulations to 10,000
(np.random.choice([0, 1], (10_000, 3)).sum(axis=1) >= 2).mean()
```

## Curriculum Examples
