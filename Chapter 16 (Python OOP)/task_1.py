# Basic Class and Object Creation
'''
Problem:
1. Create a class Car with the following attributes:
- make (string)
- model (string)
- year (integer)
2. Create an instance of the class with values for make, model, and year.
3. Print the instance's attributes.

Example Output:

Make: Toyota
Model: Camry
Year: 2020

'''
#----------------------------------------------------------------------
class Car:
    pass

my_car = Car()

my_car.make = "Toyota"
my_car.model = "Camry"
my_car.year = 2020

print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")
#-----------------------------------------------------------------------
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car("Toyota", "Camry", 2020)

print(f"Make: {my_car.make}\nModel: {my_car.model}\nYear: {my_car.year}")
