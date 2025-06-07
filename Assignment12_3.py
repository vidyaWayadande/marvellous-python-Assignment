class Arithmetic:
    def __init__(self):
        # Initialize instance variables to 0
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        # Accept values for value1 and value2 from the user
        self.value1 = float(input("Enter the first value: "))
        self.value2 = float(input("Enter the second value: "))

    def Addition(self):
        # Perform addition and return the result
        return self.value1 + self.value2

    def Subtraction(self):
        # Perform subtraction and return the result
        return self.value1 - self.value2

    def Multiplication(self):
        # Perform multiplication and return the result
        return self.value1 * self.value2

    def Division(self):
        # Perform division and return the result
        if self.value2 != 0:
            return self.value1 / self.value2
        else:
            return "Error: Division by zero is not allowed."


# Creating multiple objects of Arithmetic class
obj1 = Arithmetic()
obj2 = Arithmetic()

# Accepting values for obj1 and obj2
print("For object 1:")
obj1.Accept()
print("For object 2:")
obj2.Accept()

# Performing arithmetic operations for obj1
print(f"Addition of obj1: {obj1.Addition()}")
print(f"Subtraction of obj1: {obj1.Subtraction()}")
print(f"Multiplication of obj1: {obj1.Multiplication()}")
print(f"Division of obj2: {obj2.Division()}")
