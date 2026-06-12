"""
Task 2 — Multiple Inheritance

Create class Teacher with method:
- teach()

Create class Principal with method:
- manage_school()

Create class HeadTeacher that inherits 
BOTH Teacher and Principal with method:
- take_assembly()

Create object and call all methods
"""
class Teacher:
    def __init__(self,name):
        self.name = name

    def teach(self):
        print(f"{self.name} is teaching")


class Principal:
    def manage_school(self):
        print(f"{self.name} is managing the school")


class HeadTeacher(Teacher, Principal):
    def take_assembly(self):
        print(f"{self.name} is taking assembly")


print("\n----- Multiple Inheritance -----")
ht = HeadTeacher("Komal")
ht.teach()
ht.manage_school()
ht.take_assembly()
