# main.py
import librosa
import soundfile as sf
from efekty import amplify, normalize_audio, add_reverb, add_echo, pitch_shift, change_tempo

def apply_effect(file_path, effect_name, *args):
    # Wczytaj plik audio
    y, sr = librosa.load(file_path, sr=None)

    # Zastosowanie wybranego efektu
    if effect_name == 'normalize':
        y_processed = normalize_audio(y)
    elif effect_name == 'reverb':
        y_processed = add_reverb(y, sr, *args)
    elif effect_name == 'echo':
        y_processed = add_echo(y, sr, *args)
    elif effect_name == 'pitch_shift':
        y_processed = pitch_shift(y, sr, *args)
    elif effect_name == 'tempo_change':
        y_processed = change_tempo(y, *args)
    elif effect_name == 'amplify':
        y_processed = amplify(y, *args)
    else:
        print("Nieznany efekt.")
        return

    # Zapis przetworzonego pliku
    output_path = 'przetworzony_plik_audio.wav'
    sf.write(output_path, y_processed, sr)
    print(f"Efekt został zastosowany i zapisany w '{output_path}'.")

if __name__ == "__main__":
    print("Uruchom 'gui.py', aby użyć interfejsu.")
