# Base class
class Animal:
    def eat(self):
        print("This animal is eating.")

    def sleep(self):
        print("This animal is sleeping.")


# Subclass that inherits from Animal
class Dog(Animal):
    def bark(self):
        print("The dog is barking.")


# Create an instance of Dog
dog = Dog()

# Call methods from both Animal (inherited) and Dog (specific to Dog)
dog.eat()  # Inherited from Animal class
dog.sleep()  # Inherited from Animal class
dog.bark()  # Specific to Dog class
