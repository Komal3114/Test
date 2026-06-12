# Parent Class
class Father:
    def __init__(self, name):
        self.name = name

    def property(self):
        print(f"{self.name} owns a house")

    def money(self):
        print(f"{self.name} has money")


# Child 1
class Son(Father):
    def cricket(self):
        print(f"{self.name} plays cricket")


# Child 2
class Daughter(Father):
    def dance(self):
        print(f"{self.name} loves dancing")


# Grandchild (Multilevel Inheritance)
class GrandSon(Son):
    def gaming(self):
        print(f"{self.name} plays games")


# Objects
s = Son("Rahul")
s.property()
s.money()
s.cricket()

print()

d = Daughter("Sita")
d.property()
d.money()
d.dance()

print()

g = GrandSon("Aman")
g.property()     # From Father
g.money()        # From Father
g.cricket()      # From Son
g.gaming()       # Own method