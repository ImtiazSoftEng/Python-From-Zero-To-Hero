#Access and Modify Python Global Variable
c=1 #global variable
def add():
    print(c)
add() #accessing global variable

#i want to modify the global variable without global keyword
a=10 #global variable
def add():
    #increment a by 5
    #a=a+5 #this will give error because a is local variable
    print(a)

add()

#Example: Changing Global Variable From Inside a Function using global
#declare a global variable
c=1
def add():
    #using of global keyword
    global c
    #increment c by 5
    c=c+5
    print(c)

add()
print(c)