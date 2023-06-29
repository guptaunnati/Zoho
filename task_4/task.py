# -*- coding: utf-8 -*-
"""task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HAyi70L4aRGnX2eyGpHgHagBQNiAAxFf
"""

import torch
from torch import nn

torch.__version__

# Create *known* parameters
weight = 0.7
bias = 0.3

# Create data
start = 0
end = 1
step = 0.02
X = torch.arange(start, end, step).unsqueeze(dim=1)
y = weight * X + bias

X[:10], y[:10]

# train/test split
train_split = int(0.8 * len(X)) # 80% of data used for training set, 20% for testing 
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

len(X_train), len(y_train), len(X_test), len(y_test)

# Linear Regression model class
class LinearRegressionModel(nn.Module): 
    def __init__(self):
        super().__init__() 

        self.layer_1=nn.Linear(in_features=1, out_features=3)
        self.layer_2= nn.Linear(in_features=3, out_features=1)

    
    def forward(self, x: torch.Tensor) -> torch.Tensor: 
        # return self.weights * x + self.bias
        return self.layer_2(self.layer_1(x))
    

torch.manual_seed(42)

model_0 = LinearRegressionModel()

# List named parameters 
model_0.state_dict()

# Make predictions with model
with torch.inference_mode(): 
    y_preds = model_0(X_test)

y_test, y_preds

# loss function
loss_fn = nn.MSELoss() 

# optimizer
optimizer = torch.optim.SGD(params=model_0.parameters(), 
                            lr=0.01)

torch.manual_seed(42)

epochs = 100

train_loss_values = []
test_loss_values = []
epoch_count = []

for epoch in range(epochs):
    for batch, (X, y) in enumerate(X_train, y_train):
        ### Training

        model_0.train()

        # 1. Forward pass 
        y_pred = model_0(X_train)
        # print(y_pred)

        # 2. loss 
        loss = loss_fn(y_pred, y_train)

        # 3. Zero grad 
        optimizer.zero_grad()

        # 4. Loss backwards
        loss.backward()

        # 5. optimizer
        optimizer.step()

        ### Testing

        # evaluation mode
        model_0.eval()

        with torch.inference_mode():
            # 1. Forward pass 
            test_pred = model_0(X_test)

            # 2. loss 
            test_loss = loss_fn(test_pred, y_test.type(torch.float))
        
        if epoch % 10 == 0:
            epoch_count.append(epoch)
            train_loss_values.append(loss.detach().numpy())                
            test_loss_values.append(test_loss.detach().numpy())
            print(f"Epoch: {epoch} | MSE Train Loss: {loss} | MSE Test Loss: {test_loss} ")

model_0.state_dict()

