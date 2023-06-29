from torchmetrics.audio.pesq import PerceptualEvaluationSpeechQuality
from torchmetrics.audio.stoi import ShortTimeObjectiveIntelligibility
import py_stft
import torchaudio

def resample_if_necesaary(audio_file_path):
    audio, sr = torchaudio.load(audio_file_path)
    resampled_audio_file_path = "audio.wav"
    if sr!=16000:
        py_stft.resample_audio(resampled_audio_file_path, audio_file_path, 16000)

    return(torchaudio.load(resampled_audio_file_path))
def pesq(audio1, audio2):
    audio1, sr = resample_if_necesaary(audio1)
    audio2, sr = resample_if_necesaary(audio2)
    m_pesq = PerceptualEvaluationSpeechQuality(sr, "wb")
    print(f"PESQ: {m_pesq(audio1, audio2)}")

def stoi(audio1, audio2):
    audio1, sr = py_stft.read_audio_file(audio1)
    audio2, sr = py_stft.read_audio_file(audio2)
    m_stoi = ShortTimeObjectiveIntelligibility(sr, False)
    print(f"STOI: {m_stoi(audio1, audio2)}")


resampled_audio_file_path= "resampled_audio.wav"
reconstructed_audio_file_path  = "reconstructed_audio.wav"
pesq(resampled_audio_file_path, reconstructed_audio_file_path)
stoi(resampled_audio_file_path, reconstructed_audio_file_path)