with open("file.csv") as file:
    for line in sorted(file):
        # row = line.rstrip().split(",")
        name, house = line.rstrip().split(",")
        # print(f"{row[0]} is in {row[1]}")
        print(name, house)
