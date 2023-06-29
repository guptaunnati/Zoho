from model_cnn import CNNNetwork
from preprocessed_dataset import UrbanSoundDataset
from accuracy_fn import acc_fn
from torch import nn
from torchsummary import summary
import torch
import torchaudio
from torch.utils.data import Dataset, DataLoader, random_split


if __name__ == '__main__':

    # instantiate data
    ANNOTATION_FILE = '/home/unnati-pt6974/pt6974_unnati/source/Audio/UrbanSound8K/metadata/UrbanSound8K.csv' 
    AUDIO_DIR = '/home/unnati-pt6974/pt6974_unnati/source/Audio/UrbanSound8K/audio'
    SAMPLE_RATE = 16000
    NUM_SAMPLES = 32000
    
    mel_spectogram = torchaudio.transforms.MelSpectrogram(
        sample_rate = SAMPLE_RATE,
        n_fft = 1024,
        hop_length = 512,
        n_mels = 64
    )
    usd = UrbanSoundDataset(ANNOTATION_FILE,
                             AUDIO_DIR,
                             mel_spectogram,
                             SAMPLE_RATE,
                             NUM_SAMPLES
                               )
    
    BATCH_SIZE = 128
    LEARNING_RATE =1e-5

    # dataset
    train_ds, test_ds = random_split(usd, [6900, len(usd)-6900])

    # dataloader 
    train_dl = DataLoader(train_ds,
                           batch_size=BATCH_SIZE,
                           shuffle=True)
    test_dl = DataLoader(test_ds,
                           batch_size=BATCH_SIZE,
                           shuffle=False)

    # instantiate model 
    model = CNNNetwork()
    # summary(model, (1, 64, 63))

    # initialize loss, optimiser
    loss_fn = nn.CrossEntropyLoss()
    opt= torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

    #train model
    epochs = 10

    for epoch in range(epochs):
        model.train()
        train_loss = 0
        test_loss = 0
        test_acc = 0
        for batch in train_dl:
            signal, label = batch
            # forward_pass
            preds = model(signal)
            # loss
            loss = loss_fn(preds, label)
            train_loss+=loss
            # zero_grad
            opt.zero_grad()
            # back propogation
            loss.backward()
            #step
            opt.step()
        
        train_loss = train_loss/len(train_dl)
        
        model.eval()
        with torch.inference_mode():
            for batch in test_dl:
                signal, label = batch
                # forward_pass
                preds = model(signal)
                # loss
                loss = loss_fn(preds, label)
                test_loss+=loss
                test_acc+=acc_fn(preds, label)
            
        
            test_loss = test_loss/len(test_dl)
            test_acc = test_acc/len(test_dl)

        print(f"Epoch: {epoch+1}, Train Loss: {train_loss : .3f}, Val Loss: {test_loss: .3f}, Val Acc: {test_acc: .3f}")
      
    # save model
    torch.save(model.state_dict(), 'audio_classification.pth')
        







