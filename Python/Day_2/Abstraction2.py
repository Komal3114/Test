from abc import ABC, abstractmethod

# Principal = ABC
# Rules = abstractmethod
class Principle(ABC):

    @abstractmethod
    def wear_uniform(self):  # Rule 1
        pass
    @abstractmethod
    def do_homework(self): # Rule 2
        pass

# Students ko rules follow karni nahi padenge
class Students(Principle):

    def wear_uniform(self):
        print("Uniform Phen Liya")

    def do_homework(self):
        print("homework kar liya")

s = Students()
s.wear_uniform()
s.do_homework()


