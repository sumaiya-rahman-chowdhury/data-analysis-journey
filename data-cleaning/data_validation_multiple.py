#data_validation_multiple ,
#create a new column that tells us whether a row is valid.
import pandas as pd

data = {
    "Salary": [20000, 25000, -5000, 30000, 0, 45000],
}
df = pd.DataFrame(data)
# validation flag
# df["Valid_Age"] = (df["Age"]>=18) & (df["Age"]<=60)
# print(df)

df["Valid_Salary"] = df["Salary"] > 0
print(df)
