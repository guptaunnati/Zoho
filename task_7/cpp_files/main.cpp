#include <bits/stdc++.h>
#include "load.hpp"

using namespace std;

int main(){

    // audio_data 
    std::vector<float> audio_data = read_audio_file("/home/unnati-pt6974/pt6974_unnati/source/task_7/audio_16k.wav");

    // for(int i =79990; i<audio_data.size(); i++){
    //     std::cout<<audio_data[i]<<std::endl;
    // }

    // apply stft
    vector<vector<complex<float>>> stft = compute_stft(audio_data);
    // cout<<stft.size()<<" "<<stft[0].size();
    for(int i=0; i<10; i++){
        cout<<stft[i][i]<<endl;
    }

    // magnitude
    vector<vector<float>> mag = calculate_magnitude(stft);
    // cout<<mag[10][200]<<endl;

    // phase
    vector<vector<float>> phase = calculate_phase(stft);
    // cout<<phase[10][200]<<endl;


    vector<vector<float>> mel_spectrogram = compute_mel_spectrogram(audio_data);
    
    return 0;
}