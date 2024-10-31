import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from glob import glob
import librosa
import librosa.display
import IPython.display as ipd

from itertools import cycle

# Define colors
sns.set_theme(style="white", palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
color_cycle = cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])

# Read files
audio_files = glob('./Samples/*.wav')
y, sr = librosa.load(audio_files[0]) # samples, sample rate
print(f'y value: {y[:5]}')
print(f'y shape: {y.shape}')
print(f'sample rate: {sr}')

pd.Series(y).plot(figsize=(15,5), lw=1, title='Audio Wave', color=color_pal[0])
plt.show()

# Cut off values lower (quieter) then given threshold top_db
y_trimmed = librosa.effects.trim(y, top_db=100)[0]
pd.Series(y_trimmed).plot(figsize=(15,5), lw=1, title='Audio Wave trimmed top 20db', color=color_pal[1])
plt.show()

# show specific
pd.Series(y[30000:30500]).plot(figsize=(15, 5),
                  lw=1,
                  title='Raw Audio Zoomed In Example',
                 color=color_pal[2])
plt.show()

# create spectogram
D = librosa.stft(y)
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max) # transfer amplitude to db

# plot transformed data
fig, ax = plt.subplots(figsize=(15, 5))
img = librosa.display.specshow(S_db, x_axis='time', y_axis='log', ax=ax)
ax.set_title('Spectogram Example', fontsize=20)
fig.colorbar(img, ax=ax, format=f'%0.2f')
plt.show()

# Mel(ody) spectogram
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
S_db_mel = librosa.amplitude_to_db(np.abs(S), ref=np.max) # transfer amplitude to db

# plot transformed data
fig, ax = plt.subplots(figsize=(15, 5))
img = librosa.display.specshow(S_db_mel, x_axis='time', y_axis='log', ax=ax)
ax.set_title('Mel Spectogram Example', fontsize=20)
fig.colorbar(img, ax=ax, format=f'%0.2f')
plt.show()