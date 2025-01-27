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
with open("./Chapter 24 (Python files management)/sample.txt", "w") as sample:
        sample.write("Hello world! This is a file.")
        
with open("./Chapter 24 (Python files management)/sample.txt", "r") as sample:
        data = sample.read()
        count = len(data.split())
        print(f"The file contains {count} words")
