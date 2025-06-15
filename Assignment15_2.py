# Accept filename from user
filename = input("Enter the filename to open: ")

try:
    # Open the file in read mode
    with open(filename, "r") as file:
        content = file.read()
        print(f"\nContents of {filename}:\n")
        print(content)
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
