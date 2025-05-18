# Lambda function to multiply two numbers
multiply = lambda a, b: a * b

# Accept two inputs from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Display result
print("Output:", multiply(num1,num2))