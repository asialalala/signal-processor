# main.py
import librosa
import soundfile as sf
from efekty import amplify, normalize_audio, add_reverb, add_echo, pitch_shift, change_tempo
from pygame import mixer

mixer.init()
is_playing = False
sound : any
sound_channel = mixer.Channel(1)

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

def start(sound_path):
    global is_playing
    global sound
    global sound_channel
    is_playing = True
    sound = mixer.Sound(sound_path)
    sound_channel.play(sound)

def pause():
    global is_playing
    global sound_channel
    global sound
    if  is_playing :
        is_playing = False
        sound_channel.pause()
    else :
        sound_channel.unpause()
        is_playing = True
    

if __name__ == "__main__":
    print("Uruchom 'gui.py', aby użyć interfejsu.")
