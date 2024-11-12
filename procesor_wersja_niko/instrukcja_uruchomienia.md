
### Opis działania programu do przetwarzania dźwięku

Projekt jest realizacją procesora sygnałowego zaimplementowanego w języku programowym Python. 
Aplikacja umozliwia użytkownikowi wybór efektu i dostosowania parametrów oraz podglądu efektów na pliku dźwiękowym, z możliwością odtwarzania i pauzowania przetworzonego pliku.
Nie jest mozliwe nakładanie efektów na siebie.

Program składa się z trzech plików: `efekty.py`, `gui.py`, i `main.py`. Poniżej znajdziesz instrukcję krok po kroku oraz szczegóły dotyczące działania programu.

---

### Wykorzystane biblioteki
Poniezej opisano cel wykorzystania kazdej z bibliotek.
- numpy - używana do podstawowych operacji matematycznych i przetwarzania sygnału, np. *normalize_audio*
- librosa - zastosowana do analizy i przetwarzania dźwięku: *pitch_shift*, *change_tempo* oraz przetwarzanie spektrogramu w celu oddzielenia czestotliwosci niskich i wysokich
- scipy - używana jest głównie do przetwarzania sygnału za pomocą funkcji *fftconvolve*
- PySimpleGUI - służy do tworzenia GUI,
- soundfile - wykorzystana do zapisu przetworzonych plików audio w formacie WAV
- pygame - używana do obsługi dźwięku. *mixer* w pygame pozwala na odtwarzanie, zatrzymywanie i kontrolowanie dźwięków muzyki w aplikacji.


---

### Opis działania krok po kroku:
1. **Wybór pliku audio**: Po uruchomieniu `gui.py`, pojawi się okno, w którym możesz wybrać plik audio z komputera.
2. **Wybór efektu**: Wybierz jeden z efektów (normalizacja, pogłos, echo, itp.).
3. **Ustawienie parametrów efektu** (opcjonalnie): Dla niektórych efektów dostępne są dodatkowe parametry, np. poziom pogłosu, opóźnienie echa czy współczynnik pogłośnienia.
4. **Zastosowanie efektu**: Kliknij przycisk „Zastosuj efekt”. Plik audio zostanie przetworzony i zapisany jako `przetworzony_plik_audio.wav` w tym samym folderze, co plik źródłowy.

---

### Diagram przypadków uzycia
Ponizej przedstawiono diagram przypadków uzycia, na ktorym widoczne sa operacje dostepne dla urzytkownika.
W celu edycji diagramu mozna skorzystac z nastepujacego [linku](https://app.diagrams.net/#G1ui_W7STf7rl0ggz2sRm-IsosKM65SGZI#%7B%22pageId%22%3A%22CR_MfkM-ACaT6Vu6J4YW%22%7D),
a następnie pobrać edytowany plik i go podmienić.

![diagram przypadkow uzycia](./procesorSygnałowy.drawio.png)

---

### Opis słowny architektury planowanego oprogramowania

- Wejścia
  - *Plik audio* z rozszerzeniem .wav, który ma być przetwarzany
  - *Efekt dźwiękowy*, który ma być nałożony na wybrany plik
  - *Parametry efektu*, o ile są wymagane
- Przetwarzanie wewnętrzne 
  - *Moduł GUI* składa się z wyboru pliku audio, wyboru efektu oraz parametrów, a take przycisku odtwarzania i wstrzymywania nagrania.
  - *Moduł przetwarzania audio* umozliwia nałozenie efektu na wgrany plik audio. Wymaga podania sygnału *y* oraz częstotliwości jego próbkowania *sr*. Dostepne sa ponizej wymienione [efekty]
  - *Moduł odtwarzania audio* realizujący odtworzenie, wstrzymanie oraz wznowienie przetworzonego dźwięku.
- Wyjścia
  - *Przetworzony plik audio*, czyli wynik nałozenia efektu na wczytany plik,
  - *Interfejs użytkownika*, informujący o aktualnie wykonywanych działaniach.
- Struktura danych
  - *Tablica NumPy*, która przechowuje sygnał dźwiękowy *y* w postaci próbek.

---

### Opis teoretyczny zaimplementowanych efektów [efekty]

- Normalizacja - normalizuje sygnał audio *y* do zakresu [-1, 1],
- Dodawanie pogłosu - dodaje efekt pogłosu o wskazanym poziomie,
- Dodawanie echa - dodaje efekt echa z wskazanym opóźnieniem i współczynnikiem zaniku,
- Przesunięcie wysokości dźwięku (pitch shift) - zmienia wysokość dźwięku o wskazaną różnicę,
- Zmiana tempa - zwiększa lub zmniejsza tempo dźwięku o wskazany współczynnik bez zmiany częstotliwości dźwięku,
- Pogłośnienie i ściszenie - pogłaśnia lub ścisza dźwięk o wskazany współczynnik,
- Edycja basów i sopranów - umożliwia wzmocnienie basow lub sopranow.

---

### Instrukcja uruchomienia

#### 1. **Zainstaluj wymagane biblioteki**
Program wymaga kilku bibliotek do działania. Możesz je zainstalować, uruchamiając następującą komendę:

```bash
pip install numpy librosa scipy PySimpleGUI soundfile pygame
```

#### 2. **Opis plików**
   - **`efekty.py`**: Zawiera funkcje efektów dźwiękowych, które można zastosować do plików audio. Funkcje obejmują:
     - Normalizacja
     - Dodawanie pogłosu
     - Dodawanie echa
     - Przesunięcie wysokości dźwięku (pitch shift)
     - Zmiana tempa
     - Pogłośnienie i ściszenie
     - Edycja basów i sopranów
   - **`gui.py`**: Tworzy graficzny interfejs użytkownika przy użyciu `PySimpleGUI`. Umożliwia wybór pliku audio oraz efektu, który ma zostać zastosowany. Interfejs zapewnia również możliwość ustawienia parametrów dla wybranego efektu.
   - **`main.py`**: Obsługuje ładowanie pliku audio i zastosowanie wybranego efektu przy użyciu funkcji z pliku `efekty.py`. Zapisuje przetworzony plik jako `przetworzony_plik_audio.wav`.

#### 3. **Uruchomienie programu**
Aby uruchomić aplikację z interfejsem graficznym, wykonaj w terminalu następujące polecenie:

```bash
python gui.py
```
