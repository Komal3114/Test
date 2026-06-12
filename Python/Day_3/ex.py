"""
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()

print(f"Name : {data['name']}")
print(f"Email : {data['email']}")
print(f"City : {data['address']['city']}")
"""

"""
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()

for user in data:
    print(f"Name : {user['name']} - Email: {user['email']}")
"""

"""
Task - 1

Create a program:

1. Call this API:
   https://jsonplaceholder.typicode.com/posts

2. Print only FIRST 5 posts:
   - Post ID
   - Title
"""

"""
import requests

# API Call
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# Convert response to JSON
posts = response.json()

# Print first 5 posts
for post in posts[:5]:
    print("Post ID:", post["id"])
    print("Title:", post["title"])
    print("-" * 40)
"""


"""
fruits = ["apple", "banana", "mango"]

fruits.append("orange") # Add at end
print(fruits)

fruits.insert(1, "grapes") # Add at position
print(fruits)

fruits.remove("banana") # Remove at value
print(fruits)

fruits.pop()  # Remove last
print(fruits)

print(len(fruits))      # Length
print(fruits.sort())    # Sort
"""


""""
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0:5])
print(numbers[5:])
print(numbers[:5])
print(numbers[::2])
"""


"""
# Normal way
numbers = []
for i in range(1,6):
    numbers.append(i)
print(numbers)

# Comprehensive way - one line
numbers = [i for i in range(1,6)]
print(numbers) # [1,2,3,4,5]

# Even Numbers
evens = [i for i in range(1,11) if i % 2 == 0]
print(evens) # [2,4,6,8,10]

# Squares
squares = [i*i for i in range(1,6)]
print(squares) # [1,4,9,10,25]
"""


"""
Create a list of 10 students:
["Rahul", "Priya", "Rohan", "Sneha", 
"Amit", "Pooja", "Vikas", "Neha", 
"Raj", "Anita"]

Do these operations:
1. Print first 5 students
2. Print last 5 students
3. Print every 2nd student
4. Add "Riya" at end
5. Remove "Rahul"
"""

"""
# List of students
students = [
    "Rahul", "Priya", "Rohan", "Sneha",
    "Amit", "Pooja", "Vikas", "Neha",
    "Raj", "Anita"
]

# 1. Print first 5 students
print("First 5 students:")
print(students[:5])

# 2. Print last 5 students
print("\nLast 5 students:")
print(students[-5:])

# 3. Print every 2nd student
print("\nEvery 2nd student:")
print(students[::2])

# 4. Add "Riya" at end
students.append("Riya")
print("\nAfter adding Riya:")
print(students)

# 5. Remove "Rahul"
students.remove("Rahul")
print("\nAfter removing Rahul:")
print(students)
"""


