# Inheritance

# Heirarchical - One Parent - Multiple Childs

'''
Hierarchical Inheritance is a inheritance in which a single base class is inherited by 
multiple child classes. 
'''

class Phone:
    def __init__(self, model, storage):
        self.model = model
        self.storage = storage

    def call(self):
        print(f"Calling from {self.model}...")


class IPhone(Phone):
    def __init__(self, model, storage, os):
        super().__init__(model, storage)
        self.os = os

    def face_id(self):
        print("Id'ing the face...")


class Android(Phone):
    def __init__(self, model, storage, os):
        super().__init__(model, storage)
        self.os = os

    def dual_sim(self):
        print("Using Dual Sim feature...")

ip = IPhone("IPhone13", "2TB", "Mac")
android = Android("Samsung", "1TB", "JellyBean")
print("------------------------------------")
print(ip.model)
print(ip.storage)
print(ip.os)
ip.call()
print("------------------------------------")
print(android.model)
print(android.storage)
print(android.os)
android.call()
print("------------------------------------")