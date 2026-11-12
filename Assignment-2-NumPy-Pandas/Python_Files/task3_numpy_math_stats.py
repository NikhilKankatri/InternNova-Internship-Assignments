# Task 3: NumPy Mathematical & Statistical Operations
import numpy as np

# Dataset: marks of 10 students in two subjects
maths = np.array([78, 85, 62, 90, 55, 73, 88, 67, 94, 81])
science = np.array([72, 80, 70, 85, 60, 65, 91, 74, 89, 77])
print("Maths  :", maths)
print("Science:", science)

print("\n--- Mathematical Operations ---")
print("Addition      :", maths + science)
print("Subtraction   :", maths - science)
print("Multiplication:", maths * science)
print("Division      :", np.round(maths / science, 2))

print("\n--- Statistical Functions (Maths marks) ---")
print("Mean              :", np.mean(maths))
print("Median            :", np.median(maths))
print("Minimum           :", np.min(maths))
print("Maximum           :", np.max(maths))
print("Standard Deviation:", round(float(np.std(maths)), 2))
print("Sum               :", np.sum(maths))

print("\n--- Statistical Functions (Science marks) ---")
print("Mean              :", np.mean(science))
print("Median            :", np.median(science))
print("Minimum           :", np.min(science))
print("Maximum           :", np.max(science))
print("Standard Deviation:", round(float(np.std(science)), 2))
print("Sum               :", np.sum(science))
