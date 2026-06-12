class Dog:
    def sound(self):
        print("Dog says Woof !!")

class Cat:
    def sound(self):
        print("Cat Says Meow !!")

class Cow:
    def sound(self):
        print("Cow Says Moo !!")

# Same Method Name - sound()
# Different Behavior

d = Dog()
d.sound()

c = Cat()
c.sound()

co = Cow()
co.sound()