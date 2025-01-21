# Constructor Method (__init__)
'''
Problem:
1. Create a class Rectangle with the following attributes:
width (integer)
height (integer)
2. Use the __init__ method to initialize the attributes when an object is created.
3. Create an instance of Rectangle and print its width and height.

Example Output:

Width: 5
Height: 10

'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
instance = Rectangle(5, 10)
print(f"Width: {instance.width}\nHeight: {instance.height}")
