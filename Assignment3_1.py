# Accept the number of elements
n = int(input("Enter number of elements: "))

# Initialize an empty list
numbers = []

# Accept elements from the user
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

# Calculate the sum of elements
total = sum(numbers)

# Display the result
print("Addition of all elements:",total)