numbers = [2, 4, 6, 8, 10]

result = filter(lambda x: x <= 10, map(lambda x: x * 2, numbers))

print(list(result))
