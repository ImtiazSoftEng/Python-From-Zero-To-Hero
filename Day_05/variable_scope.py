#Python Local Variables
def greet():
    message='Hello'
    print('local', message)
greet()
#try to access message outside the function
#outside greet() function
#print(message)


#Python Global Variables
#declare a global variable
message='Hello'
def greet():
    #declare a local variable
    message='Hello'
    print('local', message)
greet()
print('global', message)


#Python Nonlocal Variables
#outside function
def outer():
    message='local'
    #nested function
    def inner():
        nonlocal message
        message='nonlocal'
        print('inner:', message)

    inner()
    print('outer:', message)    

outer()