import subprocess
import numpy as np
import torch

"""
used the execution files to compare the programs output supposed to be compared 
"""

def test_cpp_programs():

    # Run program1
    result1 = subprocess.check_output(["./inf"]).decode("utf-8")
    # Parse output into a numpy array
    output1 = torch.tensor(result1.split("")).reshape((2,3,2))

    # Run program2
    result2 = subprocess.check_output(["./fft"]).decode("utf-8")
    # Parse output into a numpy array
    output2 = torch.tensor(result2.split("")).reshape((2,3,2))

    # Compare output
    assert torch.allclose(output1, output2)
