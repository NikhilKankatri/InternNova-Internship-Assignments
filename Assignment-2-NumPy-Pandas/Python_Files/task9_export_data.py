# Task 9: Exporting Data
import os
import pandas as pd

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "student_performance.csv"))

# Process: fill missing values and add derived columns
for col in ["Attendance_Pct", "Math", "Science", "English"]:
    df[col] = df[col].fillna(df[col].median())
df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mean()).round(1)
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = (df["Total"] / 3).round(2)
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Export
out_path = os.path.join(BASE, "processed_students.csv")
df.to_csv(out_path, index=False)
print("Exported to:", out_path)

# Verify by reading the exported file back
check = pd.read_csv(out_path)
print("\nVerification - shape of exported file:", check.shape)
print("Columns:", list(check.columns))
print("Missing values in exported file:", int(check.isnull().sum().sum()))
print("Identical to processed DataFrame:", check.round(2).equals(df.round(2)))
print("\nFirst 5 rows of exported file:\n", check.head())
