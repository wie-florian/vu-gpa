# -*- coding: utf-8 -*-
# GPA 2025

# -------------
# Aufgabe 1
# -------------

# Beginn: Beispiel für die Aufgabe:

# Funktionalität: Gibt alle durch 5 teilbaren Zahlen im Intervall [6,56] aus.
# Implementierung:
#	* for-Schleife für das Iterieren über das Intervall
# 	* In der Verzweigung wird mit Modulo-Berechnung festgestellt, ob der aktuelle Wert von i durch 5 teilbar ist
# 	* Ist dies der Fall, wird die Zahl ausgegeben. Dabei wird bei print das Schlüsselwortargument end auf ' ' gesetzt
#     und daher wird nicht in die nächste Zeile gesprungen
#   * Die Zuweisung i=0 hat keine Auswirkung: am Beginn jedes Schleifendurchlaufs wird i auf den nächsten Wert aus
#     range(6, 57) gesetzt, unabhängig vom aktuellen Wert. Dies passiert hier sofort nach der Zuweisung i=0, d.h.
#     der Wert wird nie verwendet.
for i in range(6, 57):
    if i % 5 == 0:
        print(i, end=' ')
    i = 0
print()

# Alternative Implementierung mittels while Schleife
# Hinweis: verschiedene Alternativen möglich
numb = 6
while numb < 57:
    if numb % 5 == 0:
        print(numb, end=' ')
    numb += 1
print()

numb = 10
while numb < 57:
    print(numb, end=' ')
    numb += 5
print()

# //----- Ende Beispiel


# Aufgabe 1.1:
print('Aufgabe 1.1')
# Funktionalität: Testet wie viele Zahlen von -25 bis 25 die Bedingung erfüllen.
# Implementierung:
# Mit Start und Stopp wird das zu testende Intervall festgelegt (wobei stop auch getestet wird).
# der counter numb wird initialisiert (mit = 0), wenn die Bedingung "polynom > 0" erfüllt wird, wird
# der counter um eins erhöht. Am Ende wird der counter ausgegeben.
start = -25
stop = 25
numb = 0
for x in range(start, stop+1):
    if x**4 - 5 * x**3 + 2 * x**2 - 2025*x > 0:
        numb += 1
print('Das Ergebnis:', numb)
print()


# Alternative Implementierung als while-Schleife
# sollte für alle natürliche Zahlen start ≤ stop gleiches Verhalten besitzen
print('Aufgabe 1.1 mittels while:')
# Ihre Implementierung (1.1) hier
x = -25
numb = 0
while x in range(start, stop+1):
    if x**4 - 5 * x**3 + 2 * x**2 - 2025*x > 0:
        numb += 1
    x += 1
print('Das Ergebnis:', numb)
print()


print()
print()


# Aufgabe 1.2:
print('Aufgabe 1.2')
# Funktionalität: Die while loop durchsucht jedes Zeichen eines eingabe strings auf eine Ziffer und schreibt diese ins
#                 Ergebnis welches am Ende ausgegeben wird
# Implementierung:
#   Ein Index und ein leerer result string wird initialisiert. Die while loop läuft für jeden index im eingabe string
#   Mittels if wird der character im string mit dem aktuell index auf eine Zahl untersucht
#   wenn eine Zahl gefunden wird, wird diese in den result string am ende hinzugefügt.
#   Nachdem der ganze string gelesen wurde und die loop beendet ist, wird das ergebnis ausgegeben
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
# Ihre Implementierung (1.2) hier

result2 = ''
for i in range(0, len(text)):
    if text[i] in '0123456789':
        result2 = result2 + text[i]

print('Das Ergebnis:', result2)
print()

print()
print()


# Aufgabe 1.3:
print('Aufgabe 1.3')
# Funktionalität: Von einer Startzahl werden die Schritte gezählt wie oft die Startzahl um 1% erhöht werden muss
#                 um die Zahl zu erreichen. Beispiel - Geldanlage. Wie viele Jahre dauert es ist ein Sparziel zu
#                 erreichen mit einer Startanlage (start) und dem Ziel als eingabe.
# Implementierung:
#  Die while-loop läuft solange der Startwert kleiner als das Ziel ist und die maximale Schrittweise nicht erreicht ist.
#  *Zu Beginn user wird nach einem Ziel (int) gefragt.
#  *Die maximale Anzahl an Schritten sowie der Startwert werden als variablen festgelegt.
#  *Der Stepcounter wird auch ala Variable initialisiert (mit 0)
#  -- Am Ende wird die Anzahl der Schritte ausgegeben, welche nötig sind bis entweder start >= goal ist oder die maximale
#     Anzahl an Schritten erreicht wird.
goal = int(input('Bitte eine natürliche Zahl eingeben (int): '))
max_steps = 1000
steps = 0
start = 49.99
while start < goal and steps < max_steps:
    start *= 1.01
    steps += 1
