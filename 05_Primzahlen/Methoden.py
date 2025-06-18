from math import sqrt

def is_prime(number: int):
    
    sq_num = int(sqrt(number))
    zaehler = 2
    while sq_num >= zaehler:
        rest = number % zaehler
        if rest == 0:
            return False
        zaehler += 1   
    return number != 1

Eingabe= input ("Geben Sie eine Zahl ein: ")
Zahl = int(Eingabe)
Ergebnis = is_prime(Zahl)
if Ergebnis == True:
    print("Die Zahl ist eine Primzahl")
else:
    print ("Die Zahl ist keine Primzahl")