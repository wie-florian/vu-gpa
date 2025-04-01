# -*- coding: utf-8 -*-
# GPA 2025


# -------------
# Aufgabe 1
# -------------

# Beispiele aus der Angabe

2 + 2 * 3.0  # Multiplikation von 2 mit 3.0 gefolgt von Addition mit 2; 8.0; float

'Hello' * 2  # String mit sich selbst verketten, 'HelloHello', str (String)

# Ihre Lösungen ab hier:

257 - 2 ** 8    # 257 abzgl. 8-faches Potenzieren von 2 -> 1, int

4 * 2.5     # Multiplikation von 4 mit 2.5 9.0 -> 10.0, float

'1' + '2.0'     # Addition von strings -> 12.0, str

20 // (7 % 4)   # Division von 20 ohne Rest durch Rest von (7/4) -> int, weil '//' immer int

float('123456789'[2])   # Konvertiert index '2' aus dem string in einen float -> 3, float

'Donau Dampfschiff'[6:] + 'Donau Dampfschiff'[:5] # Schneiden des Strings ab index 6 bis zum Ende ':', plus die Zeichen des zweiten strings bis exkl 5. index -> Output str

4 > 3 and 8 > 7     # (bool value True, weil 4>3 wahr ist) logisches und (True, weil 8>7), da beide True -> True, bool

4 > (3 and 8) > 7   # (3 and 8) gibt nur int der zweiten Zahl, somit 4 > 8 > 7, weil 8 > 7 False --> False, bool

'b' and 'a' in 'gpa' # 'b' and 'a' is not a working operation, hence only checks if str'a' in str'gpa' -> True, bool

'Madam'[0::-1]  # Takes the first character of the string from index 0 to end (:), with reverse steps - and a step size 1 -> m, str


# -------------
# Aufgabe 2
# -------------
print('\n\n############### Aufgabe 2')
l_cm = 455  # Länge des Zimmers in cm
b_cm = 290  # Länge des Zimmers in cm
h_cm = 242  # Höhe des Zimmers in cm

l = l_cm / 100     # Länge des Zimmers in m
b = b_cm / 100     # Breite des Zimmers in m
h = h_cm / 100     # Höhe des Zimmers in m

e = 5       # Quadratmeterzahl pro Liter Farbe in cm²/L

Literpreis = 4.99   # Literpreis der Farbe in €/L

Flaeche = (2 * l * h + 2 * b * h + l * b)
Volumen_Farbe = Flaeche / e
Gesamtpreis = Volumen_Farbe * Literpreis

print(f"Sie werden eine Fläche von ca. {Flaeche} m² streichen. \n"
      f"Dafür benötigen Sie {round(Volumen_Farbe, 3)}L Farbe. \n"
      f"Diese kostet {round(Gesamtpreis, 3)}€.")

# -------------
# Aufgabe 3
# -------------

print('\n\n############### Aufgabe 3')
print('Compliance Check für deine Fahrt -- Cheap Transport Ltd.')


# um den Input bitten
planned_load  = int(input('Was ist das Gewicht der geplanten Ladung? > '))
max_load = int(input('Was ist die maximal zulässige Zuladung des Fahrzeugs? > '))

# Ausgaben identifizieren (1.)
# TODO: Zeilen markieren in denen etwas ausgegeben wird.

if planned_load >= 20 and 0 < max_load < 7500:
    if planned_load > max_load:
        print('Nicht gut - aber geht noch!')    # Ausgabe
    elif planned_load > max_load * 2:
        print('Das ist jetzt sogar für uns zu viel.')   # unerreichba, da wenn erreicht, voerheriges auch immer erreicht
    elif planned_load == max_load:
        print('Punktlandung')   # Ausgabe
    else:
        print('Mehr Ladung möglich!')   # Ausgabe
else:
    if planned_load < 20:
        print('Nur 20kg? Brings mim Fahrrad!')
    if max_load >= 7500:
        print('Dafür haben wir keinen Führerschein!')



# Codeüberdeckung (2.)
# planned_load = 21
# max_load = 1
# Erzeugte Ausgabe: Nicht gut - aber geht noch!

# planned_load = 21
# max_load = 21
# Erzeugte Ausgabe: Punktlandung

# planned_load = 5
# max_load = 5000
# Erzeugte Ausgabe: Nur 20kg? Brings mim Fahrrad!

# planned_load = 5
# max_load = 8000
# Erzeugte Ausgabe: Nur 20kg? Brings mim Fahrrad! und Dafür haben wir keinen Führerschein!

# planned_load = 21
# max_load = 8000
# Erzeugte Ausgabe: Dafür haben wir keinen Führerschein!

# planned_load = 20
# max_load = 20
# Erzeugte Ausgabe: Punktlandung

# planned_load = TODO
# max_load = TODO
# Erzeugte Ausgabe: TODO

# Existiert ein "Weg" ohne Ausgabe? nein


# -----------------------
# Aufgabe 4 (Variante 1)
# -----------------------
print('Japanische Stockwerke')
print(
    f"In Japan werden Stockwerke mit einer Zahl und einem Buchstaben gekennzeichnet. \n"
    f"Die Zahl gibt die Stockwerksnummer vom Erdgeschoss an. \n"
    f"Der Buchstabe kennzeichnet ob das Stockwerk ober (F) oder unter (B) dem Erdgeschoss liegt. \n"
    f"Die Zahl 4 wird meist ausgelassen. \n \n"
    f"Dieses Programm konvertiert ein japanisches Stockwerk zu einem österreichischen Stockwerk. \n"
)

choice = str(input("Geben Sie ein japanisches Stockwerk ein:"))

digit = int(choice[0:len(choice) - 1])
letter = str(choice[-1])

oe_vz = ""
oe_nummer = 0

if digit < 5:
    oe_nummer = digit - 1
elif digit >= 5:
    oe_nummer = digit - 2
else:
    print('Das sollte nicht passieren.')

if letter == "B":
    oe_vz = "-"
    oe_nummer = oe_nummer + 1


if digit == 4:
    print(f"Ein japanisches Stockwerk mit der Zahl 4 wird meist ausgelassen. \n"
          f"Sollte es doch vorkommen entspricht es dem {oe_vz}{oe_nummer}.Stock.")
else:
    print(f"Das Stockwerk {choice} entspricht dem {oe_vz}{oe_nummer}.Stock.")
