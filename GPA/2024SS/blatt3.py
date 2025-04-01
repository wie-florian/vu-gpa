# -*- coding: utf-8 -*-
# GPA 2024


# -------------
# Aufgabe 1
# -------------


happy = '\\o/'
sad = '/o\\'
fence = ' | '


def fans(n, goals_home, goals_away):
    if n % 2 == 0:
        fans_home = n // 2
        fans_away = n // 2
    else:
        fans_home = n // 2 + 1
        fans_away = n // 2
    if goals_home > goals_away:
        home = happy * fans_home
        away = sad * fans_away
    elif goals_home < goals_away:
        home = sad * fans_home
        away = happy * fans_away
    else:
        home = happy * fans_home
        away = happy * fans_away
    return home + fence + away


def count_questions_answered(text):
    is_question = 0
    count_answered = 0
    for i in text:
        if i == '?':
            is_question = 1
        elif i == '!' and is_question == 1:
            count_answered += 1
            is_question = 0
    return count_answered


def print_most_answers(*texts):
    n_ans_max = 0
    ans_max = ''
    for i in texts:
        n_ans = count_questions_answered(i)
        if n_ans > n_ans_max:
            n_ans_max = n_ans
            ans_max = i
    if n_ans_max == 0 and len(texts) != 0:
        return texts[0]
    return ans_max


# Enthält alle Aufrufe der Funktionen aus Aufgabe 1
def exercise1():
    print('Beispiele Fans:')
    print(fans(2, 2, 2))
    print(fans(5, 2, 1))
    print(fans(3, 1, 2))
    print(fans(4, 1, 2))
    print(fans(4, 2, 1))

    print('Beispiele Fragen:')
    print(count_questions_answered('warum?darum!wer?du!ich?ja!'))
    print(count_questions_answered('Darf ich ein Eis?'))
    print(count_questions_answered('Wann? Wo? Ja!'))
    print(count_questions_answered('Ja! ?Wirklich?? JA!! Warum?'))
    print(count_questions_answered('Das ist keine Frage'))
    print(count_questions_answered('Ist das eine Frage? Ja.'))

    print('Beispiele Antworten:')
    print(print_most_answers())
    print(print_most_answers(''))
    print(print_most_answers('Keine Frage'))
    print(print_most_answers('Zwei Fragen??', 'Eine Antwort!?'))
    print(print_most_answers('Zwei Fragen??', 'Frage?'))
    print(print_most_answers('', '?', 'Ich?Ja du!'))
    print(print_most_answers('', 'schwer?Ja!Echt?Jup!', '?!?!?', '?!'))
    print(print_most_answers('?!1', '?!1?!2?!3??!', '-?!1?!2?!', '?!1?!2?!'))
    print(print_most_answers('?!1?!2', '-', '?!1?!2?!3?!', '!!', '?!1?!2?!3'))


exercise1()

# -------------
# Aufgabe 2
# -------------


def compare(a, b):
    ans = ''
    for i in range(len(a)):
        x = 0
        j = 0
        while j < len(b) and x == 0:
            if a[i] == b[j]:
                ans += a[i]
                x = 1
            j += 1
    return len(ans)


def progress_bar(length, checked):
    if length >= checked:
        return 'x' * checked + '-' * (length - checked)
    else:
        return 'x' * length


def format_line(line, separator, blocksize):
    new_line = ''
    block = blocksize
    for i in range(len(line)):
        if i == block:
            new_line += separator
            block += blocksize
        new_line += line[i]
    return new_line


def check(a, b):
    n_same = compare(a, b)
    bar = progress_bar(len(a), n_same)
    format_bar = format_line(bar, ' ', 4)
    return format_bar


