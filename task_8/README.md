Load an audio of 16000Hz frequency into tensor using pytorch.

Resample the audio using pytorch  to 48000 Hz frequency.  This audio will be considered as original audio. [https://pytorch.org/tutorials/beginner/audio_preprocessing_tutorial.html#resampling]

Apply STFT on this audio and store the magnitude and phase.

Now load the magnitude and phase from the stored data and convert this into complete audio using ISTFT.

Compare the torch points of original audio and result audio. This should be same.

Calculate torchmetrics PESQ and STOI for original audio and resultant audio and compare the result. This should be same.

Perform this same operation in cpp. i.e, Create an application in cpp which uses STFT and gets the magnitude and phase component from the audio.

Use Pybind and get this magnitude and phase returned from cpp into Python.

Compare the magnitude and phase return by both cpp(using Pybind) and python using Pytest.


#### Files:
##### 1. py_stft: 
Contains function:
- read_audio_file: load audio -> tensor
- resample_audio: resample the audio using pytorch -> "resampled_audio.wav"
- compute_stft: compute stft of the audio
- calculate_magnitude: calculate magnitude of the stft computed
- calculate_phase: calculate phase of the stft computed

##### 2. reconstruct_audio
Contains function:
- reconstruct_audio: reonstructed the audio from the mag and phase calculated -> "reconstructed_audio.wav"
- test_audio: test the original audio and reconstructed audio, are same or not

##### 3. test_audio.py
Contains function for speech enhancement testing:
- PESQ (Perceptual Evaluation Speech Quality) 
- STOI (Short Time Objective Intelligibility)

##### 4. cpp_stft.cpp
Contains the implementation of functions to compute: STFT, STFT magniitude, STFT phase

##### 5. cpp_stft.hpp
Header file that contains the declarations of functions.


##### 6. wrapper.cpp
program to create python bindings for load.cpp funtions.

#### 6. test.py 
pytest program to compare the outputs from cpp and python program for computing stft, mel spectrogram

#### 7. tasks.py
for execution of files.(invoke tool)
