students = ["Hermoine", "Harry", "Ron"]

print(students)
print(students[0])

# for student in students:
#     print(student)


#range(start_index, ending_index+1, iterate_by)
for i in range(0, len(students), 2):
    print(students[i])