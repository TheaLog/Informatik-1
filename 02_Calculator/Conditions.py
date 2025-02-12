dayofweek = input("Bitte geben Sie den Wochentag ein: ")
time = int(input("Bitte geben Sie die Uhrzeit ein (Stunde im 24-Stunden-Format): "))

if dayofweek == "Montag":
    print("Heute ist Montag!")
    if time < 11:
        print("Guten Morgen!")
    elif time < 15:
        print("Frohes Arbeiten!")
    else:
        print ("Feierabend!")
else:
    print("Heute ist nicht Montag!")