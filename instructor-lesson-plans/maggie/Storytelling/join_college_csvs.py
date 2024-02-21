df1 = pd.read_csv("cc_institution_details.csv", encoding = "iso-8859-1")
# df1.columns
# df1.head()
# df1.shape

df2 = pd.read_csv("scorecard.csv", encoding = "iso-8859-1") 
# df2.columns
# df2.head()
# df2.shape

# compute the percent missing for each column
# identify those where percent missing is < 25%
# reset index to set column names as 1st column
cols = pd.DataFrame(df2.isnull().sum()/df2.shape[0] < .25).reset_index()

# keep only columns where second column (whose name is '0' (but stored as an integer!)) is true

cols_to_keep = cols[cols[0]]

# select columns from df2 whose name matches those in the cols_to_keep list
df2 = df2[cols_to_keep['index']]

# drop the column no longer needed
df2.drop(columns = ['Unnamed: 0'], inplace = True)

# merge df1 and df2 
df = pd.merge(df1, df2, how = "left", left_on = "unitid", right_on = "UNITID")

# write final dataframe to csv
df.to_csv("colleges.csv")




