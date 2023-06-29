name = input("What's name? ")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name =="Draco":
#     print("Slytherin")
# else:
#     print("Who?")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermoine":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Malfoy":
        print("Slytherin")
    case _ :
        print("Who?")