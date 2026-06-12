"""
Q8. Perform the following List operations: (2 Marks) 

• Create a list of 5 student names 
• Add 2 more names using append() and insert() 
• Remove a name using remove() and delete by index using pop() 
• Sort the list alphabetically and print it in reverse order 
• Slice the list to print only the first 3 elements
"""
"""
# Create a list of 5 student names
students = ["Rahul", "Priya", "Rohan", "Sneha", "Amit"]

# Add 2 more names
students.append("Neha")
students.insert(2, "Vikas")

# Remove a name and delete by index
students.remove("Amit")
students.pop(3)

# Sort the list alphabetically
students.sort()

# Print in reverse order
print("Reverse Order:", students[::-1])

# Print first 3 elements
print("First 3 Elements:", students[:3])
"""


"""
Q9. Perform the following Set and Tuple operations: (2 Marks) 
• Create a set of 5 programming languages (include 2 duplicates) — print to show uniqueness 
• Create another set of 3 languages and perform: union, intersection, difference 
• Create a tuple of 5 city names • Count occurrences of a city, find its index, and check if a city exists in the tuple 
• Try to modify the tuple and handle the error with a proper message
"""

"""
# Set Operations

# Create a set with duplicates
languages1 = {"Python", "Java", "C++", "Python", "Java", "JavaScript", "C"}

print("Set 1 (Duplicates Removed):", languages1)

# Create another set
languages2 = {"Python", "Java", "Go"}

# Union
print("Union:", languages1.union(languages2))

# Intersection
print("Intersection:", languages1.intersection(languages2))

# Difference
print("Difference:", languages1.difference(languages2))


# Tuple Operations

cities = ("Delhi", "Mumbai", "Pune", "Delhi", "Bhopal")

# Count occurrences
print("Count of Delhi:", cities.count("Delhi"))

# Find index
print("Index of Pune:", cities.index("Pune"))

# Check existence
if "Mumbai" in cities:
    print("Mumbai exists in the tuple")
else:
    print("Mumbai does not exist in the tuple")

# Try to modify tuple
try:
    cities[0] = "Indore"
except TypeError:
    print("Error: Tuples are immutable and cannot be modified.")
"""


"""
Q10. Perform the following Dictionary operations: (2 Marks) 
• Create a dictionary of 3 students: {'name': ..., 'age': ..., 'marks': ...} 
• Add a new student and update marks of an existing student 
• Delete a student using del and check if a key exists using 'in' 
• Loop through the dictionary and print all keys, values, and items 
• Convert all student names to a list using dict.keys()
"""
"""
# Create a dictionary of students
students = {
    "Rahul": {"age": 20, "marks": 85},
    "Priya": {"age": 21, "marks": 90},
    "Rohan": {"age": 19, "marks": 75}
}

# Add a new student
students["Sneha"] = {"age": 20, "marks": 92}

# Update marks of an existing student
students["Rohan"]["marks"] = 80

# Delete a student
del students["Priya"]

# Check if a key exists
if "Rahul" in students:
    print("Rahul exists in the dictionary")
else:
    print("Rahul does not exist")

# Print all keys
print("\nKeys:")
for key in students.keys():
    print(key)

# Print all values
print("\nValues:")
for value in students.values():
    print(value)

# Print all items
print("\nItems:")
for item in students.items():
    print(item)

# Convert student names to a list
student_names = list(students.keys())
print("\nStudent Names List:", student_names)
"""