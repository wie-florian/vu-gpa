# -*- coding: utf-8 -*-
# GPA 2025


# -------------
# Aufgabe 1
# -------------

# Beispiele aus der Angabe

2 + 2 * 3.0  # Multiplikation von 2 mit 3.0 gefolgt von Addition mit 2; 8.0; float

'Hello' * 2  # String mit sich selbst verketten, 'HelloHello', str (String)

# Ihre Lösungen ab hier:

# TODO:


# -------------
# Aufgabe 2
# -------------
print('\n\n############### Aufgabe 2')
# TODO: Lösung implementieren


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

if planned_load >=  20 and 0 < max_load < 7500:
    if planned_load > max_load:
        print('Nicht gut - aber geht noch!')
    elif planned_load > max_load * 2:
        print('Das ist jetzt sogar für uns zu viel.')
    elif planned_load == max_load:
        print('Punktlandung')
    else:
        print('Mehr Ladung möglich!')
else:
    if planned_load < 20:
        print('Nur 20kg? Brings mim Fahrrad!')
    if max_load >= 7500:
        print('Dafür haben wir keinen Führerschein!')
        

# Codeüberdeckung (2.)
# TODO: Geben Sie hier die geforderten Inputs mit der jeweils erwarteten Ausgabe an und
#       markieren Sie im Code oben alle Zeilen mit Ausgabe die nie erreicht werden.
#       (Hinweis: es kann auch mehr oder weniger als die unten vorbereitete Anzahl an
#                 Antwortmöglichkeiten geben. Bitte entsprechend anpassen.

# planned_load = TODO
# max_load = TODO
# Erzeugte Ausgabe: TODO

# planned_load = TODO
# max_load = TODO
# Erzeugte Ausgabe: TODO

# planned_load = TODO
# max_load = TODO
# Erzeugte Ausgabe: TODO

# planned_load = TODO
# max_load = TODO
# Erzeugte Ausgabe: TODO

# planned_load = TODO
# max_load = TODO
# Erzeugte Ausgabe: TODO

# planned_load = TODO
# max_load = TODO
# Erzeugte Ausgabe: TODO

# planned_load = TODO
# max_load = TODO
# Erzeugte Ausgabe: TODO

# Existiert ein "Weg" ohne Ausgabe? TODO (ja|nein)


# -----------------------
# Aufgabe 4 (Variante 1)
# -----------------------

print('\n\n############### Aufgabe 4')

# TODO: Lösung implementieren

