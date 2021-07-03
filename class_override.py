"""class Person:

    def print2(self):
        print("This is a person obj")
        return self

class Employee(Person):
    def print2(self):
        print("This is a employee obj")
        return self

employee1 = Employee()
employee1.print2().print2()
"""

from abc import ABC,abstractmethod

class Rectangle:
    def __init__(self,bardzr,laynq):
        self.bardzr = bardzr
        self.laynq = laynq
    @abstractmethod
    def area(self):
        pass

class Square(Rectangle):
    def __init__(self,bardzr,laynq,erkar):
        super().__init__(bardzr,laynq)
        self.erkar = erkar

    def area(self):
        return (self.bardzr * self.laynq * self.erkar)


Square1 = Square(7,2,3)
Rectangle1 = Rectangle(2,4)
print(Square1.area())
