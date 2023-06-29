from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def operate(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Processing...")
    
    def operate(self):
        print("Operate")
    
    def operations(self):
        print("Operating...")
    
class Headphone(Laptop):
    def connect(self, lap):
        print("Connecting...")
        lap.process()
        print("Connected.")


lap1 = Laptop()
# lap1.process()

head1= Headphone()
head1.connect(lap1)

lap1.operations()
