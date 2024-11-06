# Defining the Car class
class Car:
    # Constructor to initialize the attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to display the car details
    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Calling the display_info method to print the car details
my_car.display_info()
