#Example 1: Function to add 3 numbers
def adder(x,y,z):
    print("Sum of 3 numbers is: ", x+y+z)
adder(10,20,30)
#Example 2: Using *args to pass the variable length arguments to the function
print("\nExample 2: Using *args to pass the variable length arguments to the function")
def adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum of numbers is: ", sum)
adder(10,20,30)
adder(10,20,30,40,50)
adder(1,2,3,4,5,6,7,8,9,10)
#Example 3: Using **kwargs to pass the variable keyword arguments to the function 
print("\nExample 3: Using **kwargs to pass the variable keyword arguments to the function")
def intro(**data):
    print("\nData type of argument: ", type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))
intro(Firstname = "Imtiaz", Lastname = "Khan", Age = 22, Country = "Pakistan")
intro(Firstname = "John", Lastname = "Doe", Age = 30, Country = "USA", Profession = "Engineer")
intro(Firstname = "Alice", Lastname = "Smith", Age = 25, Country = "Canada", Hobby = "Reading", Language = "English")