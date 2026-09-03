"""
Salary
20,000
22,000
24,000
25,000
23,000
500,000  ← Outlier
outlier is unusal value , far from other value

#basic formula is
IQR = Q3 - Q1
Q1 = 25
Q3 = 75

=> THEN
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR

"""

import pandas as pd

df = pd.read_csv("data_set_name.csv")
df["Salary"].describe()

"""
count        6
mean     102333
std      195000
min       20000
25%       22000
50%       23500
75%       24750
max      500000

"""
# we can get Q1 & Q2
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

# then lower and upper value =>
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# now lets find potential outliers =>
df[[(df["Salary"] < lower) | (df["Salary"] > upper)]]

#first a value is outliner then invalid
