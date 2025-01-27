# Task 5: Method Overriding
'''
Problem:
1. In Task 4, override the __init__ method of ElectricCar to initialize both the attributes of Vehicle and ElectricCar (using super()).
2. Call the __init__ method from ElectricCar and print the values of all attributes.

Example Output:

Make: Tesla
Model: Model X
Year: 2023
Battery Size: 120
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

        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Battery Size: {self.battery_size}")

my_car = ElectricCar("Tesla", "Model S", 2022, 100)
