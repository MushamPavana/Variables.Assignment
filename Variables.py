###create an employee class and add details of employee  using three deferent variables and access that variables in all possible ways.

class Employee:
    total_employees = 0

    def __init__(self, name, salary): # Instance Variable
        self.name = name
        self.salary = salary
        Employee.total_employees += 1 # static variable 

    def display_employee_details(self): # local variable
        department = "Python"
        print(f"Employee Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {department}") # local variable

    def display_total_employees(self):
        print(f"Total Employees: {Employee.total_employees}") # static variable

employee1 = Employee("Ashish", 100000)
employee2 = Employee("Jane Smith", 600000)

 # Instance variable
print("Employee 1 Name:", employee1.name)
print("Employee 1 Salary:", employee1.salary)
print("Employee 2 Name:", employee2.name)
print("Employee 2 Salary:", employee2.salary)

print("Total Employees:", Employee.total_employees) # static variable

employee1.display_employee_details() # local variable

