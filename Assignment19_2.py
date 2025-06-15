import os
import sys

def rename_files(directory, old_ext, new_ext):
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    files_renamed = 0

    for filename in os.listdir(directory):
        if filename.endswith(old_ext):
            base = filename[: -len(old_ext)]
            new_name = base + new_ext
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_name}")
                files_renamed += 1
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

    if files_renamed == 0:
        print(f"No files with extension '{old_ext}' found in '{directory}'.")
    else:
        print(f"\nTotal files renamed: {files_renamed}")

def main():
    if len(sys.argv) != 4:
        print("Usage: DirectoryRename.py <Directory> <OldExtension> <NewExtension>")
        print('Example: DirectoryRename.py "Demo" ".txt" ".doc"')
        sys.exit(1)

    dir_name = sys.argv[1]
    old_ext = sys.argv[2]
    new_ext = sys.argv[3]

    if not old_ext.startswith('.') or not new_ext.startswith('.'):
        print("Error: Extensions must start with a dot (e.g., .txt, .doc)")
        sys.exit(1)

    rename_files(dir_name, old_ext, new_ext)

if __name__ == "__main__":
    main()
