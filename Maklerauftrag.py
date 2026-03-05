# Überschrift des Programms
print("FLÄCHENRECHNER")
print("========================================")

# Liste zum Speichern aller Räume (Name + Fläche)
raeume = []

# Variable für die gesamte Wohnfläche
gesamt = 0

# Steuerungsvariable für die Hauptschleife
fertig = False

# Hauptschleife läuft so lange, bis der Benutzer "nein" eingibt
while fertig == False:

    # Benutzer gibt den Namen des Raumes ein
    name = input("Raumname eingeben: ")

    # Falls kein Name eingegeben wurde
    if name == "":
        print("Kein Name eingegeben...")
    else:

        # Auswahl der Raumform
        print("Was für ein Raum?")
        print("1 Rechteck")
        print("2 Mit Einbuchtung")

        auswahl = input("Bitte 1 oder 2 eingeben: ")

        # -------------------------
        # OPTION 1: Rechteckiger Raum
        # -------------------------
        if auswahl == "1":

            # Länge und Breite einlesen
            # Komma wird durch Punkt ersetzt (wichtig für float)
            laenge = input("Länge in m eingeben: ").replace(",", ".")
            breite = input("Breite in m eingeben: ").replace(",", ".")

            # Umwandlung in Dezimalzahlen
            laenge = float(laenge)
            breite = float(breite)

            # Flächenberechnung (Länge × Breite)
            flaeche = laenge * breite

            print(f'Fläche ist: {flaeche} m²')

        # -------------------------
        # OPTION 2: Raum mit Einbuchtung
        # -------------------------
        elif auswahl == "2":

            # Außenmaße des Raumes
            L = float(input("Außen Länge in m: ").replace(",", "."))
            B = float(input("Außen Breite in m: ").replace(",", "."))

            # Grundfläche berechnen
            flaeche = L * B

            # Schleife für mehrere Einbuchtungen
            nochwas = True

            while nochwas:

                frage = input("Einbuchtung? ja/nein: ")

                if frage == "ja":

                    # Maße der Einbuchtung
                    a = float(input("Länge in m von Einbuchtung: ").replace(",", "."))
                    b = float(input("Breite in m von Einbuchtung: ").replace(",", "."))

                    # Fläche der Einbuchtung wird abgezogen
                    flaeche = flaeche - (a * b)

                    print(f'Neue Fläche: {flaeche} m²')

                elif frage == "nein":
                    # Keine weitere Einbuchtung → Schleife beenden
                    nochwas = False
                else:
                    print("Nicht verstanden...")

        # -------------------------
        # Falsche Eingabe bei der Auswahl
        # -------------------------
        else:
            print("Falsche Eingabe")
            flaeche = 0  # Damit keine Fehlermeldung entsteht

        # Raumname und berechnete Fläche speichern
        raeume.append([name, flaeche])

        # Fläche zur Gesamtfläche addieren
        gesamt = gesamt + flaeche

        print(f'Bisherige Gesamtfläche: {gesamt} m²')

        # Benutzer fragen, ob ein weiterer Raum eingegeben werden soll
        ende = input("Noch ein Raum? ja/nein: ")

        if ende == "nein":
            fertig = True  # Hauptschleife beenden


# -------------------------
# AUSGABE DER ERGEBNISSE
# -------------------------

print("\nErgebnis:")
print("----------------------------------------")

# Alle gespeicherten Räume ausgeben
for eintrag in raeume:
    print(eintrag[0], ":", eintrag[1], "m²")

print("----------------------------------------")
print(f'Gesamtfläche ist: {gesamt} m²')