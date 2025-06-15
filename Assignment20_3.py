import os
import sys
import hashlib

def calculate_checksum(file_path):
    """Calculate SHA-256 checksum of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except Exception as e:
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python DirectoryDuplicateRemoval.py <directory_name>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        sys.exit(1)

    checksums = {}
    deleted_files = []

    # Walk through the directory and calculate checksums
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            checksum = calculate_checksum(file_path)
            if checksum is None:
                print(f"Warning: Could not read file {file_path}")
                continue
            if checksum in checksums:
                # Duplicate found — delete the current file
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    print(f"Deleted duplicate file: {file_path}")
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")
            else:
                checksums[checksum] = file_path

    # Write deleted duplicates to Log.txt in current directory
    with open("Log.txt", "w") as log_file:
        if deleted_files:
            log_file.write("Deleted duplicate files:\n")
            for file in deleted_files:
                log_file.write(file + "\n")
            print(f"Deleted duplicates logged in 'Log.txt'.")
        else:
            log_file.write("No duplicate files were found to delete.\n")
            print("No duplicate files found.")

if __name__ == "__main__":
    main()
