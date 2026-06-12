"""
Task - 1

Create a list of 5 fruits:
["apple", "banana", "mango", 
 "orange", "grapes"]

Do these operations:
1. Print first 3 fruits
2. Add "pineapple" at end
3. Remove "banana"
4. Print final list
"""
"""
# Create a list of fruits
fruits = ["apple", "banana", "mango", "orange", "grapes"]

# 1. Print first 3 fruits
print("First 3 fruits:", fruits[:3])

# 2. Add "pineapple" at end
fruits.append("pineapple")

# 3. Remove "banana"
fruits.remove("banana")

# 4. Print final list
print("Final list:", fruits)
"""

"""
Task - 2

Create a tuple of student info:
- name, age, city, course

Unpack the tuple and print:

Name  : Rahul
Age   : 20
City  : Pune
Course: Python
"""

"""
# Create a tuple of student information
student_info = ("Rahul", 20, "Pune", "Python")

# Unpack the tuple
name, age, city, course = student_info

# Print the details
print("Name  :", name)
print("Age   :", age)
print("City  :", city)
print("Course:", course)
"""


"""
Task - 3

Create a set of students:
["Rahul", "Priya", "Rahul",
 "Rohan", "Priya", "Sneha"]

1. Print set (duplicates remove!)
2. Add "Amit"
3. Remove "Rohan"
4. Print final set
"""

"""
# Create a set of students
students = {"Rahul", "Priya", "Rahul", "Rohan", "Priya", "Sneha"}

# 1. Print set (duplicates are removed automatically)
print("Original Set:", students)

# 2. Add "Amit"
students.add("Amit")

# 3. Remove "Rohan"
students.remove("Rohan")

# 4. Print final set
print("Final Set:", students)
"""


"""
Task - 4

Create dictionary of 3 students 
with marks:
- Rahul → 85
- Priya → 90
- Rohan → 65

Loop and print:
- marks > 75 → "Pass"
- marks < 75 → "Fail"

Expected Output:
Rahul - Pass
Priya - Pass
Rohan - Fail
"""

"""
# Create dictionary of students and marks
students = {
    "Rahul": 85,
    "Priya": 90,
    "Rohan": 65
}

# Check pass or fail
for name, marks in students.items():
    if marks > 75:
        print(name, "- Pass")
    else:
        print(name, "- Fail")
"""