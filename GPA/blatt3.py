# -*- coding: utf-8 -*-
# GPA 2025

# -------------
# Aufgabe 1
# -------------

def count_unfollowed(line, symbol, blocks):
    # print(line)
    count = 0  # Starte den counter

    # for loop für jeden index in line außer den letzten
    for i in range(len(line)-1):
        # Test ob line[i] gleich dem symbol und ob der folgende nicht in blocks
        if line[i] == symbol and line[i+1] not in blocks:
            # print(line[i], line[i+1])
            count += 1  # wenn zutrifft erhöhe counter um 1

    # Teste ob das letzte Zeichen gleich dem Symbol, da vorher ausgelassen
    # es gibt kein nachfolgendes zeichen, also muss dies nicht geprüft werden
    if line[-1] == symbol:
        count += 1

    # print(count)
    return count

def fun_with_numbers(line):
    line = line + ' '   # add space after line so we can loop through the whole line
    summe = 0
    ignore_next = True

    # print(line)
    for i in range(len(line)):
        if line[i].isdigit() and line[i+1] != '?':
            if ignore_next:
                ignore_next = False
                # print(f"ignore {line[i]}")
            else:
                summe += int(line[i])
                ignore_next = True
                # print(f"add {line[i]}")

    # print(summe)
    return summe

def visualize_standings(p1, p2, ratio, length = 10, p1_symb = '#', p2_symb = '-'):
    # Startet die Ausgabe mit [] um p1
    ausgabe = f'[{str(p1)}]'
    # p1_symb wird so oft hinzugefügt wie ratio*length abgerundet ist
    # int schneidet komma einfach weg, somit wird immer abgerundet
    # für p2_symb wird genau umgekehrt gearbeitet, somit werden es auch nie mehr symbole als length
    ausgabe += p1_symb * int(ratio * length)
    ausgabe += p2_symb * (length - int(ratio * length))
    # Zum Abschluss noch p2 anhängen
    ausgabe += f'[{str(p2)}]'
    # print(ausgabe)
    return ausgabe

# Enthält alle Aufrufe der Funktionen aus Aufgabe 1
def exercise1():
    count_unfollowed('eis essen kennt keine grenzen', 'e', 'in')
    count_unfollowed('2025-02-29', '2', '-500')
    count_unfollowed('99 Luftballons, nicht 9', '9', '')
    count_unfollowed('Der Sommer kann kommen', 'm', 'mE')

    fun_with_numbers('12?34/5?678')
    fun_with_numbers('2025?')
    fun_with_numbers('1.?2.3.4.5??6.?')
    fun_with_numbers('nur 1 oder 2?')

    visualize_standings('Player1', 'Player2', 0.5, 10, '#', '-')
    visualize_standings('Player1', 'Player2', 0.5)
    visualize_standings('Player1', 'Player2', 0.5, 8)
    visualize_standings('Red', 'Blue', 0.75, p1_symb='>', p2_symb=':')
    visualize_standings('Ryu', 'Ken', 0.2, 11)
    visualize_standings('Ryu', 'Ken', 0.09, 10)
    
    return

# -------------
# Aufgabe 2
# -------------
def validate_floor_name(name):
    """
    Validating if name is a valid japanese floor name.

    :param name: to be tested floorname
    :return: True if name is valid, False otherwise
    """
    flag = True # Using a flag that is true by default, and set to false if some criteria are not met

    if name[-1] not in 'BF':    # Test if last is B or F
        flag = False
    for i in range(len(name)-1):    # Check if every character is an int except last
        if name[i] not in '0123456789':
            flag = False
    if name[0] not in '123456789':  # Check if first digit is a 0
        flag = False

    # print(flag)
    return flag

def translate_floor_plan(name):
    """
    Translate japanese floor to western floor.
    :param name: to be tested
    :return: translated floor as int
    """
    floor = int(name[:-1])
    if name[-1] == 'F':
        floor -= 1
    elif name[-1] == 'B':
        floor = -floor

    # print(type(floor))
    return floor

