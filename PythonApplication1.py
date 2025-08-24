# Notenrechner
# -*- coding: utf-8 -*-

def berechne_durchschnitt(noten):
    return sum(noten)/len (noten)

def main():
    print("Willkommen zum Notenrechner")
    
    eingabe = input("Bitte geben Sie Ihre Noten (mit Leerzeichen getrennt): ")
    # Beispiel: 1.7 2.3 3.0
    
    # Eingabe in Liste von Zahlen umwandeln
    noten = [float(x) for x in eingabe.split()]
    
    durchschnitt = berechne_durchschnitt(noten)
    print("Durchschnitt =", round(durchschnitt, 2))

if __name__ == "__main__":
    main()
