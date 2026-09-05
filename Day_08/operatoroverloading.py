#Python Special Functions
number1 = 5

# similar to number2 = number1 + 6
number2 = number1.__add__(6)
    
print(number2)  # 11

#Example: Add Two Coordinates (Without Overloading)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_point(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
p1 = Point(1, 2)
p2 = Point(2, 3)
p3 = p1.add_point(p2)
print(f"Point 3: ({p3.x}, {p3.y})")

#Example: Add Two Coordinates (With Overloading)
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    
p1 = Point(1, 2)
p2 = Point(2, 3)

# this statment calls the __add__() method
p3 = p1 + p2

print((p3.x, p3.y))   # Output: (3, 5)

#Overloading Comparison Operators
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # overload < operator
    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Alice", 20)
p2 = Person("Bob", 30)

print(p1 < p2)  # prints True
print(p2 < p1)  # prints False