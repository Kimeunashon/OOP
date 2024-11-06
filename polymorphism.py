# Define the Cat class
class Cat:
    def make_sound(self):
        print("Meow")

# Define the Dog class
class Dog:
    def make_sound(self):
        print("Woof")

# Function that takes an object and calls the make_sound method
def animal_sound(animal):
    animal.make_sound()  # Calls the make_sound method of the passed object

# Create instances of Cat and Dog
cat = Cat()
dog = Dog()

# Demonstrate polymorphism by passing instances of Cat and Dog to the same function
animal_sound(cat)  # Outputs: Meow
animal_sound(dog)  # Outputs: Woof
