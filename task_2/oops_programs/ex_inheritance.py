class Demo:
    def __init__(self):
        print("'__init__' is called")
        # self.name=name
        # self.id=id

    def __call__(self):
        print("'_call__' is called")


a = Demo()

a()