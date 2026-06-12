"""
Task 5 — Hybrid (Advanced Students)

Create class Animal with method:
- breathe()

Create Dog(Animal) with method:
- bark()

Create Cat(Animal) with method:
- meow()

Create Pet(Dog, Cat) with method:
- play()

Create object of Pet and call all methods
"""
class Animal:
    def breathe(self):
        print("Animal is breathing")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


class Pet(Dog, Cat):
    def play(self):
        print("Pet is playing")


print("\n----- Hybrid Inheritance -----")
p = Pet()
p.breathe()
p.bark()
p.meow()
p.play()