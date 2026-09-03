# lets imagine our data => 10, 12, 14, 15, 16, 18, 20, 100
# clearly 100 unusal here .
# we will see how python identify it =>
import pandas as pd
import numpy as np

# df = []
df = pd.DataFrame({"Salary": [10, 12, 14, 15, 16, 18, 20, 100]})
# print(df)
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
# print(Q1,Q3)
IQR = Q3 - Q1
print("IQR:", IQR)
# then lower and upper value =>
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
# condition to find outliers =>
outliers = df[(df["Salary"] < lower) | (df["Salary"] > upper)]
print(outliers)

# flow
# Q1 → Q3 → IQR → Lower/Upper Bound → Find Outliers
# replace outliers with mean or median value
# df.loc[df["Salary"] > upper, "Salary"] = np.nan

