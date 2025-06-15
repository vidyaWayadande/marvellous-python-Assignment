import sys
import shutil

def main():
    # Check if a filename is provided via command line
    if len(sys.argv) != 2:
        print("Usage: python script.py <source_filename>")
        return

    source_file = sys.argv[1]
    destination_file = "Demo.txt"

    try:
        # Copy content from source to Demo.txt
        shutil.copyfile(source_file, destination_file)
        print(f"Contents copied from {source_file} to {destination_file}.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