print('Das Ergebnis:', steps)

# Alternative Implementierung als for-Schleife
# sollte auch für andere natürliche Zahlen für budget und max_steps funktionieren.
print('Aufgabe 1.3 mittels for:')
# Ihre Implementierung (1.3) hier
start_step = 0
steps2 = 0
start = 49.99   # reinitialize start
for step in range(start_step, max_steps):
    if start < goal:
        start *= 1.01
        steps2 += 1
print('Das Ergebnis:', steps2)


print()
print()


# -------------
# Aufgabe 2
# -------------

# 2.1
print('\nAufgabe 2.1')
n = 0
stop = 2048
result = ''
while n < stop + 1:
    if n > 0 and (n & (n - 1) == 0):
        result = result + str(n) + ' '
    n += 1
print(result)

# 2.2
print('\nAufgabe 2.2')
start = 50
stop = 100
cum_sum = 0
for i in range(start, stop+1):
    if i % 2 == 0:
        cum_sum += i
    elif i % 3 == 0:
        cum_sum += i
print(cum_sum)


# 2.3
print('\nAufgabe 2.3')
numbers = str(input('Geben Sie eine Liste von Zahlen ein: '))
output = ''
for i in range(0, len(numbers)):
    test = numbers[-(i+1)]
    if int(test) >= 5:
        output = output + test + '!'
    else:
        output = output + '!' + test
print(output)

# 2.4
print('\nAufgabe 2.4')
# TODO
input_string = input('Geben Sie eine Liste von Zahlen ein: ')
idx = 0
output = ''
while idx < len(input_string):
    i = int(input_string[idx])
    if idx < len(input_string)-1:
        j = int(input_string[idx+1])
        diff = j - i
        output = output + str(i) + '(' + str(diff) + ')'
    else:
        output = output + str(i)
    idx += 1
print(output)


# -------------
# Aufgabe 3
# -------------

# 3.1
print('\nAufgabe 3.1: print_winner')
def print_winner(first, second):
    m = len(first)
    n = len(second)
    print((n+2)*' ' + first)
    print(' ' + second + '|' + m * '-' + '|')
    print('|' + n * '-' + '|' + m * ' ' + '|')
    return


print_winner('a', 'b')

# 3.2
print('\nAufgabe 3.2: occurs_more_often')
def occurs_more_often(line, val_1, val_2):
    count_1 = 0
    count_2 = 0
    i = 0
    while i < len(line):
        if line[i] == val_1:
            count_1 += 1
        elif line[i] == val_2:
            count_2 += 1
        i += 1

    if count_1 >= count_2:
        result = val_1
    else:
        result = val_2

    return result


print(occurs_more_often('sommerschlussverkauf', 's', 'm'))
print(occurs_more_often('sommer', 'o', 'e'))
print(occurs_more_often('sommer', 'g', 'e'))
print(occurs_more_often('sommer', 'p', 'a'))

3.3
print('\nAufgabe 3.3: run_tournament')
def run_tournament(line, s1, s2, s3):
    first = s1
    second = s2
    if occurs_more_often(line, s2, s3) == s3:
        second = s3

    if occurs_more_often(line, s2, s1) == s2 and occurs_more_often(line, s2, s3) == s2:
        first = s2
        if occurs_more_often(line, s1, s3) == s1:
            second = s1
        else:
            second = s3
    elif occurs_more_often(line, s3, s1) == s3 and occurs_more_often(line, s3, s2) == s3:
        first = s3
        if occurs_more_often(line, s1, s2) == s1:
            second = s1
        else:
            second = s2

    print_winner(first, second)
    return


run_tournament('sommerschlussverkauf', 'o', 'm', 's')
run_tournament('sommerschlussverkauf', 'u', 'm', 's')
run_tournament('sommerschlussverkauf', 'm', 'u', 's')
run_tournament('sommerschlussverkauf', 's', 'u', 'm')

# -------------
# Aufgabe 4
# -------------
def welcome():
    print(r"""
###############
Lade Koffein...
###############
#----------------------------------#
Koffein geladen. Bereit zum Einsatz.
#----------------------------------#    
    """)
    return


