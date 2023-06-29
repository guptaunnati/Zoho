# -*- coding: utf-8 -*-
"""house_price_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Av_txHjccAEHsA08rBcqYi_E5lnYa7vo
"""

import numpy as np
import pandas as pd
import torch

from torchvision.datasets.utils import download_url

# download_url('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', root = '.')

dataframe = pd.read_csv('BostonHousing.csv')
dataframe.head()

# Convert from Pandas dataframe to numpy arrays
inputs = dataframe.drop('medv', axis=1).values
targets = dataframe[['medv']].values
inputs.shape, targets.shape

type(inputs), type(targets)

# numpy array to torch.tensor
inputs = torch.from_numpy(inputs).type(torch.float32)
targets = torch.from_numpy(targets).type(torch.float32)

type(inputs), type(targets)

# dataset

from torch.utils.data import TensorDataset

ds = TensorDataset(inputs, targets)

ds[0]

# split train / test data

from torch.utils.data import random_split

train_split = int(0.8 * len(ds))
# print(train_split)
train_ds, test_ds = random_split(ds, [train_split, len(ds)-train_split])
len(train_ds), len(test_ds)

# dataloader

from torch.utils.data import DataLoader

train_dl = DataLoader(dataset = train_ds,
                      batch_size = 32,
                      shuffle = False)

test_dl = DataLoader(dataset = test_ds,
                      batch_size = 32,
                      shuffle = False)

# model
from torch import nn
class HousePricePrediction(nn.Module):
  def __init__(self):
    super().__init__()
    self.layer = nn.Linear(in_features = 13, out_features = 1)

  def forward(self, x : torch.Tensor ) -> torch.Tensor:
    return self.layer(x)

# instance
model_0 = HousePricePrediction()
model_0

# train
loss_fn = nn.MSELoss()
optimiser = torch.optim.SGD(params= model_0.parameters(), lr = 5e-7)

# training loop
import torch.nn.functional as F
epochs = 10

for epoch in range(100):
  # Training Phase 
  model_0.train()
  for batch in train_dl:
    inputs, targets = batch 
    out = model_0(inputs)                 # Generate predictions
    loss = loss_fn(out, targets)
    loss.backward()
    optimiser.step()
    optimiser.zero_grad()

  ##Testing Phase
  model_0.eval()
  with torch.inference_mode():
    for batch in test_dl:
      inputs, targets = batch 
      out = model_0(inputs)                 # Generate predictions
      test_loss = loss_fn(out, targets)

  if epoch %10 == 0: 
    print(f"Epoch : {epoch} | Train Loss: {loss} | Test Loss: {test_loss}")
