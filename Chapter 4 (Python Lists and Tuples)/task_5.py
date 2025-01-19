#Task 5: Swap Values Using Tuples
number1 = float(input("Enter first value:\n"))
number2 = float(input("Enter second value:\n"))
print(f"Before Swap: First Value = {number1}, Second Value = {number2}\n")
### python swap method
number1, number2 = number2, number1
print("Python swap method:")
print(f"After Swap: First Value = {number1}, Second Value = {number2}\n")
### arithmetic method
number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2
print("Arithmetic method:")
print(f"After Swap: First Value = {number1}, Second Value = {number2}")
