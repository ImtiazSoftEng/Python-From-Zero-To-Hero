task=input("Task:")
while task!="q":
    print("Task done!")
    task=input("Task:")
#This statement is outside the loop
print("All tasks completed! ")

#Example: Print Numbers from 1 to n
n=10
i=1
while i<=n:
    print(i)
    i+=1
#Example: Sum Numbers Until User Enters Zero
total=0
n=float(input("Enter a number (0 to quit):"))

while n!=0.0:
    total+=n
    n=float(input("Enter a number (0 to quit):"))
print(f"Sum:{total}")

#Break and Continue Statements
while True:
    number=int(input("Enter a Number:"))
    if number==0:
        break   
    print(f"You entered: {number}")
#The continue Statement
i=0
while i<10:
    i+=1
    #skip odd numbers
    if i%2!=0:
        continue
    print(i)


#While Loop with Else Clause
attempts=3
while attempts>0:
    pin=input("Enter your pin:")
    if pin=="1212":
        print("Access granted")
        break

    attempts-=1
    print(f"Incorrect pin. You have {attempts} attempts left.")
else:
    print("Too many failed attempts. Access denied.")