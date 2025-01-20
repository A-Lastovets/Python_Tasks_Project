#Task 2: Sum of Even Numbers in a List
my_list2 = [10, 20, 30, 40, 50, 11, 17, 22]
sum_even_numbers = 0
count_even_numbers = 0
for number in my_list2:
    if number % 2 == 0:
        sum_even_numbers += number
        count_even_numbers += 1
print(f"Sum of even numbers: {sum_even_numbers}\nNumber of even numbers: {count_even_numbers}")
