"""
Q1. Create a class Employee with: (3 Marks) 
• Private variable __salary = 50000 
• Method increment() → salary += 10000 
• Method deduct() → salary -= 5000 
• Method get_salary() → print salary 
Create 2 objects and call all methods on both.
"""
"""
# Employee class
class Employee:
    def __init__(self):
        self.__salary = 50000  # Private variable

    def increment(self):
        self.__salary += 10000

    def deduct(self):
        self.__salary -= 5000

    def get_salary(self):
        print("Salary:", self.__salary)


# Create 2 objects
emp1 = Employee()
emp2 = Employee()

# Operations on Employee 1
print("Employee 1:")
emp1.get_salary()
emp1.increment()
emp1.get_salary()
emp1.deduct()
emp1.get_salary()

# Operations on Employee 2
print("\nEmployee 2:")
emp2.get_salary()
emp2.increment()
emp2.get_salary()
emp2.deduct()
emp2.get_salary()
"""


"""
Q2. Create Abstract class Vehicle with: (4 Marks) 
• Abstract methods: start(), stop(), fuel_type() 

Create 3 child classes: 
• Car → 'Car started' / 'Petrol' 
• Bike → 'Bike started' / 'Petrol' 
• Tesla → 'Tesla started' / 'Electric' 

Create objects and call all methods.
"""
"""
from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass


# Child Class - Car
class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def fuel_type(self):
        print("Petrol")


# Child Class - Bike
class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")

    def fuel_type(self):
        print("Petrol")


# Child Class - Tesla
class Tesla(Vehicle):
    def start(self):
        print("Tesla started")

    def stop(self):
        print("Tesla stopped")

    def fuel_type(self):
        print("Electric")


# Create Objects
car = Car()
bike = Bike()
tesla = Tesla()

# Call Methods
print("Car:")
car.start()
car.stop()
car.fuel_type()

print("\nBike:")
bike.start()
bike.stop()
bike.fuel_type()

print("\nTesla:")
tesla.start()
tesla.stop()
tesla.fuel_type()
"""


"""
Q3. Create a Hybrid Inheritance program: (3 Marks) 

• Father: property(), business() 
• Son(Father): study() 
• Daughter(Father): dance() 
• GrandChild(Son, Daughter): gaming() 

Create object of GrandChild and call ALL methods.
"""
"""
# Father Class
class Father:
    def property(self):
        print("Father has property")

    def business(self):
        print("Father runs a business")


# Son Class
class Son(Father):
    def study(self):
        print("Son is studying")


# Daughter Class
class Daughter(Father):
    def dance(self):
        print("Daughter is dancing")


# GrandChild Class (Hybrid Inheritance)
class GrandChild(Son, Daughter):
    def gaming(self):
        print("GrandChild is playing games")


# Create object of GrandChild
gc = GrandChild()

# Call all methods
gc.property()
gc.business()
gc.study()
gc.dance()
gc.gaming()
"""