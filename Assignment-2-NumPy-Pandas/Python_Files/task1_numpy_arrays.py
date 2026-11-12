# Task 1: NumPy Introduction & Arrays
import numpy as np

# Array with at least 10 numbers
arr = np.array([12, 45, 7, 23, 89, 34, 56, 11, 78, 90, 5, 67])
print("Array:", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)

# One-dimensional array
arr_1d = np.array([1, 2, 3, 4, 5])
print("\n1-D array:", arr_1d)
print("1-D shape:", arr_1d.shape, "| dimensions:", arr_1d.ndim)

# Two-dimensional array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\n2-D array:\n", arr_2d)
print("2-D shape:", arr_2d.shape, "| size:", arr_2d.size,
      "| dtype:", arr_2d.dtype, "| dimensions:", arr_2d.ndim)
