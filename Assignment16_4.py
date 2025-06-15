# Open the file in write mode
file = open("numbers.txt", "w")

# Loop to accept 10 numbers from the user
for i in range(10):
    num = input(f"Enter number {i + 1}: ")
    file.write(num + "\n")

# Close the file
file.close()

print("10 numbers have been written to numbers.txt.")
