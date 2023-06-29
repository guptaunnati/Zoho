# try:
#     x=int(input("Enter no. : "))
# except ValueError:
#     print("X is not an integer")
# else: 
#     print(x)

while True:
    try:
        x=int(input("Enter no. : "))
    except ValueError:
        # print("X is not an integer")
        pass
    else: 
        print(x)
        break

