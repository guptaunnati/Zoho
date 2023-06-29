from torch.utils.data import Dataset
import pandas as pd
import torch
import torchaudio
import os

class UrbanSoundDataset(Dataset):
    def __init__(self, annotations_file, audio_dir):
        self.annotations = pd.read_csv(annotations_file)
        self.audio_dir = audio_dir
        pass

    def __len__(self):
        return len(self.annotations)
    
    def __getitem__(self, index):
        audio_sample_path = self.get_audio_path(index)
        label = self.get_label(index)

        signal, sr = torchaudio.load(audio_sample_path)
        return signal, label
    
    def get_audio_path(self, index):
        fold = f"fold{self.annotations.iloc[index, 5]}"
        path = os.path.join(self.audio_dir, fold, self.annotations.iloc[index, 0])
        return path
    
    def get_label(self, index):
        return self.annotations.iloc[index, 6]
    

ANNOTATION_FILE = '/home/unnati-pt6974/Desktop/Audio/UrbanSound8K/metadata/UrbanSound8K.csv' 
AUDIO_DIR = '/home/unnati-pt6974/Desktop/Audio/UrbanSound8K/audio'
usd = UrbanSoundDataset(ANNOTATION_FILE, AUDIO_DIR)
print(usd[0])