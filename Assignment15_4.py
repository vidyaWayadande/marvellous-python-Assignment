# Accept two file names from the user
file1 = input("Enter the first filename: ")
file2 = input("Enter the second filename: ")

try:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()

        if content1 == content2:
            print("Success: Files have the same contents.")
        else:
            print("Files have different contents.")

except FileNotFoundError as e:
    print(f"Error: {e.filename} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
