'''
Task 3: Basic Decorator
Problem:
Create a decorator uppercase_decorator that modifies the behavior of a function so that it always returns the result in uppercase.
Apply uppercase_decorator to a function greet() that returns "Hello".

Example Output:
HELLO

'''
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "Hello"

print(greet())
