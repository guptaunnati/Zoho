from torch.utils.data import Dataset
import pandas as pd
import torch
import torchaudio
import os

class UrbanSoundDataset(Dataset):
    def __init__(self, annotations_file, audio_dir, transformation, target_sample_rate):
        self.annotations = pd.read_csv(annotations_file)
        self.audio_dir = audio_dir
        self.transformation = transformation
        self.target_sample_rate = target_sample_rate

    def __len__(self):
        return len(self.annotations)
    
    def __getitem__(self, index):
        audio_sample_path = self.get_audio_path(index)
        label = self.get_label(index)

        signal, sr = torchaudio.load(audio_sample_path)
        signal = self.resample_if_necesaary(self, signal, sr)
        signal = self.mix_if_necessary(signal)
        signal = self.transformation(signal)
        return signal, label
    
    def get_audio_path(self, index):
        fold = f"fold{self.annotations.iloc[index, 5]}"
        path = os.path.join(self.audio_dir, fold, self.annotations.iloc[index, 0])
        return path
    
    def get_label(self, index):
        return self.annotations.iloc[index, 6]
    
    def resample_if_necesaary(self, signal, sr):
        if sr != self.target_sample_rate :
            resampler = torchaudio.transforms.Resample(sr, self.target_sample_rate)
            signal = resampler(signal)
        return signal
    
    def mix_if_neesary(self, signal):
        if signal.shape[0]>1:
            signal = torch.mean(signal, dim = 0, keepdim = True)
        return signal
    
if __name__ =="__main__":
    ANNOTATION_FILE = '/home/unnati-pt6974/Desktop/Audio/UrbanSound8K/metadata/UrbanSound8K.csv' 
    AUDIO_DIR = '/home/unnati-pt6974/Desktop/Audio/UrbanSound8K/audio'
    SAMPLE_RATE = 16000
    
    mel_spectogram = torchaudio.transforms.MelSpectogram(
        sample_rate = SAMPLE_RATE,
        n_fft = 1024,
        hop_length = 512,
        n_mels = 64
    )
    usd = UrbanSoundDataset(ANNOTATION_FILE, AUDIO_DIR, mel_spectogram)
    print(usd[0])