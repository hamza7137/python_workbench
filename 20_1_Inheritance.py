# Inheritance

'''
Inheritance is a concept in (OOP) that allows a child or derived class to inherit 
attributes and methods from parent or base class).

Here, a parent class Animal is created that has a method info(). 
Then a child class Dog is created that inherits from Animal and adds additional behavior.
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
# Inherited method
d.info()     
d.sound()