def exercise2():
    print('compare:')
    print(compare('tattoo', 'otto'))
    print(compare('HALLO', 'hallo'))
    print(compare('Affe', 'Saft'))
    print(compare('Kaffee', 'Elfe'))
    print(compare('2 4 6 8', '0 123456789'))

    print('progress_bar:')
    print((progress_bar(10, 5)))
    print(progress_bar(4, 4))
    print(progress_bar(5, 0))
    print(progress_bar(3, 6))
    print(progress_bar(10, 9))

    print('format_line:')
    print(format_line('ichlesdasnie', ' ', 3))
    print(format_line('1234567890', '-', 4))
    print(format_line('TU', 'W', 2))
    print(format_line('GPAGPAGPA', '! ', 3))

    print('check:')
    print(check('Affe', 'Saft'))
    print(check('Sag niemals...', '... nie'))
    print(check('fertig geladen', 'beim laden'))
    print(check('vor langer, langer Zeit ...', '... in einer weit entfernten Galaxie'))
    print(check('1234567890', '100110111201120'))


exercise2()

# -------------
# Aufgabe 3
# -------------


# (1)
def highest_digit_1(text):
    digit = -1
    for char in text:
        if char.isdigit():
            digit = int(char)


# Bewertung der Funktion:
# Die Funktion gibt nichts zurück, weder mittels return noch mit print und ist somit unvollständig
# Sie gibt auch nur die letzte Ziffer des textes aus anstatt die höchste.


# wenn nötig, korrigieren/vervollständigen Sie die Funktion:
# (dies ist eine Kopie der obigen Funktion - verwenden Sie bitte diese
#  Kopie und lassen Sie die obige Version als "Originalversion" unverändert.)
def highest_digit_1_correct(text):
    digit = -1
    for char in text:
        if char.isdigit() and int(char) > digit:
            digit = int(char)
    return digit


# (2)
def highest_digit_2(a):
    digit = -1
    for i in range(len(a)):
        if a[i] > digit:
            pass


# Bewertung der Funktion:
# Die Funktion versucht a[i] mit digit zu vergleich, also ein str mit einem int. dadurch kann sie nicht funktionieren
# weiters fehlt wieder eine Ausgabe (print/return)


# wenn nötig, korrigieren/vervollständigen Sie die Funktion:
# (dies ist eine Kopie der obigen Funktion - verwenden Sie bitte diese
#  Kopie und lassen Sie die obige Version als "Originalversion" unverändert.)
def highest_digit_2_correct(a):
    digit = -1
    for i in range(len(a)):
        if a[i].isdigit() and int(a[i]) > digit:
            digit = int(a[i])
            pass
    return digit


# (3)
def highest_digit_obscure(line):
    max_digit = -1
    for char in line[::-1]:
        if '0' <= char <= '9':
            digit = int(char)
            max_digit = max_digit if max_digit > digit else digit
    return max_digit

# Bewertung der Funktion:
# Die Funktion funktioniert ist aber etwas umständlich. die range für die for schleife ist etwas umständlich,
# auch weil sie rückwärts die Zeichen durchgeht
# Korrekturen (falls nötig):
# keine Korrekturen notwendig


# (4)
def highest_digit_beginner(line):
    max_digit = -1
    for char in line:
        if char.isdigit():
            digit = int(char)
            max_digit = max_digit + digit
    return max_digit


# Bewertung der Funktion:
# die  funktion addiert alle ziffern und sucht nicht den maximal wert
# Korrekturen (falls nötig):

def highest_digit_beginner_correct(line):
    max_digit = -1
    for char in line:
        if char.isdigit():
            digit = int(char)
            max_digit = max(max_digit, digit)
    return max_digit


def exercise3():
    # Hier könnten Ihre Testfälle stehen
    pass


# -------------
# Aufgabe 4
# -------------


# -- Beispiel für eine Lösung/Antwort:

# Funktionalität: Berechnet die Binärdarstellung der Zahl n
#                 (= fügt die Reste der wiederholten Division von n durch 2 zu einem String zusammen)
# Basisfall:     Die Zahl n ist kleiner 2 → es wird 0 oder 1 zurückgegeben.
# "Verkleinerung" des Problems im Rekursionsschritt:
#                n wird halbiert (und falls nötig auf die nächste ganze Zahl abgerundet)
#                dadurch verkleinert sich die Distanz zum Basisfall n < 2 in jedem Schritt.
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


