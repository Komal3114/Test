"""
Task 3 — Multilevel Inheritance

Create class School with method:
- infrastructure()

Create class Department(School) with method:
- department_name()

Create class Classroom(Department) with method:
- total_students()

Create object of Classroom and call all methods
"""

class School:
    def infrastructure(self):
        print("School has good infrastructure")


class Department(School):
    def department_name(self):
        print("Department : Computer Science")


class Classroom(Department):
    def total_students(self):
        print("Total Students : 60")


print("\n----- Multilevel Inheritance -----")
c = Classroom()
c.infrastructure()
c.department_name()
c.total_students()
