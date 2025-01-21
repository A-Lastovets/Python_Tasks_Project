# Task 7: Dunder Method (__eq__)
'''
Problem:
1. Create a class Person with attributes name and age.
2. Override the __eq__() method to compare two Person objects based on their name and age.
3. Create two instances of Person and check if they are equal using the == operator.

Example Output:

Are they equal? True
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, value):
        if isinstance(value, Person):
            return self.name == value.name and self.age == value.age
        return False
    
one_person = Person("Anton", 32)
second_person = Person("Artem", 32)

print(f"Are they equal? {one_person == second_person}")  # False
