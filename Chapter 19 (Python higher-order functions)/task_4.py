'''
Task 4: Decorator with Arguments
Problem:
Create a decorator multiply_decorator that takes a parameter factor and multiplies the return value of a function by that factor.
Apply multiply_decorator to a function get_price() that returns a price (e.g., 50).
Call the decorated function with a factor of 2 and print the result.
Example Output:

100

'''
def multiply_decorator(factor):
    def decorator(func):
        def multiply():
            value = func()
            return value * factor
        return multiply
    return decorator

@multiply_decorator(2)
def get_price():
    return 50

print(get_price())
