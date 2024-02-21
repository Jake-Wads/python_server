# Useful Libraries


## Exploratory Data Analysis
For when you want an overview of a pandas DataFrame with significantly more depth than `.describe()`, try out [https://github.com/pandas-profiling/pandas-profiling](https://github.com/pandas-profiling/pandas-profiling). Install with `conda install -c conda-forge pandas-profiling` or `pip install pandas-profiling`.

Some features of Pandas Profiling include:
- Essentials like types, unique values, missing values
- Quantile statistics
- Descriptive statistics
- Most frequent values
- Histogram
- Correlations highlighting of highly correlated variables
- Missing values matrix

## Model Interpretation
For a useful library to help with explaining and interpreting models, try out **EL5**, short for "Explain it To Me Like I'm 5". Documentation is at [https://eli5.readthedocs.io/en/latest](https://eli5.readthedocs.io/en/latest/) and the source code is available from [https://github.com/TeamHG-Memex/eli5](https://github.com/TeamHG-Memex/eli5). To install, do `conda install -c conda-forge eli5` or `pip install eli5`.

## Plotting SciKit Learn Objects
- Add plotting functionality to scikit-learn objects with https://github.com/reiinakano/scikit-plot