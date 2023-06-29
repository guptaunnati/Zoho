# print("meow")
# print("meow")
# print("meow")

# # for loop
# for i in range(3):
#     print("meow")

# # while loop
# i=3
# while i!=0:
#     print("meow")
#     i=i-1

def main():
    num =get_number()
    meow(num)

def get_number():
    while True:
        num = int(input("Enter no. : "))
        if(num>0):
            return num
        
def meow(n):
    for _ in range(n):
        print("meow")

main()
