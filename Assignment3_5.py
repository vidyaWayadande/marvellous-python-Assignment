# MarvellousNum.py

def ChkPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        return True
    

    # main.py

from MarvellousNum import ChkPrime

def ListPrime(numbers):
    prime_sum = 0
    for num in numbers:
        if ChkPrime(num):
            prime_sum += num
    return prime_sum

# Main logic
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

result = ListPrime(numbers)

print("Addition of prime numbers is:",result)
