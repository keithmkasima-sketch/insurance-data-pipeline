import pandas as pd
import sqlite3

# 1. Locate the data
file_path = "data/insurance_Dataset.csv"

# 2. Extract
df = pd.read_csv(file_path)
print("Raw data preview:")
print(df.head())

# 3. Remove duplicate values
df = df.drop_duplicates()

# 4. Handle missing values
df = df.dropna(subset=["age", "sex", "smoker", "charges"])  # drop rows missing critical values
df = df.fillna({
    "bmi": df["bmi"].mean(),
    "region": "unknown"
})

# 5. Convert to the right data types
df["age"] = df["age"].astype(int)
df["children"] = df["children"].astype(int)
df["bmi"] = df["bmi"].astype(float)
df["charges"] = df["charges"].astype(float)

# 6. Standardize text
df["sex"] = df["sex"].str.strip().str.lower()
df["smoker"] = df["smoker"].str.strip().str.lower()
df["region"] = df["region"].str.strip().str.lower()

# 7. Create a database
conn = sqlite3.connect("insurance_clean.db")

# 8. Load the clean data into a database table
df.to_sql("insurance", conn, if_exists="replace", index=False)

# Verify
print("Cleaned data preview:")
print(df.head())

# Example analysis
avg_charges = df.groupby("smoker")["charges"].mean()
print("\nAverage charges by smoker status:")
print(avg_charges)

conn.close()