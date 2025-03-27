# -*- coding: utf-8 -*-
# GPA 2025

# -------------
# Aufgabe 1
# -------------

# # Beginn: Beispiel für die Aufgabe:
#
# # Funktionalität: Gibt alle durch 5 teilbaren Zahlen im Intervall [6,56] aus.
# # Implementierung:
# #	* for-Schleife für das Iterieren über das Intervall
# # 	* In der Verzweigung wird mit Modulo-Berechnung festgestellt, ob der aktuelle Wert von i durch 5 teilbar ist
# # 	* Ist dies der Fall, wird die Zahl ausgegeben. Dabei wird bei print das Schlüsselwortargument end auf ' ' gesetzt
# #     und daher wird nicht in die nächste Zeile gesprungen
# #   * Die Zuweisung i=0 hat keine Auswirkung: am Beginn jedes Schleifendurchlaufs wird i auf den nächsten Wert aus
# #     range(6, 57) gesetzt, unabhängig vom aktuellen Wert. Dies passiert hier sofort nach der Zuweisung i=0, d.h.
# #     der Wert wird nie verwendet.
# for i in range(6, 57):
#     if i % 5 == 0:
#         print(i, end=' ')
#     i = 0
# print()
#
# # Alternative Implementierung mittels while Schleife
# # Hinweis: verschiedene Alternativen möglich
# numb = 6
# while numb < 57:
#     if numb % 5 == 0:
#         print(numb, end=' ')
#     numb += 1
# print()
#
# numb = 10
# while numb < 57:
#     print(numb, end=' ')
#     numb += 5
# print()

# //----- Ende Beispiel


# # Aufgabe 1.1:
# print('Aufgabe 1.1')
# # Funktionalität: Testet wie viele Zahlen von -25 bis 25 die Bedingung erfüllen.
# # Implementierung:
# # Mit Start und Stopp wird das zu testende Intervall festgelegt (wobei stop auch getestet wird).
# # der counter numb wird initialisiert (mit = 0), wenn die Bedingung "polynom > 0" erfüllt wird, wird
# # der counter um eins erhöht. Am Ende wird der counter ausgegeben.
# start = -25
# stop = 25
# numb = 0
# for x in range(start, stop+1):
#     if x**4 - 5 * x**3 + 2 * x**2 - 2025*x > 0:
#         numb += 1
# print('Das Ergebnis:', numb)
# print()
#
#
# # Alternative Implementierung als while-Schleife
# # sollte für alle natürliche Zahlen start ≤ stop gleiches Verhalten besitzen
# print('Aufgabe 1.1 mittels while:')
# # TODO: Ihre Implementierung (1.1) hier
# x = -25
# numb = 0
# while x in range(start, stop+1):
#     if x**4 - 5 * x**3 + 2 * x**2 - 2025*x > 0:
#         numb += 1
#     x += 1
# print('Das Ergebnis:', numb)
# print()
#
#
# print()
# print()


# Aufgabe 1.2:
print('Aufgabe 1.2')
# Funktionalität: TODO: Beschreibung der Funktionalität (1.2)
# Implementierung:
#       * TODO: Beschreibung der Implementierung (1.2)
text = input("Geben Sie bitte einen Text ein: ")
result = ''
idx = 0
while idx < len(text):
    if text[idx] in '0123456789':
        result = result + text[idx]
    idx += 1
print('Das Ergebnis:', result)
print()

# Alternative Implementierung als for-Schleife
print('Aufgabe 1.2 mittels for:')
# TODO: Ihre Implementierung (1.2) hier


print()
print()


# # Aufgabe 1.3:
# print('Aufgabe 1.3')
# # Funktionalität: TODO: Beschreibung der Funktionalität (1.3)
# # Implementierung:
# #       * TODO: Beschreibung der Implementierung (1.3)
# goal = int(input('Bitte eine natürliche Zahl eingeben (int): '))
# max_steps = 1000
# steps = 0
# start = 49.99
# while start < goal and steps < max_steps:
#     start *= 1.01
#     steps += 1
# print('Das Ergebnis:', steps)
#
# # Alternative Implementierung als for-Schleife
# # sollte auch für andere natürliche Zahlen für budget und max_steps funktionieren.
# print('Aufgabe 1.3 mittels for:')
# # TODO: Ihre Implementierung (1.3) hier
#
#
# print()
# print()
#
#
# # -------------
# # Aufgabe 2
# # -------------
#
# # 2.1
# print('\nAufgabe 2.1')
# # TODO
#
#
# # 2.2
# print('\nAufgabe 2.2')
# # TODO
#
#
# # 2.3
# print('\nAufgabe 2.3')
# # TODO
#
#
# # 2.4
# print('\nAufgabe 2.4')
# # TODO
#
#
# # -------------
# # Aufgabe 3
# # -------------
#
# # 3.1
# print('\nAufgabe 3.1: print_winner')
# # TODO: Funktion print_winner
#
#
# # 3.2
# print('\nAufgabe 3.2: occurs_more_often')
# # TODO: Funktion occurs_more_often
#
#
# # 3.3
# print('\nAufgabe 3.3: run_tournament')
# # TODO: Funktion run_tournament
#
#
# # -------------
# # Aufgabe 4
# # -------------
#
# # TODO: Kaffeemaschine implementieren
