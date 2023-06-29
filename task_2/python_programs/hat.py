import random

class Hat:
    def __init__(self):
        self.houses=["Gryffindor", "Slytherin", "Ravenclaw", "HUfflepuff"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is in ", random.choice(cls.houses))



Hat.sort("Harry")