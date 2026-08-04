#Example: Python if Statement
age=int(input("Enter your age:"))
#check if age is greater than or equal to 18
if age>=18:
     print("Grant access to the website")
print("Program completed")

#Example: Python if…else Statement

age=int(input("Enter your age:"))
if age>=18:
    print("Grant access to the website")
else:
    print("Deny access to the website")

#Example: Authenticate User Logic Using if...else
#username and password stored in database
username_db="admin"
password_db="admin123"

#Username and password entered by user
username=input("Enter your username:")
password=input("Enter your password:")

#check if username & password in database matches with user input
if(username==username_db) and (password==password_db):
    print("Login successful")
else:
    print("Login failed. Invalid username or password")

#Example: Python if…elif…else Statement
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif age >= 18:
    print("Grant access.")
else:
    print("Deny access.")
#Nested if Statements
age = int(input("Enter your age: "))

# Condition to check if age is less than 18
if age < 18:

    # If age is less than 18, condition to check if it's negative
    if age < 0:
        print("Invalid age.")
    else:
        print("Deny access.")
else:
    print("Grant access.")
#Example: Largest of Three Numbers
#Taking three numbers as input from the user
n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))    
n3=float(input("Enter third number: "))
if n1>=n2 and n1>=n3:
    largest=n1
elif n2>=n1 and n2>=n3:
    largest=n2  
else:
    largest=n3  
print("The largest number is:",largest)