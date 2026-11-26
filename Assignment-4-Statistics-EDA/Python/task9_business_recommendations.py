# Task 9: Business Recommendations - the numbers behind each recommendation
import os
import pandas as pd

pd.set_option("display.width", 130)
BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "store_sales_clean.csv"), parse_dates=["Order_Date"])
df["Margin"] = df["Profit"] / df["Total_Sales"] * 100

print("=== Recommendation 1: limit deep discounts, especially on Electronics ===")
hi = df["Discount_Pct"] >= 20
print("Average profit margin, discount 0-15% :", round(df.loc[~hi, "Margin"].mean(), 1), "%")
print("Average profit margin, discount 20%+  :", round(df.loc[hi, "Margin"].mean(), 1), "%")
print("Average quantity per order, discount 0-15% :", round(df.loc[~hi, "Quantity"].mean(), 2))
print("Average quantity per order, discount 20%+  :", round(df.loc[hi, "Quantity"].mean(), 2))
e = df[df["Category"] == "Electronics"]
print("Electronics margin, discount 0-15% :", round(e.loc[e["Discount_Pct"] < 20, "Margin"].mean(), 1), "%")
print("Electronics margin, discount 20%+  :", round(e.loc[e["Discount_Pct"] >= 20, "Margin"].mean(), 1), "%")
print("Orders with a loss:", int((df["Profit"] < 0).sum()), "of", len(df), "| of those with discount 20%+:", int(((df["Profit"] < 0) & hi).sum()))
print("Total profit lost on loss-making orders:", round(df.loc[df["Profit"] < 0, "Profit"].sum(), 0))

print("\n=== Recommendation 2: speed up deliveries in the slowest region ===")
reg = df.groupby("Region").agg(avg_delivery=("Delivery_Days", "mean"), avg_rating=("Customer_Rating", "mean"), orders=("Order_ID", "count")).round(2)
print(reg.to_string())
slow = df[df["Delivery_Days"] >= 7]; fast = df[df["Delivery_Days"] <= 3]
print("Share of orders delivered in 7+ days:", round(len(slow) / len(df) * 100, 1), "%")
print("Average rating, delivery 3 days or less:", round(fast["Customer_Rating"].mean(), 2))
print("Average rating, delivery 7 days or more:", round(slow["Customer_Rating"].mean(), 2))
print("Share of 7+ day orders that come from East:", round((slow["Region"] == "East").mean() * 100, 1), "%")

print("\n=== Recommendation 3: plan stock and marketing for the Oct-Dec season ===")
m = df.groupby(df["Order_Date"].dt.month)["Total_Sales"].sum()
q4 = m.loc[10:12].sum() / m.sum() * 100
print("Share of yearly sales in Oct-Dec:", round(q4, 1), "% (3 of 12 months = 25.0% if sales were even)")
print("Average monthly sales Jan-Sep :", round(m.loc[1:9].mean(), 0))
print("Average monthly sales Oct-Dec :", round(m.loc[10:12].mean(), 0))
