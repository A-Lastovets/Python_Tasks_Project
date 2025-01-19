#Task 7: Modify a List Using a While Loop
numbers = [-3, 5, 0, -1, 8, 2]
count = 0
while count < len(numbers):
    if numbers[count] < 0:
        numbers[count] = 0
    elif numbers[count] > 0:
        numbers[count] *= 2
    count += 1
print(numbers) 
