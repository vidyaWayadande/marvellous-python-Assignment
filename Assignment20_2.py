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
        print("Usage: python DirectoryDuplicate.py <directory_name>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        sys.exit(1)

    checksums = {}
    duplicates = []

    # Walk through the directory and calculate checksums
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            checksum = calculate_checksum(file_path)
            if checksum is None:
                print(f"Warning: Could not read file {file_path}")
                continue
            if checksum in checksums:
                # Duplicate found
                duplicates.append(file_path)
            else:
                checksums[checksum] = file_path

    # Write duplicates to tog.txt in current directory
    with open("tog.txt", "w") as log_file:
        if duplicates:
            log_file.write("Duplicate files found:\n")
            for dup_file in duplicates:
                log_file.write(dup_file + "\n")
            print(f"Duplicate files have been logged in 'tog.txt'.")
        else:
            log_file.write("No duplicate files found.\n")
            print("No duplicate files found.")

if __name__ == "__main__":
    main()
