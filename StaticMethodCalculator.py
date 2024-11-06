class Calculator:
    # Static attribute to count the number of times the add() method is called
    count = 0

    # Static method to add two numbers
    @staticmethod
    def add(num1, num2):
        # Increment the count each time the add() method is called
        Calculator.count += 1
        return num1 + num2

# Demonstrating the use of the static method and updating the count
result1 = Calculator.add(5, 3)
print("Sum:", result1)  # Output: Sum: 8
print("Add method called:", Calculator.count, "times")  # Output: Add method called: 1 times

result2 = Calculator.add(10, 20)
print("Sum:", result2)  # Output: Sum: 30
print("Add method called:", Calculator.count, "times")  # Output: Add method called: 2 times
