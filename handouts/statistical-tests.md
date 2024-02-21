# Statistical Tests

I want to compare two variables:

| Var 1       | Var 2       | You Should Use |
| -----       | -----       | -------------- |
| Continuous  | Continuous  | Pearson R      |
| Continuous  | Categorical | T Test         |
| Categorical | Categorical | $\chi^2$       |

- p value: how likely is it that we have the results that we have due to chance;
  Usually we want this to be very small, (typically < 0.05)
- if p is small, we reject the null hypothesis
- if p is large, we fail to reject the null hypothesis

## Pearson R

- compares two continuous variables
- our test statistic ($r$) gives us the strength and direction of the
  *linear* correlation between the two vars
- $H_0$: there is no linear correlation between the two vars

## T-Test

- compares means for some continuous variable for 2 groups (or 1 group vs a
  population mean)
- assumes the continuous var is normally distributed, equal variance in both
  groups
- $H_0$: the means are the same for each group

## Chi Square Test

- used to compare two categorical variables
- compares observed vs expected proportions
- $H_0$: the two vars are independent
