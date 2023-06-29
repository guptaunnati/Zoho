import pytest
import example
import torch
from pyfft import calculate_rfft


def test_inference_fft():

    # Run program1: FFT (CPP)
    result1 = float(example.fft())
    # Parse output into a numpy array
    output1 = torch.tensor(result1)

    # Run program2:  CPP inferencing of onnx model
    result2 =  example.inference()
    # Parse output into a numpy array
    output2 = torch.tensor(result2)

    # Compare output
    assert torch.allclose(output1, output2), "Program 1 and program 2 gives different values"

def test_fft_inference():
    # Run program1: FFT (PY)
    result1 = calculate_rfft()
    # Parse output into a numpy array
    output1 = torch.tensor(result1).type(torch.float32)

    # Run program2:  CPP inferencing of onnx model
    result2 =  example.inference()
    # Parse output into a numpy array
    output2 = torch.tensor(result2).type(torch.float32)

    # Compare output
    assert torch.allclose(output1, output2), "Program 1 and program 2 gives different values"

    

if __name__ == "__main__":

    # Run program1
    result1 = float(example.fft())
    # Parse output into a numpy array
    output1 = torch.tensor(result1)

    # Run program2
    result2 =  example.inference()
    # Parse output into a numpy array
    output2 = torch.tensor(result2)

    # Compare output
    assert torch.allclose(output1, output2), "Program 1 and program 2 gives different values"
