def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
list_values = [5, 6, 7]
for i in list_values:
    print(f" {i}! = {factorial(i)}")
    