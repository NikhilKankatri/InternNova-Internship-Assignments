# Task 3: Simple Calculator
 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
 
print("Addition       :", num1 + num2)
print("Subtraction    :", num1 - num2)
print("Multiplication :", num1 * num2)
 
# division and modulus fail if the second number is 0
if num2 == 0:
    print("Division       : Cannot divide by zero")
    print("Modulus        : Cannot divide by zero")
else:
    print("Division       :", num1 / num2)
    print("Modulus        :", num1 % num2)
 