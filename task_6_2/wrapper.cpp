#include "/home/unnati-pt6974/pt6974_unnati/source/pybind11-2.10.3/include/pybind11/pybind11.h"
#include "/home/unnati-pt6974/pt6974_unnati/source/pybind11-2.10.3/include/pybind11/complex.h"
#include "/home/unnati-pt6974/pt6974_unnati/source/pybind11-2.10.3/include/pybind11/stl.h"

#include <bits/stdc++.h>
#include "rfft.hpp"

namespace py = pybind11;

PYBIND11_MODULE(cal_rfft, m){
    m.doc() = "RFFT";
    m.def("read_audio_file", &read_audio, py::return_value_policy::reference);
    m.def("rfft", &cal_rfft, py::return_value_policy::reference);
    m.def("inf_rfft", &cal_inference_rfft, py::return_value_policy::reference);
}