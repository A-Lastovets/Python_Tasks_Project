# Task 3: Instance Method
'''
Problem:
1. Modify the Rectangle class from Task 2 to include a method area() that calculates and returns the area of the rectangle (width * height).
2. Create an instance and call the area() method to get the rectangle's area.

Example Output:

Area: 50
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        result = self.width * self.height
        return result

instance = Rectangle(5, 10)
calculate = instance.area()

print(f"Width: {instance.width}\nHeight: {instance.height}\nArea: {calculate}")
