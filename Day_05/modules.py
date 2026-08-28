#python Modules addition
def add(a,b):
    result=a+b
    return result
print(add(5, 10))

#Import Python Standard Library Modules
#import standard library module

import math
#use math.pi to get the value of pi
print("The value of pi is:", math.pi)

#Python import with Renaming
import math as m
print("The value of pi is:", m.pi)


#Import all names
from math import *
print("The value of pi is:", pi)

#The dir() built-in function
print(dir(examples))
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add function', 'math', 'm', 'pi', 'sqrt', 'x        ']
import examples
print(examples.__doc__) 

a = 1
b = "hello"

import math

print(dir())

['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter']