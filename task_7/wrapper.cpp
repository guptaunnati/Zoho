#include "/home/unnati-pt6974/pt6974_unnati/source/pybind11-2.10.3/include/pybind11/pybind11.h"
#include "/home/unnati-pt6974/pt6974_unnati/source/task_7/cpp_files/load.hpp"
#include <bits/stdc++.h>
#include "/home/unnati-pt6974/pt6974_unnati/source/pybind11-2.10.3/include/pybind11/complex.h"
#include "/home/unnati-pt6974/pt6974_unnati/source/pybind11-2.10.3/include/pybind11/stl.h"
namespace py = pybind11;

PYBIND11_MODULE(stft, m){
    m.doc() = "STFT";
    m.def("read_audio_file", &read_audio_file, py::return_value_policy::reference);
    // m.def("read_audio_file_py", [] (const char* audio_file_path) {
    //     std::vector<float> result = read_audio_file(audio_file_path);
    //     pybind11::list py_result;
    //     for (const auto& x : result) {
    //         py_result.append(x);
    //     }
    //     return py_result;
    // });

    m.def("compute_stft", &compute_stft, py::return_value_policy::reference);
    m.def("magnitude", &calculate_magnitude, py::return_value_policy::reference);
    m.def("phase", &calculate_phase, py::return_value_policy::reference);
    m.def("melspectrogram", &compute_mel_spectrogram, py::return_value_policy::reference);
}