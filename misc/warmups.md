# Warmup Exercises

Make sure you have the `pydataset` library installed.

```
python -m pip install --upgrade pydataset
```

also,

```
conda install -c conda-forge vega_datasets
```

## General

> Take the word EASY: Its first three letters — E, A and S — are the fifth,
> first, and nineteenth letters, respectively, in the alphabet. If you add 5, 1,
> and 19, you get 25, which is the value of the alphabetical position of Y, the
> last letter of EASY.

> Can you think of a common five-letter word that works in the opposite way — in
> which the value of the alphabetical positions of its last four letters add up
> to the value of the alphabetical position of its first letter?

[NPR Sunday Puzzle for 2016-04-03](http://www.npr.org/2016/04/03/472825113/got-2-words-in-the-same-category-its-rhymin-time)

You can find a list of words on your mac at `/usr/share/dict/words`.

---

Decode the following message:

```
NDM2ZjY0NjU3NTcwMjA1MjZmNjM2YjczMjEwYQo=
```

```
# To generate the message
echo 'Codeup Rocks!' | xxd -p | base64
# to decode
echo NDM2ZjY0NjU3NTcwMjA1MjZmNjM2YjczMjEwYQo= | base64 --decode | xxd -r -p
```

## Pandas

- [Aggregating + Time series aggregations + visualizations](https://gist.github.com/zgulde/96991fedca29ff5371f5e7fa00d3fa95)

---

Copy the table below (taken from the syllabus) and use pandas create a dataframe
based on it, and transform it into the schedule by weeks table.

| Module           | Topic                 | Start Date |
| ------           | -----                 | ---------- |
| Fundamentals     | Intro To Data Science | 2019-08-20 |
|                  | Excel                 | 2019-08-22 |
|                  | Storytelling          | 2019-08-26 |
| Tools            | CLI and Git           | 2019-08-30 |
|                  | SQL                   | 2019-09-03 |
|                  | Python                | 2019-09-11 |
|                  | Stats                 | 2019-09-30 |
| Methodologies I  | Regression            | 2019-10-07 |
|                  | Classification        | 2019-10-17 |
|                  | Clustering            | 2019-10-28 |
|                  | Time Series Analysis  | 2019-11-07 |
| Methodologies II | Anomaly Detection     | 2019-11-18 |
|                  | NLP                   | 2019-11-25 |
|                  | Distributed ML        | 2019-12-09 |
|                  | Advanced Topics       | 2020-01-06 |
|                  | Capstone              | 2020-01-13 |

## Regression
- While this warmup was delivered during regression, it's more of a comprehensive warmup of pandas so far and not regression specific, https://github.com/CodeupClassroom/curie-ds-methodologies/blob/master/dataframe_warmup.ipynb

### Swiss

Create a notebook or python script named `regression_warmup` for this exercise.

1. Load the swiss data set

    ```python
    from pydataset import data

    data('swiss')
    ```

    Skim through the documentation for the dataset

    ```python
    data('swiss', show_doc=True)
    ```

    We'll be using `Fertility` as our target variable to predict.

1. Briefly take a look at the data. You won't need to do any cleaning or
   preparation, but you should get an overview of the data. Visualize the
   distribution of each variable, and take a look at how the individual features
   correlate with the target variable.

1. Split the data into training and test data sets.

1. Fit a linear model using `Agriculture` and `Catholic` as the independent
   variables. Measure the model's performance.

1. Fit a linear model using `Education` and `Examination`. Measure the model's
   performance.

1. Use the best of the above two models and measure that model's performance on
   the test set.

1. Fit a linear model using all of the independent variables. Take a look at the
   resulting model's coefficients. What do these tell us? How do we interpret
   them?

## Classification

### Swiss

1. Load the `swiss` data set
1. Transform the `Catholic` variable into a categorical variable named
   `is_catholic`. The values should be either `Catholic` or `Not Catholic`.
1. Drop the `Catholic` column.
1. Split the data into training and test data sets. We will be trying to predict
   whether or not a province is catholic.
1. Fit a decision tree classifier using the `Education` and `Fertility`
   features. Measure the model's performance.
1. Fit a logistic regression model using `Agriculture` and `Examination`.
   Measure the model's performance.
1. Fit a K Nearest Neighbors model using two features of your choice. Measure
   the model's performance.
1. Use the best model from the ones above on your test data set and evaluate the
   model's predictions.
1. Explain how/why your model is making the predictions that it is.

## Tidying Data

Below is a csv file of student attendance. `P` represents that the student was
present, `A` represents an absence, `H` represents a half day, and `T`
represents a tardy.

    name,2018-01-01,2018-01-02,2018-01-03,2018-01-04,2018-01-05,2018-01-06,2018-01-07,2018-01-08,2018-01-09,2018-01-10,2018-01-11,2018-01-12,2018-01-13,2018-01-14,2018-01-15,2018-01-16,2018-01-17,2018-01-18,2018-01-19,2018-01-20,2018-01-21,2018-01-22,2018-01-23,2018-01-24,2018-01-25,2018-01-26,2018-01-27,2018-01-28,2018-01-29,2018-01-30,2018-01-31
    Sally,P,T,T,H,P,A,T,T,T,P,P,P,T,P,P,A,T,A,A,A,P,T,P,P,A,H,P,T,T,P,P
    Jane,A,P,T,T,T,T,A,T,P,T,H,T,P,H,T,P,P,P,T,P,H,P,P,A,A,P,A,T,H,T,T
    Billy,A,T,A,A,H,T,P,T,P,P,T,P,T,P,P,P,A,T,T,P,H,T,P,P,P,P,T,T,T,A,A
    John,P,T,H,P,P,T,P,P,T,T,P,A,P,P,P,T,P,H,P,T,P,T,P,A,H,A,T,A,T,H,P

Transform the data so that it is in a tidy format, that is, it should look like
this:

    name,date,value
    Sally,2018-01-01,P
    Sally,2018-01-02,T
    Sally,2018-01-03,T
    Sally,2018-01-04,H
    Sally,2018-01-05,P

Next, calculate an attendnace percentage for each student. 2 half days == 1
absence, and 10 tardies == 1 absence. You should end up with this:

              value
    name
    Billy  0.454839
    Jane   0.425806
    John   0.545161
    Sally  0.483871

---

Below is a csv of data that is untidy, two variables are combined together in
the first column.

    one:A,62.8
    one:A,62.6
    two:A,60.1
    two:A,62.3
    three:A,62.7
    three:A,63.1
    one:B,60.0
    one:B,61.4
    two:B,57.5
    two:B,56.9
    three:B,61.1
    three:B,58.9
    one:C,58.7
    one:C,57.5
    two:C,63.9
    two:C,63.1
    three:C,65.4
    three:C,63.7
    one:D,57.1
    one:D,56.4
    two:D,56.9
    two:D,58.6
    three:D,64.7
    three:D,64.5
    one:E,55.1
    one:E,55.1
    two:E,54.7
    two:E,54.2
    three:E,58.8
    three:E,57.5
    one:F,63.4
    one:F,64.9
    two:F,59.3
    two:F,58.1
    three:F,60.5
    three:F,60.0
    one:G,62.5
    one:G,62.6
    two:G,61.0
    two:G,58.7
    three:G,56.9
    three:G,57.7
    one:H,59.2
    one:H,59.4
    two:H,65.2
    two:H,66.0
    three:H,64.8
    three:H,64.1
    one:I,54.8
    one:I,54.8
    two:I,64.0
    two:I,64.0
    three:I,57.7
    three:I,56.8
    one:J,58.3
    one:J,59.3
    two:J,59.2
    two:J,59.2
    three:J,58.9
    three:J,56.6

- What is the average of group `two`? 60.145
- What is the average of subgroup `I`? 58.683333

---

Go find the worst visualization you can! Some examples:

- https://i.kinja-img.com/gawker-media/image/upload/s--IKbw0j5q--/c_scale,f_auto,fl_progressive,q_80,w_800/18ymoh22sul3lpng.png
- http://viz.wtf/image/182610975453
- http://viz.wtf/image/182558288809

---

`data('SupremeCourt')` -- what is each justice's average vote?

- melt, aggregate

---

Data from [the game show Friend or Foe](https://en.wikipedia.org/wiki/Friend_or_Foe%3F_(game_show))

`data('FriendFoe')`

- On average, how much does the cash prize increase each round?
- What percentage of the time did the participants cooperate? Not cooperate?
- Does the partner's age make a difference in

---

```python
import pandas as pd
from sklearn.datasets import load_boston

def pluck(d, *ks):
    return [d[k] for k in ks]

description, cols, X, y = pluck(load_boston(), 'DESCR', 'feature_names', 'data', 'target')

print(description)

df = pd.DataFrame(X, columns=cols).assign(target=y)
```

---

## Stats Word Problems / Simulations

1. My son has about a 30% chance of taking a nap on a given weekend day. What is
   the probability that he doesn't nap at all over the weekend? Naps at least
   one of the two days? Naps both days?

    ```python
    binom(2, .3).pmf([0, 1, 2])
    ```

1. How likely is it that you roll doubles when rolling two dice?

    ```python
    (np.random.choice(range(1, 7), 10**5) == np.random.choice(range(1, 7), 10**5)).mean()
    ```

1. You've heard that the Esquire has a great lunch time burger special; it's so
   good you want to eat there every day for lunch. Unfortunately, the service at
   the Esquire can be kind of slow; slow enough that there's a 40% chance that
   you come back to class late if you go there to eat.

    Your data science instructor has to start class on time after lunch, but also
    understands the value of a good burger. She is aware of the 40% chance that you
    show up late, and says that if you can say there's at least an 85% chance you
    won't be late back from lunch this week, you can go eat at the Esquire as many
    times as you like. How many times should you go out to eat the burger special
    this week?

## Uncategorized / WIP

Needs a melt

```python
data('USArrests')
```

---

1. Load the `painters` data set.
1. Read the documentation and transform the `School` column into the actual
   values.
1. Create a feature named `Overall` that is the average of all of the exams.
1. Compare the average examination scores by school.

---

Shape transformation

- `data("HairEyeColor")`

---

1. Load the `PlantGrowth` data set.
1. Use statistical testing to determine if there is a significant difference in
   the weights between the plants in the control group, treatment1 group, and
   treatment2 group.

---

- `data('mtcars')`: visualize mpg vs disp by cyl

---

- `data('VietNamH')`
    - Is there a significant difference in sex between the head of the household
      for farming homes vs non-farming homes?
- `data('Pastes')`: which paste is the best? Is this statistically significant?
- `data('DoctorAUS')`
    - is the number of people with chronic conditions or not distributed evenly
      among the different types of insurance? (chi2)
- `data('epi')` & `data('epi.dictionary')` for personality test / questions
- `data('Ketchup')`
- `data('Yogurt')` for reshaping
- `data('HI')` data on husband and wives health insurance

---

- Download the [city of san antonio 311 service call data set here](https://data.sanantonio.gov/dataset/service-calls)
- Use clustering to create clusters based on x coordinate and y coordinate
- Compare the clusters you created to the `Council District` feature on your
  data set

---

`data('cake')` -- breakage angle of chocolate cakes

[More docs here.](http://r.789695.n4.nabble.com/New-details-about-Cochran-and-Cox-s-chocolate-cake-data-td4694001.html)

- are `temperature` and `temp` the same?
- Create a line plot that shows the temperature vs the angle of breakage, with
  color indiciating different recipes
- Does the recipe or temperature effect the angle of breakage?

---

## pandas practice warmup

```
from pydataset import data
tips = data('tips')
```

- What is the difference between `tips['total_bill']` and `tips.total_bill`?
- What is the difference between `tips[['total_bill']]` and
  `tips['total_bill']`?
- What is the largest tip? The smallest? Was the person that gave the smallest
  tip a smoker? What was the party size of the group that gave the largest tip?
- What is the average total bill?
- What is the average total bill for parties of 4 or more?
- What is the average tip percentage? (hint: you'll need to make a new column
  for this)
- What is the average tip percentage for parties of 4 or more?
- What is the lowest bill for a party of 2?
- What is the highest bill for a party of 4 or more?
- Is the tip amount changed by party size? Is the tip percentage changed by
  party size?

---

Review Questions

- What is the difference between python and bash? What do they have in common?
- What is the difference between git and github?
- What is the difference between adding, committing, and pushing?
- What is the difference between dictionaries and lists?
- How is a dataframe different from a list of lists?
- How is a dataframe different from a 2-d numpy array?
- What is the difference between matplotlib and seaborn?
- What is the difference between pandas and numpy?
- How is a dataframe different from a series?

---

- [School Fight Songs](https://github.com/fivethirtyeight/data/tree/master/fight-songs)
- [data link](https://projects.fivethirtyeight.com/data-webpage-data/datasets/fight-songs.zip)

---

create a function that takes in a categorical column and gives back the top n
values and "Other" for the rest

---

Kaggle Datasets

- [New York AirBNB](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data)
    - id: listing ID
    - name: name of the listing
    - host_id: host ID
    - host_name: name of the host
    - neighbourhood_group: location
    - neighbourhood: area
    - latitude: latitude coordinates
    - longitude: longitude coordinates
    - room_type: listing space type
    - price: price in dollars
    - minimum_nights: amount of nights minimum
    - number_of_reviews: number of reviews
    - last_review: latest review
    - reviews_per_month: number of reviews per month
    - calculated_host_listings_count: amount of listing per host
    - availability_365: number of days when listing is available for booking
- [Ramen Reviews](https://www.kaggle.com/residentmario/ramen-ratings)
    - Review #
    - Brand
    - Variety
    - Style
    - Country
    - Stars
    - Top Ten
    - group by country, style, agg stars
    - how many top ten are null?
- [Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews)
- [Google Play Store Apps](https://www.kaggle.com/lava18/google-play-store-apps)
- [Kickstarter Projects](https://www.kaggle.com/kemical/kickstarter-projects)
- [Used Cars](https://www.kaggle.com/austinreese/craigslist-carstrucks-data)
    - Careful, this one's a little over 1GB
- [Boston Crimes](https://www.kaggle.com/AnalyzeBoston/crimes-in-boston)

## Git Warmup

Between each step below, run `git status` to check the state of the repository.

1. Create a directory named `git_warmup` within `~/codeup-data-science`.

1. Create a git repository in the directory you just made.

1. Use VS Code to create a file named `numbers.txt`. It should have the
   following contents:

   ```
   one
   two
   three
   four
   ```

1. Add and commit the `numbers.txt` file with a descriptive commit message.

1. What does `working tree clean` mean?

1. Add a new line to `numbers.txt` that contains `five`. What does `git status`
   tell you now?

1. Run `git diff` and inspect the output. What do you notice.

1. Run `git add numbers.txt`, then run `git diff` again. What do you notice?

    Recall that when we run `git add`, the added files are *staged*, and will be
    added to the next commit. Run `git diff` again, but add the `--cached` flag
    to the command.

1. Commit the changes you've made with a descriptive commit message.

1. Delete the first line of the file, and change the word `two` to the number 2.

1. Run `git diff` and inspect the output. What do you notice?

1. Add and commit your changes with a descriptive commit message.

1. Run `git log` and inspect the output. What do you see?

1. For every unique hash from the output of the command above, do the following:

    - Run `git show HASH`. What information does this give you?
    - Run `git diff HASH`. What information does this give you?

1. What is the difference between `git show` and `git diff`

---

## Regression Modeling Warmup

1. Using `pydataset`, load the `faithful` dataset and read it's documentation.
1. What is pearson's r for the two variables?
1. Visualize the relationship between the variables.
1. Build a linear model that predicts `eruptions` based on `waiting`.
1. Create a visualization with your predictions
    1. `waiting` should be on the x axis, and `eruptions` on the y
    1. Use color to differentiate the actual vs predicted values.
    1. Add a descriptive title.
    1. Change the y ticks such that they are all integers (i.e. no decimals)
    1. Add the root mean squared error of your predictions as an annotation.

```python
from pydataset import data
```

```python
data('faithful', show_doc=True)
```

```python
df = data('faithful')
df.head()
```

```python
from scipy import stats

'r = {:.2f}, p = {:.3}'.format(*stats.pearsonr(df.waiting, df.eruptions))
```

```python
import seaborn as sns

sns.relplot(data=df, x='waiting', y='eruptions')
```

```python
from sklearn.linear_model import LinearRegression
```

```python
lm = LinearRegression()
lm.fit(df[['waiting']], df.eruptions)

df['predicted'] = lm.predict(df[['waiting']])

df.head()
```

```python
%matplotlib inline
import matplotlib.pyplot as plt

plt.scatter(df.waiting, df.eruptions, label='Actual')
plt.scatter(df.waiting, df.predicted, label='Predicted')
plt.xlabel('Waiting')
plt.ylabel('Eruptions')
plt.legend()
```

```python
import pandas as pd

df.head()
```

```python
from math import sqrt
from sklearn.metrics import mean_squared_error

(pd.melt(df, id_vars='waiting')
 .pipe((sns.relplot, 'data'), x='waiting', y='value', hue='variable'))

# waiting should be on the x axis, and eruptions on the y
# Use color to differentiate the actual vs predicted values.
# Add a descriptive title.
# Change the y ticks such that they are all integers (i.e. no decimals)
# Add the root mean squared error of your predictions as an annotation.

rmse = mean_squared_error(df.eruptions, df.predicted)

plt.ylabel('# of Eruptions')
plt.title('Actual vs Predicted Number of Eruptions')
plt.yticks(range(1, 7))
plt.text(50, 5.5, 'RMSE: {:.2}'.format(rmse))
```

---

## Distributions Warmup

It's another day at the office at Big Research Co &trade;. You look up from your
laptop and see a woman in a lab coat standing in front of your desk.

"I need some help" she says. "We lost some subjects from the trial."

She notices a curious look on your face. "Not like that, they just ran away.
We didn't lock the doors soon enough."

"Anyway, there's probably like a 70%, no maybe 80%, no, let's say 90% chance
that a given subject will stick around, and I need to run the study again with
10, or 20 subjects. We need to gather enough data on them to justify the cost,
so I need you to figure out what are the probabilities are that at least half of
them stick around, only 1 person leaves, and that all the subjects stay."

She sees you start to form another question and cuts you off.

"Don't ask. You *really* don't want to know."

---

- What probability distribution would you use to model the scenario outlined
  above?
- Calculate all the requested probabilities. Use all the possible combinations
  of subject count and chance that a subject will stay in the study.
- **Bonus**: visualize the requested probabilities.

## Hints

- Use `scipy.stats` for this.
- A fancy list comprehension or the `itertools` module can help you find
  all the possible combinations.
- Each distribution has a cumulative density function that tells you the
  likelihood that a value falls at or below a given point.
- Consider storing the results of your calculations in a data frame.

```python
from scipy import stats
import pandas as pd

# pmf = probability of a single point
# cdf = cumulative probability

# stats.binom.pmf(n=10, p=.9, k=10)

# stats.binom.cdf(n=20, p=.8, k=20)
# stats.binom.pmf(n=20, p=.8, k=20)

stats.binom.cdf(n=10, p=.8, k=5) # probability that half *or fewer* subjects stick around
1 - stats.binom.cdf(n=10, p=.8, k=5) # probability that more than half stick around (survival function)
stats.binom.sf(n=10, p=.8, k=5) # survival function
```

```python
n_subjects = 10
p_subject_stays = .7
n_subjects_that_stay = range(11)

# probability that a given number of subjects stick around
pmfs = [stats.binom.pmf(n=n_subjects, p=p_subject_stays, k=k) for k in n_subjects_that_stay]

df = pd.DataFrame(dict(n_subjects_that_stay=n_subjects_that_stay, pmf=pmfs))

df['cdf'] = df.n_subjects_that_stay.apply(lambda k: stats.binom.cdf(p=p_subject_stays, n=n_subjects, k=k))

print(df)

plt.figure(figsize=(12, 10))
plt.plot(df.n_subjects_that_stay, df.pmf, label='pmf(k)')
plt.plot(df.n_subjects_that_stay, df.cdf, label='cdf(k)')
plt.ylabel('P(that many subjects stay)')
plt.xlabel('# of Subjects That Stay')
plt.legend()
```

```python
import itertools as it
from scipy import stats
import pandas as pd
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns

ps = [.7, .8, .9]
ns = [10, 20]
ks = range(20)

cdfs = [(p, n, k, stats.binom.cdf(n=n, p=p, k=k)) for p, n, k in it.product(ps, ns, ks)]
df = pd.DataFrame(cdfs, columns=['p', 'n', 'k', 'cdf(k)'])
df.loc[(df.n == 10) & (df.k > 10), 'cdf(k)'] = np.nan
df.dropna(inplace=True)

sns.relplot(data=df, x='k', y='cdf(k)', hue='p', col='n', kind='line')
```

---

impute with:

- group mean: `groupby().transform`
- linear regression model prediction

## Time Series

```
from vega_datasets import data
data.iowa_electricity()
```

- lineplot of generation over time, hue=source
- display data as table where years are columns, source is rows
- is total generation increasing over time?
    - make a visual that controls for this
    - control for increasing consumption over time
    - express each # as a % of the year's total

---

```
from vega_datasets import data
data.sf_weather() # 1 year, hourly
data.seattle_temps() # 1 year, hourly
data.seattle_weather() # 3 years, min, max, wind, precip, weather
```

- create 4 categories for temperature, cold, cool, warm, hot
- how does the occurances of these 4 categories change month over month? i.e.
  how many days have each distinction? Visualize this and give the visual
  appropriate colors for each category.
- create pretty labels for time plots
- visualize the number of days of each month that fall into each bin by year
    (i.e. x=month, y=n_days, hue=temp_bin) or st similar

---

[Time series aggregating warmup](https://gist.github.com/zgulde/96991fedca29ff5371f5e7fa00d3fa95)

---

```
from vega_datasets import data
data.seattle_weather()
```

- what's the sunniest year?
- In which month does it rain the most?
- Which month has the most number of days with a non-zero amount of
  precipitation?

---

## TS AD Warmup

```python
import pandas as pd
import numpy as np
np.random.seed(13)

## Create the anomoluous data

idx = pd.date_range('20191124', freq='30min', periods=96)
group = np.random.choice(['a', 'b'], 96)

df = pd.DataFrame(dict(group=group, x=0), index=idx)

df.loc[df.group == 'a', 'x'] = np.random.normal(200, 13, ((df.group == 'a').sum(), ))
df.loc[df.group == 'b', 'x'] = np.random.normal(25, 5, ((df.group == 'b').sum(), ))

df.loc['2019-11-25 14:00:00', 'x'] = 220 + np.random.random()
df.loc['2019-11-25 14:00:00', 'group'] = 'b'

df.to_csv('ts_ad_warmup.csv', index=True)

## Detecting the Anomaly

### Visually

import matplotlib.pyplot as plt
plt.ion()
import seaborn as sns

sns.scatterplot(x=range(len(df)), y=df.x, hue=df.group)

sns.lineplot(x=df.index, y=df.x, hue=df.group)

sns.boxplot(data=df, y='x', x='group')

### With a Z-score

df['z_x_by_group'] = df.groupby('group').x.transform(lambda x: (x - x.mean()) / x.std())
df[df['z_x_by_group'].abs() > 3]

### With IQR

def find_outliers(x: pd.Series, k=1.5) -> pd.Series:
    '''
    Detect outliers in the series.

    Returns
    -------

    A pandas Series of boolean values indicating whether each point is an
    outlier or not.

    Parameters
    ----------

    k : value to multiply the iqr by for outlier detection. Default 1.5

    Example
    -------

    >>> df = pd.DataFrame(dict(x=[1, 2, 3, 4, 5, 6, 100],
    ...                        y=[-100, 5, 3, 4, 1, 2, 0]))
    >>> df
         x    y
    0    1 -100
    1    2    5
    2    3    3
    3    4    4
    4    5    1
    5    6    2
    6  100    0
    >>> find_outliers(df.x)
    0    False
    1    False
    2    False
    3    False
    4    False
    5    False
    6     True
    Name: x, dtype: bool
    >>> df[find_outliers(df.x)]
         x  y
    6  100  0
    '''
    q1 = x.quantile(0.25)
    q3 = x.quantile(0.75)
    iqr = q3 - q1
    return (x < q1 - k * iqr) | (x > q3 + k * iqr)

df[df.groupby(df.group).x.transform(find_outliers)]

# Note that we could also split into two sepearate dataframes by group and go
# from there.
```

## Other

Amazon Web Services [Snowmobile](https://aws.amazon.com/snowmobile/).

- Create an analogy for an exabyte -- e.g. football fields of macbooks
- If you hire 3 of these 100PB trucks and they drive 200 miles, what kind of
  bandwith are you getting?

---

```python
from vega_datasets import data

df = data.gapminder()
```

- Which country has the biggest change in life expectancy?

---

https://www.gwern.net/Google-shutdowns#analysis


---

```python
from vega_datasets import data

stocks = data.stocks()
stocks.pivot_table('price', 'date', 'symbol')
```

---

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from pydataset import data
```

1. Use the code below to load a dataset on voting behavior:

    ```python
    df = data('voteincome')
    df
    ```

1. Drop the `year` and `state` columns.

1. Run the code below:

    ```python
    df.groupby('vote').mean()
    ```

    - What did the above code do?
    - What does the output tell us?
    - Based on what you observe, which variables do you think will be the most
      useful in predicting whether or not someone votes?

1. Split the data into X and y, y being whether or not someone voted, and X
   being everything else (i.e. everything except for the columns we dropped
   previously).

1. Create a logistic regression model that predicts whether or not someone will
   vote. What is it's accuracy?

1. Create a decision tree model that predicts whether or not someone will vote.
   Use a max depth of 4 for the decision tree. What is the decision tree's
   accuracy?

1. Evaluate which factors are the most impactful in making each model's
   decision.

    - The logistic regression model has a property named `coef_` that contains
      the coefficients of the logistic regression model. The order of the values
      corresponds to the order of the columns in the X dataframe. A higher
      absolute value for a coeficcient indicates that feature carries more
      weight in making the model's prediction.

    - The decision tree model has a property named `feature_importances_` that
      indicates how important each feature is to the model's prediction. A
      higher number indicates a more impactful feature.

1. Do the decision tree and logistic regression model agree on which features
   are the most important in determining voting behavior? Does this agree with
   what you predicted earlier?

---

```python
# - region: U. S. Census regions. A factor with levels: `ENC`, East North
#   Central `ESC`, East South Central; `MA`, Mid-Atlantic; `MTN`, Mountain; `NE`,
#   New England; `PAC`, Pacific; `SA`, South Atlantic; `WNC`, West North Central;
#   `WSC`, West South Central.
# - pop: Population: in 1,000s.
# - SATV: Average score of graduating high-school students in the state on the
#   _verbal_ component of the Scholastic Aptitude Test (a standard university
#   admission exam).
# - SATM: Average score of graduating high-school students in the state on the
#   _math_ component of the Scholastic Aptitude Test.
# - percent: Percentage of graduating high-school students in the state who took
#   the SAT exam.
# - dollars: State spending on public education, in \$1000s per student.
# - pay: Average teacher's salary in the state, in $1000s.
df = data('States')
df['SAT'] = df.SATV + df.SATM

X, y = df.rformula('SAT ~ percent + dollars + pay + pop')
lr = LinearRegression().fit(X, y)
tree = DecisionTreeRegressor(max_depth=4).fit(X, y)

residuals = pd.DataFrame(dict(
    y=y,
    lr=y - lr.predict(X),
    tree=y - tree.predict(X),
))
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.scatter(residuals.y, residuals.lr, c='blue')
ax1.set(title='LinearRegression')
ax2.scatter(residuals.y, residuals.tree, c='orange')
ax2.set(title='DecisionTree')

pd.concat([
    pd.Series(dict(zip(X.columns, lr.coef_))),
    pd.Series(dict(zip(X.columns, tree.feature_importances_)))
], axis=1)

df = data('poisons')
df.pivot_table('time', 'poison', 'treat')

# * state state ID code
# * year year
# * mrall traffic fatality rate (deaths per 10000)
# * beertax tax on case of beer
# * mlda minimum legal drinking age
# * jaild mandatory jail sentence ?
# * comserd mandatory community service ?
# * vmiles average miles per driver
# * unrate unemployment rate
# * perinc per capita personal income
df = data('Fatality')
df.drop(df.query('vmiles > 18').index, inplace=True)
df.jaild = np.where(df.jaild == 'no', 0, 1)
df.comserd = np.where(df.comserd == 'no', 0, 1)
```

---

1. fit a decision tree regressor w/ max depth of None, why are all residuals 0?



## PySpark Warmups

# Spark API Mini Exercises

Copy the code below to create a pandas dataframe with 20 rows and 3 columns:

```python
import pandas as pd
import numpy as np

np.random.seed(13)

pandas_dataframe = pd.DataFrame(
    {
        "n": np.random.randn(20),
        "group": np.random.choice(list("xyz"), 20),
        "abool": np.random.choice([True, False], 20),
    }
)
```

1. Spark Dataframe Basics

    1. Use the starter code above to create a pandas dataframe.
    1. Convert the pandas dataframe to a spark dataframe. From this point
       forward, do all of your work with the spark dataframe, not the pandas
       dataframe.
    1. Show the first 3 rows of the dataframe.
    1. Show the first 7 rows of the dataframe.
    1. View a summary of the data using `.describe`.
    1. Use `.select` to create a new dataframe with just the `n` and `abool`
       columns. View the first 5 rows of this dataframe.
    1. Use `.select` to create a new dataframe with just the `group` and `abool`
       columns. View the first 5 rows of this dataframe.
    1. Use `.select` to create a new dataframe with the `group` column and the
       `abool` column renamed to `a_boolean_value`. Show the first 3 rows of
       this dataframe.
    1. Use `.select` to create a new dataframe with the `group` column and the
       `n` column renamed to `a_numeric_value`. Show the first 6 rows of this
       dataframe.

1. Column Manipulation

    1. Use the starter code above to re-create a spark dataframe. Store the
       spark dataframe in a varaible named `df`

    1. Use `.select` to add 4 to the `n` column. Show the results.

    1. Subtract 5 from the `n` column and view the results.

    1. Multiply the `n` column by 2. View the results along with the original
       numbers.

    1. Add a new column named `n2` that is the `n` value multiplied by -1. Show
       the first 4 rows of your dataframe. You should see the original `n` value
       as well as `n2`.

    1. Add a new column named `n3` that is the n value squared. Show the first 5
       rows of your dataframe. You should see both `n`, `n2`, and `n3`.

    1. What happens when you run the code below?

        ```python
        df.group + df.abool
        ```

    1. What happens when you run the code below? What is the difference between
       this and the previous code sample?

        ```python
        df.select(df.group + df.abool)
        ```

    1. Try adding various other columns together. What are the results of
       combining the different data types?

1. Spark SQL

    1. Use the starter code above to re-create a spark dataframe.
    1. Turn your dataframe into a table that can be queried with spark SQL. Name
       the table `my_df`. Answer the rest of the questions in this section with
       a spark sql query (`spark.sql`) against `my_df`. After each step, view
       the first 7 records from the dataframe.
    1. Write a query that shows all of the columns from your dataframe.
    1. Write a query that shows just the `n` and `abool` columns from the
       dataframe.
    1. Write a query that shows just the `n` and `group` columns. Rename the
       `group` column to `g`.
    1. Write a query that selects `n`, and creates two new columns: `n2`, the
       original `n` values halved, and `n3`: the original n values minus 1.
    1. What happens if you make a SQL syntax error in your query?

1. Type casting

    1. Use the starter code above to re-create a spark dataframe.

    1. Use `.printSchema` to view the datatypes in your dataframe.

    1. Use `.dtypes` to view the datatypes in your dataframe.

    1. What is the difference between the two code samples below?

        ```python
        df.abool.cast('int')
        ```

        ```python
        df.select(df.abool.cast('int')).show()
        ```

    1. Use `.select` and `.cast` to convert the `abool` column to an integer
       type. View the results.
    1. Convert the `group` column to a integer data type and view the results.
       What happens?
    1. Convert the `n` column to a integer data type and view the results. What
       happens?
    1. Convert the `abool` column to a string data type and view the results.
       What happens?

1. Built-in Functions

    1. Use the starter code above to re-create a spark dataframe.
    1. Import the necessary functions from `pyspark.sql.functions`
    1. Find the highest `n` value.
    1. Find the lowest `n` value.
    1. Find the average `n` value.
    1. Use `concat` to change the `group` column to say, e.g. "Group: x" or
       "Group: y"
    1. Use `concat` to combine the `n` and `group` columns to produce results
       that look like this: "x: -1.432" or "z: 2.352"

1. Filter / Where

    1. Use the starter code above to re-create a spark dataframe.
    1. Use `.filter` or `.where` to select just the rows where the group is `y`
       and view the results.
    1. Select just the columns where the `abool` column is false and view the
       results.
    1. Find the columns where the `group` column is *not* `y`.
    1. Find the columns where `n` is positive.
    1. Find the columns where `abool` is true and the `group` column is `z`.
    1. Find the columns where `abool` is true or the `group` column is `z`.
    1. Find the columns where `abool` is false and `n` is less than 1
    1. Find the columns where `abool` is false or `n` is less than 1

1. When / Otherwise

    1. Use the starter code above to re-create a spark dataframe.
    1. Use `when` and `.otherwise` to create a column that contains the text "It
       is true" when `abool` is true and "It is false"" when `abool` is false.
    1. Create a column that contains 0 if n is less than 0, otherwise, the
       original n value.

1. Sorting

    1. Use the starter code above to re-create a spark dataframe.
    1. Sort by the `n` value.
    1. Sort by the `group` value, both ascending and descending.
    1. Sort by the group value first, then, within each group, sort by `n`
       value.
    1. Sort by `abool`, `group`, and `n`. Does it matter in what order you
       specify the columns when sorting?

1. Aggregating

    1. What is the average `n` value for each group in the `group` column?
    1. What is the maximum `n` value for each group in the `group` column?
    1. What is the minimum `n` value by `abool`?
    1. What is the average `n` value for each unique combination of the `group`
       and `abool` column?

