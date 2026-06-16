"""
Q4. Create a Student Registration System: (5 Marks) 
• Create your own exception: InvalidAgeError 
• Create your own exception: InvalidMarksError 
• Ask user to enter: name, age, marks 
• If age < 15 or age > 30 → raise InvalidAgeError 
• If marks < 0 or marks > 100 → raise InvalidMarksError • If valid → print 'Student registered successfully!'
• Handle both exceptions and add finally block.
"""

class InvalidAgeError(Exception):
    pass

class InvalidMarksError(Exception):
    pass

try:
    nam = input("Enter Student Name : ")
    age = int(input("Enter Age : "))
    marks = float(input("Enter marks : "))

    if age < 15 or age > 30:
        raise InvalidAgeError("Age must be between 15 and 30")
    
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")
    
    print("Student registered successfully!")


except InvalidAgeError as e:
    print("InvalidAgeError:", e)

except InvalidMarksError as e:
    print("InvalidMarksError:", e)

except ValueError:
    print("Please enter valid numeric values for age and marks.")

finally:
    print("Registration process completed.")