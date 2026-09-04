#practical_exercise
import pandas as pd
import numpy as np
data = {
    "Name": ["A", "B", "C", "D", "E", "E"],
    "Age": [25, -5, 30, "40", None, 150],
    "Salary": [30000, 25000, -10000, 40000, None, 50000],
    "City": ["Dhaka", " dhaka ", "DHAKA", "Pabna", "pabna", "Pabna"]
}
df = pd.DataFrame(data)
#inspect the data
# print(df.head())
# print(df.info())
# print(df.isnull().sum())
# print(df.duplicated().sum())
df["City"] = df["City"].str.strip().str.title()
df["Age"] =  pd.to_numeric(df["Age"],errors='coerce')
df[(df["Age"] < 0) | (df["Age"] > 100)]
# print(df[(df["Age"] < 0) | (df["Age"] > 100)])
df.loc[(df["Age"]<0)|(df["Age"]>100),"Age"] = np.nan
# print(df["Age"].isnull().sum())
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)
df.loc[df["Salary"] <= 0, "Salary"] = np.nan
median_salary = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(median_salary)
# print(df)
print("Missing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nAge validation:")
print(df[(df["Age"] < 0) | (df["Age"] > 100)])

print("\nSalary validation:")
print(df[df["Salary"] <= 0])

print("\nCity values:")
print(df["City"].value_counts())

"""
Raw Dataset
     ↓
Inspect
     ↓
Find Missing Values
     ↓
Standardize Text
     ↓
Fix Data Types
     ↓
Detect Invalid Values
     ↓
Replace Invalid Values
     ↓
Handle Missing Values
     ↓
Validate
     ↓
Clean Dataset ✅
"""