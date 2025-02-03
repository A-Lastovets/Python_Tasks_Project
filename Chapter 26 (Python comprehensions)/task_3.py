'''
Task 3: Dictionary Comprehension

Problem:
Create a dictionary comprehension where the keys are numbers from 1 to 5, and the values are their squares.
Print the resulting dictionary.

Example Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

numbers = range(1, 6)
squares = {x: x ** 2 for x in numbers}
print(squares)

