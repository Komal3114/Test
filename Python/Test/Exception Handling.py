"""
Q4. Create class AgeVerification: (4 Marks) 

• Method set_age(age): 
→ If age < 0 : raise ValueError 
→ If age < 18 : raise custom UnderAgeError 
→ If age > 100 : raise custom InvalidAgeError 
→ Else : print 'Valid age!' 

• Handle all exceptions with finally block.
"""
"""
# Custom Exceptions
class UnderAgeError(Exception):
    pass

class InvalidAgeError(Exception):
    pass


# AgeVerification Class
class AgeVerification:
    def set_age(self, age):
        try:
            if age < 0:
                raise ValueError("Age cannot be negative")
            elif age < 18:
                raise UnderAgeError("Under Age")
            elif age > 100:
                raise InvalidAgeError("Invalid Age")
            else:
                print("Valid age!")

        except ValueError as e:
            print(e)

        except UnderAgeError as e:
            print(e)

        except InvalidAgeError as e:
            print(e)

        finally:
            print("Age verification completed.")


# Create object
obj = AgeVerification()

# Test cases
obj.set_age(-5)
obj.set_age(15)
obj.set_age(120)
obj.set_age(25)
"""


"""
Q5. Create a Login System: (4 Marks) 
• Private variable __password = 'python@123' 
• Private variable __attempts = 3 
• Method login(password): 
→ Wrong password: attempts -= 1, show remaining 
→ If attempts == 0: raise AccountLockedError 
→ Correct: print 'Login successful!' 

• Handle AccountLockedError with finally block.
"""

# Custom Exception
class AccountLockedError(Exception):
    pass


# Login System Class
class LoginSystem:
    def __init__(self):
        self.__password = "python@123"
        self.__attempts = 3

    def login(self, password):
        try:
            if self.__attempts == 0:
                raise AccountLockedError("Account Locked!")

            if password == self.__password:
                print("Login successful!")
            else:
                self.__attempts -= 1
                print("Wrong password!")
                print("Remaining Attempts:", self.__attempts)

                if self.__attempts == 0:
                    raise AccountLockedError("Account Locked!")

        except AccountLockedError as e:
            print(e)

        finally:
            print("Login process completed.\n")


# Create object
user = LoginSystem()

# Test cases
"""
user.login("abc")
user.login("123")
user.login("xyz")"""
user.login("python@123")