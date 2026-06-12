"""
Q6. Create a Student Report System: (3 Marks) 

• Create 'report.txt' with 5 students and marks: 
Rahul-85, Priya-90, Rohan-78, Sneha-92, Amit-65

• Read file and print only students with marks > 80 
• Handle FileNotFoundError with finally block.
"""
"""
# Create report.txt and write student data
with open("report.txt", "w") as file:
    file.write("Rahul-85\n")
    file.write("Priya-90\n")
    file.write("Rohan-78\n")
    file.write("Sneha-92\n")
    file.write("Amit-65\n")

# Read file and print students with marks > 80
try:
    with open("report.txt", "r") as file:
        for line in file:
            name, marks = line.strip().split("-")
            if int(marks) > 80:
                print(name, "-", marks)

except FileNotFoundError:
    print("File not found!")

finally:
    print("File operation completed.")
"""


"""
Q7. Create an Employee File System: (3 Marks) 

• Create 'employees.txt' with 3 employees 
• Read the file and print 
• Append 2 more employees 
• Read updated file 
• Delete the file and verify using os.path.exists()
"""
"""
import os

# Create employees.txt with 3 employees
with open("employees.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Priya\n")
    file.write("Rohan\n")

# Read and print the file
print("Initial Employee List:")
with open("employees.txt", "r") as file:
    print(file.read())

# Append 2 more employees
with open("employees.txt", "a") as file:
    file.write("Sneha\n")
    file.write("Amit\n")

# Read updated file
print("Updated Employee List:")
with open("employees.txt", "r") as file:
    print(file.read())

# Delete the file
os.remove("employees.txt")

# Verify deletion
if not os.path.exists("employees.txt"):
    print("File deleted successfully.")
else:
    print("File still exists.")
"""
