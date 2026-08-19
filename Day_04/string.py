#Python Strings
#Python Multiline Strings
#Multiline string
message = """ To avoid pain, they avoid pleasure. To avoid death, they avoid life.
 To avoid life, they avoid love. To avoid love, they avoid pain. To avoid pain, they avoid pleasure. To avoid death, they avoid life"""
print(message)

#Accessing String Characters
model='ChatGPT'
#Access the first character
print(model[0])
#Access the fifth character
print(model[4])
#Access the last character
print(model[-1])
#Access the second last character
print(model[-2])
#Access characters from index 0 to 3
print(model[0:4])

#Srting are Immutable
"""model='ChatGPT'
model[0]='B'  #Error
print(model)
"""
#Modifying a String is possible by creating a new string
model='ChatGPT'
version='4'
model=model+ " "+version
print(model)

#Python String Methods
text="ChatGPT is a Great AI model"
#Replace "ChatGPT" with "Claude"
print(text)
new_text=text.replace("ChatGPT","Claude")
print(new_text)
#String Membership Test
print('Chat' in 'ChatGPT')        # True
print('Claude' not in 'ChatGPT')  # True
#Iterate Through a String
model = 'Opus'

for c in model:
    print(c)
 #Python String Length
model = 'Opus'
# Count the number of characters
print(len(model))   # Output: 4
#String Formatting (f-Strings)
company = 'Google'
field = 'AI'

message = f'{company} is an {field} company.'
print(message)