import pandas as pd

df = pd.read_csv("data.csv")
df["City"].unique()
# to count unique value
df["column_name"].value_counts()
# remove the extra space:
df[""] = df[""].str.strip()
# covert lower and upercase
df["City"] = df["City"].str.lower()
df["City"] = df["City"].str.upper()
# capitalization for names and titles ex : Dhaka , New York
# its "title case" a whole diff case ex : dhaKA=> Dhaka.
df["City"] = df["City"].str.title()

# chain method
df["City"] = df["City"].str.strip().str.lower().str.title()

# replace : dacca => Dhaka
df[""] = df[""].replace("Dacca", "Dhaka")
# multiple replacement :
df[""] = df[""].replace({"Dcca": "Dhaka", "ABC ": "Rajshahi"}).str.strip()

# real Data Cleaning Workflow

# 1. Inspect
df["City"].unique()

# 2. Remove extra spaces
df["City"] = df["City"].str.strip()

# 3. Standardize capitalization
df["City"] = df["City"].str.title()

# 4. Check again
df["City"].unique()
