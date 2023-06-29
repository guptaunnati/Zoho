#include <bits/stdc++.h>
#ifndef CPP_STFT_HPP
#define CPP_STFT_HPP

std::vector<float> read_audio_file(const char* audio_file_path);

std::vector<std::vector<float>> calculate_magnitude(std::vector<std::vector<std::complex<float>>> stft);

std::vector<std::vector<float>> calculate_phase(std::vector<std::vector<std::complex<float>>> stft);

std::vector<std::vector<std::complex<float>>> compute_stft(std::vector<float> audio_data);

std::vector<std::vector<float>> compute_mel_spectrogram(std::vector<float> audio_data);

#endif