# Employee class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

# Payroll class
class Payroll:
    def __init__(self):
        # List to store employee objects
        self.employees = []

    def add_employee(self, employee):
        # Add employee to the payroll
        self.employees.append(employee)

    def calculate_total_payroll(self):
        # Sum the salary of all employees in the payroll
        total = sum(employee.get_salary() for employee in self.employees)
        return total

# Usage example
# Creating employee objects
emp1 = Employee("Joseph", 1000)
emp2 = Employee("Habiba", 2000)
emp3 = Employee("Bob", 40000)

# Creating payroll object
payroll = Payroll()

# Adding employees to the payroll
payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.add_employee(emp3)

# Calculating total payroll
total_payroll = payroll.calculate_total_payroll()

# Output the total payroll and employee details
print(f"Total Payroll: {total_payroll}")
for emp in payroll.employees:
    print(f"Employee: {emp.name}, Salary: {emp.salary}")
