
import py_stft
import numpy as np
import librosa
import torch
import torchaudio


def reconstruct_audio(audio_file_path, length, mag, phase):
    reconstructed_stft = mag * np.exp(1j * phase)
    reconstructed_audio = librosa.istft(reconstructed_stft, length=length, n_fft=2048, hop_length=1024, win_length=2048, window="hann", center=True)
    torchaudio.save(audio_file_path, torch.from_numpy(reconstructed_audio).reshape(1, reconstructed_audio.size), 48000)

def test_audio(audio1, audio2):
    audio1, _ = py_stft.read_audio_file(audio1)
    audio2, _ = py_stft.read_audio_file(audio2)
    print(torch.allclose(audio1, audio2))


if __name__ == "__main__":
    audio_file_path = "audio_16k.wav" 

    # resample audio
    resampled_audio_file_path, target_sr= "resampled_audio.wav", 48000
    py_stft.resample_audio(resampled_audio_file_path, audio_file_path, target_sr)
    reconstructed_audio_file_path  = "reconstructed_audio.wav"

    audio, _ = py_stft.read_audio_file(resampled_audio_file_path)
    stft = py_stft.compute_stft(audio)
    mag = py_stft.calculate_magnitude(stft)
    phase = py_stft.calculate_phase(stft)

    reconstruct_audio(reconstructed_audio_file_path, audio.numel(), mag, phase)

    test_audio(resampled_audio_file_path, reconstructed_audio_file_path)
