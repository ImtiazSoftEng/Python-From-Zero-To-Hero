#Example 1: Python Function Arguments
def add_numbers(a,b):
    sum=a+b
    print("The sum is:", sum)
add_numbers(5, 10)

#Function Argument with Default Values
def add_numbers(a=7,b=8):
    sum=a+b
    print("The sum is:", sum)
#function call with two arguments
add_numbers(3, 10)
#function call with one argument
add_numbers(9)
#function call with no argument
add_numbers()


#Python Keyword Argument
def display_info(first_name, last_name):
    print("First Name:", first_name)
    print("Last Name:", last_name)
display_info(first_name="Imtiaz", last_name="Ali")

#Python Function With Arbitrary Arguments
#program to find sum of multiple numbers using arbitrary arguments
def find_sum(*numbers):
    result=0
    for num in numbers:
        result =result + num
    print("The sum is:", result)
#Function call with 3 arguments
find_sum(5, 10, 15)
#function call with 2  arguments
find_sum(7, 8)