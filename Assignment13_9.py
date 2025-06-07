class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False

# Creating instances of Product
product1 = Product("Laptop", 999)
product2 = Product("Smartphone", 999)
product3 = Product("Tablet", 499)

# Comparing products
print(product1 == product2)  # Output: True
print(product1 == product3)  # Output: False
