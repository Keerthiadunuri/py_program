from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area of Rectangle:", self.length * self.breadth)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14
        print("Area of Circle:", pi * self.radius * self.radius)
r = Rectangle(10, 12)
c = Circle(7)
r.area()
c.area()
