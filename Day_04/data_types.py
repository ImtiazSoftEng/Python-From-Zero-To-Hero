num1 = 5
print(num1, 'is of type', type(num1))
num2 = 5.0
print(num2, 'is of type', type(num2))
num3 = 1 + 2j
print(num3, 'is complex number?', isinstance(1 + 2j, complex))

import random

print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']

# get random item from list1
print(random.choice(list1))

# Shuffle list1
random.shuffle(list1)

# Print the shuffled list1
print(list1)

# Print random element
print(random.random())