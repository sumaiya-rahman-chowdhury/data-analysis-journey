import pandas as pd

df = pd.read_csv("data_set_name.csv")
#data type conversion
df["column_name"] = df["column_name"].astype(int)
df["Age"] = df["Age"].astype(int)

"""
"25" → 25
"30" → 30
"""
# suppose age = unknown
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

""" pd.to_numeric() = convert values into number
errors="coerce" = if val cant be converted, replaced in with NAN
"""
# date conversion
df["Date"] = pd.to_datetime(df["Date"])
year = df["Date"].dt.year
month = df["Date"].dt.month

""" 
Handling bad dates:
suppose data :
2026-09-01
not available
2026-09-03

solution => df["Date"] = pd.to_datetime(
df["Date"] , errors = "coerce"
)

outut : 2026-09-01
NaT
2026-09-03

"""
