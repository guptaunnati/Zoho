import math

def sigmoid(x):
    y = 1.0 / math.exp(x)
    return y

def activate(inputs, weights):
    # net input
    h = 0
    for i, w in zip(inputs, weights):
        h += i * w

    # activation
    return sigmoid(h)

if __name__  == '__main__':
    inputs = [.5, .3, .2]
    weights = [.4, .7, .2]
    output = activate(inputs, weights)
    print(output) 