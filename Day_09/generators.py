#Example: Python Generator
import numbers
from unittest import result


def my_generator(n):

    #initialize counter
    value=0

    #loop until the counter is than n
    while value<n:

        #produce the current value of the counter
        yield value

        #increment the counter

        value+=1

#iterate over the generator object produced by the my_generator function
for value in my_generator(3):
    #print each value produced by the generator
    print(value)  # Output: 0 1 2


    print(" Python Generator Expression")
    #Example 2: Python Generator Expression

#create the generator expression
squares_generator=(i*i for i in range(5))

#iterate over the generator and print the values
for i in squares_generator:
    print(i)  # Output: 0 1 4 9 16

print("Use of Python Generators")
    #Use of Python Generators
class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result
numbers = PowTwo(4)

for number in numbers:
    print(number)
print("Python Infinite Iterators")
def PowTwoGen(max=0):
    n=0
    while n<=max:
        yield 2**n
        n+=1
for value in PowTwoGen(10):
    print(value)

#Pipelining Generators
print("Pipelining Generators")
def fibonacci_numbers(nums):
    x,y=0,1
    for _ in range(nums):
        x,y=y,x+y
        yield x
def square(nums):
    for num in nums:
        yield num**2
print(sum(square(fibonacci_numbers(10))))  # Output: 4895
