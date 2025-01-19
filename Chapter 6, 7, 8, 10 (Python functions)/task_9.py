from functools import reduce
numbers = [1, 2, 3, 4]

running_total = []
add_to_total = lambda total, x: total + x

current_sum = 0
for num in numbers:
    current_sum = add_to_total(current_sum, num)
    running_total.append(current_sum)

print(running_total)
