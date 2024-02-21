
#tabular data manipulation
import numpy as np
import pandas as pd

#datetime utilities
from datetime import timedelta, datetime

import os
import acquire
import wrangle

################################### Prep Store Function #################################

def prep_store_data():
    '''
    This function takes in a df and changes date dtypes, resets date as index,
    creates new columns for month, weekday, and total sales
    and returns that as a new pandas dataframe
    '''
    
    #assign variable df from the acquire function
    df= acquire.get_store_data()
    
    #change data type on sale_date
    df.sale_date = df.sale_date.astype('datetime64[ns]')
    #set the index to sale_date
    df = df.set_index('sale_date').sort_index()
    
    #create new colum for month
    df['month'] = df.index.month_name()
    #create new colum for weekday
    df['day_of_week'] = df.index.day_name()
    #create new colum for sale total
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df

########################## Prep Germany Function ##########################

def prep_germany_data():
    '''
    This function takes in a df and changes date dtypes, resets date as index,
    creates new columns for month, weekday, and total sales
    and returns that as a new pandas dataframe
    '''
    
    #assign variable df from the acquire function
    df= acquire.get_germany_data()
    
    #change data type on Date
    df.Date = df.Date.astype('datetime64[ns]')
    #set the index to Date
    df = df.set_index('Date').sort_index()
    #rename columns
    df = df.rename(columns={'Consumption':'consumption', 'Wind':'wind', 'Solar':'solar','Wind+Solar':'wind_solar'})
    
    #create new colum for month
    df['month'] = df.index.month_name()
    #create new colum for weekday
    df['day_of_week'] = df.index.day_name()
    #create new column for year
    df['year'] = df.index.year
    #fill nulls with 0
    df = df.fillna(0)
    
    return df

########################## Prep Saas Data Function ##########################

def prep_saas_data():
    '''
    This function takes in a df and changes date dtypes, resets date as index,
    creates new columns for month, weekday, and total sales
    and returns that as a new pandas dataframe
    '''
    
    #assign variable df from the acquire function
    df= pd.read_csv('saas.csv')
    
    #rename columns by lowercasing them all
    df.columns = [col.lower() for col in df]
               
    #change data type on Date
    df.month_invoiced = df.month_invoiced.astype('datetime64[ns]')
    #set the index to Date
    df = df.set_index('month_invoiced').sort_index()
    #change amount from float to int
    df.amount = df.amount.astype(int)
    #change sub type from float to int
    df.subscription_type = df.subscription_type.astype(int)
    
    #create new colum for month
    df['month'] = df.index.month_name()
    #create new colum for weekday
    df['day_of_week'] = df.index.day_name()
    #create new column for year
    df['year'] = df.index.year
    
    return df

  
########################### Convert to Datetime Function #######################

def convert_to_datetime(df):
    '''
    This function takes in a dataframe
    and converts the sales_date column to a datetime
    '''
    df.sale_date = pd.to_datetime(df.sale_date, infer_datetime_format=True)
    return df

########################### Plot Distributions Function #########################

def plot_distributions(df):
    for col in list(df.columns.drop('Date')):
        plt.figure()
        sns.histplot(df[col])
        plt.title('Distribution of {}'.format(col))
