import math

class Shape:
    """Base class for shapes."""
    
    def area(self):
        """Calculate area - must be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Rectangle shape class."""
    
    def __init__(self, length, width):
        """Initialize Rectangle with length and width."""
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape class."""
    
    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius
    
    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)