#Python break and continue


#Example: break in for Loop
number=int(input("Enter a number:"))
for i in range(1, 6):

     #Terminate the loop if i equals number
     if i==number:
            break
     print(i)
#Example: break in while Loop
while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    print(f"You entered {number}")
#Example: continue in for Loop
for i in range(1, 11):

    # Condition to check if a number is even
    if i % 2 == 0:
        continue
    print(i)
#Example: Sum of Only Positive Numbers
total = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    # Skip negative numbers
    if number < 0:
        continue

    # End the loop if the user enters 0
    if number == 0:
        break

    total += number

print(f"Sum of positive numbers: {total}")

#Loop with else Clause
stock = ['Laptop', 'Keyboard', 'Mouse']

order = input("Enter the product you want to buy: ")

for product in stock:
    if product == order:
        print(f"{order} is available. Adding to cart.")
        break
else:
    print(f"Sorry, {order} is out of stock.")