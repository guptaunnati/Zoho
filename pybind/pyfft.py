import numpy as np
from scipy.io import wavfile

def calculate_rfft():
    sr, audio_data = wavfile.read("/home/unnati-pt6974/pt6974_unnati/source/pybind/audio.wav")
    rfft = np.fft.rfft(audio_data)
    mag = np.abs(rfft)
    return mag[0][0]

if __name__ == "__main__":
    calculate_rfft()