#Task 6: Modify Values in a Nested List
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_grid = []
for rows in grid:
    for index, item in enumerate(rows):
        if item % 2 == 0:
            rows[index] = item * 2
        else:
            rows[index] = 0
    new_grid.append(rows)

for new_rows in new_grid:
    print(new_rows)
