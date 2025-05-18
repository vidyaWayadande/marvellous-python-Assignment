from functools import reduce

# Step 1: Accept input list from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("List after filter:", even_numbers)

# Step 3: Map to calculate square of each even number
squared = list(map(lambda x: x ** 2, even_numbers))
print("List after map:", squared)

# Step 4: Reduce to get the sum of squares
total = reduce(lambda x, y: x + y, squared)
print("Output of reduce:",total)