# Überschrift des Programms ausgeben
print("FLÄCHENRECHNER")
print("=" * 40)

# Liste für alle Räume (Name + berechnete Fläche)
raeume = []

# Variable für die gesamte Fläche aller Räume
gesamt = 0.0

# Hauptschleife: läuft so lange, bis der Benutzer "nein" eingibt
while True:

    # Raumname abfragen
    name = input("\nRaumname: ")

    # Prüfen, ob ein Name eingegeben wurde
    if name == "":
        print("Name darf nicht leer sein.")
        continue  # Zurück zum Anfang der Schleife

    # Raumtyp auswählen
    print("1 = Rechteck")
    print("2 = Mit Einbuchtungen")
    typ = input("Auswahl (1/2): ")

    # Fall 1: Einfacher rechteckiger Raum
    # Fläche = Länge * Breite
    if typ == "1":
        a = float(input("Länge: ").replace(",", "."))
        b = float(input("Breite: ").replace(",", "."))
        flaeche = a * b

    # Fall 2: Raum mit Einbuchtungen
    # Erst Gesamtfläche berechnen,
    # dann Einbuchtungen abziehen
    elif typ == "2":
        L = float(input("Außen-Länge: ").replace(",", "."))
        B = float(input("Außen-Breite: ").replace(",", "."))
        flaeche = L * B

        # Schleife für beliebig viele Einbuchtungen
        while True:
            weiter = input("Einbuchtung hinzufügen? (ja/nein): ").lower()

            # Wenn keine weitere Einbuchtung gewünscht ist
            if weiter == "nein":
                break

            # Einbuchtung hinzufügen und Fläche abziehen
            if weiter == "ja":
                a = float(input("  Länge: ").replace(",", "."))
                b = float(input("  Breite: ").replace(",", "."))
                flaeche -= a * b

            # Ungültige Eingabe
            else:
                print("Bitte ja oder nein eingeben.")

    # Ungültige Auswahl beim Raumtyp
    else:
        print("Ungültige Auswahl.")
        continue

    # Raum zur Liste hinzufügen
    # (Name und berechnete Fläche)
    raeume.append((name, flaeche))

    # Fläche zur Gesamtfläche addieren
    gesamt += flaeche

    # Ergebnis für diesen Raum anzeigen
    print(f"{name}: {flaeche:.2f} m²")

    # Aktuelle Gesamtfläche anzeigen
    print(f"Gesamt bisher: {gesamt:.2f} m²")

    # Benutzer fragen, ob ein weiterer Raum berechnet werden soll
    stop = input("Weiteren Raum berechnen? (ja/nein): ").lower()

    # Wenn nein → Schleife beenden
    if stop == "nein":
        break


# Übersicht aller Räume
print("\nÜBERSICHT")
print("=" * 40)

# Alle gespeicherten Räume ausgeben
for name, flaeche in raeume:
    print(f"{name}: {flaeche:.2f} m²")

# Trennlinie
print("-" * 40)

# Gesamtfläche ausgeben
print(f"Gesamtfläche: {gesamt:.2f} m²")