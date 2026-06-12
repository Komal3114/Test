"""
Create a program:
- Ask user to enter age
- If age less than 18
  → print "Voting nahi kar sakte!"
- If age 18 or above
  → print "Vote kar sakte ho!"
- finally
  → print "Thank you!"
"""

try:
    age = int(input("Enter your age: "))

    if age < 18:
        print("Voting nahi kar sakte!")
    else:
        print("Vote kar sakte ho!")

finally:
    print("Thank you!")