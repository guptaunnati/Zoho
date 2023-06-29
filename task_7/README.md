#### Completed on March 17, 2023

Load an audio of 16000Hz frequency into tensor using pytorch.

Apply STFT on this audio and store the magnitude and phase.

Apply Mel-filter on this magnitude and find MelSpectrogram.

Load the same audio in cpp.

Apply STFT using cpp and find magnitude and phase.

Apply Mel-filter on this STFT magnitude with the same attributes as was done in python.

Design a python program where you could get the output[STFT and Mel] of cpp program using pybind.

Now compare the values and ensure both are same.

Write a Pytest to prove the same.


----
#### 1. cpp_files
        |- load.cpp: contains the implementation of functions to compute: STFT, STFT magniitude, STFT phase, Mel Spectrogram
        |- load.hpp: header file that contains the declarations of functions.
        |- main.cpp: contains the implementation of load.cpp


#### 2. py_files
        |- load.py: contains the implementation of functions to compute: STFT, STFT magniitude, STFT phase, Mel Spectrogram
        |- main.py: contains the implementation of load.py


#### 3. wrapper.cpp
        program to create python bindings for load.cpp funtions.

#### 4. test.py 
        pytest program to compare the outputs from cpp and python program for computing stft, mel spectrogram

#### 5. tasks.py
        for execution of files.(invoke tool)


---
#### Testing:

Use command: **invoke all**

