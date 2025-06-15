# Accept file name from user
filename = input("Enter the file name: ")

try:
    # Open the file in read mode
    with open(filename, "r") as file:
        content = file.read()
        print("\n--- File Contents ---")
        print(content)
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
