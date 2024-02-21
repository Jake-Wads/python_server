# Performing a chi^2 independence test with python
# -----------------------------------------------

from seaborn import load_dataset
from scipy.stats import chi2_contingency

# 0. Get some data
tips = load_dataset('tips')

# 1. make a crosstab
pd.crosstab(tips.sex, tips.smoker)

# 2. Feed the crosstab into the chi2_contingency function
chi2_contingency(pd.crosstab(tips.sex, tips.smoker))

# 3. Get the results back
statistic, p_val, df, expected = chi2_contingency(pd.crosstab(tips.sex, tips.smoker))