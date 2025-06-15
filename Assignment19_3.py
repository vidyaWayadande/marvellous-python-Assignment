import os
import sys
import shutil

def copy_files(source_dir, dest_dir):
    # Check if source directory exists
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Create destination directory if it doesn't exist
    try:
        os.makedirs(dest_dir, exist_ok=True)
        print(f"Destination directory '{dest_dir}' created.")
    except Exception as e:
        print(f"Error creating destination directory: {e}")
        return

    files_copied = 0

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isfile(source_path):
            try:
                shutil.copy2(source_path, dest_path)
                print(f"Copied: {item}")
                files_copied += 1
            except Exception as e:
                print(f"Error copying {item}: {e}")

    if files_copied == 0:
        print("No files found to copy.")
    else:
        print(f"\nTotal files copied: {files_copied}")

def main():
    if len(sys.argv) != 3:
        print("Usage: DirectoryCopy.py <SourceDirectory> <DestinationDirectory>")
        print('Example: DirectoryCopy.py "Demo" "Temp"')
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    copy_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()
