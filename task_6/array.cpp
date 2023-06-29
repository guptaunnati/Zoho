#include<bits/stdc++.h>
#include <sndfile.h>


using namespace std;

int main()
{
    // read audio
    SF_INFO sfInfo;
    SNDFILE *audioFile = sf_open("audio.wav", SFM_READ, &sfInfo);
    if (!audioFile)
    {
        std::cerr << "Error: could not open audio file." << std::endl;
    }

    // Read audio data
    std::vector<short> audioData(sfInfo.frames*sfInfo.channels);
    sf_read_short(audioFile, &audioData[0], sfInfo.frames*sfInfo.channels);

    // Close audio file
    sf_close(audioFile);

    //audio_data
    int j=0;
    float x[audioData.size()/2][2];
    for(int i=0; i<audioData.size();){
        x[j][0] = audioData[i];
        x[j][1] = audioData[i+1];
        j++;
        i+=2;
    }
    
    // print
    for(int i = 0; i < 3; i++){
        for(int j = 0; j< 2; j++){
            std::cout<<x[i][j]<<" ";
        }
        std::cout<<"\n";
    } 

    std::cout<<"...";

  return 0;
}
