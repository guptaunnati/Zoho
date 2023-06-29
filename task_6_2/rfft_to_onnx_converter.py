import numpy as np
import mlprodict.npy.numpy_onnx_impl as npnx
from mlprodict.npy import onnxnumpy_np
from mlprodict.npy.onnx_numpy_annotation import NDArrayType
# from mlprodict.onnx_conv import to_onnx

def dft_real_cst(N, fft_length):
    n = np.arange(N)
    k = n.reshape((N, 1)).astype(np.float64)
    M = np.exp(-2j * np.pi * k * n / fft_length)
    both = np.empty((2,) + M.shape)
    both[0, :, :] = np.real(M)
    both[1, :, :] = np.imag(M)
    return both

@onnxnumpy_np(signature=NDArrayType(("T:all", ), dtypes_out=('T',)))
def onnx_rfft(x, fft_length=None):
    if fft_length is None:
        raise RuntimeError("fft_length must be specified.")

    size = fft_length // 2 + 1
    cst = dft_real_cst(fft_length, fft_length).astype(np.float32)
    xt = npnx.transpose(x, (1, 0))
    res = npnx.matmul(cst[:, :, :fft_length], xt[:fft_length])[:, :size, :]
    return npnx.transpose(res, (0, 2, 1))

rnd = np.random.randn(268237, 2).astype(np.float32)
onnx_rfft(rnd, fft_length=rnd.shape[1])
onnx_rfft_model = onnx_rfft.to_onnx()

# onnx model
with open("onnx_rfft_model.onnx", "wb") as f:
    f.write(onnx_rfft_model.SerializeToString())