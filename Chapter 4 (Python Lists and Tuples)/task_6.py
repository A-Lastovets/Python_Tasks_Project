#Task 6: Unpack Tuples with Mixed Data
data = (42, 3.14, "Hello", True)
for i in data:
    if isinstance(i, int):
        print(f"Integer: {i} (Type: {type(i)})")
    elif isinstance(i, float):
        print(f"Float: {i} (Type: {type(i)})")
    elif isinstance(i, str):
        print(f"String: {i} (Type: {type(i)})")
    elif isinstance(i, bool):
        print(f"Boolean: {i} (Type: {type(i)})")
