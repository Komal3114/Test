"""Task 1 — Polymorphism 🎯 Create 3 classes:
- Car → drive() → "Car is driving" 
- Bike → drive() → "Bike is driving" 
- Cycle → drive() → "Cycle is driving" 
Create objects of all 3 Call drive() on each
"""

class Car:
    def drive(self):
        print("Car is driving")

class Bike:
    def drive(self):
        print("Bike is driving")

class Cycle:
    def drive(self):
        print("Cycle is driving")

# Objects
c1 = Car()
b1 = Bike()
cy1 = Cycle()

# Calling same method
c1.drive()
b1.drive()
cy1.drive()