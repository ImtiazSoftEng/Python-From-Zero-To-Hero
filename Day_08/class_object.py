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