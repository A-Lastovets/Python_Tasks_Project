#Task 2: Password Validator
print('''
    Welcome to the Password Validation Tool!
    At least 8 characters long.
    Contains the word "Python".
    Does not contain any spaces.
    You have 3 attempts to check, then you will have to wait 15 minutes.
''')
i = 1
while i <= 3:
    password = input("Please enter your password: \n")
    if len(password) < 8:
        print("Password is invalid. Your password must contain at least 8 characters.\nPlease try again.\n")
        i += 1
        continue
    elif " " in password:
        print("Password is invalid. Your password must not contain spaces.\nPlease try again.\n")
        i += 1
        continue
    elif "Python" not in password:
        print("Password is invalid. Your password must contain the word Python.\nPlease try again.\n")
        i += 1
    else:
        print("Your password has been successfully verified and is ready for use.")
        break
else:
    print("You have exceeded the maximum number of attempts. Please wait 15 minutes before trying again.")
