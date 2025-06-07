class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)  # Calling the constructor of the base class
        self.subject = subject
        self.salary = salary

    def display(self):
        super().display()  # Calling the display method of the base class
        print(f"Subject: {self.subject}")
        print(f"Salary: ₹{self.salary}")

# Creating an instance of Teacher
teacher = Teacher("Mr. Sharma", 40, "Mathematics", 50000)

# Displaying the details of the teacher
teacher.display()
