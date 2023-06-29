students = {
    "Hermoine" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Malfoy" : "Slytherin",
}

print(students["Hermoine"])

for student in students:
    print(student, end=", ")  # print keys
    print(students[student]) # print value