"""
Create a program:
- Ask user to enter a number
- Divide 100 by that number
- If user enters 0 
  → print "Zero se divide nahi kar sakte!"
- If user enters abc
  → print "Sirf number enter karo!"
"""

try:
    num = int(input("Enter a number: "))

    result = 100 / num
    print("Result =", result)

except ZeroDivisionError:
    print("Zero se divide nahi kar sakte!")

except ValueError:
    print("Sirf number enter karo!")
    