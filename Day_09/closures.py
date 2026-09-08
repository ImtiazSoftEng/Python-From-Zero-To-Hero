#Nested function in Python

def greet(name):
    #inner function
    def display_name():
        print("Hi", name)
    #call the inner function
    display_name()
#call the outer function
greet("Imtiaz")  

#Python Closures
print("Python Closures")
def greet():
    #variable defined outside the inner function
    name = "Imtiaz"
    #returning the inner function
    return lambda:"Hi " + name
#call the outer function
message = greet()
#call the inner function
print(message())  

#Example: Print Odd Numbers using Python Closure
print(" Print Odd Numbers using Python Closure")
def calculate_odd_numbers():
    num = 1
    def inner_function():
        nonlocal num
        num +=2
        return num
    return inner_function
#call the outer function
odd=calculate_odd_numbers()
#call the inner function
print(odd())  # Output: 3
print(odd())
print(odd())
#call the outer function again to create a new closure
odd2=calculate_odd_numbers()
print(odd2())  # Output: 3
print("##############################################")
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))