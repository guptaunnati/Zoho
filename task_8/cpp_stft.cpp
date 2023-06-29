#include <bits/stdc++.h>
#include <sndfile.h>
#include "cpp_stft.hpp"
#include "/home/unnati-pt6974/pt6974_unnati/source/LibrosaCpp/librosa/librosa.h"

using namespace std;

//read audio file
std::vector<float> read_audio_file(const char* audio_file_path){
    SF_INFO sfInfo;
    SNDFILE *audioFile = sf_open(audio_file_path, SFM_READ, &sfInfo);
    if (!audioFile)
    {
        std::cerr << "Error: could not open audio file." << std::endl;
    }

    // Read audio data
    std::vector<float> audioData(sfInfo.frames*sfInfo.channels);
    sf_read_float(audioFile, &audioData[0], sfInfo.frames*sfInfo.channels);

    // Close audio file
    sf_close(audioFile);

    // extract signal 
    vector<float> audio_data;
    for(int i=0; i< int(audioData.size()); i+=sfInfo.channels){
        audio_data.push_back(audioData[i]);
    }

    return audio_data;
}

// calculate magnitude
vector<vector<float>> calculate_magnitude(vector<vector<complex<float>>> stft){
    vector<vector<float>> mag (stft.size(), vector<float>(stft[0].size()));
    int row = int(mag.size());
    int col = int(mag[0].size());
    for(int i = 0; i<row; i++){
        for(int j=0; j<col; j++){
            mag[i][j] = abs(stft[i][j]);
        }
    }
    return mag;
}

// calculate phase
vector<vector<float>> calculate_phase(vector<vector<complex<float>>> stft){
    vector<vector<float>> phase (stft.size(), vector<float>(stft[0].size()));
    int row = int(phase.size());
    int col = int(phase[0].size());
    for(int i = 0; i<row; i++){
        for(int j=0; j<col; j++){
            phase[i][j] = arg(stft[i][j]);
        }
    }
    return phase;
}

// compute stft
vector<vector<complex<float>>> compute_stft(vector<float> audio_data){
    vector<vector<complex<float>>> stft = librosa::Feature::stft(audio_data, 2048, 1024, "hann", true, "reflect");
    // cout<<stft.size()<<" "<<stft[0].size();

    return stft;
}

// compute mel spectrogram
vector<vector<float>> compute_mel_spectrogram(vector<float> audio_data){
    vector<vector<float>> mels = librosa::Feature::melspectrogram(audio_data, 16000, 2048, 1024, "hann", true, "reflect", 2, 128, 0, 8000);
    // cout<<mels.size()<<" "<<mels[0].size()<<endl;
    // for(int i=0; i<10; i++){
    //     cout<<mels[7][i]<<" ";
    // }
    return mels;
}
 

