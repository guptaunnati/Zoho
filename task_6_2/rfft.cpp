#include <bits/stdc++.h>
#include <onnxruntime_cxx_api.h>
#include <sndfile.h>
#include "rfft.hpp"

using namespace std;

// read audio
std::vector<float> read_audio(const char* audio_file_path)
{
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

// calculate dft
vector<vector<vector<double>>> dft_real_cst(int fft_length)
{
    vector<double> m(fft_length);
    for(int i=0; i<fft_length; i++){
        m[i] = i / double(fft_length);
    }
 
    vector<vector<double>> l(fft_length, vector<double>(fft_length));
    for(int i=0; i<fft_length; i++){
        for(int j = 0; j<fft_length; j++){
            l[i][j] = i * m[j];
        }
    }
 
    double pi = 2 * acos(0.0);

    vector<vector<double>> o(fft_length, vector<double>(fft_length));
    for(int i = 0; i<fft_length; i++){
        for(int j=0; j<fft_length; j++){
            o[i][j] = l[i][j] * -2 * pi;
        }
    }
    
    vector<vector<vector<double>>> both(2, vector<vector<double>>(fft_length, vector<double>(fft_length)));
    for(int i=0; i<fft_length; i++){
        for(int j = 0; j<fft_length; j++){
            both[0][i][j] = cos(o[i][j]); // real
            both[1][i][j] = sin(o[i][j]); // imaginary
        }
    }

    return both;
}

// calculate rfft 
vector<vector<vector<double>>> cal_rfft(const char* audio_file_path)
{
    auto audio_data = read_audio(audio_file_path); 

    // extract audio_data
    vector<vector<float>> x(2, vector<float>(audio_data.size()/2));
        
    int j=0;
    for(int i=0; i<int(x[0].size()); i+=2){
        x[0][j] = audio_data[i];
        x[1][j] = audio_data[i+1];
        // cout<< audio_data[0][j]<<" "<<audio_data[1][j]<<endl;
        j++;
    }
    
    int fft_length = x.size();
    // int size = fft_length/ 2 + 1;
    vector<vector<vector<double>>> cst = dft_real_cst(fft_length);

    vector<vector<vector<double>>> res(2, vector<vector<double>>(fft_length, vector<double>(batch_size)));
    int M = fft_length;
    int N = fft_length;
    int P = fft_length;
    int Q = batch_size; 

    // Perform multiplication
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < Q; k++) {
                for (int l = 0; l < P; l++) {
                    res[i][j][k] += cst[i][j][l] * x[l][k];
                }
            }
        } 
    }

    vector<vector<vector<double>>> output(2, vector<vector<double>>(batch_size, vector<double>(fft_length)));
    
    // output
    for(int i = 0 ; i < 2 ; i++) {
        for(int j = 0 ; j < batch_size; j++) {
            for(int k = 0 ; k < fft_length ; k++) {
                output[i][j][k]  = res[i][k][j];
                // std::cout << output[i][j][k] << " ";
            }
            // std::cout << "\n";
        }
    } 

    return output;
}


// onnx cpp inference
std::vector<std::vector<std::vector<double>>> cal_inference_rfft(const char* audio_file_path)
{
    std::vector<float> audioData = read_audio(audio_file_path);
  
  std::array<float, batch_size * 2> input_audio_;
 
  std::array<float, batch_size * 4> results_;
//   int64_t result_{0};

  // ONNX runtime environment
  Ort::Env env;
  
  // ONNX runtime sesson
  Ort::Session session_{env, "onnx_rfft_model.onnx", Ort::SessionOptions{nullptr}};

  // input tensor
  Ort::Value input_tensor_{nullptr};
  // input shape
  std::vector<int64_t> input_shape_{batch_size, 2};

  // input_name, output_name  
  std::array<char* ,2> ipNames ;
  std::array<char* ,2> opNames ; 
  
  // output tensor
  Ort::Value output_tensor_{nullptr};
  // output shape
  std::vector<int64_t> output_shape_{2, batch_size, 2};

  auto memory_info = Ort::MemoryInfo::CreateCpu(OrtDeviceAllocator, OrtMemTypeCPU);

  // allocator
  Ort::AllocatorWithDefaultOptions allocator;

  // input data
  for(int i=0; i< batch_size *2; i++) {
    input_audio_[i] = float(audioData[i]);
    // std::cout << input_audio_[i] << " ";
    }

  // allocator to extract input output attributes 
  Ort::AllocatedStringPtr ipPtr = session_.GetInputNameAllocated(0, allocator);
  auto ipName = ipPtr.get();
  //std::cout << ipName << " ";
  Ort::AllocatedStringPtr opPtr = session_.GetOutputNameAllocated(0, allocator);
  auto opName = opPtr.get();  
  //std::cout << opName << "\n";
  auto ipShape = session_.GetInputTypeInfo(0).GetTensorTypeAndShapeInfo().GetShape();
  
  // input tensor, output tensor
  input_tensor_ = Ort::Value::CreateTensor<float>(memory_info, input_audio_.data(), input_audio_.size(), input_shape_.data(), input_shape_.size());
  output_tensor_ = Ort::Value::CreateTensor<float>(memory_info, results_.data(), results_.size(), output_shape_.data(), output_shape_.size());
  
  ipNames = { ipName  ,ipName};
  opNames = { opName , opName}; 
  
  // Run session
  session_.Run(Ort::RunOptions{nullptr}, ipNames.data(), &input_tensor_, 1, opNames.data(), &output_tensor_, 1);
  
  std::vector<std::vector<std::vector<double>>> output (2, vector<vector<double>>(batch_size, vector<double>(2)));

  // output array
  int m = 0;
  for(int i = 0 ; i < 2 ; i++) {
    for(int j = 0 ; j < batch_size ; j++) {
        for(int k = 0 ; k < 2 ; k++) {
            output[i][j][k] = results_[m];
            // std::cout << output[i][j][k] << " ";
            m++;
            }
        // std::cout << "\n";
        }
    } 

    return output;
}
