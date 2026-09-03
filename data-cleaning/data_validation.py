# data_validation
import pandas as pd

data = {
    "Age": [18, 25, 42, 61, 35, 10, 60],
}
df = pd.DataFrame(data)
df = df[(df["Age"] < 18) | (df["Age"] > 60)]
print(df)
