Würfeln = [1, 2, 3, 4, 5, 6]
import random

print ("Sie kommen ins Gefängnis")
Anz_Wurf = 0

while Anz_Wurf < 3:
    stringA = input("Möchten Sie sich freikaufen? (y/n): ")
    if stringA == "y":
        break
    elif stringA == "n" :
        print("Bitte würfeln")
        Anz_Wurf += 1
        Würfel1 = random.choice(Würfeln)
        Würfel2 = random.choice(Würfeln)
        print("Die Zahlen lauten: ", Würfel1, "und", Würfel2)
        if Anz_Wurf <= 3 and Würfel1 == Würfel2:
            print("Pasch!")
            break
        elif Anz_Wurf < 3 and Würfel1 != Würfel2:
            print("kein Pasch")
            continue
        elif Anz_Wurf == 3 and Würfel1 != Würfel2:
            print("Sie haben 3 mal geworfen, Sie müssen sich freikaufen")
            break
    else :
        print("Bitte geben Sie y oder n ein")

print("Sie kommen aus dem Gefängnis frei")
