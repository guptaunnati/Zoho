
class Student:

    def __init__(self, name, house, patronus):
        self.name=name
        self.house=house
        self.patronus=patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name=name
       
    @property 
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house=house

    def charm(self):
        match self.patronus:
            case "stag":
                print("Horse")
            case _ :
                print("Wand")
    
def main():
    student = get_student()
    print(student)
    student.charm()


def get_student():
    name=input("Name: ")
    house= input("House: ")
    patronus= input("Patronus: ")
    return Student(name, house, patronus)


if __name__=="__main__":
    main()