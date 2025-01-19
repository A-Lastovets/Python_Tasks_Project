#Task 1: Loop through a List and Modify Elements
my_list = [3, 7, 1, 9, 4]
new_list = []
for index, number in enumerate(my_list):
    new_number = number * 3
    new_list.append(new_number)
    if new_number > 15:
        new_list[index] = "Too large"
print(new_list)
