# Define a list of student names
student_names = ["Pavan", "Pravin","Aniket", "Yash", "Krishn"]

# Open the file in write mode (this creates the file if it doesn't exist)
with open("student.txt", "w") as file:
    # Write each name on a new line
    for name in student_names:
        file.write(name + "\n")

print("student.txt has been created with 5 student names.")
