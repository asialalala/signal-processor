import PySimpleGUI as sg
from main import apply_effect

def create_window():
    layout = [
        [sg.Text('Wybierz plik audio:'), sg.Input(), sg.FileBrowse(key='file', button_text="Przeglądaj")],
        [sg.Text('Wybierz efekt:')],

        # Normalization Effect
        [sg.Radio('Normalizacja', 'effect', key='normalize', enable_events=True)],

        # Reverb Effect
        [sg.Radio('Pogłos', 'effect', key='reverb', enable_events=True)],
        [sg.pin(sg.Column([
            [sg.Text('Poziom pogłosu (0.0 - 1.0):')],
            [sg.Slider(range=(0, 1), resolution=0.1, orientation='h', key='reverb_amount')],
        ], key='reverb_params', visible=False))],

        # Echo Effect
        [sg.Radio('Echo', 'effect', key='echo', enable_events=True)],
        [sg.pin(sg.Column([
            [sg.Text('Opóźnienie echa (s):')],
            [sg.Slider(range=(0, 1), resolution=0.1, orientation='h', key='echo_delay')],
            [sg.Text('Współczynnik zaniku echa (0.0 - 1.0):')],
            [sg.Slider(range=(0, 1), resolution=0.1, orientation='h', key='echo_decay')],
        ], key='echo_params', visible=False))],

        # Pitch Shift Effect
        [sg.Radio('Zmiana wysokości dźwięku', 'effect', key='pitch_shift', enable_events=True)],
        [sg.pin(sg.Column([
            [sg.Text('Liczba półtonów do przesunięcia:')],
            [sg.Slider(range=(-12, 12), resolution=1, orientation='h', key='pitch_steps')],
        ], key='pitch_shift_params', visible=False))],

        # Tempo Change Effect
        [sg.Radio('Zmiana tempa', 'effect', key='tempo_change', enable_events=True)],
        [sg.pin(sg.Column([
            [sg.Text('Współczynnik zmiany tempa (np. 1.2 dla przyspieszenia o 20%):')],
            [sg.Slider(range=(0.5, 2), resolution=0.1, orientation='h', key='tempo_rate')],
        ], key='tempo_change_params', visible=False))],

        # Amplify Effect
        [sg.Radio('Podgłośnienie', 'effect', key='amplify', enable_events=True)],
        [sg.pin(sg.Column([
            [sg.Text('Współczynnik podgłośnienia (np. 1.5):')],
            [sg.Slider(range=(1, 2), resolution=0.1, orientation='h', key='volume_factor_amplify')],
        ], key='amplify_params', visible=False))],

        # Attenuate Effect
        [sg.Radio('Ściszenie', 'effect', key='attenuate', enable_events=True)],
        [sg.pin(sg.Column([
            [sg.Text('Współczynnik ściszenia (np. 0.5):')],
            [sg.Slider(range=(0, 1), resolution=0.1, orientation='h', key='volume_factor_attenuate')],
        ], key='attenuate_params', visible=False))],

        [sg.Button('Zastosuj efekt'), sg.Button('Wyjście')]
    ]
    return sg.Window('Procesor Dźwięku', layout, finalize=True)

def update_visibility(values, window):
    # Hide all parameter controls
    for key in ['reverb_params', 'echo_params', 'pitch_shift_params', 'tempo_change_params', 'amplify_params', 'attenuate_params']:
        window[key].update(visible=False)

    # Show parameter controls for the selected effect
    if values['reverb']:
        window['reverb_params'].update(visible=True)
    elif values['echo']:
        window['echo_params'].update(visible=True)
    elif values['pitch_shift']:
        window['pitch_shift_params'].update(visible=True)
    elif values['tempo_change']:
        window['tempo_change_params'].update(visible=True)
    elif values['amplify']:
        window['amplify_params'].update(visible=True)
    elif values['attenuate']:
        window['attenuate_params'].update(visible=True)

def main():
    window = create_window()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Wyjście':
            break

        # Update parameter visibility based on selected effect
        if event in ('normalize', 'reverb', 'echo', 'pitch_shift', 'tempo_change', 'amplify', 'attenuate'):
            update_visibility(values, window)

        # Apply the selected effect
        if event == 'Zastosuj efekt':
            file_path = values['file']
            if not file_path:
                sg.popup('Proszę wybrać plik audio.')
                continue

            # Determine which effect to apply and collect parameters
            if values['normalize']:
                apply_effect(file_path, 'normalize')
            elif values['reverb']:
                reverb_amount = values['reverb_amount']
                apply_effect(file_path, 'reverb', reverb_amount)
            elif values['echo']:
                delay = values['echo_delay']
                decay = values['echo_decay']
                apply_effect(file_path, 'echo', delay, decay)
            elif values['pitch_shift']:
                n_steps = int(values['pitch_steps'])
                apply_effect(file_path, 'pitch_shift', n_steps)
            elif values['tempo_change']:
                rate = values['tempo_rate']
                apply_effect(file_path, 'tempo_change', rate)
            elif values['amplify']:
                factor = values['volume_factor_amplify']
                apply_effect(file_path, 'amplify', factor)
            elif values['attenuate']:
                factor = values['volume_factor_attenuate']
                apply_effect(file_path, 'attenuate', factor)

            sg.popup("Efekt został zastosowany! Plik zapisany jako 'przetworzony_plik_audio.wav'.")

    window.close()

if __name__ == "__main__":
    main()
