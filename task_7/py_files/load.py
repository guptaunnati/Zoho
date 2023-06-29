import torchaudio
import numpy as np
import librosa

def read_audio_file(audio_file_path):
    audio_data, sr = torchaudio.load(audio_file_path)
    audio_data = audio_data.reshape(audio_data[0].size())

    # tensor to numpy ndarray
    audio_data = np.array(audio_data)
    return audio_data, sr

# stft calculation
def compute_stft(audio_data):
    stft = librosa.stft(audio_data, n_fft=2048, hop_length=1024, window="hann", center=True, pad_mode="reflect").transpose() 
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