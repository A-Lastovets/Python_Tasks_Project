#Task 6: Nested Ternary for Temperature Description
temperature = float(input("Please enter a temperature:\n"))
if temperature < 15:
    grade = "Cold"
elif 15 <= temperature <= 30:
    grade = "Warm"
else:
    grade = "Hot"
print(grade)
