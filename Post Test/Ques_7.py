"""
Q7. Set & Dictionary Operations: (6 Marks) 
• Create a set of 6 students (with 2 duplicates) 
• Print set — duplicates automatically removed 
• Add 2 new students to set 
• Create a dictionary of 4 students with their marks 
• Loop through dictionary: → marks >= 75: print 'Distinction' → marks >= 60: print 'Pass' → marks < 60 : print 'Fail'
"""

students = {"Rahul", "Priya", "Amit", "Sneha", "Rahul", "Priya"}

print("Student Set:")
print(students)

students.add("Rohan")
students.add("Kavya")

print("\nAfter Adding New Students:")
print(students)

marks = {
    "Rahul": 85,
    "Priya": 72,
    "Amit": 58,
    "Sneha": 65
}

print("\nStudent Results:")
for name, mark in marks.items():
    if mark >= 75:
        print(name, "-", mark, ": Distinction")
    elif mark >= 60:
        print(name, "-", mark, ": Pass")
    else:
        print(name, "-", mark, ": Fail")