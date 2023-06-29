#include <bits/stdc++.h>
#include <sndfile.h>
#include "rfft.hpp"

using namespace std;
int main()
{   
    // rfft: cpp
    auto rfft = cal_rfft("audio.wav");
    // cout<<rfft.size()<<" "<<rfft[0].size()<<" "<<rfft[0][0].size();
    // for(int i=0; i<3; i++){
    //     cout<< rfft[0][i][0]<<", "<<rfft[1][i][1]<< " ";
    // }
   
    // rfft: onnx cpp inference  
    auto inf_rfft = cal_inference_rfft("audio.wav");
    cout<<inf_rfft.size()<<" "<<inf_rfft[0].size()<<" "<<inf_rfft[0][0].size();
    // for(int i=0; i<3; i++){
    //     cout<< rfft[0][i][0]<<", "<<rfft[1][i][1]<< " ";
    // }
    
    return 0;
}