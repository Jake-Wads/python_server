# Scaling

[Visual Demos](https://stats-demos.zach.wiki/)

1. Train Test Split

    Scaling params found from train, applied to test.

2. Scaling - when, where, what, why, and how

    - why
        - visualize the combination of 2 variables with different scales
        - stats tests that assume normality
        - improves most model's implementation
        - a better interpretation of the data (e.g. log scaling)
        - combining features
    - when
        - data prep / exploration
        - when one of the conditions above is met. Otherwise, it's better to work with the original units
    - where
        - the training dataset
        - usually just the independent variables
    - how:
        - sklearn.preprocessing -- requires 2d array
        - make the thing, fit the thing, use the thing
        - `.fit` to learn parameters, `.transform` to apply the scaling
        - seperate scaled dataframes and/or columns

3. Linear Scaling

    - MinMax: everything between 0 and 1
        $$ x' = \frac{x - \text{max}(x)}{\text{max}(x) - \text{min}(x)} $$
    - Standard: a zscore, standard deviations from the mean, **center** + **scale**
        $$ x' = \frac{x - \bar{x}}{s_x} $$
    - Robust: robust to and preserves outliers
        $$ x' = \frac{x - \text{med}(x)}{\text{IQR}_x} $$

4. Non-linear Scaling

    - Power Transform: choose $\lambda$ (-5 to 5) s.t. the standard deviation of the resulting distribution is the smallest

        Yeo-Johnson

        $$
        \begin{split}x_i^{(\lambda)} =
        \begin{cases}
         [(x_i + 1)^\lambda - 1] / \lambda & \text{if } \lambda \neq 0, x_i \geq 0, \\[8pt]
        \ln{(x_i) + 1} & \text{if } \lambda = 0, x_i \geq 0 \\[8pt]
        -[(-x_i + 1)^{2 - \lambda} - 1] / (2 - \lambda) & \text{if } \lambda \neq 2, x_i < 0, \\[8pt]
         - \ln (- x_i + 1) & \text{if } \lambda = 2, x_i < 0
        \end{cases}\end{split}
        $$

        Box-Cox (only positive data)

        $$
        \begin{split}x_i^{(\lambda)} =
        \begin{cases}
        \dfrac{x_i^\lambda - 1}{\lambda} & \text{if } \lambda \neq 0, \\[8pt]
        \ln{(x_i)} & \text{if } \lambda = 0,
        \end{cases}\end{split}
        $$

    - Quantile: data points are "ranked", for a normal output, highest_orig -> highest_norm and then 2nd highest, etc

    - Log

        $$ x' = \log_b{x} $$

        $$ b^{x'} = x $$

        Sometimes you can just set the x/y scale w/ matplotlib instead of
        actually transforming the data