def status(coffee, water, descale_counter):
    print()
    print('=== ' + 'Status: ')
    print('    ' + 'Bohnen: ' + str(coffee /1000) + ' kg')
    print('    ' + 'Wasser: ' + str(water/1000) + ' l')

    if descale_counter >= 3:
        print("HINWEIS! Maschine sollte entkalkt werden !")
    return


def options():
    print()
    print(r"""
=== (Hauptmenü) Deine Möglichkeiten :
    [ kaffee ] Kaffee machen
    [ bohnen ] Kaffeebohnen nachfüllen
    [ wasser ] Wasser nachfüllen
    [ entkalken ] Maschine entkalken
    [ quit ] Maschine ausschalten
    """)
    return


def refill_water(water):
    print()
    print(f">>> Wasserstand: {water} ml (max. 1l)")
    water_fill = int(input('Wassermenge in ml eingeben: '))
    if water + water_fill > 1000:
        print(f">>> Das war zu viel, {water_fill - (1000 - water)} ml Wasser verschwinden ins nichts.")
        water = 1000
    else:
        water = water + water_fill
    return water


def refill_coffee(coffee):
    print()
    print(f">>> Es sind {coffee} g im Behälter (max. 450 g)")
    coffee_fill = int(input('Bohnenmenge in g eingeben: '))
    if coffee + coffee_fill > 1000:
        print(f">>> Das war zu viel, {coffee_fill - (1000 - coffee)} g Bohnen verschwinden ins nichts.")
        coffee = 450
    else:
        coffee = coffee + coffee_fill
    return coffee


def goodbye():
    print()
    print('=== ' + 'Koffein wird entladen...')
    print('=== ' + 'Auf wiedersehen!')
    return


def make_coffee(coffee, water, descale_counter):
    # Asking for the coffee amount, checking input and available bean amount
    strength = int(input(f'Bitte Stärke wählen: \n  [1] schwach (15g), [2] mittel  (30g), [3] stark [45g]: '))
    if strength not in [1, 2, 3]:
        print(f" > Diese Auswahl habe ich nicht... < ")
        return coffee, water, descale_counter
    else:
        coffee_amount = 15 * strength
    if coffee_amount > coffee:
        print(">>> Ich habe zu wenig Bohnen. Bitte nachfüllen. \n >> Wähle [bohnen].")
        return coffee, water, descale_counter
    coffee = coffee - coffee_amount
    print(f">>> Mahle Bohnen : Bruiiiiii , grrrrrrrr , chk")

    # Water input, check
    size = int(input(f'Bitte die Kaffeegröße wählen: \n [1] klein (75 ml) , [2] mittel (150 ml) , [3] groß (225 ml): '))
    if size not in [1, 2, 3]:
        print(f" > Diese Auswahl habe ich nicht... < ")
        return coffee, water, descale_counter
    else:
        water_amount = 75 * size
    if water_amount > water:
        print(">>> Ich habe zu wenig Wasser. Bitte nachfüllen. \n >> Wähle [wasser].")
        return coffee, water, descale_counter
    water = water - water_amount
    print(f">>> Brühe ... Brühe ...")
    print(f">>> Kaffee ist fertig... klingt des ned unheimlich zärtlich...!")

    descale_counter += 1
    return coffee, water, descale_counter


def kaffeemaschine():
    welcome()
    coffee = 30  # in g
    water = 200  # in ml
    descale_counter = 0
    options()
    on = True
    while on:
        status(coffee, water, descale_counter)
        options()
        text = str(input('Deine Auswahl : ')).lower()
        if 'quit' in text:
            if text != 'quit':
                print(">>> Ich glaube du meinst \"quit\".")
            on = False
            goodbye()

        elif 'wasser' in text:
            if text != 'wasser':
                print(">>> Ich glaube du meinst \"wasser\".")
            water = refill_water(water)

        elif 'bohnen' in text:
            if text != 'bohnen':
                print(">>> Ich glaube du meinst \"bohnen\".")
            coffee = refill_coffee(coffee)

        elif 'entkalken' in text:
            print("--- Entkalkungsvorgang läuft ... abgeschlossen.")
            descale_counter = 0

        elif 'kaffee' in text:
            if text != 'kaffee':
                print(">>> Ich glaube du meinst \"kaffee\".")
            coffee, water, descale_counter = make_coffee(coffee, water, descale_counter)

        else:
            print(" > Ich verstehe deine Eingabe nicht. < ")

    return


kaffeemaschine()