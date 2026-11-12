# Task 8: Basic File Handling
 
filename = "introduction.txt"
 
# create the file and write my introduction
f = open(filename, "w")
f.write("Hello, my name is Nikhil Kankatri.\n")
f.write("I am studying B.E. in Computer Science and Engineering.\n")
f.write("I am learning Python for data analytics.\n")
f.close()
print("File created and written successfully.\n")
 
# read it back and display
f = open(filename, "r")
content = f.read()
f.close()
 
print("Contents of the file:")
print(content)