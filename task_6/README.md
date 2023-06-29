Create python library which takes audio as input and provides magnitude after applying RFFT on audio.

Export this method of python library into onnx model.

Run this onnx model and pass the audio and get magnitude as output.

Create a cpp program which takes audio as input and stores this audio as array.You can use any thirdparty library for this.

Access the onnx model using cpp program and get the magnitude as output.

Increase the intra-processing threads to 10 and note the performance changes.

Perform RFFT in cpp and compare the values obtained from onnx to that calculated in cpp itself.

Ensure comparison says that the result are same from python and cpp.

Resources,
Audio - https://dylanmeeus.github.io/posts/audio-from-scratch-pt1/
https://pudding.cool/2018/02/waveforms/
Signal processing techniques.
Importance of ONNX

----
**FILES:**
**1. rfft_to_onnx_converter.py**

Creates a onnx model "onnx_rfft_model.onnx", calculates rfft for a audio file.

**2. run.py**

Run the onnx model and pass the audio and get rfft as output.


**3. array.cpp** 

Cpp program which takes audio as input and stores this audio as array.


**4. inference.cpp**

Access the onnx model using cpp program and get rfft as output.
```
C++ inferencing => Initialisation => Runtime environment : ONNX Runtime
                                  => options : ONNX runtime session
                => Inference

runtime env      -|   
session options   | => ONNX runtime session  => Allocator --extract--> input_name, output_name, type, shape  
onnx model       -|                          => Run -> inference
```

**4. fft.cpp**

Perform RFFT in cpp without third party libraries.

-----------------
**FLOW :**

* **rfft_to_onnx_converter.py** creates a onnx model : **onnx_rfft_model.onnx**
*  This model is accessed using python and cpp through **run.py** and **inference.cpp** respectively.
* Calculate rfft using **fft.cpp**

---
**TESTING :**
Performed testing for the outputs of inference.cpp (uses onnx_model created for rfft calculation) and fft.cpp (calculates rfft) are close or not.

* Used pybind (allow you to call functions and pass data from Python to C++) : **wrapper.cpp**

* Tested the outputs : **test.py**

* Used invoke Tool (invoke is the tool you’ll be using to build and test Python bindings): **tasks.py**

**dir :** pybind
**Use command :** invoke all

-----












