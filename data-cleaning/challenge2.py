import pandas as pd
import numpy as np
#data cleaning and validation task 2
data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106, 107],
    "Name": ["Ali", "Sara", "John", "Mina", "Rafi", "Nadia", "Tania"],
    "Age": [25, "30", -5, None, 150, 35, 28],
    "Salary": [30000, 45000, 25000, -10000, 500000, None, 35000],
    "City": [" dhaka", "DHAKA", "Pabna ", "pabna", "Rajshahi", "rajshahi", "Dhaka"],
}
df = pd.DataFrame(data)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df.loc[(df["Age"] < 0) | (df["Age"] > 100), "Age"] = np.nan
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)
# Salary validation
df.loc[(df["Salary"] < 0), "Salary"] = np.nan
median_salary = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(median_salary)
# city inconsistance
df["City"] = df["City"].str.strip().str.title()
city_inconsistance = df["City"].value_counts()
# outlier detection
Q3 = df["Salary"].quantile(0.75)
Q1 = df["Salary"].quantile(0.25)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df["Salary"] < lower) | (df["Salary"] > upper)]
dup_values = df.duplicated().sum()
# keep outliers cause its valid .
print(df)
print("Missing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nInvalid Age:")
print(df[(df["Age"] < 0) | (df["Age"] > 100)])

print("\nInvalid Salary:")
print(df[df["Salary"] <= 0])