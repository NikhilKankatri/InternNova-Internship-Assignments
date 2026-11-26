# Task 8: EDA - Correlation & Insights
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.width", 130)
BASE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(BASE, "outputs", "figures"); os.makedirs(FIG, exist_ok=True)
df = pd.read_csv(os.path.join(BASE, "store_sales_clean.csv"), parse_dates=["Order_Date"])
df["Profit_Margin_Pct"] = df["Profit"] / df["Total_Sales"] * 100
sns.set_theme(style="whitegrid")

# --- Correlation analysis
num = ["Unit_Price", "Quantity", "Discount_Pct", "Delivery_Days", "Customer_Rating", "Total_Sales", "Profit", "Profit_Margin_Pct"]
corr = df[num].corr()
pairs = corr.where(np.triu(np.ones(corr.shape, dtype=bool), k=1)).stack().sort_values(key=abs, ascending=False)
print("=== Strongest correlations (absolute value) ===")
print(pairs.head(8).round(3).to_string())

# --- Pattern 1: delivery time vs rating
print("\n=== Average rating by delivery time ===")
r = df.groupby("Delivery_Days")["Customer_Rating"].agg(["mean", "count"]).round(2)
print(r.to_string())
plt.figure(figsize=(8, 4))
rr = r[r["count"] >= 5]
plt.plot(rr.index, rr["mean"], marker="o", color="#1f77b4", linewidth=2)
plt.title("Average Customer Rating by Delivery Time"); plt.xlabel("Delivery time (days)"); plt.ylabel("Average rating (1-5)")
plt.ylim(1, 5); plt.grid(alpha=0.3); plt.tight_layout()
plt.savefig(os.path.join(FIG, "fig8_rating_by_delivery.png"), dpi=150); plt.close()

# --- Pattern 2: discount vs profit margin
print("\n=== Profit margin and quantity by discount level ===")
d = df.groupby("Discount_Pct").agg(orders=("Order_ID", "count"), avg_quantity=("Quantity", "mean"),
                                   avg_margin=("Profit_Margin_Pct", "mean"), total_profit=("Profit", "sum")).round(2)
print(d.to_string())
plt.figure(figsize=(8, 4))
plt.bar(d.index.astype(str) + "%", d["avg_margin"], color=["#2a9d8f" if v > 0 else "#d1495b" for v in d["avg_margin"]])
plt.title("Average Profit Margin by Discount Level"); plt.xlabel("Discount given"); plt.ylabel("Average profit margin (%)")
plt.axhline(0, color="black", linewidth=0.8); plt.grid(axis="y", alpha=0.3); plt.tight_layout()
plt.savefig(os.path.join(FIG, "fig8_margin_by_discount.png"), dpi=150); plt.close()

# --- Pattern 3: category profitability
print("\n=== Category profitability ===")
c = df.groupby("Category").agg(sales=("Total_Sales", "sum"), profit=("Profit", "sum"))
c["margin_pct"] = (c["profit"] / c["sales"] * 100).round(1)
c = c.sort_values("margin_pct", ascending=False).round(0)
print(c.to_string())
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(c.index, c["margin_pct"], color="#2a9d8f")
for i, v in enumerate(c["margin_pct"]): ax.text(i, v, f"{v:.1f}%", ha="center", va="bottom", fontsize=9)
ax.set_title("Profit Margin by Category"); ax.set_xlabel("Category"); ax.set_ylabel("Profit margin (%)")
ax.grid(axis="y", alpha=0.3); plt.tight_layout()
plt.savefig(os.path.join(FIG, "fig8_margin_by_category.png"), dpi=150); plt.close()

# --- Trend: seasonality
q = df.groupby(df["Order_Date"].dt.quarter)["Total_Sales"].sum()
print("\n=== Sales by quarter ===")
print(q.round(0).to_string(), "\nQ4 share of yearly sales:", f"{q[4] / q.sum() * 100:.1f}%")

# --- Region delivery
print("\n=== Region summary ===")
print(df.groupby("Region").agg(orders=("Order_ID", "count"), avg_delivery=("Delivery_Days", "mean"),
                               avg_rating=("Customer_Rating", "mean")).round(2).to_string())
