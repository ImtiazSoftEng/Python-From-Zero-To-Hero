#Example of a recursive function
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=3
print("The factorial of", n, "is", factorial(n))

#Python Program to Find Sum of Natural Numbers Using Recursion
print("Python Program to Find Sum of Natural Numbers Using Recursion")
def recursive_sum(n):
    if n<=1:
        return n
    else:
        return n + recursive_sum(n-1)
#Change this value for a different result
num=5
if num<0:
    print("Enter a positive number")
else:
    print("The sum is", recursive_sum(num))

#Python Program to Find the Fibonacci Sequence Using Recursion
print("Python Program to Find the Fibonacci Sequence Using Recursion")
def recursive_fibonacci(n):
    if n<=1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

#Change this value for a different result
nterms=10
if nterms<=0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recursive_fibonacci(i))