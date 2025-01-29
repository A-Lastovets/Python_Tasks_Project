'''
Task 3: Append and Display File Content
Problem:
Create a program that appends a new line to a file called log.txt with the current date and time. Then, read and display the entire file content.
If the file doesn't exist, create it.
Append the current date and time in the format: YYYY-MM-DD HH:MM:SS.
Print the entire content of the file after the new line is added.
Example Execution:
On the first run:
log.txt created.
Appended: 2024-12-26 15:00:00

On the second run:
Appended: 2024-12-26 15:01:00

File content:
2024-12-26 15:00:00
2024-12-26 15:01:00

'''
from datetime import datetime
import os

def append_data():
    file_name = "./Chapter 24 (Python files management)/log.txt"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(file_name)

    try:
        with open(file_name, "a") as file:
            file.write(current_time + "\n")
            if not file_exists:
                print("log.txt created.")
            print(f"Appended: {current_time}")

        with open(file_name, "r") as file:
            print("File content:")
            print(file.read())
    except Exception as e:
        print(f"An error occurred: {e}")

append_data()
