# GrandParents
class Grandfather:
    def __init__(self,name):
        self.name = name

    def property(self):
        print(f"{self.name} owns a house")

# Parent
class Father (Grandfather):
    def business(self):
        print(f"{self.name} runs a shop")

# Child 
class Son(Father):
    def study(self):
        print(f"{self.name} is studying")

# Object
s = Son("Rahul")
s.property() # GrandParents se mila
s.business() # Parents se mila
s.study() # Son ka apna


