# Task 3: Correlation & Probability Basics
import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "store_sales_clean.csv"))

def describe(r):
    a = abs(r)
    strength = "very weak / no" if a < 0.2 else "weak" if a < 0.4 else "moderate" if a < 0.6 else "strong"
    return f"{strength} {'positive' if r > 0 else 'negative'} relationship"

print("=== CORRELATION (Pearson) ===")
pairs = [("Delivery_Days", "Customer_Rating"), ("Discount_Pct", "Quantity"), ("Unit_Price", "Customer_Rating")]
for a, b in pairs:
    r = df[a].corr(df[b])
    print(f"{a} vs {b}: r = {r:.3f} -> {describe(r)}")

print("\n=== PROBABILITY ===")
n = len(df)
p_high = (df["Customer_Rating"] >= 4).mean()
print(f"Total orders: {n}")
print(f"1. P(rating is 4 or 5)               = {(df['Customer_Rating'] >= 4).sum()}/{n} = {p_high:.3f} ({p_high*100:.1f}%)")
p_elec = (df["Category"] == "Electronics").mean()
print(f"2. P(order is in Electronics)        = {(df['Category'] == 'Electronics').sum()}/{n} = {p_elec:.3f} ({p_elec*100:.1f}%)")
fast = df[df["Delivery_Days"] <= 3]
slow = df[df["Delivery_Days"] >= 7]
p_fast = (fast["Customer_Rating"] >= 4).mean()
p_slow = (slow["Customer_Rating"] >= 4).mean()
print(f"3. P(rating >= 4 | delivered in 3 days or less) = {(fast['Customer_Rating'] >= 4).sum()}/{len(fast)} = {p_fast:.3f} ({p_fast*100:.1f}%)")
print(f"4. P(rating >= 4 | delivered in 7 days or more) = {(slow['Customer_Rating'] >= 4).sum()}/{len(slow)} = {p_slow:.3f} ({p_slow*100:.1f}%)")
both = ((df["Category"] == "Electronics") & (df["Discount_Pct"] >= 20)).mean()
print(f"5. P(Electronics AND discount >= 20%) = {both:.3f} ({both*100:.1f}%)")
