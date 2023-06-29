#include <iostream>
#include <sndfile.h>

int main(int argc, char** argv)
{
    // Open the audio file for reading
    SF_INFO sfinfo;
    SNDFILE* infile = sf_open("/home/unnati-pt6974/pt6974_unnati/source/task_6/audio.wav", SFM_READ, &sfinfo);
    if (!infile) {
        std::cerr << "Error opening audio file: " << sf_strerror(NULL) << "\n";
        return 1;
    }

    // Check the number of channels in the file
    if (sfinfo.channels == 1) {
        std::cout << "Mono audio file\n";
    } else if (sfinfo.channels == 2) {
        std::cout << "Stereo audio file\n";
    } else {
        std::cout << "Unsupported number of channels: " << sfinfo.channels << "\n";
    }

    // Close the audio file
    sf_close(infile);

    return 0;
}
