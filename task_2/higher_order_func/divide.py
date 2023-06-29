def divisor(x):
    def divident(y):
        return y/x
    return divident

divide=divisor(2)
print(divide(10))