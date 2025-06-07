class Book:
    def __init__(self, price=0.0):
        self.__price = price  # Private attribute

    def get_price(self):
        """Getter method to access the price."""
        return self.__price

    def set_price(self, price):
        """Setter method to modify the price."""
        if price >= 0:
            self.__price = price
        else:
            print("Price cannot be negative.")

# Creating an instance of Book
my_book = Book()

# Setting the price using the setter method
my_book.set_price(500)

# Getting the price using the getter method
print(f"The price of the book is: ₹{my_book.get_price()}")
