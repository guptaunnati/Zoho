"""
./inf and ./fft are execution files of cpp programs, whose outputs we are supposed to compare.

subprocess library is used to get the output from thoe cpp program's exeution files 
"""


import subprocess
import pytest

def test_cpp_programs_output_closeness():
    # Run the first program and capture its output
    first_output = subprocess.check_output(["./inf"])

    # Run the second program and capture its output
    second_output = subprocess.check_output(["./fft"])

    assert first_output == second_output, "output of programs are not equal"


