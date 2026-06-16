"""
Q9. JSON — Student Database: (5 Marks) 
• Create a list of 4 students: Each student: name, age, city, course, marks 
• Save to 'students.json' with indent=4 
• Read the file back 
• Print only students with marks > 70 
• Print total number of students
"""

import json

students = [
    {
        "name": "Rahul",
        "age": 20,
        "city": "Bhopal",
        "course": "B.Tech",
        "marks": 85
    },
    {
        "name": "Priya",
        "age": 21,
        "city": "Indore",
        "course": "BCA",
        "marks": 78
    },
    {
        "name": "Amit",
        "age": 19,
        "city": "Gwalior",
        "course": "B.Sc",
        "marks": 65
    },
    {
        "name": "Sneha",
        "age": 22,
        "city": "Jabalpur",
        "course": "B.Tech",
        "marks": 92
    }
]


with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Data saved to students.json")


with open("students.json", "r") as file:
    data = json.load(file)


print("\nStudents with marks > 70:")
for student in data:
    if student["marks"] > 70:
        print(student["name"], "-", student["marks"])


print("\nTotal Number of Students:", len(data))