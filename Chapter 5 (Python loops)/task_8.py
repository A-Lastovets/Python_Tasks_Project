#Bonus Task 8: Simulate a Do-While Loop in Python
while True:
    number = int(input("Please enter a value between 1 and 10:\n"))
    if number not in range(1, 11):
        print("Invalid input. Try again.")
    else:
        print(f"Thank you! Your number is: {number}")
        break
