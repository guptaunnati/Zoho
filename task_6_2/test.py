import pytest
import cal_rfft
import torch
from pyrfft import py_cal_rfft

# @pytest.fixture
# def get_audio_data():
#     audio_file_path = "audio.wav"
#     audio_data = cal_rfft.read_audio_file(audio_file_path)
#     return audio_data

def test_rfft_cpp_inference():

    # rfft(CPP)
    result1 = cal_rfft.rfft("audio.wav")
    output1 = torch.tensor(result1, dtype=torch.complex64)

    # rfft(CPP inferencing -> onnx model)
    result2 =  cal_rfft.inf_rfft("audio.wav")
    output2 = torch.tensor(result2, dtype=torch.complex64)

    # Compare output
    assert torch.allclose(output1, output2), "Program 1 and program 2 gives different values"

def test_rfft():
    
    # rfft(CPP)
    result1 = cal_rfft.rfft("audio.wav")
    output1 = torch.tensor(result1, dtype=torch.complex64)
    print(output1, output1.shape)

    # rfft(PY)
    result2 =  py_cal_rfft("audio.wav")
    output2 = torch.tensor(result2, dtype=torch.complex64)
    print(output2, output2.shape)

    # Compare output
    assert torch.allclose(output1, output2), "Program 1 and program 2 gives different values"

    