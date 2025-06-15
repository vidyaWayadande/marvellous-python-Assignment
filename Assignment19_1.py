import os
import sys

def find_files_by_extension(directory, extension):
    try:
        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        
        if not files:
            print(f"No files with extension '{extension}' found in '{directory}'.")
        else:
            print(f"Files with extension '{extension}' in '{directory}':")
            for file in files:
                print(f"  - {file}")

    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: DirectoryFileSearch.py <Directory> <Extension>")
        print('Example: DirectoryFileSearch.py "Demo" ".txt"')
        sys.exit(1)

    dir_name = sys.argv[1]
    file_ext = sys.argv[2]

    find_files_by_extension(dir_name, file_ext)

if __name__ == "__main__":
    main()
