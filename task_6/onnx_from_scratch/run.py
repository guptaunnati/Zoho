import onnxruntime as ort
import numpy as np
import librosa
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
# audio_data = audio_data.reshape(268237*2)

# print(audio_data, sr)
# mg = get_magnitude(audio_data)

# run model
magnitude = model.run(None, {'x': audio_data.astype(np.float32)})[0][0]
magnitude =np.abs(magnitude).astype(np.float16)
print(magnitude)
print(magnitude.shape)
# print(mg)

