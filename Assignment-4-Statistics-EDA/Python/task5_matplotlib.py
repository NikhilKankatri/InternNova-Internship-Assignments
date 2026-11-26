# Task 5: Matplotlib Visualization (line, bar, pie, histogram, scatter)
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

BASE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(BASE, "outputs", "figures"); os.makedirs(FIG, exist_ok=True)
df = pd.read_csv(os.path.join(BASE, "store_sales_clean.csv"), parse_dates=["Order_Date"])
lakh = FuncFormatter(lambda v, _: f"{v/100000:.0f}L" if v else "0")       # 1L = 1,00,000
BLUE, RED = "#1f77b4", "#d1495b"

# 1. Line chart - monthly sales trend
monthly = df.groupby(df["Order_Date"].dt.month)["Total_Sales"].sum()
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
plt.figure(figsize=(8, 4))
plt.plot(months, monthly.values, marker="o", color=BLUE, linewidth=2)
plt.title("Monthly Total Sales, 2025"); plt.xlabel("Month"); plt.ylabel("Total Sales (Rs, L = lakh)")
plt.gca().yaxis.set_major_formatter(lakh); plt.grid(alpha=0.3); plt.tight_layout()
plt.savefig(os.path.join(FIG, "fig5_line_monthly_sales.png"), dpi=150); plt.close()
print("Line chart saved. Best month:", months[monthly.values.argmax()], f"({monthly.max():,.0f})")

# 2. Bar chart - sales by category
cat = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 4))
bars = plt.bar(cat.index, cat.values, color="#2a9d8f")
plt.title("Total Sales by Product Category"); plt.xlabel("Category"); plt.ylabel("Total Sales (Rs, L = lakh)")
plt.gca().yaxis.set_major_formatter(lakh)
for b in bars:
    plt.text(b.get_x() + b.get_width() / 2, b.get_height(), f"{b.get_height():,.0f}", ha="center", va="bottom", fontsize=8)
plt.grid(axis="y", alpha=0.3); plt.tight_layout()
plt.savefig(os.path.join(FIG, "fig5_bar_category_sales.png"), dpi=150); plt.close()
print("Bar chart saved.\n", cat.round(0).to_string())

# 3. Pie chart - share of sales by region
reg = df.groupby("Region")["Total_Sales"].sum()
plt.figure(figsize=(5.5, 5.5))
plt.pie(reg.values, labels=reg.index, autopct="%1.1f%%", startangle=90,
        colors=["#1f77b4", "#ff9f1c", "#2a9d8f", "#d1495b"], wedgeprops=dict(edgecolor="white"))
plt.title("Share of Total Sales by Region"); plt.tight_layout()
plt.savefig(os.path.join(FIG, "fig5_pie_region_share.png"), dpi=150); plt.close()
print("Pie chart saved.\n", (reg / reg.sum() * 100).round(1).to_string())

# 4. Histogram - delivery days
plt.figure(figsize=(8, 4))
plt.hist(df["Delivery_Days"], bins=range(1, 15), color="#8d6cab", edgecolor="white", align="left")
plt.axvline(df["Delivery_Days"].mean(), color=RED, linestyle="--", label=f"Mean = {df['Delivery_Days'].mean():.1f} days")
plt.title("Distribution of Delivery Time"); plt.xlabel("Delivery time (days)"); plt.ylabel("Number of orders")
plt.legend(); plt.grid(axis="y", alpha=0.3); plt.tight_layout()
plt.savefig(os.path.join(FIG, "fig5_histogram_delivery_days.png"), dpi=150); plt.close()
print("Histogram saved.")

# 5. Scatter plot - sales vs profit, coloured by category
plt.figure(figsize=(8, 4.5))
colors = dict(zip(sorted(df["Category"].unique()), ["#1f77b4", "#ff9f1c", "#2a9d8f", "#d1495b", "#8d6cab"]))
for c, g in df.groupby("Category"):
    plt.scatter(g["Total_Sales"], g["Profit"], s=22, alpha=0.75, label=c, color=colors[c])
plt.title("Total Sales vs Profit per Order"); plt.xlabel("Total Sales (Rs)"); plt.ylabel("Profit (Rs)")
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}"))
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}"))
plt.legend(title="Category", fontsize=8); plt.grid(alpha=0.3); plt.tight_layout()
plt.savefig(os.path.join(FIG, "fig5_scatter_sales_profit.png"), dpi=150); plt.close()
print("Scatter plot saved. Correlation Total_Sales vs Profit:", round(df["Total_Sales"].corr(df["Profit"]), 3))
