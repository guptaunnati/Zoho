import onnxruntime as ort
import numpy as np
from scipy.io import wavfile
# from new3 import get_magnitude

from onnxruntime_extensions import get_library_path

so = ort.SessionOptions()
so.register_custom_ops_library(get_library_path())

# Create the session with the desired execution providers
providers = ['CPUExecutionProvider', 'CUDAExecutionProvider']
model = ort.InferenceSession('onnx_rfft_model.onnx', providers=providers)

# input 
audio_file = 'audio.wav'
sr, audio_data = wavfile.read(audio_file)
# audio_data_2 = audio_data.astype(np.float32)
# print(audio_data_2)

# run model
rfft = model.run(None, {'x': audio_data.astype(np.float32)})[0][0]
print(rfft, rfft.shape)
# mag = np.abs(rfft)

