# Task 2: Variance & Standard Deviation
import os
import numpy as np
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "store_sales_clean.csv"))

for col in ["Delivery_Days", "Customer_Rating", "Total_Sales"]:
    x = df[col].to_numpy(dtype=float)
    print(f"--- {col} ---")
    print("Mean                         :", round(x.mean(), 2))
    print("Variance (population, ddof=0):", round(np.var(x), 2))
    print("Variance (sample, ddof=1)    :", round(np.var(x, ddof=1), 2))
    print("Std deviation (population)   :", round(np.std(x), 2))
    print("Std deviation (sample)       :", round(np.std(x, ddof=1), 2))
    print("Coefficient of variation     :", f"{np.std(x, ddof=1) / x.mean() * 100:.1f}%")
    print()

# Manual check of the formula on Delivery_Days
x = df["Delivery_Days"].to_numpy(dtype=float)
manual_var = ((x - x.mean()) ** 2).sum() / (len(x) - 1)
print("Manual sample variance of Delivery_Days:", round(manual_var, 4))
print("Manual sample std deviation            :", round(manual_var ** 0.5, 4))

# Spread inside the mean +/- 1 standard deviation
m, sd = x.mean(), x.std(ddof=1)
share = ((x >= m - sd) & (x <= m + sd)).mean() * 100
print(f"\nDelivery_Days within mean +/- 1 SD ({m - sd:.1f} to {m + sd:.1f} days): {share:.1f}% of orders")
