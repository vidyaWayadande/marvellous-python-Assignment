import os

# Accept filename from the user
filename = input("Enter the filename: ")

# Check if the file exists in the current directory
if os.path.isfile(filename):
    print(f"The file '{filename}' exists in the current directory.")
else:
    print(f"The file '{filename}' does NOT exist in the current directory.")
