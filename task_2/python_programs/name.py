name=input("What's your name? ")

# file= open("file1.txt", "a")
# file.write(name)
# file.close()

with open("file2.txt", "a") as file:
    file.write(f"{name}\n")