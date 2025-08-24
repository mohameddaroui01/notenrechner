# data_logger_plot.py
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt 

def analyse_daten(daten):
    print("Anzahl Messwerte: ", len(daten))
    print("Minimum:", min(daten))
    print("Maximum: ", max(daten))
    print("Durchschnitt:", round(sum(daten)/len(daten), 2))
    
    plt.plot(daten, marker="o")
    plt.title("Messwerte Verlauf")
    plt.xlabel("Messung")
    plt.ylabel("wert")
    plt.show()
def main():
    print("Daten-Logger gestartet")
    eingabe = input("Bitte Messwerte eingaben (mit Leerzeichen getrennt): ")
    try:
          daten = [float(x) for(x) in eingabe.split()]
    except ValueError:
          print("Fehler: Bitte nur Zahlen eingeben! ")
          return
    if not daten:
        print("Keine Daten. ")
        return 
    analyse_daten(daten)
if __name__ == "__main__":
    main() 
