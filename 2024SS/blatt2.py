# -*- coding: utf-8 -*-
# GPA 2024

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
for i in range(6, 57):
    if i % 5 == 0:
        print(i, end=' ')
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
# Funktionalität: TODO: Beschreibung der Funktionalität (1.1)  [nur 3/4 benötigt]
# Implementierung:
#       * TODO: Beschreibung der Implementierung (1.1) [nur 3/4 benötigt]
r = 7       # Alternative Implementierung sollte für natürliche Zahlen r > 0 gleiches Verhalten besitzen
value = 0
for a in range(0, 11):
    value += a * r
    print(a, '*', r, '=', a * r)
print('Und in Summe macht das:', value)
print()

# Alternative Implementierung als while-Schleife
print('Aufgabe 1.1 mittels while:')
# TODO: Ihre Implementierung (1.1) hier


print()
print()

# Aufgabe 1.2:
print('Aufgabe 1.2')
# Funktionalität:
# Die while Schleife zieht von a solange den Wert b ab, bis b größer oder gleich groß wie a ist. Bei jeder
# Ausführung wird 'working...' geschrieben und am Ende 'Ergebnis: [Endwert von a]'
# Implementierung:
# Die While-Schleife läuft solange der Mathematische Ausdruck erfüllt wird also der boolsche Wert 'True' ist.
# In der Schleife wird dann jeweils a = a - b in abgekürzter Schreibweise berechnet und somit der Wert a jedesmal
# angepasst und 'working...' ausgegeben. Wenn der boolsche Wert 'False' ausgegeben wird also a <= b ist läuft die
# Schleife nicht mehr und der neue Wert von a wird ausgegeben.
a = 13  # Alternative Implementierung sollte für natürliche Zahlen a, b > 0 gleiches Verhalten besitzen
b = 3
while a - b > 0:
    a -= b
    print('working...', end=' ')
print('\nErgebnis:', a)
print()

