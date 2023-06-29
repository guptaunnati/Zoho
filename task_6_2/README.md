#### Task 6 (Refactor)

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



#### Files:

###### 1. rfft.cpp
Contains the c++ implementation to compute: read_audio_file. rfft, onnx c++ inference(rfft).

###### 2. rfft.hpp
Header file that contains the declaration of the functions.

###### 3. main.cpp
Contains the implementation of rfft.cpp.

###### 4. rfft_to_onnx_converter.py
Create a ONNX model, that calculates rfft. -> "onnx_rfft_model

##### 5. run.py
Python inferencing of the ONNX model created.

##### 6. test.py
Program to test the outputs.

##### 7. wrapper.cpp
CPP program(pybind), to wrap(python bindings) the cpp programs.

##### 8. tasks.py
used a invoke tool, for execution of files. 














