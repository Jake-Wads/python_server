## Exploration

Explore the target against the independent features.

- survived vs age, fare
    - survived as categorical
    - box, violin, and swarmplots, two distplots on top of eachother
    - fancy: subplot histogram, shared x
- survived as categorical, sex, pclass, embark town
    - crosstab
    - sns.heatmap
    - (maybe) `group_proportions`
    - (maybe) `crosstab_heatmap`
    - (maybe) `category_scatter`

`survived` can be treated as either a categorical variable, or a number. For example, we could do survived.mean to find the survival rate (overall or for a subgroup) or sum to get the number that survived.

- survived as a number vs sex, pclass, embark town
    - groupby + .sum + .mean
    - .plot.bar
    - sns.barplot
    - add hline for survival rate `ax.hlines(df.survived.mean(), *ax.get_xlim())`
- bin age and use it as a category
- combinations of 3: sex, pclass, embark_town, values=survived
    - crosstab w/ values= (different than normalize=True!)
    - pivot_table
    - sns.heatmap
    - (maybe) `crosstab_scatter`

```python
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic = titanic.drop(columns=['adult_male', 'alive', 'alone', 'who'])
titanic.head()
```
