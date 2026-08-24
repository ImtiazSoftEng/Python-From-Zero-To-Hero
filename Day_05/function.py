#Python Function
import math


def greet():
    print("Hello, welcome to the Python function tutorial!")

#Call the function
greet()
print("Outside the function")


#Python Function Arguments

def greet(name):
    print("Hello",name)
#Passing arguments to a function
greet("Imtiaz")

#Function to Add Two Numbers
def add_numbers(num1, num2):
    sum=num1 + num2
    print("The sum is:", sum)
#Fuction call with values
add_numbers(5, 10)

#The return Statement
def find_square(num):
    result = num * num
    return result   
#Function call
square=find_square(5)
print("The square is:", square)

#Python Library Function
import math
#sqr compute square root
square_root = math.sqrt(16)
print("The square root is:", square_root)
#power compute power
power = math.pow(2, 3)
print("The power is:", power)
