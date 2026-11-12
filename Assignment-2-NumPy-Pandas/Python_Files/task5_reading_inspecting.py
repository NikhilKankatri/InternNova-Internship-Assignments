# Task 5: Reading & Inspecting Data
import os
import pandas as pd

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "student_performance.csv"))

print("First 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())
print("\nRows and columns:", df.shape)
print("Number of rows:", df.shape[0], "| Number of columns:", df.shape[1])
print("\nColumn names:", list(df.columns))
print("\nData types:\n", df.dtypes)
print("\nInfo:")
df.info()
print("\nDescribe:\n", df.describe().round(2))
