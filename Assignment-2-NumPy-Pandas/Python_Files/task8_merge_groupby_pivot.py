# Task 8: Merge, Concatenate, GroupBy & Pivot Table
import os
import pandas as pd

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)

BASE = os.path.dirname(os.path.abspath(__file__))
students = pd.read_csv(os.path.join(BASE, "student_performance.csv"))
batch2 = pd.read_csv(os.path.join(BASE, "student_performance_batch2.csv"))
depts = pd.read_csv(os.path.join(BASE, "departments.csv"))

print("Departments table:\n", depts)

# ---- Merge on a common column ----
merged = pd.merge(students, depts, on="Department", how="left")
print("\nMerged (students + departments) on 'Department':")
print(merged[["Student_ID", "Name", "Department", "HOD", "Block"]].head())
print("Merged shape:", merged.shape)

# ---- Concatenate ----
combined = pd.concat([students, batch2], ignore_index=True)
print("\nConcatenate batch 1 + batch 2:")
print("Batch 1:", students.shape, "| Batch 2:", batch2.shape, "| Combined:", combined.shape)
print(combined.tail())

# Prepare a total/average column for analysis
combined["Total"] = combined[["Math", "Science", "English"]].sum(axis=1)
combined["Average"] = combined[["Math", "Science", "English"]].mean(axis=1).round(2)

# ---- GroupBy ----
print("\nGroupBy Department - mean of subjects:")
print(combined.groupby("Department")[["Math", "Science", "English"]].mean().round(2))

print("\nGroupBy Department - multiple aggregates on Math:")
print(combined.groupby("Department")["Math"].agg(["count", "sum", "mean", "min", "max"]).round(2))

print("\nGroupBy Gender - average of 'Average':")
print(combined.groupby("Gender")["Average"].mean().round(2))

# ---- Pivot Table ----
pivot = pd.pivot_table(combined, index="Department", columns="Gender",
                       values="Average", aggfunc="mean").round(2)
print("\nPivot table: Department (rows) x Gender (columns), mean Average:")
print(pivot)

pivot2 = pd.pivot_table(combined, index="Department", values=["Math", "Science", "English"],
                        aggfunc=["mean", "max"]).round(2)
print("\nPivot table: Department summary (mean & max per subject):")
print(pivot2)