# Funktionalität: Berechnet die Summe der Quadrate von allen durch 3 teilbaren zahlen im intervall
# Basisfall: lower wird quadriert und zu einer Summe addiert
# "Basisfall zum Abbruch": wenn lower > upper, wir 0 zurückgegeben
# "Verkleinerung" des Problems im Rekursionsschritt: wenn lower nicht durch 3 teilbar ist, wird lower um 1 erhöht
# und das ergebnis bleibt unverändert
# Berechnung der Lösung im Rekursionsschritt: wenn lower durch 3 teilbar ist, wird das lower quadriert
# und zur Summe addiert

# Annahme: lower, upper sind ganze Zahlen (int)
def mystery_calculation(lower, upper):
    if lower > upper:
        return 0
    elif lower % 3 == 0:
        return (lower ** 2) + mystery_calculation(lower + 3, upper)
    else:
        return mystery_calculation(lower + 1, upper)


# Funktionalität:
# Basisfall: lower**2 == upper dann wird True ausgegeben
# Basisfälle zum Abbruch (bzw False Ausgabe): upper ist kleiner als 0 oder lower > upper oder lower > sqrt(upper),
# "Verkleinerung" des Problems im Rekursionsschritt:
# wir erhöhen lower so lange bis lower**2 == upper ist und kommen so den Basisfall immer um 1 näher
# Berechnung der Lösung im Rekursionsschritt:
# Die Berechnung ist eigentlich nur ein Abgleich (lower**2 == upper) welcher zu True führt

# Annahme: lower, upper sind ganze Zahlen (int)
def mystery_check(lower, upper):
    if upper < 0:
        return False
    if lower >= upper:
        return False
    return ((lower * lower) == upper) or mystery_check(lower + 1, upper)


# Funktionalität: Sucht und gibt den letzten Vokal des Texts aus.
# Basisfall: der text ist leer oder enthält keine Vokale, die funktion gibt den letzten gespeichert Vokal
# oder einen leeren string zurück
# "Verkleinerung" des Problems im Rekursionsschritt: in jedem Schritt wird der String verkürzt
# Berechnung der Lösung im Rekursionsschritt:
# bei jedem durchlauf wird das erste zeichen des strings überprüft, ob es ein vokal ist, wenn ja, wird dieser
# gespeichert, wenn nicht, dann nicht

# Annahmen: text ist ein String
def mystery_selection(text):
    if not text:
        return ''
    else:
        x = mystery_selection(text[1:])
        if text[0] in 'aeiou' and x == '':
            return text[0]
        else:
            return x


# Funktionalität: fügt dem string 'text' nach b Zeichen 's' ein, beginnend mit a
# Basisfall 1: b <= 0, dann wird der ganze text zurückgegeben
# Basisfall 2: a <= 0 dann wird s noch vor dem ersten zeichen eingefügt
# Basisfall 3: Wenn a > 0 und der text leer ist, dann wir ein leerer string ausgegeben
# Basisfall 4: Nach dem a.ten zeichen wird der string 's' eingefügt
# "Verkleinerung" des Problems im Rekursionsschritt:
# in jedem Schritt wird das erste Zeichen des textes entfernt, und der eingabe 'text' string
# verkürzt
# Berechnung der Lösung im Rekursionsschritt:
# String 's' wird an der Stelle a des 'text' strings eingefügt und a wird reduziert.


def mystery_string(text, a, b, s):
    if b <= 0:
        return text
    elif a <= 0:
        return s + mystery_string(text, b, b, s)
    elif not text:
        return ''
    else:
        return text[0] + mystery_string(text[1:], a - 1, b, s)


if __name__ == '__main__':
    exercise1()
    exercise2()
    exercise3()
    # Aufgabe 4 hat keine geforderted Aufrufe, Sie können aber hier eigene Testfälle einfügen
