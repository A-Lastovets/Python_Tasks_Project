def format_name(name, title="Mr./Ms."):
    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Ms."
    else:
        return "Wrong input, please try again..."

    name_format = name.split()
    first_name = name_format[0]

    formatted_string = f"Title: {title}, Name: {first_name}"
    return formatted_string

while True:
    name_input = input("What is your name?\n")
    gender = input("What is your gender? (male/female)\n").strip().lower()

    result = format_name(name_input, gender)
    
    if "Wrong input" in result:
        print(result)
    else:
        print(result)
        break
