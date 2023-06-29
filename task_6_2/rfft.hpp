#ifndef RFFT_HPP
#define RFFT_HPP

# define batch_size 1024

std::vector<float> read_audio(const char* audio_file_path);
std::vector<std::vector<std::vector<double>>> dft_real_cst(int fft_length);
std::vector<std::vector<std::vector<double>>> cal_rfft(const char* audio_file_path);
std::vector<std::vector<std::vector<double>>> cal_inference_rfft(const char* audio_file_path);

#endif