# Open the file in read mode
file = open("data.txt", "r")

# Initialize counters
line_count = 0
word_count = 0
char_count = 0

# Read the file line by line
for line in file:
    line_count += 1
    word_count += len(line.split())
    char_count += len(line)

# Close the file
file.close()

# Display the results
print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Number of characters:", char_count)
