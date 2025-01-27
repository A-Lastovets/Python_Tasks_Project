'''
Task 1: Write User Input to a File
Problem:
Create a program that prompts the user to enter their name, age, and favorite color. Write this information to a file called user_info.txt in the following format:
Name: [User's Name]  
Age: [User's Age]  
Favorite Color: [User's Favorite Color]

Example Input:
Enter your name: Alice  
Enter your age: 25  
Enter your favorite color: Blue

Expected Output in user_info.txt:
Name: Alice  
Age: 25  
Favorite Color: Blue
'''

start = True
# user_data = ""
user_data = []

while start:
    while True:
        name = input("Please enter your name:\n").capitalize()
        if not name.isalpha():
            print("Error: Name should only contain letters. Please try again.")
        else:
            user_data.append(name)
            break
    while True:
        try:
            age = int(input("Please enter your age:\n"))
            if age <=0:
                print("Error: Age must be a positive number. Please try again.")
            else:
                user_data.append(age)
                break
        except ValueError:
            print("Error: Age must be an integer. Please try again.")
    while True:
        favorite_color = input("Please enter your favorite color:\n").capitalize()
        if not favorite_color.isalpha():
            print("Error: Favorite color should only contain letters. Please try again.")
        else:
            user_data.append(favorite_color)
            break

    with open("./Chapter 24 (Python files management)/user_info.txt", "w") as user_info:
        for data in user_data:
            data = name, age, favorite_color
        user_info.write(f"Name: {name}\nAge: {age}\nFavorite color: {favorite_color}")

    print(f"Thank you, {name}!\nYour file was created!")

    # with open("./Chapter 24 (Python files management)/user_info.txt", "w") as user_info:
    #     user_data = f"Name: {name}\nAge: {age}\nFavorite color: {favorite_color}"
    #     user_info.write(user_data)

    start = False
