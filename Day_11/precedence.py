#Precedence and Associativity of Operators in Python
a = 20
b = 10
c = a + b * 2
print(c)

# Precedence of or & and
meal = "fruit"

money = 0

if meal == "fruit" or meal == "sandwich" and money >= 2:
    print("Lunch being delivered")
else:
    print("Can't deliver lunch")

    # Precedence of or & and
meal = "fruit"

money = 0

if (meal == "fruit" or meal == "sandwich") and money >= 2:
    print("Lunch being delivered")
else:
    print("Can't deliver lunch")

    #Associativity of Python Operators
# Left-right associativity
# Output: 3
print(5 * 2 // 3)

# Shows left-right associativity
# Output: 0
print(5 * (2 // 3))
# Shows the right-left associativity of **
# Output: 512, Since 2**(3**2) = 2**9
print(2 ** 3 ** 2)

# If 2 needs to be exponated fisrt, need to use ()
# Output: 64
print((2 ** 3) ** 2)