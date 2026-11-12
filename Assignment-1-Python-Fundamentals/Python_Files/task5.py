# Task 5: Loops
 
# 1. numbers from 1 to 20 using for loop
print("Numbers 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")
print()
 
# 2. multiplication table
n = int(input("\nEnter a number for its table: "))
print("Multiplication table of", n)
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
 
# 3. even numbers from 1 to 50 using while loop
print("\nEven numbers 1 to 50:")
num = 1
while num <= 50:
    if num % 2 == 0:
        print(num, end=" ")
    num += 1
print()