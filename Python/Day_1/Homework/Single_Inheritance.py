"""
Task 1 — Single Inheritance

Create a class Person with methods:
- walk()
- talk()

Create a class Student that inherits Person with methods:
- study()
- attend_class()

Create object and call all methods
"""

class Person:
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")

    def talk(self):
        print(f"{self.name} is talking")


class Student(Person):
    def study(self):
        print(f"{self.name} is studying")

    def attend_class(self):
        print(f"{self.name} is attending class")


print("----- Single Inheritance -----")
s = Student("Komal")
s.walk()
s.talk()
s.study()
s.attend_class()