#include "/home/unnati-pt6974/pt6974_unnati/source/pybind11-2.10.3/include/pybind11/pybind11.h"
#include "rfft.hpp"
#include "cppinference.hpp"

// int add(int n1, int n2){
//     return n1 + n2;
// }

namespace py = pybind11;

PYBIND11_MODULE(example, m){
    m.doc() = "RFFT";
    // m.def("sum", &add);
    m.def("fft", &cppfft, "Program 1");
    m.def("inference", &cppinference, "Program2");
}