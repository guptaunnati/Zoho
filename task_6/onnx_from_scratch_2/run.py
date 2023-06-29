import onnxruntime as ort
import librosa
from scipy.io import wavfile
# from new3 import get_magnitude
import numpy as np

# Create the session with the desired execution providers
providers = ['CPUExecutionProvider', 'CUDAExecutionProvider']
model = ort.InferenceSession('model8.onnx', providers=providers)

# input 
audio_file = '/home/unnati-pt6974/pt6974_unnati/source/task_6/onnx_from_scratch/audio1.wav'
sr, audio_data = wavfile.read(audio_file)
audio_data = audio_data.astype(np.float32)

# # print(audio_data, sr)
# mg = get_magnitude(audio_data)

# run model
magnitude = model.run(None, {'audio_data': audio_data})[0]
print(magnitude)