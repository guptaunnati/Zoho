import numpy as np
import onnx
from onnx import helper
from onnx import TensorProto

def get_magnitude(audio_data):
    audio_fft = np.fft.rfft(audio_data)

    mag = np.abs(audio_fft)
    return mag

# input
audio_data = np.random.rand(268237, 2).astype(np.float32)

# output 
magnitude = get_magnitude(audio_data)

# onnx model
input = helper.make_tensor_value_info('audio_data', TensorProto.FLOAT, [268237, 2])
output = helper.make_tensor_value_info('magnitude', TensorProto.FLOAT, [268237, 2])
fft_node = helper.make_node('DFT', ['audio_data'], ['audio_fft'])
mag_node = helper.make_node('Abs', ['audio_fft'], ['magnitude'])

# Create the graph
graph_def = helper.make_graph([fft_node, mag_node], 'audio_processing', [input], [output])

# Create the model
model_def = helper.make_model(graph_def, producer_name='audio_processing')

# Save the model
onnx.save(model_def, 'model8.onnx')
