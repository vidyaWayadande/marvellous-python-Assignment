class Vehicle:
    def start(self):
        print("The vehicle is starting.")

class Car(Vehicle):
    def start(self):
        super().start()  # Call the parent class's start method
        print("The car is now ready to drive.")

# Create an instance of Car
my_car = Car()

# Call the overridden start method
my_car.start()
