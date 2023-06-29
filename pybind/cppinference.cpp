#include <onnxruntime_cxx_api.h>
#include <bits/stdc++.h>
#include <sndfile.h>
#include "cppinference.hpp"

float cppinference()
{
  // input data
  SF_INFO sfInfo;
  SNDFILE *audioFile = sf_open("audio.wav", SFM_READ, &sfInfo);
  if (!audioFile)
  {
      std::cerr << "Error: could not open audio file." << std::endl;
      return 1;
  }

  // Read audio data
  std::vector<short> audioData(sfInfo.frames*sfInfo.channels);
  sf_read_short(audioFile, &audioData[0], sfInfo.frames*sfInfo.channels);

  // Close audio file
  sf_close(audioFile);

  std::vector<float> input_data(audioData.begin(), audioData.begin()+10);
	// std::array<int64_t, 2> input_shape = {static_cast<int64_t>(input_data.size()/2), static_cast<int64_t>(2)};


//   static constexpr const int width_ = 2;
//   static constexpr const int height_ = 20;
  
  std::array<float, 10> input_audio_;
 
  std::array<float, 10 * 2> results_;
//   int64_t result_{0};

  Ort::Env env;
  Ort::Session session_{env, "/home/unnati-pt6974/pt6974_unnati/source/task_6/onnx_rfft_model.onnx", Ort::SessionOptions{nullptr}};

  Ort::Value input_tensor_{nullptr};
  std::vector<int64_t> input_shape_{batch_size, 2};

  std::array<char* ,2> ipNames ;
  std::array<char* ,2> opNames ; 
  

  Ort::Value output_tensor_{nullptr};
  std::vector<int64_t> output_shape_{2, batch_size, 2};


    auto memory_info = Ort::MemoryInfo::CreateCpu(OrtDeviceAllocator, OrtMemTypeCPU);
    Ort::AllocatorWithDefaultOptions allocator;

    for(int i=0; i< batch_size * 2; i++) {

        input_audio_[i] = audioData[i];
        // std::cout << input_audio_[i] << " ";

    }


    Ort::AllocatedStringPtr ipPtr = session_.GetInputNameAllocated(0, allocator);
    auto ipName = ipPtr.get();
    //std::cout << ipName << " ";
    Ort::AllocatedStringPtr opPtr = session_.GetOutputNameAllocated(0, allocator);
    auto opName = opPtr.get();
    //std::cout << opName << "\n";
    
    auto ipShape = session_.GetInputTypeInfo(0).GetTensorTypeAndShapeInfo().GetShape();
 
    input_tensor_ = Ort::Value::CreateTensor<float>(memory_info, input_audio_.data(), input_audio_.size(), input_shape_.data(), input_shape_.size());
    output_tensor_ = Ort::Value::CreateTensor<float>(memory_info, results_.data(), results_.size(), output_shape_.data(), output_shape_.size());

    ipNames = { ipName  ,ipName};
    opNames = { opName , opName}; 

    //auto opVal = session_.Run( Ort::RunOptions{nullptr} , ipNames.data(), &input_tensor_, 2, opNames.data(), 2);
    session_.Run(Ort::RunOptions{nullptr}, ipNames.data(), &input_tensor_, 1, opNames.data(), &output_tensor_, 1);
    //  std::cout<<"\n";
    // std::cout<<results_.size() << "\n";

    float output[2][batch_size][2];  
    int m = 0;
    for(int i = 0 ; i < 2 ; i++) {
        for(int j = 0 ; j < batch_size ; j++) {
            for(int k = 0 ; k < 2 ; k++) {
                output[i][j][k] = results_[m];
                std::cout << output[i][j][k] << " ";
                m++;
            }
            std::cout << "\n";
        }
    } 
   
    // for(int i = 0 ; i < batch_size * 4 ; i+=2)
    //     std::cout<<results_[i]<<" "<<results_[i+1] << std::endl;
    // std::cout<<"...."<<std::endl;

    float real = output[0][0][0];
    float img = output[1][0][0];

    float mag = float (sqrt(real * real + img * img));
    return mag;
}


















