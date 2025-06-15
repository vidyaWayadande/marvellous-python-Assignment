import os
import sys
import shutil

def copy_files_with_extension(source_dir, dest_dir, extension):
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    if not extension.startswith('.'):
        print("Error: File extension should start with a dot, e.g. '.exe'")
        return

    try:
        os.makedirs(dest_dir, exist_ok=True)
        print(f"Destination directory '{dest_dir}' is ready.")
    except Exception as e:
        print(f"Error creating destination directory: {e}")
        return

    copied_count = 0
    for filename in os.listdir(source_dir):
        if filename.endswith(extension):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)

            if os.path.isfile(source_path):
                try:
                    shutil.copy2(source_path, dest_path)
                    print(f"Copied: {filename}")
                    copied_count += 1
                except Exception as e:
                    print(f"Error copying {filename}: {e}")

    if copied_count == 0:
        print(f"No files with extension '{extension}' found in '{source_dir}'.")
    else:
        print(f"\nTotal files copied: {copied_count}")

def main():
    if len(sys.argv) != 4:
        print("Usage: DirectoryCopyExt.py <SourceDirectory> <DestinationDirectory> <Extension>")
        print('Example: DirectoryCopyExt.py "Demo" "Temp" ".exe"')
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    extension = sys.argv[3]

    copy_files_with_extension(source_dir, dest_dir, extension)

if __name__ == "__main__":
    main()
