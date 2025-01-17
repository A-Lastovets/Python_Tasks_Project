names = ["Alice", "Bob", "Charlie"]

result = list(map(lambda name: (name, len(name)), names))

print(result)
