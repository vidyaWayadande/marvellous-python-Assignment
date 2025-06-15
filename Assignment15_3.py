import sys

def main():
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_file> <destination_file>")
        sys.exit(1)
    
    source_file = sys.argv[1]
    dest_file = sys.argv[2]

    try:
        # Open source file and read content
        with open(source_file, "r") as src:
            content = src.read()

        # Open destination file and write content
        with open(dest_file, "w") as dst:
            dst.write(content)

        print(f"Contents copied from {source_file} to {dest_file}.")
    
    except FileNotFoundError:
        print(f"Error: Source file '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
