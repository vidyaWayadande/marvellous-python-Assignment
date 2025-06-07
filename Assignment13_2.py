class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create an instance of Rectangle
rect = Rectangle(10, 5)

# Calculate and display the area and perimeter
print(f"Area: {rect.area()}")           # Output: Area: 50
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 30
