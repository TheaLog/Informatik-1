Nachziehstapel = ["gr7", "gl2", "+4", "ro5"]

while len(Nachziehstapel) !=0 :
    aktuelleKarte = Nachziehstapel.pop(0)

    if aktuelleKarte =="+4" :            #weil es zu kompliziert ist, zu prüfen, ob die Karte passt
        print("+4 Kann gespielt werden") # wir ersetzen hier nur die "passt"-Prüfung
        break
    else:
        print("Karte passt nicht, bitte weitere Karte ziehen")

if len(Nachziehstapel) == 0:
    print("Stapel ist leer")
else:
    print("Stapel ist nicht leer")
