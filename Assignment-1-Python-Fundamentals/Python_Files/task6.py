# Task 6: Functions
 
def square(x):
    return x * x
 
 
def average(a, b, c):
    return (a + b + c) / 3
 
 
n = float(input("Enter a number to find its square: "))
print("Square of", n, "is", square(n))
 
print()
print("Enter three numbers to find the average")
x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))
print("Average is", round(average(x, y, z), 2))