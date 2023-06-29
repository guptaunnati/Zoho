# Write a small program to indicate the difference between init and call function. 

class Instance:
    def __init__(self, value):
        print("__init__ is called")
        self.value = value

    def __call__(self):
        print("__call__ is called")
        print("The value is:", self.value)

# Initialization
a = Instance("Hello")

# Calling
a() # Output: The value is: Hello
