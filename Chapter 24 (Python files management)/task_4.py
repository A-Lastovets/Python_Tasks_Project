'''
Task 4: Reading and Writing a CSV File
Problem:
Create a program that does the following:
Write a CSV file named students.csv with columns: Name, Age, and Grade.
Populate it with at least 3 rows of sample data (e.g., "Alice", 25, "A").
Read the file and calculate the average age of the students.
Display the content of the CSV file along with the average age.
Example Input (Data in students.csv):
Name,Age,Grade
Alice,25,A
Bob,22,B
Charlie,24,A

Expected Output:
File content:
Name: Alice, Age: 25, Grade: A
Name: Bob, Age: 22, Grade: B
Name: Charlie, Age: 24, Grade: A

Average Age: 23.67
'''
import csv

students = [
    {"Name": "Alice", "Age": 25, "Grade": "A"},
    {"Name": "Bob", "Age": 22, "Grade": "B"},
    {"Name": "Charlie", "Age": 24, "Grade": "A"},
]

file_name = "./Chapter 24 (Python files management)/students.csv"

with open(file_name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Grade"])
    writer.writeheader()
    writer.writerows(students)

with open(file_name, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    student_data = list(reader)
    print("File content:")

    for student in student_data:
        print(f"Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}")
    
    ages = [int(student["Age"]) for student in student_data]

if ages:
    average_age = sum(ages) / len(ages)
    print(f"\nAverage Age: {round(average_age, 2)}")
else:
    print("No data available")
