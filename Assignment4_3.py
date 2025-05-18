from functools import reduce

# Step 1: Accept list of numbers from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Use filter to select numbers >= 70 and <= 90
filtered = list(filter(lambda x: 70 <= x <= 90, numbers))
print("List after filter:", filtered)

# Step 3: Use map to increase each number by 10
mapped = list(map(lambda x: x + 10, filtered))
print("List after map:", mapped)

# Step 4: Use reduce to get the product of all numbers
product = reduce(lambda x, y: x * y, mapped)
print("Output of reduce:",product)