#assign value to site_name variable
from doctest import Example


site_name = 'programiz.pro'
print(site_name)

#assign a new value to site_name variable
site_name = 'apple.com'
print(site_name)

#Assign the multiple values to multiple variables in a single line
a,b,c = 5,10, 'hello'
print(a) # print 5
print(b) # print 10
print(c) # print 'hello'
#Assign the same value to multiple variables in a single line
x = y = z = 100
print(x) # print 100
print(y) # print 100
print(z) # print 100

#convert lower data type to higher data type is called type casting of implicit type casting
interger_number = 10
float_number = 10.5
new_number = interger_number + float_number
#display new value and resulting data type
print("value:",new_number)
print("data type:",type(new_number))

#convert higher data type to lower data type is called type casting of explicit type casting
num_string = "100"
num_interger=23
print("data type of num_string before type casting:",type(num_string))
# Explicit type conversion
num_string = int(num_string)
print("data type of num_string after type casting:",type(num_string))
num_sum = num_string + num_interger
print("sum:",num_sum)
print("data type of num_sum:",type(num_sum))

#Python Basic Input/Output
print('Python is powerful ')
print('Good morning!')
print("It is raining today")

#print with end whitespace
print("Good morning!", end=' ')
print("It is raining today")

#print with separator
print('New Year',2026,'See you soon', sep='-')


#Example: Print Python Variables and Literals
number = 10
name = 'John'
#print literals and variables
print(5)
print(number)
print(name)

#Example: Print Concatenated Strings
print('Hello' + ' ' + 'World!') #concatenated string

#Output formatting
x = 10
y = 20
print('The value of x is {} and y is {}'.format(x,y)) #using format() method

#Example: Python User Input
#using input() to take user input
num=input("Enter a number: ")
print("You entered:", num)
print("Data type of input is:", type(num)) 

#Python Operators
#1. Python Arithmetic Operators
sub=10-5 #5
#Example 1: Arithmetic Operators in Python
a=7
b=2
#addition
print('sum:',a+b) 
#subtraction
print('difference:',a-b)
#multiplication
print('product:',a*b)
#division
print('quotient:',a/b)
#floor division
print('floor division:',a//b)
#modulus
print('modulus:',a%b)
# a to the power of b
print('exponent:',a**b)
#Example 2: Assignment Operators
#assign 10 to variable a
a=10
#assign 5 to variable b
b=5
#assign to the sum of a and b to a
a+=b #a=a+b
print(a)
#output: 15

#Example 3: Comparison Operators
a=5
b=2
#equal to operator
print('a==b:',a==b) #
#not equal to operator
print('a!=b:',a!=b) 
#greater than operator
print('a>b:',a>b)
#less than operator
print('a<b:',a<b)
#greater than or equal to operator
print('a>=b:',a>=b)
#less than or equal to operator
print('a<=b:',a<=b)

#Example 4: Logical Operators
#logical AND operator
print(True and True) #True
print(True and False) #False
#logical OR operator
print(True or False) #True
print(False or False) #False
#logical NOT operator
print(not True) #False
print(not False) #True
#Example 4: Identity operators in Python
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False

print(x2 is y2)  # prints True

print(x3 is y3)  # prints False
#Example 5: Membership operators in Python
message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True

# check if 'hello' is present in message string
print('hello' not in message)  # prints True

# check if '1' key is present in dict1
print(1 in dict1)  # prints True

# check if 'a' key is present in dict1
print('a' in dict1)  # prints False