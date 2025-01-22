# Task 8: Class Method and Static Method
'''
Problem:
1. Create a class Employee with the following:
name (string)
salary (float)
2. Add a class method from_string() that creates an Employee instance from a string in the format "name, salary".
3. Add a static method is_high_salary() that checks if an employee's salary is above 100,000.
4. Demonstrate creating an employee from a string and checking their salary.

Example Output:

Employee name: Alice, Salary: 120000
Is the salary high? True
'''

class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_info: str):
        name, salary = emp_info.split(", ")
        return cls(name, float(salary))
    
    @staticmethod
    def is_high_salary(salary: float):
        return salary > 100000
    
emp_info = "Alice, 120000"
employee = Employee.from_string(emp_info)

print(f"Employee Name: {employee.name}, Salary: {employee.salary}")

print("Is the salary high?", Employee.is_high_salary(employee.salary))
