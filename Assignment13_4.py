class Student:
    # Class variable shared among all instances
    school_name = "ABC High School"

    def __init__(self, name, roll_no):
        # Instance variables unique to each object
        self.name = name
        self.roll_no = roll_no

    def display(self):
        # Display student details and school name
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"School: {Student.school_name}")


# Creating multiple objects of Student class
student1 = Student("Alice", 101)
student2 = Student("Bob", 102)

# Displaying details of each student
print("Student 1 Details:")
student1.display()

print("\nStudent 2 Details:")
student2.display()

# Changing the school name using the class name
Student.school_name = "XYZ International School"

# Displaying updated details
print("\nUpdated Student 1 Details:")
student1.display()

print("\nUpdated Student 2 Details:")
student2.display()
