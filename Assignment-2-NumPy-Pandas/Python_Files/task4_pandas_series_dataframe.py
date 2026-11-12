# Task 4: Pandas Series & DataFrame
import pandas as pd

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)

# Series
series = pd.Series([250, 300, 150, 400, 350],
                   index=["Mon", "Tue", "Wed", "Thu", "Fri"],
                   name="Daily_Sales")
print("Pandas Series:\n", series)

# DataFrame with student information
data = {
    "Student_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Aarav", "Ananya", "Rohan", "Priya", "Karan", "Sneha"],
    "Department": ["CSE", "ECE", "CSE", "ISE", "ME", "CSE"],
    "Marks": [88, 92, 75, 81, 67, 95],
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
print("\nColumn names:", list(df.columns))
print("Index:", df.index)

# Add a new column
df["Grade"] = ["A" if m >= 85 else "B" if m >= 70 else "C" for m in df["Marks"]]
print("\nUpdated DataFrame:\n", df)
