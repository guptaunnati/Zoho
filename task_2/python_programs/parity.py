def main():
    x = int(input("Enter the value of x: "))

    # if isEven(x):
    #     print("Even")
    # else:
    #     print("Odd")
    print("Even") if isEven(x) else print("Odd")

def isEven(n):
    # if n%2==0:
    #     return True
    # else:
    #     return False

    # return True if n%2==0 else False
    return n%2==0

main()