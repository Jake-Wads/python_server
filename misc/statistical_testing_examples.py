# # chi2

import pandas as pd
from scipy import stats
import seaborn as sns

tips = sns.load_dataset('tips')

# H0: sex is indep of whether or not someone is a smoker

contingency_table = pd.crosstab(tips.sex, tips.smoker)

chi2_statistic, p, df, expected_values = stats.chi2_contingency(contingency_table)

# Now we can look at p to decide whether to reject / fail to reject H0.

# # Pearson R

from scipy import stats
import seaborn as sns
import pandas as pd

tips = sns.load_dataset('tips')

# H0: there is not linear correlation
#
# How strong is the linear correlation between tip amount and total bill?
r, p = stats.pearsonr(tips.total_bill, tips.tip)

# # T Test

from scipy import stats
import seaborn as sns
import pandas as pd

tips = sns.load_dataset('tips')

# There are two kinds of t-tests:
#
# - `stats.ttest_1samp`: comparse the mean for a specific subgroup to the
#   population mean
# - `stats.ttest_ind`: compares means for 2 subgroups
#
# In both cases, H0: the means are the same
#
# Is the total bill amount different for smokers?
smokers_total_bills = tips[tips.smoker == 'Yes'].total_bill
overall_total_bill_mean = tips.total_bill.mean()
t_stat, p = stats.ttest_1samp(smokers_total_bills, overall_total_bill_mean)

# Is the total bill amount different for parties of 2 vs 4?
parties_of_2 = tips[tips['size'] == 2]
parties_of_4 = tips[tips['size'] == 4]
t_stat, p = stats.ttest_ind(parties_of_2.total_bill, parties_of_4.total_bill)
