# Parent Class
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

# Child Class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says woof")

# Object
d = Dog("bruno")
d.eat()
d.bark()
