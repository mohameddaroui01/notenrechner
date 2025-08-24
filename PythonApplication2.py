# Mini - Taschenrechner 
#-*- coding: utf-8 -*-
def add(a, b):
    return a + b
def sub(a ,b):
    return a - b
def mul (a ,b):
    return a * b
def div (a ,b):
    if b != 0:
        return a / b
    else :
        return " Fehler: Division durch 0!"
    
def main():
    print("Wilkommen zum Mini-Taschenrechner")
    print("Waehlen Sie eine Operation: +, -, *, /")
    op = input("Operation: ")
    a = float(input("Erste Zahl " ))
    b = float(input("Zweite Zhal " ))
    if op == "+":
        print ("Ergebnis =", add(a, b))
    elif op == "-":
        print ("Egebnis :" , sub(a, b))
    elif op == "*":
        print ( " Ergebnis :" , mul (a ,b))
    elif op == "/":
        print ("Ergebnis =" , div(a ,b))
    else:
        print (" Ungeltige Operation!")
    
if __name__ == "__main__":
    main()
    
   
        
     

    