* Concept
df.head()
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()

* Purpose:

head()              → See the data

info()              → Understand columns and data types

describe()          → Check statistics

isnull().sum()      → Find missing values

duplicated().sum()  → Find duplicate rows

# patter : df.loc[condition, "column_name"] = new_value
* 
Raw Dataset
     ↓
Inspect
     ↓
Find Missing Values
     ↓
Standardize Text
     ↓
Fix Data Types
     ↓
Detect Invalid Values
     ↓
Replace Invalid Values
     ↓
Handle Missing Values
     ↓
Validate
     ↓
Clean Dataset ✅

* Data Cleaning Flow
                 RAW DATA
                    │
                    ▼
          1️⃣ INSPECT THE DATA
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       head()     info()   describe()
          │
          ▼
       2️⃣ CHECK PROBLEMS
          │
    ┌─────┼─────┬────────┬─────────┐
    ▼     ▼     ▼        ▼         ▼
 Missing  Dupes  Types   Invalid   Inconsistent
 Values  Rows    Data     Values      Text
    │     │      │        │            │
    ▼     ▼      ▼        ▼            ▼
 3️⃣ FIX EACH PROBLEM
          │
          ▼
   Missing Values
   ├─ dropna()
   └─ fillna()
       ├─ mean
       ├─ median
       └─ mode
          │
          ▼
      Duplicates
      └─ drop_duplicates()
          │
          ▼
      Data Types
      ├─ to_numeric()
      └─ to_datetime()
          │
          ▼
     Invalid Values
     ├─ detect
     ├─ correct
     ├─ replace with NaN
     └─ remove if necessary
          │
          ▼
    Text Standardization
    ├─ strip()
    ├─ lower()
    ├─ upper()
    ├─ title()
    └─ replace()
          │
          ▼
        OUTLIERS
          │
     ┌────┼────┐
     ▼    ▼    ▼
    Keep Correct Remove
          │
          ▼
     4️⃣ VALIDATE
          │
    ┌─────┼─────────┐
    ▼     ▼         ▼
 Missing Dupes   Invalid
 Values  Rows     Values
          │
          ▼
       CLEAN DATA ✅
          │
          ▼
        5️⃣ EDA 📊