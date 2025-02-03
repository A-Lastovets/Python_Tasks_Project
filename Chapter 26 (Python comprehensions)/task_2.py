'''
Task 2: List Comprehension with Condition

Problem:
Given a list of numbers from 1 to 10, use a list comprehension to create a new list containing only the even numbers.
Print the new list.

Example Output:
[2, 4, 6, 8, 10]
'''
list1 = [x for x in range(1, 11)]
print(list1)
print(id(list1))

list2 = [x for x in list1 if x % 2 == 0]
print(list2)
print(id(list2))
