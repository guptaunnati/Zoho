import pytest
import stft
import sys
import os
import py_stft
import torch
import numpy as np
import torchaudio

@pytest.fixture
def get_audio_data():
    audio_file_path = "audio_16k.wav"
    resampled_audio_file_path = "original_audio.wav"
    # audio_data = stft.read_audio_file(audio_file_path)
    # return audio_data
    py_stft.resample_audio(resampled_audio_file_path, audio_file_path, 48000)
    audio, sr = torchaudio.load(audio_file_path)
    stft_val = py_stft.compute_stft(audio).transpose()
    # # print(type(audio_data))
    # audio_data = np.array(audio_data)
    return stft_val

# @pytest.fixture
# def get_stft(get_audio_data):
#     return compute_stft(get_audio_data)


# def test_stft(get_audio_data):
#     result1 = stft.compute_stft(get_audio_data)
#     output1 = torch.tensor(result1, dtype=torch.complex64)
#     result2 = py_stft.compute_stft(np.array(get_audio_data))
#     output2 = torch.tensor(result2, dtype=torch.complex64)
#     assert torch.allclose(output1, output2, atol = 1e-2), "stft"

# def test_mel_spectrogram(get_audio_data):
#     result1 = stft.melspectrogram(get_audio_data)
#     output1 = torch.tensor(result1, dtype=torch.complex64)
#     result2 = py_stft.compute_mel_spectrogram(np.array(get_audio_data))
#     output2 = torch.tensor(result2, dtype=torch.complex64)
#     assert torch.allclose(output1, output2, atol = 1e-2), "mel spectrogram"

def test_magnitude(get_audio_data):
   
    result1 = stft.magnitude(get_audio_data)
    output1 = torch.tensor(result1, dtype=torch.float32)
    result2 = py_stft.calculate_magnitude(get_audio_data)
    output2 = torch.tensor(result2, dtype=torch.float32)
    assert torch.allclose(output1, output2, atol = 1e-2), "magnitude"

def test_phase(get_audio_data):
    result1 = stft.phase(get_audio_data)
    output1 = torch.tensor(result1, dtype=torch.float32)
    result2 = py_stft.calculate_phase(get_audio_data)
    output2 = torch.tensor(result2, dtype=torch.float32)
    assert torch.allclose(output1, output2, atol = 1e-2), "phase"


# if __name__ == "__main__":

#     audio_file_path = "/home/unnati-pt6974/pt6974_unnati/source/task_7/audio_16k.wav"
#     audio_data = stft.read_audio_file(audio_file_path)
#     test_stft(audio_data)
#     test_mel_spectrogram(audio_data)
