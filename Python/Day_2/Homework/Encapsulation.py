"""
Task 2 — Encapsulation 🔒 

Create a class MobilePhone: 
- Private variable → __battery = 100 

Create 3 methods: 
- charge() → battery += 10 
- use_phone() → battery -= 10 
- check_battery() → show battery 

Create object and call all 3 methods
"""

class MobilePhone:
    def __init__(self):
        self.__battery = 100   # Private variable

    def charge(self):
        self.__battery += 10
        print("Phone charged")

    def use_phone(self):
        self.__battery -= 10
        print("Phone used")

    def check_battery(self):
        print("Battery Level:", self.__battery)

# Object
phone = MobilePhone()

phone.check_battery()
phone.use_phone()
phone.check_battery()
phone.charge()
phone.check_battery()