'''
Task 1: Basic Higher-Order Function
Problem:
Create a higher-order function apply_function(func, value) that:
Takes a function func and a value value as arguments.
Applies the function func to the value value and returns the result.
Test apply_function by passing in a simple function like lambda x: x * 3 and a value like 4.

Example Output:
12
'''

def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x * 3, 4)
print(result)
