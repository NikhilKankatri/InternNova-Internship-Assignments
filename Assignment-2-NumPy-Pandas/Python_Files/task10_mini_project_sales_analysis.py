# Task 10: Mini Data Analysis Project - Sales Dataset
import os
import numpy as np
import pandas as pd

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)

BASE = os.path.dirname(os.path.abspath(__file__))

# 1. Load
df = pd.read_csv(os.path.join(BASE, "sales_data.csv"), parse_dates=["Date"])
print("=== 1. LOAD ===")
print(df.head())

# 2. Inspect
print("\n=== 2. INSPECT ===")
print("Shape:", df.shape)
df.info()
print(df.describe().round(2))

# 3. Missing values
print("\n=== 3. MISSING VALUES ===")
print(df.isnull().sum())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Discount_Pct"] = df["Discount_Pct"].fillna(0)            # no discount recorded -> 0
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])   # categorical -> most frequent
print("After cleaning:\n", df.isnull().sum())

# Derived columns with NumPy
df["Gross"] = df["Unit_Price"] * df["Quantity"]
df["Revenue"] = np.round(df["Gross"] * (1 - df["Discount_Pct"] / 100), 2)
df["Month"] = df["Date"].dt.month_name()

# 4. Selecting & filtering
print("\n=== 4. SELECT & FILTER ===")
print(df[["Order_ID", "Category", "Region", "Revenue"]].head())
big = df[(df["Revenue"] > 50000) & (df["Customer_Type"] == "Returning")]
print("\nReturning-customer orders with revenue > 50,000:", len(big))
print(big[["Order_ID", "Category", "Region", "Revenue"]].head())

# 5. Sorting
print("\n=== 5. SORTING ===")
print("Top 5 orders by revenue:\n",
      df.sort_values("Revenue", ascending=False)[["Order_ID", "Category", "Region", "Revenue"]].head())

# 6. GroupBy
print("\n=== 6. GROUPBY ===")
cat = df.groupby("Category")["Revenue"].agg(["count", "sum", "mean"]).round(2).sort_values("sum", ascending=False)
print("Revenue by category:\n", cat)
reg = df.groupby("Region")["Revenue"].sum().round(2).sort_values(ascending=False)
print("\nRevenue by region:\n", reg)
cust = df.groupby("Customer_Type")["Revenue"].agg(["count", "sum", "mean"]).round(2)
print("\nRevenue by customer type:\n", cust)

# 7. Pivot table
print("\n=== 7. PIVOT TABLE ===")
pivot = pd.pivot_table(df, index="Category", columns="Region", values="Revenue",
                       aggfunc="sum", fill_value=0, margins=True, margins_name="Total").round(0)
print(pivot)

# 8. Insights
print("\n=== 8. INSIGHTS ===")
top_cat = cat.index[0]
print(f"- Total revenue: {df['Revenue'].sum():,.0f} across {len(df)} orders "
      f"(average order value {df['Revenue'].mean():,.0f}).")
print(f"- Top category: {top_cat} contributes {cat['sum'].iloc[0] / df['Revenue'].sum() * 100:.1f}% of revenue.")
print(f"- Top region: {reg.index[0]} ({reg.iloc[0]:,.0f}); weakest region: {reg.index[-1]} ({reg.iloc[-1]:,.0f}).")
print(f"- Returning customers generate {cust.loc['Returning', 'sum'] / df['Revenue'].sum() * 100:.1f}% of revenue.")
monthly = df.groupby("Month")["Revenue"].sum()
print(f"- Best month: {monthly.idxmax()} ({monthly.max():,.0f}); weakest month: {monthly.idxmin()} ({monthly.min():,.0f}).")
disc = df.groupby("Discount_Pct")["Quantity"].mean().round(2)
print("- Average quantity by discount level:", disc.to_dict())

# 9. Export
df.to_csv(os.path.join(BASE, "sales_cleaned.csv"), index=False)
print("\n=== 9. EXPORT ===")
print("Saved sales_cleaned.csv with shape", pd.read_csv(os.path.join(BASE, "sales_cleaned.csv")).shape)
