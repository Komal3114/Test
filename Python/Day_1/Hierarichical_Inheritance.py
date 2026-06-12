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
        print(f"{self.name} loves Dancing")


# Child 3
class YoungSon(Father):
    def gaming(self):
        print(f"{self.name} plays games")


# Objects (IMPORTANT: pass name)
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

y = YoungSon("Aman")
y.property()
y.money()
y.gaming()