# efekty.py
import numpy as np
import librosa
import scipy.signal as signal

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
    return librosa.effects.pitch_shift(y, sr, n_steps=n_steps)

def change_tempo(y, rate):
    """Zmienia tempo odtwarzania sygnału audio."""
    return librosa.effects.time_stretch(y, rate)

def amplify(y, factor):
    """Podgłaśnia sygnał audio przez mnożenie amplitudy przez factor."""
    return y * factor
