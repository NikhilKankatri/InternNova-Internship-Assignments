# Task 7: EDA - Data Inspection & Cleaning
# Dataset: store_sales_raw.csv (online store orders, 2025). Output: store_sales_clean.csv
import os
import numpy as np
import pandas as pd

pd.set_option("display.width", 110)
pd.set_option("display.max_columns", None)
BASE = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(os.path.join(BASE, "store_sales_raw.csv"))
raw0 = df.copy()   # untouched copy for the before/after comparison
SHOW = ["Order_ID", "Region", "Category", "Quantity", "Discount_Pct", "Delivery_Days", "Customer_Rating", "Total_Sales"]

print("=== DATA INSPECTION ===")
print("Rows and columns:", df.shape)
print("\nColumn names:", list(df.columns))
print("\nData types:\n", df.dtypes)
print("\nFirst 8 rows (BEFORE cleaning):\n", df[SHOW].head(8))
print("\nStatistical summary:\n", df.describe().round(2))

print("\n=== DATA CLEANING ===")
# 1. Missing values
print("\n1. Missing values per column (before):\n", df.isnull().sum()[df.isnull().sum() > 0])

# 2. Duplicates
dup = df.duplicated().sum()
print("\n2. Duplicate records found:", dup)
df = df.drop_duplicates().reset_index(drop=True)
print("   Shape after removing duplicates:", df.shape)

# 3. Inconsistent text values
print("\n3. Region values before:", sorted(df["Region"].dropna().unique()))
print("   Category values before:", sorted(df["Category"].unique()))
df["Region"] = df["Region"].str.strip().str.title()
df["Category"] = df["Category"].str.strip().str.title()
print("   Region values after :", sorted(df["Region"].dropna().unique()))
print("   Category values after :", sorted(df["Category"].unique()))

# 4. Impossible values
bad_delivery = (df["Delivery_Days"] < 1).sum()
bad_discount = ((df["Discount_Pct"] < 0) | (df["Discount_Pct"] > 100)).sum()
bad_rating = ((df["Customer_Rating"] < 1) | (df["Customer_Rating"] > 5)).sum()
print(f"\n4. Incorrect values: Delivery_Days < 1 -> {bad_delivery}, Discount outside 0-100 -> {bad_discount}, Rating outside 1-5 -> {bad_rating}")
r = raw0.drop_duplicates()
num_bad = (r["Delivery_Days"] < 1) | (r["Discount_Pct"] < 0) | (r["Discount_Pct"] > 100) | \
          (r["Customer_Rating"] < 1) | (r["Customer_Rating"] > 5)
text_bad = (r["Region"].notna() & (r["Region"].str.strip().str.title() != r["Region"])) | \
           (r["Category"].str.strip().str.title() != r["Category"])
miss_bad = r[["Region", "Discount_Pct", "Delivery_Days", "Customer_Rating"]].isnull().any(axis=1)
problem_ids = (r.loc[num_bad, "Order_ID"].head(3).tolist() + r.loc[text_bad & ~num_bad, "Order_ID"].head(3).tolist()
               + r.loc[miss_bad & ~num_bad & ~text_bad, "Order_ID"].head(2).tolist())
print("\nExample problem rows BEFORE cleaning (wrong numbers, inconsistent text, missing values):\n",
      r[r["Order_ID"].isin(problem_ids)][SHOW].sort_values("Order_ID").to_string())
df.loc[df["Delivery_Days"] < 1, "Delivery_Days"] = np.nan
df.loc[(df["Discount_Pct"] < 0) | (df["Discount_Pct"] > 100), "Discount_Pct"] = np.nan
df.loc[(df["Customer_Rating"] < 1) | (df["Customer_Rating"] > 5), "Customer_Rating"] = np.nan

# 5. Handling missing values
# Discount can be recovered from price, quantity and total sales
implied = (1 - df["Total_Sales"] / (df["Unit_Price"] * df["Quantity"])) * 100
implied = (implied / 5).round() * 5
df["Discount_Pct"] = df["Discount_Pct"].fillna(implied)
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])                       # categorical -> most common
df["Delivery_Days"] = df["Delivery_Days"].fillna(df.groupby("Region")["Delivery_Days"].transform("median"))
df["Customer_Rating"] = df["Customer_Rating"].fillna(df["Customer_Rating"].median())
print("\n5. Missing values per column (after):\n", df.isnull().sum())

# 6. Final types and sorting
for c in ["Quantity", "Discount_Pct", "Delivery_Days", "Customer_Rating"]:
    df[c] = df[c].astype(int)
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df = df.sort_values("Order_ID").reset_index(drop=True)

assert df.isnull().sum().sum() == 0 and df.duplicated().sum() == 0
print("\nFirst 8 rows (AFTER cleaning):\n", df[SHOW].head(8))
print("\nThe same problem rows AFTER cleaning:\n", df[df["Order_ID"].isin(problem_ids)][SHOW].to_string())
print("\nFinal shape:", df.shape)
print("Data types after cleaning:\n", df.dtypes)
df.to_csv(os.path.join(BASE, "store_sales_clean.csv"), index=False)
print("\nSaved store_sales_clean.csv")
