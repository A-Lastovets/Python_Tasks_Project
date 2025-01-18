def generate_squares(n):
    for number in range(1, n + 1):
        yield number ** 2

for square in generate_squares(5):
    print(square)

result = sum(generate_squares(4))
print(f"Sum of squares up to 4: {result}")
