import pytest
import stft
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from py_files.load import compute_mel_spectrogram, compute_stft, calculate_magnitude, calculate_phase
import torch
import numpy as np

@pytest.fixture
def get_audio_data():
    audio_file_path = "/home/unnati-pt6974/pt6974_unnati/source/task_7/audio_16k.wav"
    audio_data = stft.read_audio_file(audio_file_path)
    return audio_data

# @pytest.fixture
# def get_stft(get_audio_data):
#     return compute_stft(get_audio_data)


def test_stft(get_audio_data):
    result1 = stft.compute_stft(get_audio_data)
    output1 = torch.tensor(result1, dtype=torch.complex64)
    result2 = compute_stft(np.array(get_audio_data))
    output2 = torch.tensor(result2, dtype=torch.complex64)
    assert torch.allclose(output1, output2, atol = 1e-2), "stft"

def test_mel_spectrogram(get_audio_data):
    result1 = stft.melspectrogram(get_audio_data)
    output1 = torch.tensor(result1, dtype=torch.complex64)
    result2 = compute_mel_spectrogram(np.array(get_audio_data))
    output2 = torch.tensor(result2, dtype=torch.complex64)
    assert torch.allclose(output1, output2, atol = 1e-2), "mel spectrogram"

def test_magnitude(get_audio_data):
    stft_val = stft.compute_stft(get_audio_data)
    result1 = stft.magnitude(stft_val)
    output1 = torch.tensor(result1, dtype=torch.float32)
    result2 = calculate_magnitude(np.array(stft_val))
    output2 = torch.tensor(result2, dtype=torch.float32)
    assert torch.allclose(output1, output2, atol = 1e-2), "magnitude"

def test_phase(get_audio_data):
    stft_val = stft.compute_stft(get_audio_data)
    result1 = stft.phase(stft_val)
    output1 = torch.tensor(result1, dtype=torch.float32)
    result2 = calculate_phase(np.array(stft_val))
    output2 = torch.tensor(result2, dtype=torch.float32)
    assert torch.allclose(output1, output2, atol = 1e-2), "magnitude"


# if __name__ == "__main__":

#     audio_file_path = "/home/unnati-pt6974/pt6974_unnati/source/task_7/audio_16k.wav"
#     audio_data = stft.read_audio_file(audio_file_path)
#     test_stft(audio_data)
#     test_mel_spectrogram(audio_data)
