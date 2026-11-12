# Task 4: Grade Calculator
 
marks = float(input("Enter your marks: "))
 
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"
 
print("Marks:", marks)
print("Grade:", grade)
 