# Alternative Implementierung als for-Schleife
print('Aufgabe 1.2 mittels for:')
a = 13
b = 3
for i in range(a//b):
    if a > b:
        a -= b
        print('working...', end=' ')
    else:
        pass
print('\nErgebnis:', a)
print()

print()
print()

# Aufgabe 1.3:
print('Aufgabe 1.3')
# Funktionalität: TODO: Beschreibung der Funktionalität (1.3) [nur 3/4 benötigt]
# Implementierung:
#       * TODO: Beschreibung der Implementierung (1.3) [nur 3/4 benötigt]
line = input('Bitte einen Text eingeben: ')
value = 0
idx = 0
while idx < len(line) and value >= 0:
    if line[idx] in '0123456789':
        value += int(line[idx])
    else:
        value = -1
    idx += 1
print('Text war keine Zahl! Fehlercode:' if value < 0 else 'Ziffernsumme:', value)
print()

# Alternative Implementierung als for-Schleife
print('Aufgabe 1.3 mittels for:')
# TODO: Ihre Implementierung (1.3) hier


# print()
# print()

# Aufgabe 1.4:
print('Aufgabe 1.4')
# Funktionalität: Es wird ein Raster an Zahlen erstellt mit jeweils zehn Spalten und Zeilen. Dabei wird
# in jeder Zeile entweder ['Spaltenindex'] oder ['Spaltenindex'+] ausgegeben, wobei dies abhängig von der Zeile ist.
# die letzte Ziffer ohne + gibt dabei die Zeilennummer an.
# Implementierung:
# Hier werden verschachtelte for schleifen verwendet, wobei i in der range(0, 10) läuft. und dann eine Schleife
# von (0, i+1), also bis zum aktuellen Zeilenindex läuft, welcher i ist. Damit i in der range inkludiert ist müssen
# wir +1 schreiben. die zweite Schleife läuft dann von (i+1, 10) also für jeden Index der noch nicht in der ersten
# Schleife dran kam.

for i in range(0, 10):
    for j in range(0, i + 1):
        print('[', (j + 1), '] ', sep='', end='')
    for j in range(i + 1, 10):
        print('[', (j + 1), '+]', sep='', end='')
    print()
print()

# Alternative Implementierung als while-Schleife
print('Aufgabe 1.4 mittels while:')

i = 0
while i < 10:
    j = 0
    while j < i+1:
        j += 1
        print('[', (j), '] ', sep='', end='')
    while j < 10:
        j += 1
        print('[', (j), '+]', sep='', end='')
    i += 1
    print()

print()
print()

# -------------
# Aufgabe 2
# -------------

# 2.1
for i in range(10, 30+1):
    if i % 3 == 0:
        print(i, ' ', sep='', end='')
    elif i % 7 == 0:
        print(i, ' ', sep='', end='')
    else:
        pass


print()
print()


# 2.2
x = 5
sum = 0



while True:
    if (-2 * x ** 3 + 25 * x ** 2 - 5 * x + 2024) >= 0:
        sum += x
        x += 1
    else:
        print('x: ', x, ', Summe: ', sum)
        break

print()
print()

# 2.3
text = input('Input your own string and let the magic begin: ')
n_g = 0
n_p = 0

print('Enigma is doing its magic...')

print('Here you go:')

for i in range(0, len(text)):
    if text[i] == 'g':
        n_g += 1
    elif text[i] == 'p':
        n_p += 1
    else:
        pass
    if n_g > n_p:
        print('+', sep='', end='')
    elif n_g < n_p:
        print('-', sep='', end='')
    else:
        print('=', sep='', end='')
    i += 1


print()
print()


# 2.4
string = input('Input your own string: ')
i = 0

while i <= (len(string)-2):
    if string[i+1] != string[i]:
        print(string[i],end='')
    else:
        i = len(string)
    i += 1


print()
print()


# -------------
# Aufgabe 3
# -------------

# 3.1
# TODO: Funktion  print_box
def print_box(name):
    name = str(name)
    frame = ('*' * (len(name) + 8) + '\n')
    line = ('=== ' + name + ' ===' + '\n')
    return frame + line + frame


x = print_box('GPA Teilnehmer:in')
print(x)

y = print_box('Abgabe Aufgabenblatt 2')
print(y)

z = print_box('O..O')
print(z)

a = print_box(123)
print(a)

print()
print()

# 3.2
# TODO: Funktion extract
def extract(ext):
    temp = ''
    for i in range(len(ext)):
        i += 1
        if ext[i-1] == '>' and ext[i+1] == '<':
            temp += (ext[i])
        else:
            pass
    return temp

x = extract('D>u<, und >du<, u>n<d du! D>o<ch!')
print(x)

y = extract('>nix<>!!')
print(y)

z = extract('>G<r¨uß >P<aul >A<bends>!<')
print(z)

print()
print()

# 3.3
# TODO: Funktion showcase
def showcase(msg):
    x = extract(msg)
    y = print_box(x)
    return y

z1 = showcase('>G<r¨uß >P<aul >A<treides>!<')
print(z1)

z2 = showcase('>Re<turn> <to sender')
print(z2)

z3 = showcase('>><<')
print(z3)

print()
print()


# -------------
# Aufgabe 4
# -------------

# TODO: GPA-Chatbot implementieren

name_bot = 'Hallo ich bin GPA, ein ganz normales Pferd'


def logo():
    print(r"""
               ._ o o
               \_`-)|_
              ,""       \ 
            ,"  ## |   ಠ ಠ. 
          ," ##   ,-\__    `.
        ,"       /     `--._;)
      ,"     ## /
    ,"   ##    /

                """'\r')


def banner(name):
    frame = ('*' * (len(name)) + '\n')
    line = (name + '\n')
    print(frame + line + frame)


def helps():
    title = 'Befehlsübersicht: \n'
    cmd1 = 'Hilfe ' + '.' * 7 + ' ruft diese Hilfe auf \n'
    cmd2 = 'Countdown ' + '.' * 3 + ' Startet einen Countdown \n'
    cmd3 = 'Servus ' + '.' * 6 + ' beendet das Programm \n'
    print(title + cmd1 + cmd2 + cmd3)


def countdown():
    i = int(input(' Read, Set, ... \n Moment, wo soll ich beginnen? \n >  '))
    x = 0
    while i > 0:
        print('--> ' + str(i) + ' <--')
        x = int(input('Wollen wir Abkürzen? \n '
                      '[Ja: Schritte eingeben, Nein: Zahl <= 0 eingeben] '
                      '\n > '))
        if x > 0:
            i = i - x
        else:
            i = i - 1
    print('Ring ... Ring ... Ring. Countdown beendet')
    return


def reply(rng):
    if rng == 0:
        print('Echt?')
        rng += 1
    elif rng == 1:
        print('Wirklich?')
        rng += 1
    else:
        print('Erzähl mir mehr!')
        rng = 0
    return rng


def GPA():
    i = True
    j = 0
    rng = 0
    logo()
    banner(name_bot)
    name = input('Wie ist dein Name? ')
    while i is True:
        text = input(name + '> ')
        if text.lower() == 'hilfe':
            helps()
        elif text.lower() == 'countdown':
            countdown()
        elif text.lower() == 'servus':
            return 'Tschau mit au!'
        else:
            rng = reply(rng)

c = GPA()
print(c)



