# Task 7: Strings and Collections
 
# ---- Strings ----
text = "Python for Data Analytics"
print("Original :", text)
print("upper()  :", text.upper())
print("lower()  :", text.lower())
print("replace():", text.replace("Data Analytics", "Beginners"))
print("find()   :", text.find("Data"))   # index where "Data" starts
 
# ---- Lists ----
print("\n--- List ---")
fruits = ["mango", "apple", "banana"]
print("Start    :", fruits)
fruits.append("orange")
print("append   :", fruits)
fruits.remove("apple")
print("remove   :", fruits)
fruits.sort()
print("sort     :", fruits)
 
# ---- Tuple ----
print("\n--- Tuple ---")
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
print("Tuple    :", days)
print("days[0]  :", days[0])
print("days[-1] :", days[-1])
 
# ---- Dictionary ----
print("\n--- Dictionary ---")
student = {
    "name": "Nikhil",
    "branch": "CSE",
    "year": 3,
    "cgpa": 8.2
}
print(student)
print("Name:", student["name"])
 
# ---- Set ----
print("\n--- Set ---")
skills = {"Python", "SQL", "Excel"}
print("Start    :", skills)
skills.add("Power BI")
print("add      :", skills)
skills.remove("Excel")
print("remove   :", skills)