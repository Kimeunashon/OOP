from abc import ABC, abstractmethod
import math

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius  # Area of a circle: πr^2

# Square subclass
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side  # Area of a square: side^2

# Create instances of Circle and Square
circle = Circle(5)
square = Square(4)

# Call area() on each
print(f"Area of Circle: {circle.area()}")
print(f"Area of Square: {square.area()}")
