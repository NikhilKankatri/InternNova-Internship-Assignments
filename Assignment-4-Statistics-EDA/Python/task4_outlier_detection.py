# Task 4: Outlier Detection (IQR method, confirmed with Z-score)
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(BASE, "outputs", "figures"); os.makedirs(FIG, exist_ok=True)
df = pd.read_csv(os.path.join(BASE, "store_sales_clean.csv"))
s = df["Total_Sales"]

q1, q3 = s.quantile(0.25), s.quantile(0.75)
iqr = q3 - q1
low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print("Q1 =", round(q1, 2), "| Q3 =", round(q3, 2), "| IQR =", round(iqr, 2))
print("Lower fence =", round(low, 2), "| Upper fence =", round(high, 2))

out = df[(s < low) | (s > high)]
print("\nOutliers found by the IQR method:", len(out), f"({len(out)/len(df)*100:.1f}% of orders)")
print(out[["Order_ID", "Category", "Customer_Segment", "Quantity", "Total_Sales"]].sort_values("Total_Sales", ascending=False).head(15).to_string(index=False))

z = (s - s.mean()) / s.std()
print("\nOutliers found by Z-score (|z| > 3):", int((z.abs() > 3).sum()))
print(df.loc[z.abs() > 3, ["Order_ID", "Category", "Total_Sales"]].to_string(index=False))

print("\nEffect of the outliers on the statistics:")
clean = s[(s >= low) & (s <= high)]
print(f"Mean with outliers    : {s.mean():,.2f}  | without: {clean.mean():,.2f}")
print(f"Median with outliers  : {s.median():,.2f}  | without: {clean.median():,.2f}")
print(f"Std dev with outliers : {s.std():,.2f}  | without: {clean.std():,.2f}")

fig, ax = plt.subplots(figsize=(8, 2.8))
ax.boxplot(s, orientation="horizontal", widths=0.5, patch_artist=True, boxprops=dict(facecolor="#9ec5e8"),
           flierprops=dict(marker="o", markerfacecolor="#d1495b", markeredgecolor="#d1495b", markersize=5))
ax.set_title("Box plot of Total_Sales - red dots are outliers (IQR rule)")
ax.set_xlabel("Total Sales (Rs)"); ax.set_yticks([])
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
ax.grid(axis="x", alpha=0.3); plt.tight_layout()
plt.savefig(os.path.join(FIG, "fig4_outliers_boxplot.png"), dpi=150); plt.close()
