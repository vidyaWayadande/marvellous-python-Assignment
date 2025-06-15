import sys

def main():
    # Check if both filenames are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <file1> <file2>")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    try:
        # Read contents of both files
        with open(file1, "r") as f1, open(file2, "r") as f2:
            content1 = f1.read()
            content2 = f2.read()

        # Compare contents
        if content1 == content2:
            print("Success: Both files have the same contents.")
        else:
            print("Files have different contents.")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
