# Task 7: Handling Missing Values
import os
import pandas as pd

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "student_performance.csv"))

print("BEFORE handling - shape:", df.shape)
print("\nMissing values (isnull):\n", df.isnull().head())
print("\nMissing values per column:\n", df.isnull().sum())
print("Total missing values:", df.isnull().sum().sum())
print("\nRows containing at least one missing value:", df.isnull().any(axis=1).sum())

# Option 1: remove rows that contain missing values
df_dropped = df.dropna()
print("\nAFTER dropna() - shape:", df_dropped.shape)

# Option 2: fill missing values
df_filled = df.copy()
for col in ["Attendance_Pct", "Math", "Science", "English"]:
    df_filled[col] = df_filled[col].fillna(df_filled[col].median())   # skewed/integer-like marks -> median
df_filled["Study_Hours"] = df_filled["Study_Hours"].fillna(df_filled["Study_Hours"].mean())
df_filled["Study_Hours"] = df_filled["Study_Hours"].round(1)

print("\nAFTER fillna() - shape:", df_filled.shape)
print("Missing values per column after filling:\n", df_filled.isnull().sum())

print("\nRows that had missing values - before:\n",
      df[df.isnull().any(axis=1)].head(6))
print("\nSame rows - after filling:\n",
      df_filled.loc[df[df.isnull().any(axis=1)].head(6).index])

print("""
Why handling missing data matters in Data Analytics:
- Missing values bias statistics such as mean, sum and correlation.
- Many functions and ML models fail or silently drop rows when NaN is present.
- Unhandled gaps reduce data quality and lead to wrong business decisions.
- Dropping rows loses information, while filling (mean/median) keeps the dataset size intact.
""")
