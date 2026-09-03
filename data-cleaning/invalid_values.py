import pandas as pd
import numpy as np

df = pd.read_csv("data_set_name.csv")

# step one inspect data
df.describe()
# reveal suspicious value

# min ,max value
df["column_name"].min()
df["column_name"].max()

# check multiple column
df[["column_name_one"], ["column_name_two"]].describe()

#unusal value =>
df["City"].unique()
df["City"].value_counts()

"""
output example :
Dhaka      2
Pabna      1
Unknown    1
Dkaha      1

"""
#found invalid values with condition
df[df["Age"]<0]
#if wrong or unsual val :
#Replace invalid values with NaN
df.loc[df["Age"] < 0, "Age"] = np.nan
df.loc[df["Age"] > 100, "Age"] = np.nan
#=?handle those missing values
df["Age"] = df["Age"].fillna(df["Age"].median())

#drop invalid values => filter
df = df[(df["Age"] >= 0) & (df["Age"] <= 100)]

#clean way to do
df.query("Age < 0")
df.query("Age < 0 or Age > 100")

# df[df["Age"]<0 | df["Age"]>100]
# df.loc[condition, "column"] = new_value (modify)
