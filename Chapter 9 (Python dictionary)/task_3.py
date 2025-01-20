#Task 3: Dictionary with Nested Data
books = {
    "book1": {"title": "1984", "author": "George Orwell", "year": 1949},
    "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
}
for items in books.values():
    print(f"Book: {items['title']}, Author: {items['author']}, Year: {items['year']}")
