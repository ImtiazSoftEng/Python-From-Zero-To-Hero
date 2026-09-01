#Example 1: Python Class and Objects

#define a class 
class Bike:
    name=""
    gear=0

#create objects of the class
bike1=Bike()

#access the attributes and assign values
bike1.gear=11
bike1.name="Mountain Bike"

print(f"Bike Name: {bike1.name}, Gear: {bike1.gear}")


#Create Multiple Objects of Python Class
#defie a class
class Employee:
    #define a property 
    employee_id=0

#create two objects of the Employee class
employee1=Employee()
employee2=Employee()

#access the property using employee1
employee1.employee_id=1001
print(f"Employee 1 ID: {employee1.employee_id}")

#access the property using employee2
employee2.employee_id=1002
print(f"Employee 2 ID: {employee2.employee_id}")

#Python Methods
class Room:
    length=0.0
    breadth=0.0

    #method to calculate area of the room
    def calculate_area(self):
        print(f"Area of the room: {self.length * self.breadth}")

#create an object of the Room class
study_room = Room()
#assign values to the properties
study_room.length=5.0
study_room.breadth=4.0
#access the method inside class
study_room.calculate_area()

#Python Constructors

class Bike:
    def __init__(self, name, gear):
        self.name = name
        self.gear = gear


bike1 = Bike("Mountain Bike", 11)
print(f"Bike Name: {bike1.name}, Gear: {bike1.gear}")   
