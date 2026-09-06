#Python Lambda/Anonymous Function
lambda: print("Hello World")

#Example: Python Lambda Function
#declare a lambda function
greet = lambda : print("Hello, World!")
#call the lambda function
greet()
#Python lambda Function with an Argument
#lambda that accepts one argument
greet_user = lambda name : print("Hey",name)
#lambda call
greet_user("Imtiaz Ali")



#How to use the lambda function with filter()?
#program to filter out only the even numbers from a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)

#How to use the lambda function with map()?
# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)

# Output: [2, 10, 8, 12, 16, 22, 6, 24]