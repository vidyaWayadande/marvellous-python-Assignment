class Circle:
    # Class variable for Pi
    Pi = 3.14

    def __init__(self):
        # Instance variables initialized to 0.0
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self):
        # Accept radius from user
        self.radius = float(input("Enter the radius of the circle: "))

    def CalculateArea(self):
        # Calculate area of the circle
        self.area = Circle.Pi * self.radius ** 2

    def CalculateCircumference(self):
        # Calculate circumference of the circle
        self.circumference = 2 * Circle.Pi * self.radius

    def Display(self):
        # Display the radius, area, and circumference
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area}")
        print(f"Circumference: {self.circumference}")


# Creating multiple objects of Circle class
circle1 = Circle()
circle2 = Circle()

# Calling instance methods
circle1.Accept()
circle1.CalculateArea()
circle1.CalculateCircumference()
circle1.Display()

circle2.Accept()
circle2.CalculateArea()
circle2.CalculateCircumference()
circle2.Display()
