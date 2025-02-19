dayofweek = input("Wochentag: ")

match dayofweek :
    case "Montag":
        print("Montag")
    case "Dienstag":
        print("Dienstag")
    case "Samstag" | "Sonntag" :
        print(f"Es ist Wochenende, der Tag: {dayofweek} die nächsten 24 Stunden")
    case _:
        print(f"Unbekannter Wochentag: {dayofweek}")