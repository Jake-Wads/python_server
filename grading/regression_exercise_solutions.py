## in progress!!!

## 3.0-Evaluation

# 1. 
import seaborn as sns
sns.get_dataset_names()
df = sns.load_dataset('tips')[['total_bill','tip']]
# 2.
from statsmodels.formula.api import ols
ols_model = ols('tip ~ total_bill', data=df).fit()
df['yhat'] = ols_model.predict(df.total_bill)
# 3. 
df['residual'] = df['yhat'] - df['tip']
# 4. 
import matplotlib.pyplot as plt
%matplotlib inline 
import seaborn as sns

def residual_plot(x, y): 
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y)
    
    # add the residual line at y=0
    plt.annotate('', xy=(1, 0), xytext=(50, 0), xycoords='data', textcoords='data', arrowprops={'arrowstyle': '-'})

    # set titles
    plt.title(r'Residuals', fontsize=12, color='black')
    # add axes labels
    plt.ylabel(r'residual: $\hat{y}-y$')
    plt.xlabel('total bill')
    
    return plt.show()

residual_plot(df.total_bill, df.residual)
# 5. 
sum(df.residual**2)
# 6. 
from math import sqrt
def regression_errors(y, yhat):
    sse = sum((df.yhat-df.tip)**2)
    mse = sse/len(y)
    rmse = sqrt(mse)
    return sse, mse, rmse

# 7. 
r2 = ols_model.rsquared
print('R-squared/Variance Explained = {}%'.format(round(r2,3)*100))
# 8.


# 3.1-acquire-and-prep: wrangle.py

# As a customer analyst, I want to know who has spent the most money with us over their lifetime. I have monthly charges and tenure, so I think I will be able to use those two attributes as features to estimate total_charges. I need to do this within an average of $5.00 per customer. 

1. Acquire customer_id, monthly_charges, tenure, and total_charges from `telco_churn` database for all customers with a 2 year contract.
2. Walk through the steps above using your new dataframe. You may handle the missing values however you feel is appropriate. 
3. End with a python file wrangle.py that contains the function, `wrangle_telco()`, that will acquire the data and return a dataframe cleaned with no missing values.


# 3.2-split-and-scale
# Be sure to set a random state where applicable for reproducibility!
# 1. split_my_data(X, y, train_pct) 

def split_my_data(data, train_ratio=.80, seed=123):
    '''the function will take a dataframe and returns train and test dataframe split 
    where 80% is in train, and 20% in test. '''
    return train_test_split(data, train_size = train_ratio, random_state = seed)

# 1. standard_scaler(train, test)

def standard_scaler(train, test):
    scaler = StandardScaler(copy=True, with_mean=True, with_std=True).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train_scaled, test_scaled

# 1. scale_inverse(scaler, train_scaled, test_scaled)
def my_inv_transform(scaler, train_scaled, test_scaled):
    train = pd.DataFrame(scaler.inverse_transform(train_scaled), columns=train_scaled.columns.values).set_index([train_scaled.index.values])
    test = pd.DataFrame(scaler.inverse_transform(test_scaled), columns=test_scaled.columns.values).set_index([test_scaled.index.values])
    return scaler, train, test

# 1. uniform_scaler(train, test, seed)
def uniform_scaler(train, test, seed=123):
    scaler = QuantileTransformer(n_quantiles=100, output_distribution='uniform', random_state=seed, copy=True).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train_scaled, test_scaled

# 1. gaussian_scaler(train, test, method)

def gaussian_scaler(train, test, method='yeo-johnson'):
    scaler = PowerTransformer(method, standardize=False, copy=True).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train_scaled, test_scaled

# 1. min_max_scaler(train, test, minmax_range=0,1)

def my_minmax_scaler(train, test, minmax_range=(0,1)):
    scaler = MinMaxScaler(copy=True, feature_range=minmax_range).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train_scaled, test_scaled

scaler, train_scaled, test_scaled = my_minmax_scaler(train, test)

# 1. iqr_robust_scaler(train, test)

