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