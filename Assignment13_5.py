class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

def main():
    calc = Calculator()

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {calc.multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {calc.divide(num1, num2)}")
        else:
            print("Invalid choice. Please select a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
