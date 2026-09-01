# to see missing value in df
import pandas as pd

df = pd.read_csv("data.csv")
df.isnull().sum()

""" it show us which column has missing data 
Name      0
Age       1
City      1
Salary    1
"""
"""Missing value
     ↓
 ┌───────────────┐
 │               │
Drop it       Fill it
"""
#drop the missing value :
df.dropna()
#for changed the result save df after change
df = df.dropna()

#fill the missing value 
df["column name"].fillna(25)
df["Age"].fillna(25)
# for save 
df["Age"] = df["Age"].fillna(25)
#ways to fill value :
df["Age"].mean() 
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["Age"] = df["Age"].fillna(df["Age"].median())

df["City"] = df["City"].fillna(df["City"].mode()[0])
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# outlier—an unusually large value
"""
| Situation                  | Better choice |
| -------------------------- | ------------- |
| Data has no major outliers | Mean          |
| Data has extreme outliers  | Median        |
| Categorical/text data      | Mode          |

"""

