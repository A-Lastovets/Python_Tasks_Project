# Chapter-6-7-8-10-Python-functions-

Task 1: String Manipulation Function
Problem:
Write a function format_name(name, title="Mr./Ms.") that takes two parameters:
name: a string representing a person's name.
title: a string with a default value of "Mr./Ms.".
The function should return a formatted string like: "Title: [title], Name: [name]".
The function should handle cases where name is a single name (like "Alice") or a full name (like "Alice Johnson"). If the name consists of more than one word, only the first word should be considered as the first name.
Example Output:

Title: Mr., Name: Alice
Title: Dr., Name: John

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Task 2: Function with Multiple Return Values
Problem:
Write a function min_max_avg(numbers) that takes a list of numbers as an argument.
The function should return three values:
The minimum value in the list.
The maximum value in the list.
The average of the numbers.
Ensure that the function handles edge cases where the list is empty or has only one number.
Example Output:

Min: 1, Max: 9, Average: 5.0

Edge Case Example (empty list):

Min: None, Max: None, Average: None

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Task 3: Recursive Function to Calculate Factorial
Problem:
Write a recursive function factorial(n) that calculates the factorial of a number n (i.e., n!).
The function should return 1 when n is 0 or 1, and recursively multiply the number by the factorial of n-1 for values greater than 1.
Call the function with different values for n (e.g., 5, 6, 7).
Example Output:

5! = 120
6! = 720
7! = 5040

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Task 4: Function with Keyword Arguments and Validation
Problem:
Write a function create_user(username, email, password, **kwargs) that:
Takes username, email, and password as required parameters.
Accepts any additional user details through **kwargs (e.g., age, address).
Validate that:
The username is at least 5 characters long.
The email contains @.
The password is at least 8 characters long.
Return a dictionary with the user details if validation is successful, or an error message if validation fails.
Example Output (valid input):

{'username': 'john123', 'email': 'john@example.com', 'password': 'securePass123', 'age': 30}
Example Output (invalid input):

"Error: Username must be at least 5 characters, email must contain '@', and password must be at least 8 characters long."

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Task 5: Calculate the Square of a Number
Problem:
Write a lambda function to calculate the square of a given number.
Expected Output Examples:
square(4)   # Output: 16
square(-3)  # Output: 9
square(0)   # Output: 0

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Task 6: Find the Larger of Two Numbers
Problem:
Write a lambda function to compare two numbers and return the larger one.
Expected Output Examples:
larger(10, 20)   # Output: 20
larger(-5, -10)  # Output: -5
larger(8, 8)     # Output: 8

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Task 7: Combine Names with Their Lengths (map and lambda)
Problem:
You are given a list of names. Use a lambda function and map to create a list of tuples, where each tuple contains a name and its length.
Input:
names = ["Alice", "Bob", "Charlie"]

Expected Output:
[("Alice", 5), ("Bob", 3), ("Charlie", 7)]

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Task 8: Extract Words Starting with a Specific Letter (filter and lambda)
Problem:
You are given a list of words and a target letter. Use a lambda function and filter to create a new list containing only the words that start with the given letter.
Input:
words = ["apple", "banana", "cherry", "apricot", "blueberry"]
target_letter = "a"

Expected Output:
["apple", "apricot"]

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Task 9: Create a Running Total (reduce and lambda)
Problem:
You are given a list of numbers. Use a lambda function and reduce to create a single list that represents a running total.
Input:
numbers = [1, 2, 3, 4]

Expected Output:
[1, 3, 6, 10]

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Task 10: Chain map and filter
Problem:
You are given a list of integers. Use lambda, map, and filter together to first double each number, then filter out the numbers that are greater than 10.
Input:
numbers = [2, 4, 6, 8, 10]

Expected Output:
[4, 8, 12]

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Task 11: Generate a Sequence of Squares
Problem:
Write a generator function called generate_squares that yields the squares of numbers starting from 1 up to a given number n (inclusive).
Use a for loop and the yield keyword to create the generator.
Test the generator by iterating through it and printing the values.
Example Input:
for square in generate_squares(5):
    print(square)

Expected Output:
1
4
9
16
25

Challenge:
Use the generator with the sum() function, e.g., sum(generate_squares(4)) should return 30.

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Task 12: Generate Infinite Prime Numbers
Problem Statement:
Write a generator function called generate_primes that yields prime numbers indefinitely.
Use a while loop to check for prime numbers.
Test the generator by printing the first 10 prime numbers using a for loop and enumerate.
Example Input:
primes = generate_primes()
for i, prime in enumerate(primes):
    if i >= 10:  # Stop after 10 primes
        break
    print(prime)

Expected Output:
2
3
5
7
11
13
17
19
23
29
