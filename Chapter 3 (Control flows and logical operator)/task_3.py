#Task 3: Logical Operator Practice
a = True
b = False
c = True
print(a and b) # two variables must be True. If one of them is False, then the entire line is False.
print(a or b) # If at least one value is true, then the entire string is true
print(not b) # The value of the variable changes to the opposite
print((a and c) or b) # First, we check the value in parentheses (is True), and then compare it with another value and get True.
print(a and (b or c)) # First, we check the value in parentheses (is True), and then compare it with another value and get True.
