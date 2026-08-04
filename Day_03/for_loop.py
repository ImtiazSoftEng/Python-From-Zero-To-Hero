#Example: Iterating Through a List
#A list of three AI Models
models=["Flab","ChatGPT","Gemini"]
#Access item of the list one by one

for model in models:
    print(model)
    print("---")
#Indentation in Loop
numbers=[1,2,3]
for num in numbers:
    print(num)
    print(f"Processing:{num}")
    print(f"Done with {num}")
#This statemnet is outside the loop
print("All done")

#For Loop with Python range()
for i in range(1,11):
    print(f"Displaying product: {i}")

#Example: Iterating Through a String
language="Python"
for x in language:
    print(x)

#The break Statement and the continue Statement
for num in range(1, 11):
    if num == 3:
        break
    print(num)
for num in range(1, 11):
    if num == 3:
        continue
    print(num)


#For Loop with else
stock=["Apple","Banana","Mango"]
order=input("Enter the fruit you want to order:")
for fruit in stock:
    if fruit==order:
        print(f"{order} is available. Adding to your cart.")
        break
else:
    print(f"Sorry, {order} is not available in stock.")

#Using for Loop Without Using Items
#interate from i=0 t0 3
for _ in range(4):
    print("Hello World")

#Example: Sum of Natural Numbers
#Initail value of sum is 0
total=0
#Iterate from 1 to 10
for i in range(1,11):
    total+=i #Adding i to total in easch iteration
    print(f"Total = {total}")


#Nested for loops
attributes=["Electric","Fast"]
cars=["Tesla","BMW","Mercedes"]

#outer loop iterates through the attributes list
for attribute in attributes:
    #inner loop iterates through the car list
    for car in cars:
        print(attribute,car)
    #This statement is outside the inner loop but inside the outer loop
    print("-----")
        
