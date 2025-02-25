'''
Task 5: Chaining Multiple Decorators
Problem:
Create two decorators:
double_decorator: Doubles the result of the function it decorates.
add_five_decorator: Adds 5 to the result of the function it decorates.
Apply both decorators to a function get_value() that returns 10.
Call the decorated function and print the result.

Example Output:
25

'''
def double_decorator(func):
    def double():
        value = func()
        return value * 2
    return double

def add_five_decorator(func):
    def add():
        value = func()
        return value + 5
    return add

@add_five_decorator
@double_decorator
def get_value():
    return 10

print(get_value())
