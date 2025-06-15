# Open the file in read mode
file = open("data.txt", "r")

# Read the contents of the file
content = file.read()

# Display the contents
print("Contents of data.txt:")
print(content)

# Close the file
file.close()
