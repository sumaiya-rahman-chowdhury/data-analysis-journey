# standardization.
# df["City"] = df["City"].str.strip().str.title()
import pandas as pd

data = {"City": ["Dhaka", "Dacca", "dhaka", "Chittagong", "ctg"]}
df = pd.DataFrame(data)
# df["City"] = df["City"].str.strip().str.title()
# df = df.replace('Dacca','Dhaka')
replacements = {
    "Dacca": "Dhaka",
    "ctg": "Chittagong", 
}
df["City"] = df["City"].replace(replacements)
df["City"] = df["City"].str.strip().str.title()
print(df)
