class Wizard:
    def __init__(self, name):
        self.name=name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name=name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house=house
    
    def __str__(self):
        return  f"{self.name}, {self.house}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        self._house=house

    @classmethod
    def get(cls):
        cls.name=input("Name: ")
        cls.house=input("House: ")
        return cls(name, house)

class Professor (Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject=subject

wizard = Wizard("Albus")
student =Student.get()
professor = Professor("Snape", "Dark Arts")

print(student)