def print_translation(*floors):
    """
    Write a text based on the translated floor names.
    :param floors: any number of floors
    :return: text as str
    """
    ausgabe = 'Kein Stock\n\n'  # default return
    valid_floors = []   # initializing list for validating if floor name is correct
    translated_floors = []  # initializing list for translated floor names

    for floor in floors:    # validating all floor in floors
        if validate_floor_name(floor):
            # print(floor)
            valid_floors.append(floor)  # append floor if it is valid

    for floor in valid_floors:  # translating all valid floors
        translated_floors.append(translate_floor_plan(floor))

    if translated_floors:   # if translated floors is not empty, overwrite ausgabe with new text
        i = 0
        first = True    # to flag the first floor
        while i < len(translated_floors):
            if first:   # different text for first floor
                ausgabe = f'Da lief ich in den {translated_floors[i]}. Stock\n'
                first = False   # setting flag after this
            else:   # text for all other floors
                ausgabe += f'dann lief ich in den {translated_floors[i]}. Stock\n'
            if i == len(translated_floors) - 1: # if end of list is reached, append ending
                ausgabe += '... und aus.\n\n'
            i += 1

    # print(valid_floors)
    # print(translated_floors)
    # print(ausgabe)
    return str(ausgabe)

def exercise2():
    validate_floor_name('1F')
    validate_floor_name('0F')
    validate_floor_name('F')
    validate_floor_name('2A')
    validate_floor_name('5B')
    validate_floor_name('12F')
    validate_floor_name('0123F')

    translate_floor_plan('1F')
    translate_floor_plan('1B')
    translate_floor_plan('10F')

    print_translation('0F', '1F', '2F', '3F', '4', '5F', '06F')
    print_translation('1B', 'Dach', '7F', '5B', '12F', '00')
    print_translation('0F', '0B', '1', '-2F')
    print_translation()


