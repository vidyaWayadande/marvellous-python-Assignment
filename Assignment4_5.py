from functools import reduce

# Function to check prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to multiply by 2
def multiply_by_two(num):
    return num * 2

# Function to get max of two numbers (for reduce)
def get_max(a, b):
    return a if a > b else b

# Input list from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Filter primes
prime_numbers = list(filter(is_prime, numbers))
print("List after filter:", prime_numbers)

# Map multiply by 2
mapped_numbers = list(map(multiply_by_two, prime_numbers))
print("List after map:", mapped_numbers)

# Reduce to get max
max_number = reduce(get_max, mapped_numbers)
print("Output of reduce:",max_number)