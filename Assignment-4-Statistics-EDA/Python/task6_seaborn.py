# Task 6: Seaborn Visualization (count plot, box plot, heatmap, pair plot)
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

BASE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(BASE, "outputs", "figures"); os.makedirs(FIG, exist_ok=True)
df = pd.read_csv(os.path.join(BASE, "store_sales_clean.csv"))
df["Profit_Margin_Pct"] = df["Profit"] / df["Total_Sales"] * 100
sns.set_theme(style="whitegrid")

# 1. Count plot
plt.figure(figsize=(8, 4.2))
order = df["Category"].value_counts().index
sns.countplot(data=df, x="Category", hue="Customer_Segment", order=order, palette="Set2")
plt.title("Number of Orders by Category and Customer Segment"); plt.xlabel("Category"); plt.ylabel("Number of orders")
plt.tight_layout(); plt.savefig(os.path.join(FIG, "fig6_countplot_category.png"), dpi=150); plt.close()
print("Count plot saved.\n", pd.crosstab(df["Category"], df["Customer_Segment"]))

# 2. Box plot
plt.figure(figsize=(8, 4.2))
sns.boxplot(data=df, x="Region", y="Delivery_Days", hue="Region", palette="pastel", legend=False)
plt.title("Delivery Time by Region"); plt.xlabel("Region"); plt.ylabel("Delivery time (days)")
plt.tight_layout(); plt.savefig(os.path.join(FIG, "fig6_boxplot_delivery_region.png"), dpi=150); plt.close()
print("\nBox plot saved. Median delivery days by region:\n", df.groupby("Region")["Delivery_Days"].median().to_string())

# 3. Heatmap of correlations
num = ["Unit_Price", "Quantity", "Discount_Pct", "Delivery_Days", "Customer_Rating", "Total_Sales", "Profit", "Profit_Margin_Pct"]
corr = df[num].corr()
plt.figure(figsize=(8.2, 6.4))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, linewidths=0.5, square=True, cbar_kws={"shrink": 0.8})
plt.title("Correlation Heatmap of Numerical Variables")
plt.tight_layout(); plt.savefig(os.path.join(FIG, "fig6_heatmap_correlation.png"), dpi=150); plt.close()
print("\nHeatmap saved.\n", corr.round(2).to_string())

# 4. Pair plot
g = sns.pairplot(df[["Discount_Pct", "Delivery_Days", "Customer_Rating", "Profit_Margin_Pct"]], corner=False,
                 diag_kind="hist", height=2.0, plot_kws=dict(alpha=0.5, s=18, color="#1f77b4"),
                 diag_kws=dict(color="#1f77b4", edgecolor="white"))
g.figure.suptitle("Pair Plot: Discount, Delivery, Rating and Profit Margin", y=1.02)
g.savefig(os.path.join(FIG, "fig6_pairplot.png"), dpi=130); plt.close("all")
print("\nPair plot saved.")
