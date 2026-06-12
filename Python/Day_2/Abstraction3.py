"""
a = 10
b = 0

try:
    print(a/b)
except:
    print("cannot divide by zero")

print("hello world")
"""

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Zero se divide nahi kar sakte!")

except ValueError:
    print("Sirf number enter karo!")