import pyautogui
import time
from pynput import mouse
import cv2
import numpy as np
import mss

#Tempistiche: con miglioramento velocità add. 20%
# TEMPO scadenza sessione: 7.5mm
# TEMPO ADDESTRAMETNO 1 MACCHINA: 20 * 0.8 = 16mm (con boost 20%)
# LIMITE di tempo richiesta DONAZIONE per profilo: 10mm
# MACCHINE TOTALI in 1h: 60 / 16 = 3.75 donazioni all'ora
# MACCHINE RIMANENTI DA DONARE: 3524
# TEMPO TOTALE RIMANENTE hh = 3673 / (3.75) = 939.73hh

# Funzione per eseguire lo zoom out tramite la rotellina del mouse
def zoom_out(scrolls=10, delay=0.2):
    for _ in range(scrolls):
        pyautogui.scroll(-500)  # Scorri verso il basso per fare zoom out
        time.sleep(delay)

def trova_castello(castello_path, max_attempts=10, threshold=0.5):
    # Carica l'immagine del castello
    castello = cv2.imread(castello_path)
    
    # Verifica che l'immagine sia stata caricata correttamente
    if castello is None:
        raise ValueError("Impossibile caricare l'immagine del castello. Verifica il percorso.")

    # Converti l'immagine del castello in scala di grigi
    castello_gray = cv2.cvtColor(castello, cv2.COLOR_BGR2GRAY)
    h_castello, w_castello = castello_gray.shape

    attempts = 0

    with mss.mss() as sct:
        while attempts < max_attempts:
            # Cattura lo schermo
            monitor = sct.monitors[1]  # Usa il primo monitor
            img_screen = np.array(sct.grab(monitor))

            # Converti l'immagine dello schermo in scala di grigi
            img_screen_gray = cv2.cvtColor(img_screen, cv2.COLOR_BGRA2GRAY)

            # Applica il template matching per trovare il castello all'interno dello schermo
            result = cv2.matchTemplate(img_screen_gray, castello_gray, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            # Controlla se la corrispondenza è sufficientemente alta
            if max_val >= threshold:  # Soglia di corrispondenza più bassa
                # Coordinate del punto superiore sinistro
                x, y = max_loc
                # Calcola il centro del castello
                center_x = x + w_castello // 2
                center_y = y + h_castello // 2
                return center_x, center_y  # Restituisce le coordinate centrali del castello

            attempts += 1
            time.sleep(1)  # Aspetta un secondo prima di riprovare

    raise ValueError("Castello non trovato dopo il numero massimo di tentativi.")

def click_button(x, y):
    pyautogui.click(x, y)

def naffo_1():
    # Lista delle coordinate per i click
    # Array di coordinate (escluse quelle del CC; individuate tramite AI)
    coordinate1 = [(1757, 780),(1208,236),(1395, 722)]
    coordinate2 = [(599, 810), (745, 897), (788, 675), (1063, 639), (1596, 125), (640, 682)]
    coordinate3 = [(820, 801), (1114, 692), (1796, 797), (1208, 236), (1387, 583), (157, 513), (490, 848), (739, 376), (837, 376), (697, 479), (166, 787), (1110, 165), (701, 630), (1540, 168), (1789, 792), (1208, 236), (1438, 822)]
    coordinate4 = [(589, 812), (743, 897), (787, 679), (1076, 640), (1611, 133), (638, 686)]
    coordinate5 = [(807, 808), (1099, 680), (1796, 790), (1208, 236), (1461, 570), (172, 478), (491, 873), (739, 376), (837, 376), (700, 481), (159, 771), (1145, 180), (698, 653), (1550, 165), (1758, 785), (1208, 236), (1478, 945)]
    coordinate6 = [(600, 811), (742, 905), (777, 694), (1069, 640), (1614, 130), (640, 705)]
    coordinate7 = [(803, 803), (1088, 696), (1796, 778), (1208, 236), (1475, 609), (152, 486), (497, 860), (739, 376), (837, 376), (696, 488), (156, 775), (1116, 173), (721, 674), (1550, 161)]
    time.sleep(5)

    #ARRAY COORDINATE 1
    for x, y in coordinate1:
        click_button(x, y)
        time.sleep(5)  # Attesa per il tempo tra un clic e l'altro

    #CASTELLO NAFFO1 click
    zoom_out();
    time.sleep(2)
    coordinates_castello_naffo1 = trova_castello('C:\\Users\\danie\\Desktop\\GIOCHI\\CLASH OF CLANS\\AUTOMAZIONE QUEST MACCHINE\\Python\\castello_del_clan.png');
    click_button(*coordinates_castello_naffo1);
    print("Concluso coordinate 1")
    time.sleep(5)

    #ARRAY COORDINATE 2
    for x, y in coordinate2:
        click_button(x, y)
        print("Concluso coordinate 2")
        time.sleep(5)  # Attesa per il tempo tra un clic e l'altro

    #CASTELLO NAFFO1 click richiedo truppe
    zoom_out();
    time.sleep(2)    
    coordinates_castello_naffo1_2 = trova_castello('C:\\Users\\danie\\Desktop\\GIOCHI\\CLASH OF CLANS\\AUTOMAZIONE QUEST MACCHINE\\Python\\castello_del_clan.png');
    click_button(*coordinates_castello_naffo1_2);
    time.sleep(5)

    #ARRAY COORDINATE 3
    for x, y in coordinate3:
        click_button(x, y)
        print("Concluso coordinate 3")
        time.sleep(5)  # Attesa per il tempo tra un clic e l'altro

    #CASTELLO NAFFO2 click
    zoom_out();
    time.sleep(2)
    coordinates_castello_naffo2 = trova_castello('C:\\Users\\danie\\Desktop\\GIOCHI\\CLASH OF CLANS\\AUTOMAZIONE QUEST MACCHINE\\Python\\castello_del_clan.png');
    click_button(*coordinates_castello_naffo2);
    time.sleep(5)

    #ARRAY COORDINATE 4
    for x, y in coordinate4:
        click_button(x, y)
        print("Concluso coordinate 4")
        time.sleep(5)  # Attesa per il tempo tra un clic e l'altro

    #CASTELLO NAFFO2 click richiedo truppe
    zoom_out();
    time.sleep(2)
    coordinates_castello_naffo2_2 = trova_castello('C:\\Users\\danie\\Desktop\\GIOCHI\\CLASH OF CLANS\\AUTOMAZIONE QUEST MACCHINE\\Python\\castello_del_clan.png');
    click_button(*coordinates_castello_naffo2_2);
    time.sleep(5)

    #ARRAY COORDINATE 5
    for x, y in coordinate5:
        click_button(x, y)
        print("Concluso coordinate 5")
        time.sleep(5)  # Attesa per il tempo tra un clic e l'altro

   #CASTELLO NAFFO3 click
    zoom_out();
    time.sleep(2)
    coordinates_castello_naffo3 = trova_castello('C:\\Users\\danie\\Desktop\\GIOCHI\\CLASH OF CLANS\\AUTOMAZIONE QUEST MACCHINE\\Python\\castello_del_clan.png');
    click_button(*coordinates_castello_naffo3);
    time.sleep(5)

    #ARRAY COORDINATE 6
    for x, y in coordinate6:
        click_button(x, y)
        print("Concluso coordinate 6")
        time.sleep(5)  # Attesa per il tempo tra un clic e l'altro

    #CASTELLO NAFFO3 click richiedo truppe
    zoom_out();
    time.sleep(2)
    coordinates_castello_naffo3_3 = trova_castello('C:\\Users\\danie\\Desktop\\GIOCHI\\CLASH OF CLANS\\AUTOMAZIONE QUEST MACCHINE\\Python\\castello_del_clan.png');
    click_button(*coordinates_castello_naffo3_3);
    time.sleep(5)

    #ARRAY COORDINATE 7
    for x, y in coordinate7:
        click_button(x, y)
        print("Concluso coordinate 7")
        time.sleep(5)  # Attesa per il tempo tra un clic e l'altro

#Ciclo di automazione
#CONDIZIONI DI PARTENZA: profilo pino96 loggato
#MODIFICO INTERVAL IN BASE ALLE CONDIZIONI IN CUI SONO:
interval_20 = 3600; #20 min a macchina * 3 macchine == 60min = 3600s
interval_18 = 3240; #18 min a macchina * 3 macchine == 54min = 3240s
interval_18_potionx4 = 810; #4.5 min a macchina * 3 macchine == 13.5min = 810s
interval_16 = 2880; #16 min a macchina * 3 macchine == 48min = 2880s
interval_16_potionx4 = 720; #4 min a macchina * 3 macchine == 12*60 = 720s
interval_10_potionx4 = 432; #2.4 min a macchina * 3 macchine == 7.2*60 = 432s
#TEMPO DI ESECUZIONE TOTALE: 6min (intervallo di 5s per evitare stuck su rallentamenti connessione)
import time

minutes_total = 4 # Converti in minuti

while True:
    naffo_1()  # Funzione principale
    print("Inizio dello sleep per {} minuti...".format(minutes_total))

    # Ciclo per contare e stampare i minuti durante lo sleep
    for minute in range(minutes_total):
        time.sleep(60)  # Attendi un minuto
        print(f"Minuti trascorsi: {minute + 1} su {minutes_total}", end='\r')  # Sovrascrive la riga

    # Pulizia della riga dopo lo sleep
    print(" " * 50, end='\r')  # Cancella la riga stampata prima di cliccare il bottone

    # Reload della pagina
    click_button(728, 596)