# OOP - Object Oriented Programming
# Simulating real world entities or scenarios in programming, that can be called as Object Oriented Programming

'''
OOP : is a programming paradigm based on the concept of objects that contain variables and methods.

1. Improves code reusability
2. Enhances maintainability and scalability
3. Makes programs easier to understand and manage

Class : A Class is a blueprint or template used to create objects it contains variables and methods
that objects of that class will have.

Object : An Object is an instance of a class that represents a real-world entity. 
It is used to access the variables and methods defined inside a class.
'''

# Syntax :

# class <ClassName>:
# logic

if 1 == 1:
    pass  # PlaceHolder for code

# Class - A blueprint or template for creating objects. It defines the attributes and methods that the objects created from the class will have.
# Object - An instance of a class.

# class SampleClass:
# ob1 = SampleClass()
# print(ob1.name)

class IPhone:
    def __init__(self, x, y):  # Constructor
        self.model = x
        self.storage = y

    def call(self):
        print(f"Calling from IPhone{self.model}")


# First argument should always be self - TO ANY METHOD (FUNCTION) in the class
# Constructor - Gets automatically executed when an object is created from the Class
# Constructor is not mandatory

# Method - Function specific to a Class/Object

ip1 = IPhone("13", "256GB")
print(ip1.model)
print(ip1.storage)
ip1.call()

ip2 = IPhone("14", "1TB")
print(ip2.model)
print(ip2.storage)
ip2.call()