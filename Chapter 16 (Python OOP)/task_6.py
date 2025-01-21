# Task 6: Dunder Method (__str__)
'''
Problem:
1. Create a class Book with attributes title, author, and year_published.
Override the __str__() method to return a string in the format:
"[Title] by [Author] (Published: [Year])"
2. Create an instance of Book and print it to see the custom string representation.

Example Output:

The Great Gatsby by F. Scott Fitzgerald (Published: 1925)
'''

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def __str__(self):
        return f"{self.title} by {self.author} (Published: {self.year_published})"
    
my_book = Book("The Great Gatsby", "Scott Fitzgerald", 1925)

print(my_book)
