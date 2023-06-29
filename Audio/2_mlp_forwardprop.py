import numpy as np

class MLP:
    def __init__(self, num_inputs= 3, num_hidden= [3, 5], num_outputs= 2):
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs

        layers = [self.num_inputs] + self.num_hidden + [self.num_outputs]

        # initiate random weights
        self.weights = []
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i], layers[i+1])
            self.weights.append(w)

    def forward_propogation(self, inputs):
        activations = inputs

        for w in self.weights:
            # net inputs
            net_inputs =np.dot(activations, w)

            # calculate the activation
            activations = self._sigmoid(net_inputs)

        return activations
        
    def _sigmoid(self, inputs):
        return 1 / (1 + np.exp(-inputs))
    

if __name__ == '__main__':
    # create an MLP
    model = MLP()
      
    # create some inputs
    inputs = np.random.rand(model.num_inputs)

    # forward propogation
    outputs = model.forward_propogation(inputs)

    # print the results
    print(inputs)
    print(outputs)