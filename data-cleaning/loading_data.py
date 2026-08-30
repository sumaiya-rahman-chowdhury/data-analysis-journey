import pandas as pd

df = pd.read_csv("data.csv")
# this how load dataset ,df stands for dataset
df.head() 
# preview data ,
df.head(10)
#choose how many data to see
df.info()
# to see missing value 

# now lets check missing value 
df.isnull().sum()
""" example :
Name      0
Age       1 one value miss here
City      0
Salary    1 one value miss here """
# df.isnull() then .sum => counts the true value 
# count them column by column 
# *****************
df.duplicated().sum()
# checks duplicate
df.describe()
#help us find unusal value