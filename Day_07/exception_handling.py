#Python Exception Handling
#Python try...except Block
try:
    #code that may cause exception
    pass
except:
    #code that runs if exception occurs
    pass 
#Example: Exception Handling Using try...except
try:
    numerator=10
    denominator=0
    result=numerator/denominator
    print(result)
except:
    print("Error:Denominator cannot be zero")

#Catching Specific Exceptions in Python
try:
    even_numbers=[2,4,6,8]
    print(even_numbers[5])
except IndexError:
    print("Error: Index out of range")
#Python try with else clause
#Program to print the reciprocal of even numbers
try:
    num = int(input("Enter a number:"))
    assert num % 2 == 0
except:
    print("Not an even number")
else:
    reciprocal = 1 / num
    print(reciprocal)
#Python try...finally
try:
    numerator=10
    denominator=0
    result=numerator/denominator
    print(result)
except:
    print("Error:Denominator cannot be zero")
finally:
    print("Execution completed")