#Task 2: Random Password Generator
characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
password = random.choices(characters, k=8)
print("Generated password: ", end="")
for i in password:
    print(i, end="")
print("\n")
