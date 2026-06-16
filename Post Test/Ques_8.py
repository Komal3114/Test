"""
Q8. File Handling — Employee System: (5 Marks)
• Create 'employees.txt' and write 5 employees with salary 
• Read and print the file 
• Append 2 more employees 
• Read and print updated file 
• Check if file exists using os.path.exists() 
• Delete the file
"""

import os

with open("employees.txt", "w") as file:
    file.write("Rahul - 25000\n")
    file.write("Priya - 30000\n")
    file.write("Amit - 28000\n")
    file.write("Sneha - 32000\n")
    file.write("Rohan - 27000\n")


print("Initial Employee Records:")
with open("employees.txt", "r") as file:
    print(file.read())


with open("employees.txt", "a") as file:
    file.write("Kavya - 35000\n")
    file.write("Arjun - 29000\n")


print("Updated Employee Records:")
with open("employees.txt", "r") as file:
    print(file.read())

if os.path.exists("employees.txt"):
    print("File exists.")
else:
    print("File does not exist.")


os.remove("employees.txt")
print("File deleted successfully.")