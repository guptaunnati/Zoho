from typing import Protocol

class Mobile(Protocol):
    def type(self):
        ...

    def modelName(self):
        ...

    def ramSize(self):
        ...

class Realme(Mobile):
    def type(self):
        print("Mobile")
        
    def modelName(self):
        print("5 Pro")


realme = Realme()

realme.type()