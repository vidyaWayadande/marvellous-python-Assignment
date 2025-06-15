# Open the source file in read mode and destination file in write mode
with open("source.txt", "r") as source_file:
    with open("destination.txt", "w") as dest_file:
        # Read contents from source and write to destination
        for line in source_file:
            dest_file.write(line)

print("Contents copied from source.txt to destination.txt.")
