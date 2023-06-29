import pytest
import example
import torch

def test_rfft():

    # Run program1
    result1 = example.fft()
    # Parse output into a numpy array
    output1 = torch.tensor(result1)

    # Run program2
    result2 =  example.inference()
    # Parse output into a numpy array
    output2 = torch.tensor(result2)

    # Compare output
    assert torch.allclose(output1, output2), "Program 1 and program 2 gives different values"
