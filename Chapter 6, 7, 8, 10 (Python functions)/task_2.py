def min_max_avg(numbers):

    if len(numbers) == 0:
        return "Min: None, Max: None, Average: None"

    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return f"Min: {minimum}, Max: {maximum}, Average: {average}"

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 9, 1]
list3 = []

result1 = min_max_avg(list1)
result2 = min_max_avg(list2)
result3 = min_max_avg(list3)

print(f" {result1},\n {result2},\n {result3}")
