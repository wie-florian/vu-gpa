# -*- coding: utf-8 -*-
# GPA 2024

# -------------
# Aufgabe 1
# -------------

# Beispiele aus der Angabe

3 + 4.0  # Addition zweier Zahlen, 7.0, float

'Hello' * 2  # String vervielfältigen, 'HelloHello', str (String)

# Ihre Lösungen ab hier:

2 + 2 * 3       # Multiplikation und anschließende Addition, 8, int (integer)

10 / 10 // 2    # Division mit anschließender modulo Operation (Division mit Rest), 0.0, float weil modulo 1/2

7 / (3 % 2)     # Klammer - Rest von ganzzahliger Division -> 1, int, anschließend division -> gibt immer float aus, 7.0

'0' + '1' * 4   # multiplikation und addition von '' = string, str, 01111

'ich' + 'und?'[0:3] + 'und?'[-2::-2]
# Addition von str, Intervall [x:y:z], x start (str beginnt bei 0, -1 letztes zeichen), y ende (nicht mehr dabei), z Schrittweite (wenn negativ von re nach li)
# ichunddu

'Reittier&otto'[1:0:-1]
# Intervall von str, e

True and 0  # a and b - Wertet a auf False aus, dann wird a zurückgegeben, Sonst wird b ausgewertet und der Wert von b zurückgegeben
# Wahrheitswert and 0, a ist True, also wird b ausgegeben,
# 0, int


bool('0' and 'a' in 'Hallo!')
# bool gibt True oder False aus, 0 = False, alles andere True, hier str, str immer True, wenn nicht anders definiert
# and vernküpft str '0' und str 'a' beide sind True, weil str 'Hallo!' auch True, Ausgabe True


(4 > 2) + bool(3)
# (...) ergibt True, bool(3) ergibt True, True + True = 2, int


# -------------
# Aufgabe 2
# -------------
print('\n\n############### Aufgabe 2')
# TODO: Lösung implementieren

# defininig cake size in easy units
r_cm = 15       # radius, cm
h_cm = 9        # hight, cm
N = 9           # piece count, no unit
rho_L = 0.3     # density, kg per L
k_g = 350       # calories per mass, kcal per 100_g
pi = 3.141592

# converting the units to SI
r = r_cm / 100      # cm -> m
h = h_cm / 100      # cm -> m
rho = rho_L * 1000  # kg per L -> kg per m^3
k = k_g * 10        # kcal per 100g -> kcal per kg


piece_v = (r**2 * pi * h) / N
piece_v_cm3 = piece_v * 1000 *1000  # m3 to cm3, since it is a more useful unit in that case

piece_cal = piece_v * rho * k

print('Alle Kuchenstücke sind ' + str(round(piece_v_cm3, 2)) + ' cm3 groß und haben ' + str(round(piece_cal,2)) + ' kcal!')

print('ungerundete Werte: ')
print('  1. Volumen: ' + str(piece_v_cm3))
print('  2. Energie: ' + str(piece_cal))




# -------------
# Aufgabe 3
# -------------

print('\n\n############### Aufgabe 3')
print('Willkommen im Expenditure Compliance Support Client.')

# um den Input bitten
budget = int(input('Wie groß ist das Budget? > '))
price = int(input('Was kostet das was du anschaffen willst? > '))

# Ausgaben identifizieren (1.)
# TODO: Zeilen markieren in denen etwas ausgegeben wird.

if 0 < price <= 200:
    print('Das liegt in deiner Verantwortung.')     #Ausgabe
elif price > 200:
    if 10_000 > budget > price:
        print('Es braucht die Unterschrift einer Budgetverantwortlichen!')  #Ausgabe
    elif budget < 10_000 and budget * 1.1 > price:
        print('Es braucht die Unterschrift zweier Budgetverantwortlichen!')     #Ausgabe
    elif price > budget:
        print('Das bleibt wohl eher ein Traum')     #Ausgabe
elif budget > 10_000:
    print('Das muss in einem Ausschuss diskutiert werden!') #Ausgabe
else:
    print('Das ist wohl eher ein Fall für die Sales-Abteilung!')    #Ausgabe


# Codeüberdeckung (2.)
# TODO: Geben Sie hier die geforderten Inputs mit der jeweils erwarteten Ausgabe an

# price = 50
# budget = 1000
# Erzeugte Ausgabe: Das liegt in deiner Verantwortung.

# price = 201
# budget = 1000
# Erzeugte Ausgabe: Es braucht die Unterschrift einer Budgetverantwortlichen!

# price = 201
# budget = 190
# Erzeugte Ausgabe: Es braucht die Unterschrift zweier Budgetverantwortlichen!

# price = 201
# budget = 100
# Erzeugte Ausgabe: Das bleibt wohl eher ein Traum

# price = -10
# budget = 10001
# Erzeugte Ausgabe: Das muss in einem Ausschuss diskutiert werden!

# price = -10
# budget = 1000
# Erzeugte Ausgabe: Das ist wohl eher ein Fall für die Sales-Abteilung!

# price = 201
# budget = 10001
# Erzeugte Ausgabe: $ kein output $

# Anzahl von "Wegen" durch die Struktur: 7

# Existiert ein "Weg" ohne Ausgabe? ja


# -----------------------
# Aufgabe 4 (Variante 1)
# -----------------------

print('\n\n############### Aufgabe 4')  # NICHT Teil der Ausgabe die in einem einzigen print-Statement erzeugt werden soll.
longitude = int(input('Längengrad (Longitude): '))
latitude = int(input('Breitengrad (Latitude): '))


if -180 <= longitude <= 180 and -90 <= latitude <= 90:  # (1)
    if latitude > 66 or latitude < -66:                 # (2)
        x = 'Es ist Brrr .... kalt! '
        if latitude > 66 :
            print(x + '(Untergrund: Eis)')
        elif latitude < -66:
            print(x + '(Untergrund: Land)')
    elif -23 < latitude < 23:                           # (3)
        x = 'Ohhh ... warm!'
        if latitude == 0:
            y = 'Es ist immer gleich. '
            if -80 <= longitude <= -35 or 10 <= longitude <= 45:
                print(y + '(Untergrund: Land)')
            elif 100 <= longitude <= 130:
                print(y + '(Untergrund: Gemischt)')
            else:
                print(y + '(Untergrund: Wasser)')
        else:
            print(x)
    else:
        print('Es ist Gemäßigt ... I guess.')
else:                                                   # (4)
    print('Out of this world!')
