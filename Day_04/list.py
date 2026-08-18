cart = ['apple', 'banana', 'orange']
print(cart)
# A list of mixed data types
my_list = [1, 'hello', 3.14, True]
print(my_list)

#Empty list
my_list = []
print(my_list)
vowels="aeiou"
#Convert a string to a list
vowel_list = list(vowels)   
print(vowel_list)
#Accessing List Items
languages = ['Python', 'Java', 'C++', 'JavaScript']
#Accessing the first item
print(f"Language[0]: {languages[0]}")
#Accessing the Second item
print(f"Language[2]: {languages[2]}")
#Negative Indexing
languages = ["Python", "Swift", "C++"]

# Access the last item
print('languages[-1] =', languages[-1])

# Access the third last item
print('languages[-3] =', languages[-3]) 

#Adding and updating list items
cart=['T-shirt', 'Jeans', 'Sneakers']
print(cart) 
#Update the second item to 'Shoes'
cart[1] = 'Shoes'
print(cart)
cart.append('Hat')
print(cart)
cart = ["T-shirt", "Lamp", "Pen"]
fav_items = ["Headphones", "Phone"]

# Add all the items from fav_items to cart
cart.extend(fav_items)

print(cart)    # ['T-shirt', 'Lamp', 'Pen', 'Headphones', 'Phone']
#Remove Items From a List
cart.remove('Lamp')
print(cart)    # ['T-shirt', 'Pen', 'Headphones', 'Phone']  
#Remove the last item from the list
cart.pop()
print(cart)    # ['T-shirt', 'Pen', 'Headphones']
#clear the list
cart.clear()
print(cart)    # []
#Copying a List
favorite_fruits = ['apple', 'banana', 'cherry']
cart = favorite_fruits
#Add an item to the cart
cart.append('orange')
print(f"favorite_fruits= {favorite_fruits}")
print(f"cart= {cart}")