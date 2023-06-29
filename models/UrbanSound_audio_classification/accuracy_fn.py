import torch
from torch import nn

def acc_fn(preds, labels):
  n = nn.Softmax(dim=-1)
  preds = n(preds)
  out = preds.argmax(dim=-1)
  return torch.sum(out == labels) / len(labels)