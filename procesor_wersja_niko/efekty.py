# efekty.py
import numpy as np
import librosa
import scipy.signal as signal
import matplotlib.pyplot as plt

def normalize_audio(y):
    """Normalizuje sygnał audio do zakresu [-1, 1]."""
    return y / np.max(np.abs(y))

def add_reverb(y, sr, reverb_amount=0.5):
    """Dodaje pogłos do sygnału audio."""
    reverb_kernel = np.zeros(int(sr * 0.3))  # 300 ms pogłosu
    reverb_kernel[0] = 1
    reverb_kernel[int(sr * 0.03)] = reverb_amount  # 30 ms opóźnienia
    y_reverb = signal.fftconvolve(y, reverb_kernel, mode='full')
    return y_reverb[:len(y)]

def add_echo(y, sr, delay=0.2, decay=0.5):
    """Dodaje efekt echa do sygnału audio."""
    delay_samples = int(sr * delay)
    echo_signal = np.zeros(len(y) + delay_samples)
    echo_signal[:len(y)] = y
    echo_signal[delay_samples:] += decay * y
    return echo_signal[:len(y)]

def pitch_shift(y, sr, n_steps):
    """Zmienia wysokość dźwięku o podaną liczbę półtonów."""
    return librosa.effects.pitch_shift(y, sr=sr, n_steps=n_steps)

def change_tempo(y, rate):
    """Zmienia tempo odtwarzania sygnału audio."""
    return librosa.effects.time_stretch(y, rate=rate)

def amplify(y, factor):
    """Podgłaśnia sygnał audio przez mnożenie amplitudy przez factor."""
    return y * factor

def bass_soprano(y, sr,  bass_factor=1, soprano_factor=1):
    """Podgłaśnia basy mnoąc przez bass_factor i soprany mnozac przez soprano_factor. 
    Oparte na implementacji https://librosa.org/doc/main/auto_examples/plot_vocal_separation.html """
    S_full, phase = librosa.magphase(librosa.stft(y))
    # Tworzenie filtru, ktory podzieli dzwiekna na ten z czestotliwoscia ponizej i powyzej
    # mediany czestotliwosci wystepujacych w calym nagraniu
    S_filter = librosa.decompose.nn_filter(S_full,
                                       aggregate=np.mean,
                                       metric='cosine',
                                       width=int(librosa.time_to_frames(2, sr=sr)))
    S_filter = np.minimum(S_full, S_filter)
    
    margin_i, margin_v = 2, 10
    power = 2

    # Naloz maske aby podzielic nagranie na sopran i bas
    
    mask_i = librosa.util.softmask(S_filter,
                               margin_i * (S_full - S_filter),
                               power=power)

    mask_v = librosa.util.softmask(S_full - S_filter,
                               margin_v * S_filter,
                               power=power)

    S_soprano = mask_v * S_full
    S_bass = mask_i * S_full

    y_soprano = librosa.istft(S_soprano * phase)
    y_bass = librosa.istft(S_bass * phase)

    y_soprano = y_soprano * soprano_factor
    y_bass = y_bass * bass_factor


    y_processed = y_soprano + y_bass # tutaj chyba inaczej powinien byc dodany ten dzwiek
    return y_processed
