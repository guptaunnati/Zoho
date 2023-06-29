import torchaudio
import numpy as np
import librosa
import torch

def read_audio_file(audio_file_path):
    audio_data, sr = torchaudio.load(audio_file_path)
    return audio_data, sr

def resample_audio(resampled_file_path, audio_file_path, target_sr):
    audio_data, sr = read_audio_file(audio_file_path)
    resampler = torchaudio.transforms.Resample(sr, target_sr)
    audio_data = resampler(audio_data)
    torchaudio.save(resampled_file_path, audio_data, target_sr)

# stft calculation
def compute_stft(audio_data):
    # print(type(audio_data))
    audio_data = audio_data.reshape(audio_data[0].size())
    audio_data = audio_data.numpy()
    # print(audio_data.shape)
    stft = librosa.stft(audio_data, n_fft=2048, hop_length=1024, win_length = 2048, window="hann", center=True, pad_mode="reflect") 
    return stft

def calculate_magnitude(stft):
    mag =  np.abs(stft)
    return mag

def calculate_phase(stft):
    phase = np.angle(stft)
    return phase

# mel_spectrogram
def compute_mel_spectrogram(audio_data):
    mels= librosa.feature.melspectrogram(y=audio_data, sr=16000, n_fft=2048, hop_length=1024, window="hann", center=True, pad_mode="reflect", power=2).transpose()
    return mels


if __name__ == "__main__":
    audio_file_path  = "audio_16k.wav"
    target_sr = 48000
    audio_file_path = resample_audio(audio_file_path, target_sr)
    audio_data, _ = read_audio_file(audio_file_path)
    # audio_data = audio_data.numpy()
    stft = compute_stft(audio_data)
    # print(stft)
    mag = calculate_magnitude(stft)
    phase = calculate_phase(stft)