import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override this method")


# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Function to demonstrate polymorphism
def print_area(shape):
    print(f"The area is: {shape.area()}")

# Test the polymorphism
if __name__ == "__main__":
    # Create a Rectangle and Circle instance
    rectangle = Rectangle(5, 10)
    circle = Circle(7)

    # Use the polymorphic function to print the area
    print_area(rectangle)  # Rectangle area: 5 * 10 = 50
    print_area(circle)     # Circle area: π * 7^2
