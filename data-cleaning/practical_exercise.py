#practical_exercise
import pandas as pd

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
print(df)