def iqr_robust_scaler(train, test):
    scaler = RobustScaler(quantile_range=(25.0,75.0), copy=True, with_centering=True, with_scaling=True).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return scaler, train_scaled, test_scaled

scaler, train_scaled, test_scaled = iqr_robust_scaler(train, test)

# 3.3-explore

# Create a file, explore.py, that contains the following functions for exploring your variables (features & target).
# 1. Write a function, `plot_variable_pairs(dataframe)` that plots all of the pairwise relationships along with the regression line for each pair. 

# 2. Write a function, `months_to_years(tenure_months, df)` that returns your dataframe with a new feature `tenure_years`, in complete years as a customer. 

# 3. Write a function, `plot_categorical_and_continous_vars(categorical_var, continuous_var, df)`, that outputs 3 different plots for plotting a categorical variable with a continuous variable, e.g. tenure_years with total_charges. For ideas on effective ways to visualize categorical with continuous: https://datavizcatalogue.com/. You can then look into seaborn and matplotlib documentation for ways to create plots. 



# 3.4 feature_selection

# 1. Write a function, `select_kbest_chisquared()` that takes X_train, y_train and k as input (X_train and y_train should not be scaled!) and returns a list of the top k features. 
# 2. Write a function, `select_kbest_freg()` that takes X_train, y_train (scaled) and k as input and returns a list of the top k features. 
# 3. Write a function, `ols_backware_elimination()` that takes X_train and y_train (scaled) as input and returns selected features based on the ols backwards elimination method. 
# 4. Write a function, `lasso_cv_coef()` that takes X_train and y_train as input and returns the coefficients for each feature, along with a plot of the features and their weights. 
# 5. Write 3 functions, the first computes the number of optimum features (n) using rfe, the second takes n as input and returns the top n features, and the third takes the list of the top n features as input and returns a new X_train and X_test dataframe with those top features , `recursive_feature_elimination()` that computes the optimum number of features (n) and returns the top n features. 

def optimal_number_of_features(X_train, y_train, X_test, y_test):
    '''discover the optimal number of features, n, using our scaled x and y dataframes, recursive feature
    elimination and linear regression (to test the performance with each number of features).
    We will use the output of this function (the number of features) as input to the next function
    optimal_features, which will then run recursive feature elimination to find the n best features'''

    number_of_attributes = X_train.shape[1]
    number_of_features_list=np.arange(1,number_of_attributes)
    high_score=0
    
    #Variable to store the optimum features
    number_of_features=0           
    score_list =[]
    
    for n in range(len(number_of_features_list)):
        model = LinearRegression()
        rfe = RFE(model,number_of_features_list[n])
        X_train_rfe = rfe.fit_transform(X_train,y_train)
        X_test_rfe = rfe.transform(X_test)
        model.fit(X_train_rfe,y_train)
        score = model.score(X_test_rfe,y_test)
        score_list.append(score)
        if(score>high_score):
            high_score = score
            number_of_features = number_of_features_list[n]
    return number_of_features


def optimal_features(X_train, y_train, number_of_features):
    '''Taking the output of optimal_number_of_features, as n, and use that value to 
    run recursive feature elimination to find the n best features'''
    cols = list(X_train.columns)
    model = LinearRegression()
    
    #Initializing RFE model
    rfe = RFE(model, number_of_features)

    #Transforming data using RFE
    X_rfe = rfe.fit_transform(X_train,y_train)  

    #Fitting the data to model
    model.fit(X_rfe,y_train)
    temp = pd.Series(rfe.support_,index = cols)
    selected_features_rfe = temp[temp==True].index
    
    return selected_features_rfe


# get optimal number of features
number_of_features = optimal_number_of_features(X_train, y_train, X_test, y_test)

# get feature names
my_features = optimal_features(X_train, y_train, number_of_features)

# create dataframes with only these features
X_train[my_features].head()
# X_test[my_features]



from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(tips['total_bill'],tips['tip'])

# use line_kws to set line label for legend
ax = sns.regplot(x="total_bill", y="tip", data=tips, color='b', 
 line_kws={'label':"y={0:.1f}x+{1:.1f}".format(slope,intercept)})