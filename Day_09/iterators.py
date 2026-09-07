#Iterating Through an Iterator
#define a list
my_list=[1,2,3,4,5]

# create an iterator from the list
iterator=iter(my_list)
#get the first element from the iterator
print(next(iterator))  # Output: 1
#get the second element from the iterator
print(next(iterator))  # Output: 2
#get the third element from the iterator
print(next(iterator))  # Output: 3
#get the fourth element from the iterator
print(next(iterator))  # Output: 4
#get the fifth element from the iterator
print(next(iterator))  # Output: 5
print("Using for loop:")
#using for loop
#define a list
my_list=[1,2,3,4,5]
for element in my_list:
    print(element)  # Output: 1 2 3 4 5
print("Using for loop with iterator:")
#Working of for loop for Iterators
#create a list of integer numbers
my_list=[1,2,3,4,5]
# create an iterator from the list
iterator=iter(my_list)
#using for loop to iterate through the iterator
for item in iterator:
    print(item)  # Output: 1 2 3 4 5

print(" Practice Building Custom Iterators:")
#Building Custom Iterators
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self,max=0):
         self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<=self.max:
            result=2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration
#create an object of the PowTwo class
numbers=PowTwo(3)
#create an iterator from the object
i=iter(numbers)
#Uising next to get the next interator element
print(next(i))  # Output: 1
print(next(i))  # Output: 2
print(next(i))  # Output: 4
print(next(i))  # Output: 8
#print(next(i))  # Output: StopIteration

for i in PowTwo(3):
    print(i)  # Output: 1 2 4 8 16 32
print("Python Infinite Iterators")
#Python Infinite Iterators
from itertools import count
#create an infinite interator that starts at 1 and increments by 1
infinite_iterator=count(1)
#print tje first 5 elements of the infinite iterator
for i in range(5):
    print(next(infinite_iterator))  # Output: 1 2 3 4 5
