#Nested Function
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(10)
print(result)  

#Pass Function as Argument
def add(x, y):
    return x + y
def calculate(func, a, b):
    return func(a, b)

result = calculate(add, 5, 6)
print(result)  
#Return a Function as a Value
def greeting(name):
    def hello():
        return "Hello, " + name + "!"

    return hello
greet = greeting("Alice")
print(greet())


def make_pretty(func):
    #define the inner function
    def inner():
        print("I got decorated")
        func()
    return inner
def ordinary():
    print("I am ordinary")
#decorate the ordinary function
decorated_func = make_pretty(ordinary)
#call the decorated function
decorated_func()  # Output: I got decorated \n I am ordinary
#@ Symbol With Decorator
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")
ordinary()  # Output: I got decorated \n I am ordinary

#Decorating Functions with Parameters
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)

#Chaining Decorators in Python

def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")