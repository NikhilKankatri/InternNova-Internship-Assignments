# Task 9: Student Record Management System
# Records are stored in a list of dictionaries
 
students = []
 
 
def add_student():
    roll = input("Enter roll number: ")
    # don't allow the same roll number twice
    for s in students:
        if s["roll"] == roll:
            print("A student with this roll number already exists.")
            return
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = input("Enter marks: ")
    students.append({"roll": roll, "name": name, "branch": branch, "marks": marks})
    print("Student added.")
 
 
def display_students():
    if len(students) == 0:
        print("No records found.")
        return
    print("\nRoll\tName\t\tBranch\tMarks")
    print("-" * 40)
    for s in students:
        print(s["roll"] + "\t" + s["name"] + "\t\t" + s["branch"] + "\t" + s["marks"])
 
 
def search_student():
    name = input("Enter name to search: ").lower()
    found = False
    for s in students:
        if s["name"].lower() == name:
            print("Found ->", s["roll"], s["name"], s["branch"], s["marks"])
            found = True
    if not found:
        print("Student not found.")
 
 
def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Record deleted.")
            return
    print("No student with that roll number.")
 
 
while True:
    print("\n===== Student Record System =====")
    print("1. Add student")
    print("2. Display all students")
    print("3. Search student by name")
    print("4. Delete student")
    print("5. Exit")
    choice = input("Enter your choice: ")
 
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")