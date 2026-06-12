"""
Task 4 — Hierarchical Inheritance

Create class Vehicle with methods:
- start()
- stop()

Create 3 child classes:
- Bus     → route()
- Bike    → wheelie()
- Car     → music()

Create objects of all 3 and call methods
"""

class Vehicle:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")


class Bus(Vehicle):
    def route(self):
        print("Bus is following its route")


class Bike(Vehicle):
    def wheelie(self):
        print("Bike is doing a wheelie")


class Car(Vehicle):
    def music(self):
        print("Car is playing music")


print("\n----- Hierarchical Inheritance -----")

bus = Bus()
bus.start()
bus.route()
bus.stop()

print()

bike = Bike()
bike.start()
bike.wheelie()
bike.stop()

print()

car = Car()
car.start()
car.music()
car.stop()
