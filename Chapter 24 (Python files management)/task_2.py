'''
Task 2: Count Words in a File
Problem Statement:
Write a program that reads the content of a text file sample.txt, counts the number of words in it, and displays the total word count.
Create a text file sample.txt with any content (e.g., "Hello world! This is a file.").
Open the file in read mode, count the words, and print the result.
Example Input in sample.txt:
Hello world! This is a file.

Expected Output:
The file contains 6 words.
'''
# Easy level
# with open("./Chapter 24 (Python files management)/sample.txt", "w") as sample:
#         sample.write("Hello world! This is a file.")
        
# with open("./Chapter 24 (Python files management)/sample.txt", "r") as sample:
#         data = sample.read()
#         count = len(data.split())
#         print(f"The file contains {count} words")

#Next level
def input_text():
    while True:
        user_input = input("Please enter your text:\n").strip()
        if not user_input:
            print("Error: Text cannot be empty. Please try again.")
        else:
            with open("./Chapter 24 (Python files management)/sample2.txt", "w") as sample:
                sample.write(user_input)
            print("Your text has been saved to 'sample2.txt'.")
            break

def check_text():
    try:
        with open("./Chapter 24 (Python files management)/sample2.txt", "r") as sample:
                text = sample.read()
        word_count = len(text.split())
        print(f"The number of words in the file is: {word_count}")
    except FileNotFoundError:
         print("Error: File 'sample2.txt' not found. Please make sure to write the text first.")

input_text()
check_text()
