import pandas as pd
import numpy as np

data = {
    "Name": ["Ali", "Sara", "John", "Mina", "Sara", "Rafi"],
    "Age": [22, -10, "35", None, 200, 28],
    "Salary": [25000, 30000, -5000, None, 45000, 35000],
    "City": ["dhaka", "Dhaka ", "DHAKA", "pabna", "PABNA", " Pabna "],
}

df = pd.DataFrame(data)
""""
RangeIndex: 6 entries, 0 to 5
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Name    6 non-null      str    
 1   Age     5 non-null      object 
 2   Salary  5 non-null      float64
 3   City    6 non-null      str    
dtypes: float64(1), object(1), str(2)
memory usage: 324.0+ bytes
None
N => 0
Age => 1
Salary => 1
City => 0
Note : Age has objext data type. Slary float . others okay 

"""
# Lets make age numeric firs =>
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df.loc[(df["Age"] < 0) | (df["Age"] > 100), "Age"] = np.nan
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)
df.loc[df["Salary"] <= 0,"Salary"] = np.nan
median_salary = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(median_salary)
df["City"] = df["City"].str.strip().str.title()
# df_clean = df.dropna(thresh=3)
# df_clean = df.dropna(subset=["Name", "Age", "City"], how="any")
print(df)
