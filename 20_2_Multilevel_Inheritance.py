# Multilevel Inheritance

'''
Multilevel inheritance in Python means a class (child) inherits from a parent class and then another class 
(derived) inherits from that child class, forming a chain of classes one after another.

Example:

Class A -> Parent (Base class)
Class B -> Inherits from A (Child class)
Class C -> Inherits from B (Derived class)

C inherits from B, While B inherits from A. This allows C to access the attributes and methods of both B and A.
'''
class IPhone:
    def __init__(self, model, storage):
        self.model = model
        self.storage = storage

    def call(self):
        print(f"Calling from {self.model}")


class IPhone18(IPhone):
    def __init__(self, model, storage, camera):
        super().__init__(model, storage)
        self.camera = camera

    def take_enhanced_video(self):
        print("Taking enhacned video")


class IPhone19(IPhone18):
    def __init__(self, model, storage, camera, chip):
        super().__init__(model, storage, camera)
        self.chip = chip

    def better_gaming_performance(self):
        print("Better Gaming Performance with", self.chip)    

print("------------------------------------")
ip1 = IPhone("IP17", "512GB")
print(ip1.model)
print(ip1.storage)
ip1.call()

print("------------------------------------")
ip2 = IPhone18("IP18", "1TB", "48MP")
print(ip2.model)
print(ip2.storage)
print(ip2.camera)
ip2.call()
ip2.take_enhanced_video()

print("------------------------------------")
ip3 = IPhone19("IP19", "1TB", "96MP", "M2")
print(ip3.model)
print(ip3.storage)
print(ip3.camera)
print(ip3.chip)
ip3.call()
ip3.take_enhanced_video()
ip3.better_gaming_performance()


print("------------------------------------")
