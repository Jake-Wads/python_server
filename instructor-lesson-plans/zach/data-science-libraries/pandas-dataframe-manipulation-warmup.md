---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.4
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Dataframe Manipulation Warmup

```python
import numpy as np
import pandas as pd

np.random.seed(406)

n = 5000
df = pd.DataFrame({
    'favorite_animal': np.random.choice(['cat', 'dog', 'frog', 'lemur', 'panda'], n),
    'favorite_vegetable': np.random.choice(['brussel sprouts', 'potato', 'squash'], n),
    'favorite_fruit': np.random.choice(['banana', 'apple', 'blueberries'], n),
    'wears_glasses': np.random.choice(['yes', 'no'], n),
    'netflix_consumption': np.random.normal(10, 2, n),
    'open_browser_tabs': np.random.randint(2, 90, n),
})
```

- What is the highest amount of netflix consumption? `17.535`
- How many people wear glasses? What percentage of people is this? `2555`, `.511`
- How many people's favorite animal is a dog? `1002`
- What is the most common favorite animal? `lemur`
- What is the average netflix consumption for people that prefer brussel
  sprouts? `10.008`
- What is the most common favorite fruit for people who wear glasses and have
  more than 40 open browser tabs? `blueberries`
- What percentage of people have a netflix consumption lower than 7? `.0716`
- What is the average netflix consumption for people with less than 30 open
  browser tabs? `9.91935`
- How many people *don't* wear glasses, have a favorite animal of a panda, have
  a favorite fruit of blueberries, and have more than 60 open browser tabs? What
  is the median netflix consumption for this group? What is the most common
  favorite vegetable for this group? `46`, `10.455`, `potato`
- What is the least popular combination of favorite fruit and vegetable? `apple` and `potato`
- Which combination of favorite animal and wearing glasses has the highest average
  netflix consumption? people that wear glasses and prefer pandas
- **Bonus**: for each of the above questions, what kind of visualization would
  be the most effective in conveying your answer?
