def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    return func("Hello World!")

def main():
    print(hello(loud))


if __name__=="__main__":
    main()