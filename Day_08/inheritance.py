#Example: Python Inheritance
class Animal:
    #attribute and method of the parent class
    name=""
    def eat(self):
        print("I can eat")

#inherit the Animal class
class Dog(Animal):

    #new method in subclass
    def display(self):
        #access name attribute of subclass using self
        print("My name is", self.name)
#create an object of the subclass
labrador=Dog()
#access subclass the attribute and method 
labrador.name="Tommy"
labrador.eat()
#call subclass method
labrador.display()