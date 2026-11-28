# OOP - Object Oriented Programming
# Simulating real world entities or scenarios in programming, that can be called as Object Oriented Programming

'''
Object Oriented Programming empowers developers to build modular, maintainable and scalable applications.

OOP is a way of organizing code that uses objects and classes to represent real-world entities and their behavior.

In OOP, object has attributes thing that has specific data and can perform certain actions using methods.

1. Organizes code into classes and objects.
2. Supports encapsulation to group data and methods together.
3. Enables inheritance for reusability and hierarchy.
4. Allows polymorphism for flexible method implementation.
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