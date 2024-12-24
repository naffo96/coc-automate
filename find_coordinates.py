import pyautogui
import time
from pynput import mouse
import cv2
import numpy as np

descriptions = ['settings', 'logout pino', 'clicco naffo1', 'CASTELLO NAFFO1 click', 'info', 'meno', 'rimuovi', 'rimuovi OK', 'chiudi castello',
                 'click vuoto', 'CASTELLO NAFFO1 click', 'richiedi', 'Invia','settings', 'logoutnafo1','login pino', 'aprochat pino', 'dona pino',
                  'dona dirigibile pino', 'chiudi chat pino', 'addestra button pino', 'costruisci macchine pino', 'addestra dirigibile pino',
                  'chiudi caserma pino', 'settings pino', 'logout pino','clicco naffo2', 'CASTELLO NAFFO2 click', 'info', 'meno', 'rimuovi', 'rimuovi OK', 'chiudi castello',
                 'click vuoto', 'CASTELLO NAFFO2 click', 'richiedi', 'Invia','settings', 'logoutnafo2','login pino', 'aprochat pino', 'dona pino',
                  'dona dirigibile pino', 'chiudi chat pino', 'addestra button pino', 'costruisci macchine pino', 'addestra dirigibile pino',
                  'chiudi caserma pino', 'settings pino', 'logout pino','clicco naffo3', 'CASTELLO NAFFO3 click', 'info', 'meno', 'rimuovi', 'rimuovi OK', 'chiudi castello',
                 'click vuoto', 'CASTELLO NAFFO3 click', 'richiedi', 'Invia','settings', 'logoutnafo3','login pino', 'aprochat pino', 'dona pino',
                  'dona dirigibile pino', 'chiudi chat pino', 'addestra button pino', 'costruisci macchine pino', 'addestra dirigibile pino',
                  'chiudi caserma pino'];

# Posizione dell'array da stampare
current_index = 0

print("Posiziona il cursore sul punto che ti interessa e fai clic per vedere le coordinate.")

def on_click(x, y, button, pressed):
    global current_index
    if pressed:
        # Stampa le coordinate e l'elemento dell'array sulla stessa riga
        output = f"Clic rilevato alle coordinate: X: {x}, Y: {y}  "
        
        # Stampa l'elemento dell'array, se disponibile
        if current_index < len(descriptions):
            output += descriptions[current_index]
            current_index += 1
        else:
            output += "Non ci sono più elementi da stampare."
        
        print(output)

# Avvia il listener del mouse
with mouse.Listener(on_click=on_click) as listener:
    listener.join()