#Python List Comprehension
numbers = [1, 2, 3, 4]
#list comprehension to create new list
doubled_numbers=[num*2 for num in numbers]
print(doubled_numbers)  # Output: [2, 4, 6, 8]

#for Loop vs. List Comprehension
#For Loop
numbers=[1,2,3,4,5]
squared_numbers=[]

#for loop to square each element in the list
for num in numbers:
    squared_numbers.append(num*num)
    print(squared_numbers) 
#List Comprehension
numbers=[1,2,3,4,5]
#create a new list using list comprehension
squared_numbers=[num*num for num in numbers]
print(squared_numbers) 

#Conditionals in List Comprehension
#filtering even numbers from a list
even_numbers=[num for num in range(10) if num%2==0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]


#Example: List Comprehension with String
word="Python"
vowel="aeiou"
#find vowel in the strin "Python" using list comprehension
result=[char for char in word if char in vowel]
print(result)  # Output: ['o']