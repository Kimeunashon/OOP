# Base class Employee
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        # Generic method for calculating salary in the Employee class
        print(f"{self.name}'s salary is {self.base_salary}")

# Subclass Manager
class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)  # Calling the constructor of the parent class
        self.bonus = bonus

    # Overriding the calculate_salary method for Manager
    def calculate_salary(self):
        total_salary = self.base_salary + self.bonus
        print(f"{self.name}'s salary as a Manager is {total_salary} (Base Salary + Bonus)")

# Create an Employee object for Nashon
nashon = Employee("Nashon", 50000)
nashon.calculate_salary()  # Calls the method from Employee class

# Create a Manager object for Kimeu
kimeu = Manager("Kimeu", 70000, 15000)
kimeu.calculate_salary()  # Calls the overridden method from Manager class
