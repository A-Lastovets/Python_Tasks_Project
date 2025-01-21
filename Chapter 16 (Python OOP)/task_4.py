# Task 4: Inheritance
'''
Problem:
1. Create a class Vehicle with the attributes make, model, and year.
2. Create a subclass ElectricCar that inherits from Vehicle and adds the attribute battery_size (integer).
3. Create an instance of ElectricCar, and print the attributes from both Vehicle and ElectricCar.

Example Output:

Make: Tesla
Model: Model S
Year: 2022
Battery Size: 100
'''
class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
    
class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_size: int):
        super().__init__(make, model, year)
        self.battery_size = battery_size

my_car = ElectricCar("Tesla", "Model S", 2022, 100)

print(f"Make: {my_car.make}\nModel: {my_car.model}\nYear: {my_car.year}\nBattery Size: {my_car.battery_size}")
