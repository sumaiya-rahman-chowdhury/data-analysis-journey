import pandas as pd
df = pd.read_csv("data.csv")
df.duplicated().sum()
# drop 
df.drop_duplicates()
df = df.drop_duplicates()
# certain columns.
df.duplicated(subset=["Customer_ID"])
df.duplicated(subset=["Customer_ID"]).sum()
df = df.drop_duplicates(subset=["Customer_ID"])
df.drop_duplicates(keep="first")



