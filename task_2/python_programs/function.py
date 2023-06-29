def main():
    hello()
    # name = input("What's your name? ")
    # hello(name)
    # print(name)
    print("Square of number 3 is:", square(3))

def hello(to = "Unnati"):
    print("Hello! "+to)

def square(n):
    return n*n
    # return n**2
    # return pow(n, 2)

main()