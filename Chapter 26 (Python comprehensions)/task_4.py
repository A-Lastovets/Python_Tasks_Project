'''
Task 4: Nested Comprehension

Problem:
Given a list of lists [[1, 2, 3], [4, 5], [6, 7]], use a nested list comprehension to flatten the list into a single list.
Print the flattened list.

Example Output:
[1, 2, 3, 4, 5, 6, 7]
'''

nested_list = [[1, 2, 3], [4, 5], [6, 7]]
print([number for numbers in nested_list for number in numbers])

'''
flat_list = []
for sublist in nested_list:    # take each sublist
    for num in sublist:        # iterate over sublist elements
        flat_list.append(num)  # add items to the new list
'''
