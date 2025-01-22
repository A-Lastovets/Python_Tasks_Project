# Bonus Task 9: Create a Custom Iterator for a Fibonacci Sequence
'''
Problem:
Create a custom iterator class called FibonacciIterator that generates numbers in the Fibonacci sequence. The iterator should take an input n, which specifies the maximum number of Fibonacci numbers to generate.
1. Implement the __iter__ and __next__ methods to make the class an iterator.
2. Use the iterator to generate and print the Fibonacci sequence up to n terms.

Example Input:
fib = FibonacciIterator(5)
for num in fib:
    print(num)

Expected Output:
0
1
1
2
3

Challenge:
1. Extend the iterator to raise a StopIteration exception when the maximum n is reached.
2. Use the iterator with the list() function, e.g., list(FibonacciIterator(7)) should output [0, 1, 1, 2, 3, 5, 8]

'''
class FibonacciIterator:
    def __init__(self, max_value=None):
        self.max_value = max_value
        self.a, self.b = 0, 1 # start numbers for iteration
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.max_value is not None and self.a >= self.max_value:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result
    
n = int(input("Please enter 'n': "))

fib = FibonacciIterator(n)
print("Expected Output:")
for num in fib:
    print(num)

fib_list = list(FibonacciIterator(n))

print(f"List Output: {fib_list}")
