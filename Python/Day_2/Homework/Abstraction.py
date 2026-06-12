"""
Task 3 — Abstraction 🏧 

Create Abstract class Vehicle: 
- Abstract method → start() 
- Abstract method → stop() 

Create 2 child classes: 
- Car → start() → "Car Started" → stop() → "Car Stopped" 
- Bike → start() → "Bike Started" → stop() → "Bike Stopped" 

Create objects and call methods
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

# Child Class Car
class Car(Vehicle):
    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

# Child Class Bike
class Bike(Vehicle):
    def start(self):
        print("Bike Started")

    def stop(self):
        print("Bike Stopped")

# Objects
c = Car()
b = Bike()

c.start()
c.stop()

b.start()
b.stop()