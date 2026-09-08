def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(3):

    # print each value produced by generator
    print(value)

#Example 2: Python Generator Expression
#create the generator object
print("create the generator object")
square_generator =(i*i for i in range(5))

#iterate over the generator and print the values
for i in square_generator:
    print(i)
#Easy to Implement
class PowTwo:
    def __init__(self,max=0):
        self.n=0
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        if self.n>self.max:
            raise StopIteration
        result=2**self.n
        self.n+=1
        return result
numbers = PowTwo(3)
print("Using for loop to iterate through the iterator")
for i in numbers:
    print(i)
#Pipelining Generators
def fibonacci_numbers(nums):
    x,y=0,1
    for _ in range(nums):
        x,y=y,x+y
        yield x
        x,y=y,x+y

def square(nums):
    for i in nums:
        yield i**2

print(sum(square(fibonacci_numbers(10))))


