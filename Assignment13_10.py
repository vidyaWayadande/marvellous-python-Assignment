class Employee:
    def __init__(self, name, salary, department):
        self.name = name  # Public attribute
        self._salary = salary  # Protected attribute
        self.__department = department  # Private attribute

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"Department: {self.__department}")

    def get_department(self):
        return self.__department

# Creating an instance of Employee
emp = Employee("John Doe", 50000, "Finance")

# Accessing public attribute
print("Public Attribute (Name):", emp.name)

# Accessing protected attribute (not recommended)
print("Protected Attribute (Salary):", emp._salary)

# Accessing private attribute directly will raise an AttributeError
try:
    print("Private Attribute (Department):", emp.__department)
except AttributeError as e:
    print("Error:", e)

# Accessing private attribute using name mangling
print("Private Attribute (Department) via Name Mangling:", emp._Employee__department)

# Using getter method to access private attribute
print("Private Attribute (Department) via Getter:", emp.get_department())
