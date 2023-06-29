import load

audio_file_path = "/home/unnati-pt6974/pt6974_unnati/source/task_7/audio_16k.wav"
audio_data, sr = load.read_audio_file(audio_file_path)
stft = load.compute_stft(audio_data)
magnitude = load.calculate_magnitude(stft)
phase = load.calculate_phase(stft)
mel_spectrogram = load.compute_mel_spectrogram(audio_data) 