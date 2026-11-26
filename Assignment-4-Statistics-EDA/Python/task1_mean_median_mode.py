# Task 1: Statistical Analysis - Mean, Median & Mode
# Run task7_eda_inspection_cleaning.py first (it creates store_sales_clean.csv)
import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "store_sales_clean.csv"))

for col in ["Total_Sales", "Quantity", "Delivery_Days", "Customer_Rating"]:
    s = df[col]
    mode = s.mode()
    print(f"--- {col} ---")
    print("Mean   :", round(s.mean(), 2))
    print("Median :", s.median())
    if s.value_counts().iloc[0] > 1:
        print("Mode   :", mode.tolist(), f"(appears {s.value_counts().iloc[0]} times)")
    else:
        print("Mode   : no value repeats")
    print()

# Mode of a categorical column
print("Most common Category :", df["Category"].mode()[0], f"({df['Category'].value_counts().iloc[0]} orders)")
print("Most common Region   :", df["Region"].mode()[0], f"({df['Region'].value_counts().iloc[0]} orders)")

# Mean vs median shows skew
s = df["Total_Sales"]
print("\nTotal_Sales mean - median gap:", round(s.mean() - s.median(), 2))
print("Skewness of Total_Sales:", round(s.skew(), 2))
