class Demo:
    # Class variable shared among all instances
    Value = 100

    def __init__(self, nol, no2):
        # Instance variables unique to each object
        self.nol = nol
        self.no2 = no2

    def Fun(self):
        # Instance method to display values of instance variables
        print(f"Obj1: nol = {self.nol}, no2 = {self.no2}")

    def Gun(self):
        # Instance method to display values of instance variables
        print(f"Obj2: nol = {self.nol}, no2 = {self.no2}")

# Creating two objects of Demo class
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

# Calling instance methods
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
