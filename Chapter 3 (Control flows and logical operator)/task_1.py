#Task 1: Number Range Checker
number = int(input("Please enter a number: \n"))
if number < 10:
    print("Your number is less than 10")
elif 10 <= number <= 20:
    print("Your number between 10 and 20")
else:
    print("Your number greater than 20")