# -------------
# Aufgabe 3
# -------------
def word_guess_spaghetti(secret):
    """ Implementiert ein Spiel zum Raten des Wortes secret

    Die gesamte Implementierung des Spiels in einer "Wurst",
    mit einigen Code-Wiederholungen und Entscheidungen fix kodiert.
    Sie sollten den Code besser organisieren (u.a. in Funktionen
    aufteilen, vielleicht lassen sich manche Wiederholungen auch
    durch Schleifen abbilden).

    Ablauf des Spiels:
    Das Spiel zeigt die verdeckten Stellen des zu erratenden Wortes
    an. Spieler:in gibt ein Zeichen ein, das Spiel merkt sich das
    Zeichen als erraten. Wurden alle Zeichen des Wortes erraten
    ist das Spiel gewonnen, hat das Wort noch nicht erratene Zeichen
    geht es in die nächste Runde. Wurde nach 6 Versuchen das Wort
    nicht vollständig aufgedeckt wurde das Spiel verloren, sonst
    gewonnen.

    Arguments:
    secret -- der zu erratende String
    """
    word = secret.upper()
    guesses = ''
    situation = '_' * len(word)

    msg = 'Spielstand: ' + situation + ' [0/6]'
    diff = len(msg) - len('YOUR TURN')
    print()
    print('-' * (diff // 2) + 'YOUR TURN' + '-' * (diff - diff // 2))
    print(msg)

    guess = ''
    while len(guess) != 1 or guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or guess in guesses:
        guess = input('Welchen Buchstaben wählst du als nächstes? >').upper()
        if len(guess) != 1:
            print('Bitte immer genau ein Zeichen wählen!')
        elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print('Bitte einen Buchstaben A-Z wählen')
        elif guess in guesses:
            print('Kleiner Tipp: den hast du schon probiert!')
    guesses += guess

    situation = ''
    for c in word:
        if c in guesses:
            situation += c
        else:
            situation += '_'
    if '_' in situation:
        msg = 'Spielstand: ' + situation + ' [1/6]'
        diff = len(msg) - len('YOUR TURN')
        print()
        print('-' * (diff // 2) + 'YOUR TURN' + '-' * (diff - diff // 2))
        print(msg)

        guess = ''
        while len(guess) != 1 or guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or guess in guesses:
            guess = input('Welchen Buchstaben wählst du als nächstes? >').upper()
            if len(guess) != 1:
                print('Bitte immer genau ein Zeichen wählen!')
            elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print('Bitte einen Buchstaben A-Z wählen')
            elif guess in guesses:
                print('Kleiner Tipp: den hast du schon probiert!')
        guesses += guess

    situation = ''
    for c in word:
        if c in guesses:
            situation += c
        else:
            situation += '_'
    if '_' in situation:
        msg = 'Spielstand: ' + situation + ' [2/6]'
        diff = len(msg) - len('YOUR TURN')
        print()
        print('-' * (diff // 2) + 'YOUR TURN' + '-' * (diff - diff // 2))
        print(msg)

        guess = ''
        while len(guess) != 1 or guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or guess in guesses:
            guess = input('Welchen Buchstaben wählst du als nächstes? >').upper()
            if len(guess) != 1:
                print('Bitte immer genau ein Zeichen wählen!')
            elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print('Bitte einen Buchstaben A-Z wählen')
            elif guess in guesses:
                print('Kleiner Tipp: den hast du schon probiert!')
        guesses += guess

    situation = ''
    for c in word:
        if c in guesses:
            situation += c
        else:
            situation += '_'
    if '_' in situation:
        msg = 'Spielstand: ' + situation + ' [3/6]'
        diff = len(msg) - len('YOUR TURN')
        print()
        print('-' * (diff // 2) + 'YOUR TURN' + '-' * (diff - diff // 2))
        print(msg)

        guess = ''
        while len(guess) != 1 or guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or guess in guesses:
            guess = input('Welchen Buchstaben wählst du als nächstes? >').upper()
            if len(guess) != 1:
                print('Bitte immer genau ein Zeichen wählen!')
            elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print('Bitte einen Buchstaben A-Z wählen')
            elif guess in guesses:
                print('Kleiner Tipp: den hast du schon probiert!')
        guesses += guess

    situation = ''
    for c in word:
        if c in guesses:
            situation += c
        else:
            situation += '_'
    if '_' in situation:
        msg = 'Spielstand: ' + situation + ' [4/6]'
        diff = len(msg) - len('YOUR TURN')
        print()
        print('-' * (diff // 2) + 'YOUR TURN' + '-' * (diff - diff // 2))
        print(msg)

        guess = ''
        while len(guess) != 1 or guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or guess in guesses:
            guess = input('Welchen Buchstaben wählst du als nächstes? >').upper()
            if len(guess) != 1:
                print('Bitte immer genau ein Zeichen wählen!')
            elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print('Bitte einen Buchstaben A-Z wählen')
            elif guess in guesses:
                print('Kleiner Tipp: den hast du schon probiert!')
        guesses += guess

    situation = ''
    for c in word:
        if c in guesses:
            situation += c
        else:
            situation += '_'
    if '_' in situation:
        msg = 'Spielstand: ' + situation + ' [5/6]'
        diff = len(msg) - len('YOUR TURN')
        print()
        print('-' * (diff // 2) + 'YOUR TURN' + '-' * (diff - diff // 2))
        print(msg)

        guess = ''
        while len(guess) != 1 or guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or guess in guesses:
            guess = input('Welchen Buchstaben wählst du als nächstes? >').upper()
            if len(guess) != 1:
                print('Bitte immer genau ein Zeichen wählen!')
            elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print('Bitte einen Buchstaben A-Z wählen')
            elif guess in guesses:
                print('Kleiner Tipp: den hast du schon probiert!')
        guesses += guess

    situation = ''
    for c in word:
        if c in guesses:
            situation += c
        else:
            situation += '_'
    if '_' in situation:
        msg = 'Lösung: ' + word + ' [Dein Ergebnis: ' + situation + ']'
        diff = len(msg) - len('YOU LOST')
        print()
        print('-' * (diff // 2) + 'YOU LOST' + '-' * (diff - diff // 2))
        print(msg)
    else:
        msg = 'Endstand: ' + word + ' [' + str(len(guesses)) + '/6]'
        diff = len(msg) - len('YOU WON')
        print()
        print('-' * (diff // 2) + 'YOU WON' + '-' * (diff - diff // 2))
        print(msg)


def better_word_guess(secret, max_guesses):
    # TODO: implementieren Sie die Funktionalität hier
    pass


# TODO: Mögliche Vorlage für eigene Funktion
def my_func(arg1):
    """ Kurzbeschreibung (1 Zeile)

    Evtl. genauere Beschreibung, vor allem welche Voraussetzungen
    die Argumente erfüllen müssen, damit die Funktion korrekt
    arbeitet.

    Argumentenliste:
    - arg1: int, es muss arg1 > 0 gelten
    """
    pass


# -------------
# Aufgabe 4
# -------------


# -- Beispiel für eine Lösung/Antwort:

# Funktionalität: Berechnet die Binärdarstellung der Zahl n
#                 (= fügt die Reste der wiederholten Division von n durch 2 zu einem String zusammen)
# Basisfall:     Die Zahl n ist kleiner 2 -> es wird 0 oder 1 zurückgegeben.
# "Verkleinerung" des Problems im Rekursionsschritt:
#                n wird halbiert (und falls nötig auf die nächste ganze Zahl abgerundet)
#                Dadurch verkleinert sich die Distanz zum Basisfall n < 2 in jedem Schritt.
# Berechnung der Lösung im Rekursionsschritt:
#               Das Ergebnis des rekursiven Aufrufs (ein String) wird am Ende um den Rest der Division
#               von n durch 2 erweitert (mittels Stringkonkatenation).

# Annahme: n >= 0 ist vom Typ Integer
def mystery_division(n):
    if n < 2:
        return str(n)
    else:
        return mystery_division(n // 2) + str(n % 2)

# //-- Ende Beispiel


# Funktionalität: TODO
# Basisfall: TODO
# "Verkleinerung" des Problems im Rekursionsschritt: TODO
# Berechnung der Lösung im Rekursionsschritt: TODO
def mystery_math(lower, upper):
    """
    lower -- int
    upper -- int
    """
    if lower > upper:
        return mystery_math(upper, lower)
    if upper == lower:
        return lower
    if upper - lower == 1:
        return lower + 0.5
    else:
        return mystery_math(lower + 1, upper - 1)


# Funktionalität: TODO
# Basisfall: TODO
# "Verkleinerung" des Problems im Rekursionsschritt: TODO
# Berechnung der Lösung im Rekursionsschritt: TODO
def mystery_string(line):
    """
    line -- str mit len(line) >= 1
    """
    if len(line) == 1:
        return line
    ret = mystery_string(line[1:])
    if ret[0] == '9':
        return ret
    else:
        return line


# Funktionalität: TODO
# Basisfall: TODO
# "Verkleinerung" des Problems im Rekursionsschritt: TODO
# Berechnung der Lösung im Rekursionsschritt: TODO
def mystery_test(prefix, line):
    """
    prefix -- str
    line -- str
    """
    if prefix + line == 'apple':
        return True
    elif len(line) == 0:
        return False
    else:
        return mystery_test(prefix + line[0], line[1:]) or mystery_test(prefix, line[1:])



if __name__ == '__main__':
    exercise1()
    exercise2()

    # Aufgabe 3:
    # Falls Sie die Funktion ausprobieren wollen:
    # word_guess_spaghetti('sommer')

    # Aufgabe 4 hat keine geforderten Aufrufe, Sie können aber hier eigene Testfälle einfügen
