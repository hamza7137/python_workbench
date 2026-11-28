# Inheritance

'''
Multiple inheritance in Python allows a single child class to inherit attributes and methods 
from two or more parent classes.
'''

class Phone:
    def __init__(self, model, storage):
        self.model = model
        self.storage = storage

    def call(self):
        print(f"Calling from {self.model}...")


class Tablet:
    def __init__(self, internet_speed):
        self.internet_speed = internet_speed

    def browse(self):
        print("Using the Internet Browsing Capability")


class IPhone(Phone, Tablet):
    def __init__(self, model, storage, os, internet_speed):
        Phone.__init__(self, model, storage)
        Tablet.__init__(self, internet_speed)
        self.os = os

    def face_id(self):
        print("Id'ing the face...")


ip = IPhone("IPhone13", "2TB", "Mac", "100Mbps")
ip.face_id()
ip.call()
ip.browse()
print(ip.internet_speed)