'''
Task 5: Set Comprehension with Condition

Problem:
Given a list of numbers, use a set comprehension to create a set containing only the unique squares of the even numbers.
Print the resulting set.

Example Output:
{4, 16, 36, 64, 100}
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unique_squares = set(num**2 for num in numbers if num % 2 == 0)
print(unique_squares)
