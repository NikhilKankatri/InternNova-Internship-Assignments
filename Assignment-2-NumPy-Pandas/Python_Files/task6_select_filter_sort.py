# Task 6: Selecting, Filtering & Sorting Data
import os
import pandas as pd

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "student_performance.csv"))

# Selecting columns
print("Selected columns (Name, Department, Math):\n",
      df[["Name", "Department", "Math"]].head())

# Selecting rows
print("\nFirst 5 rows using iloc[0:5]:\n", df.iloc[0:5][["Student_ID", "Name"]])
print("\nRows 10-12 using loc[10:12]:\n", df.loc[10:12, ["Student_ID", "Name", "Math"]])

# Filtering on a single condition
high_math = df[df["Math"] > 85]
print("\nStudents with Math > 85:\n", high_math[["Name", "Department", "Math"]])

# Multiple conditions
cond = df[(df["Department"] == "CSE") & (df["Math"] >= 60) & (df["Attendance_Pct"] >= 75)]
print("\nCSE students with Math >= 60 AND Attendance >= 75:\n",
      cond[["Name", "Math", "Attendance_Pct"]])

either = df[(df["Science"] > 90) | (df["English"] > 90)]
print("\nStudents with Science > 90 OR English > 90:\n",
      either[["Name", "Science", "English"]])

# Sorting
asc = df.sort_values("Math", ascending=True)
print("\nSorted by Math (ascending), first 5:\n", asc[["Name", "Math"]].head())
desc = df.sort_values("Math", ascending=False)
print("\nSorted by Math (descending), first 5:\n", desc[["Name", "Math"]].head())
