# find_inconsistencies
import pandas as pd

data = {"City": ["Dhaka", "dhaka", "DHAKA", "Pabna", "Pabna ", "Rajshahi", "Dhaka"]}
df = pd.DataFrame(data)
# print(df["City"].unique())
print(df["City"].value_counts())
# flow: inspect>
# unique()>value_counts()>
# Identify inconsistencies>
# Standardize>
# Validate again
