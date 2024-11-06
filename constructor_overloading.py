# Define the Rectangle class
class Rectangle:
    def __init__(self, length, width=None):
        # If width is not provided, treat it as a square
        if width is None:
            self.length = length
            self.width = length  # It's a square
        else:
            self.length = length
            self.width = width  # It's a rectangle

    # Method to calculate the area of the rectangle
    def area(self):
        return self.length * self.width

# Test with a square (one parameter)
square = Rectangle(5)
print("Square Area:", square.area())  # Output: 25

# Test with a rectangle (two parameters)
rectangle = Rectangle(5, 10)
print("Rectangle Area:", rectangle.area())  # Output: 50
