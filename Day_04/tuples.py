# Empty tuple
numbers = ()
print(numbers)

# Tuple having data of the same type
odd_nums = (1, 3, 5, 7)
print(odd_nums)

# Tuple having mixed data types
details = (111, "2026-08-18", "Pakistan")
print(details)
vowels = "aeiou"

# Convert a string to a tuple
vowels_tuple = tuple(vowels)
print(vowels_tuple)
id,date,location = (121,"2026-08-18","Pakistan")
print(id)
print(date)
print(location)

#Accessing value to Tuple
languages =('Python','Swift','C++')

#Access the first item
print(languages[0])
#Access the third item 
print(languages[2])

#Negative Indexing 
languages =("Python","Swift","C++")
#Access the last item
print(f"languages[-1] = {languages[-1]}")

#Access the third last item 
print(f"languages[-3] = {languages[-3]}")

#Tuples are Immutable so not possible 
cars = ("BMW", "Tesla", "Ford", "Toyota")

# Trying to change the first item
cars[0] = "Nissan"    # Error
       
print(cars)
#Deleting a Tuple
cars = ("BMW", "Tesla", "Ford", "Toyota")

# Deleting the cars tuple
del cars

print(cars)


#Python Tuple Length

cars = ("BMW", "Tesla", "Ford", "Toyota")
print(f"Total Items = {len(cars)}") 
       
# Output: Total Items = 4

#Tuple Membership Test
cars = ("BMW", "Tesla", "Ford", "Toyota")

result = "BYD" in cars
print(result)    # False

result = "Ford" in cars
print(result)    # True

#Iterating Through a Tuple
cars = ("BMW", "Tesla", "Ford", "Toyota")

for car in cars:
    print(car)