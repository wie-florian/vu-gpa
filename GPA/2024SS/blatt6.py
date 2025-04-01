# -*- coding: utf-8 -*-
# GPA 2024


# -------------
# Aufgabe 1
# -------------


def exercise1() -> None:
    print('## Aufgabe 1\n')
    elements = {
        'H': {'Name': 'Wasserstoff', 'Ordnungszahl': 1, 'Serie': {'Nichtmetalle'}, 'Periode': 1, 'Gruppe': 1,
              'Atomgewicht': 1.008},
        'He': {'Name': 'Helium', 'Ordnungszahl': 2, 'Serie': {'Edelgase'}, 'Periode': 1, 'Gruppe': 18,
               'Atomgewicht': 4.0026},
        'Ne': {'Name': 'Neon', 'Ordnungszahl': 10, 'Serie': {'Edelgase'}, 'Periode': 2, 'Gruppe': 18,
               'Atomgewicht': 20.180},
        'Li': {'Name': 'Lithium', 'Ordnungszahl': 3, 'Serie': {'Alkalimetalle'}, 'Periode': 2, 'Gruppe': 1},
        'Na': {'Name': 'Natrium', 'Ordnungszahl': 11, 'Serie': {'Alkalimetalle'}, 'Periode': 3, 'Gruppe': 1,
               'Atomgewicht': 22.990},
        'Be': {'Name': 'Beryllium', 'Ordnungszahl': 4, 'Serie': {'Erdalkalimetalle'}, 'Periode': 2, 'Gruppe': 2,
               'Atomgewicht': 9.0122},
        'S': {'Name': 'Schwefel', 'Ordnungszahl': 16, 'Serie': {'Nichtmetalle'}, 'Periode': 3, 'Gruppe': 16},
        'B': {'Name': 'Bor', 'Ordnungszahl': 5, 'Serie': {'Halbmetalle'}, 'Periode': 2, 'Gruppe': 13,
              'Atomgewicht': 10.81},
        'Hg': {'Name': 'Quecksilber', 'Ordnungszahl': 80, 'Serie': {'Übergangsmetalle'}, 'Periode': 6, 'Gruppe': 12},
        'Sb': {'Name': 'Antimon', 'Ordnungszahl': 51, 'Serie': {'Metalle', 'Halbmetalle'}, 'Periode': 5, 'Gruppe': 15},
        'Po': {'Name': 'Polonium', 'Ordnungszahl': 84, 'Serie': {'Metalle', 'Halbmetalle'}, 'Periode': 6, 'Gruppe': 16},
        'Ag': {'Name': 'Silber', 'Ordnungszahl': 47, 'Serie': {'Übergangsmetalle'}, 'Periode': 5, 'Gruppe': 11},
        'Au': {'Name': 'Gold', 'Ordnungszahl': 79, 'Serie': {'Übergangsmetalle'}, 'Periode': 6, 'Gruppe': 11,
               'Atomgewicht': 196.97},
        'At': {'Name': 'Astat', 'Ordnungszahl': 85, 'Serie': {'Halbmetalle', 'Halogene'}, 'Periode': 6, 'Gruppe': 17},
        'St': {'Name': 'Strontium', 'Ordnungszahl': 38, 'Serie': {'Erdalkalimetalle'}, 'Periode': 5, 'Gruppe': 2,
               'Atomgewicht': 87.62}
    }

    # Liste aller Elemente, deren Symbol mit einem anderen Buchstaben anfängt als ihr Name
    # Erwartete Ausgabe:
    # ['Ag-Silber', 'Au-Gold', 'H-Wasserstoff', 'Hg-Quecksilber', 'Sb-Antimon']
    # TODO: Lösung hier

    print()

    print('Geschätzte Neutronenzahlen:')
    # Für die Einträge mit Atomgewicht: Anzahl der Neutronen schätzen als Differenz von Atomgewicht und Ordnungszahl
    #     (gerundet mittels round)
    # Mögliche Ausgabe (Reihenfolge der Zeilen kann variieren)
    # Wasserstoff: 0 Neutronen
    # Helium: 2 Neutronen
    # Neon: 10 Neutronen
    # Natrium: 12 Neutronen
    # Beryllium: 5 Neutronen
    # Bor: 6 Neutronen
    # Gold: 118 Neutronen
    # Strontium: 50 Neutronen
    # TODO: Lösung hier

    print()

    # Neues Dictionary mit Nummer der Periode als Schlüssel.
    # Jedem Schlüssel wird eine Liste zugeordnet. Diese Liste enthält einen Eintrag für
    # jedes Element, dass zur entsprechenden Gruppe gehört. Die Einträge der Liste sind
    # neue Dictionaries mit den Schlüsseln 'Symbol', 'Name' und 'OZ' (als Abkürzung für Ordnungszahl),
    # welche jeweils die entsprechenden Werte enthalten.
    # Erwartetes Ergebnis (Reihenfolge der Einträge spielt keine Rolle):
    # {1: [{'Symbol': 'H', 'Name': 'Wasserstoff', 'OZ': 1},
    #      {'Symbol': 'He', 'Name': 'Helium', 'OZ': 2}],
    #  2: [{'Symbol': 'Ne', 'Name': 'Neon', 'OZ': 10},
    #      {'Symbol': 'Li', 'Name': 'Lithium', 'OZ': 3},
    #      {'Symbol': 'Be', 'Name': 'Beryllium', 'OZ': 4},
    #      {'Symbol': 'B', 'Name': 'Bor', 'OZ': 5}],
    #  3: [{'Symbol': 'Na', 'Name': 'Natrium', 'OZ': 11},
    #      {'Symbol': 'S', 'Name': 'Schwefel', 'OZ': 16}],
    #  5: [{'Symbol': 'Sb', 'Name': 'Antimon', 'OZ': 51},
    #      {'Symbol': 'Ag', 'Name': 'Silber', 'OZ': 47},
    #      {'Symbol': 'St', 'Name': 'Strontium', 'OZ': 38}],
    #  6: [{'Symbol': 'Hg', 'Name': 'Quecksilber', 'OZ': 80},
    #      {'Symbol': 'Po', 'Name': 'Polonium', 'OZ': 84},
    #      {'Symbol': 'Au', 'Name': 'Gold', 'OZ': 79},
    #      {'Symbol': 'At', 'Name': 'Astat', 'OZ': 85}]}
    # TODO: Lösung hier
    # my_elements =

    print()

    # Erweitern von my_elements um einen Eintrag mit Schlüssel 0 und Wert 'GPA'
    # Erwartetes Ergebnis (Reihenfolge der Einträge spielt keine Rolle):
    # {1: [{'Symbol': 'H', 'Name': 'Wasserstoff', 'OZ': 1},
    #      {'Symbol': 'He', 'Name': 'Helium', 'OZ': 2}],
    #  2: [{'Symbol': 'Ne', 'Name': 'Neon', 'OZ': 10},
    #      {'Symbol': 'Li', 'Name': 'Lithium', 'OZ': 3},
    #      {'Symbol': 'Be', 'Name': 'Beryllium', 'OZ': 4},
    #      {'Symbol': 'B', 'Name': 'Bor', 'OZ': 5}],
    #  3: [{'Symbol': 'Na', 'Name': 'Natrium', 'OZ': 11},
    #      {'Symbol': 'S', 'Name': 'Schwefel', 'OZ': 16}],
    #  5: [{'Symbol': 'Sb', 'Name': 'Antimon', 'OZ': 51},
    #      {'Symbol': 'Ag', 'Name': 'Silber', 'OZ': 47},
    #      {'Symbol': 'St', 'Name': 'Strontium', 'OZ': 38}],
    #  6: [{'Symbol': 'Hg', 'Name': 'Quecksilber', 'OZ': 80},
    #      {'Symbol': 'Po', 'Name': 'Polonium', 'OZ': 84},
    #      {'Symbol': 'Au', 'Name': 'Gold', 'OZ': 79},
    #      {'Symbol': 'At', 'Name': 'Astat', 'OZ': 85}],
    #  0: 'GPA'}
    # TODO: Lösung hier

    # Tests um zu überprüfen, dass an elements nichts verändert wurde:
    elements_unchanged = {
        'H': {'Name': 'Wasserstoff', 'Ordnungszahl': 1, 'Serie': {'Nichtmetalle'}, 'Periode': 1, 'Gruppe': 1,
              'Atomgewicht': 1.008},
        'He': {'Name': 'Helium', 'Ordnungszahl': 2, 'Serie': {'Edelgase'}, 'Periode': 1, 'Gruppe': 18,
               'Atomgewicht': 4.0026},
        'Ne': {'Name': 'Neon', 'Ordnungszahl': 10, 'Serie': {'Edelgase'}, 'Periode': 2, 'Gruppe': 18,
               'Atomgewicht': 20.180},
        'Li': {'Name': 'Lithium', 'Ordnungszahl': 3, 'Serie': {'Alkalimetalle'}, 'Periode': 2, 'Gruppe': 1},
        'Na': {'Name': 'Natrium', 'Ordnungszahl': 11, 'Serie': {'Alkalimetalle'}, 'Periode': 3, 'Gruppe': 1,
               'Atomgewicht': 22.990},
        'Be': {'Name': 'Beryllium', 'Ordnungszahl': 4, 'Serie': {'Erdalkalimetalle'}, 'Periode': 2, 'Gruppe': 2,
               'Atomgewicht': 9.0122},
        'S': {'Name': 'Schwefel', 'Ordnungszahl': 16, 'Serie': {'Nichtmetalle'}, 'Periode': 3, 'Gruppe': 16},
        'B': {'Name': 'Bor', 'Ordnungszahl': 5, 'Serie': {'Halbmetalle'}, 'Periode': 2, 'Gruppe': 13,
              'Atomgewicht': 10.81},
        'Hg': {'Name': 'Quecksilber', 'Ordnungszahl': 80, 'Serie': {'Übergangsmetalle'}, 'Periode': 6, 'Gruppe': 12},
        'Sb': {'Name': 'Antimon', 'Ordnungszahl': 51, 'Serie': {'Metalle', 'Halbmetalle'}, 'Periode': 5, 'Gruppe': 15},
        'Po': {'Name': 'Polonium', 'Ordnungszahl': 84, 'Serie': {'Metalle', 'Halbmetalle'}, 'Periode': 6, 'Gruppe': 16},
        'Ag': {'Name': 'Silber', 'Ordnungszahl': 47, 'Serie': {'Übergangsmetalle'}, 'Periode': 5, 'Gruppe': 11},
        'Au': {'Name': 'Gold', 'Ordnungszahl': 79, 'Serie': {'Übergangsmetalle'}, 'Periode': 6, 'Gruppe': 11,
               'Atomgewicht': 196.97},
        'At': {'Name': 'Astat', 'Ordnungszahl': 85, 'Serie': {'Halbmetalle', 'Halogene'}, 'Periode': 6, 'Gruppe': 17},
        'St': {'Name': 'Strontium', 'Ordnungszahl': 38, 'Serie': {'Erdalkalimetalle'}, 'Periode': 5, 'Gruppe': 2,
               'Atomgewicht': 87.62}
    }
    print('\nElements unverändert:', elements == elements_unchanged)  # muss True ausgeben


# -------------
# Aufgabe 2
# -------------


def parse_template(filename: str) -> None:
    # TODO: implementieren
    pass


# Sie dürfen zusätzliche Funktionen definieren, wenn Sie wollen.


def exercise2() -> None:
    print('\n\n## Aufgabe 2')
    parse_template('template1.gpa')
    parse_template('template2.gpa')
    parse_template('template3.gpa')
    parse_template('template_error.gpa')
    parse_template('gibts-nicht.gpa')  # file does not exist => check if error is handled correctly


# -------------
# Aufgabe 3
# -------------


# TODO: Implementieren der Klasse Service


# TODO: Implementieren der Klasse Customer


def exercise3() -> None:
    print('\n\n## Aufgabe 3:')

    # TODO: die Testfälle können aktiv geschalten werden sobald die Klassen Service und Customer
    #       implementiert sind. Sonst Syntaxfehler.
    # gpa = Service('Größte Programm Auswahl', 9.98)
    # print(gpa.get_advertisement())
    # print(gpa.add_movies(['Dune', 'Dune2', '007', 'Batman', 'Barbie']))
    # print(gpa.add_movies(['Arielle', 'Dune', 'LOTR', 'Jaws']))
    # print(gpa.adjust_service(-5))
    # print(gpa.get_advertisement())
    # print(gpa.adjust_service(-5))
    # print(gpa.get_advertisement())
    # print(gpa.adjust_service(10))
    # print(gpa.get_advertisement())
    #
    # print()
    # print()
    # custi = Customer('al-Gaib Paul Atreides')
    # print(custi.find_movie('Dune'))
    # custi.print_bill()
    # print(custi.subscribe(gpa))
    # print(custi.subscribe(gpa))
    # print(custi.find_movie('Dune'))
    # print(custi.find_movie('Water World'))
    #
    # ex = Service('E3 (exclusive, expensive, empty)', 120.99)
    # print(custi.subscribe(ex))
    # custi.print_bill()


def streaming_service_scenario():
    print('\n\nStreaming Service Scenario:')
    # TODO: die Testfälle können aktiv geschalten werden sobald die Klassen Service und Customer
    #       implementiert sind. Sonst Syntaxfehler.

    # gpa = Service('Genüsslicher Popcorn Abend', 9.98)
    # custi_1 = Customer('Alice')
    # custi_2 = Customer('Bob')
    # custi_3 = Customer('Eve')
    # custi_4 = Customer('Fahrenheit')
    # custi_5 = Customer('Gustav')
    # print(gpa.get_advertisement())
    # # ==##Genüsslicher Popcorn Abend##==
    # # Wir bieten 0 Filme für nur 9.98GELD monatlich!
    # custi_1.print_bill()
    # # #################
    # # Kosten von Alice:
    # # -----------
    # # Summe: 0
    # print(custi_2.find_movie('LOTR'))   # set()
    # tup = Service('TUplus', 7.95)
    # print(tup.add_movies(['LOTR', 'Arielle', 'WW', 'SW IV', 'Barbie', '007']))  # 6
    # print(tup.get_advertisement())
    # # ==##TUplus##==
    # # Wir bieten 6 Filme für nur 7.95GELD monatlich!
    #
    # print(gpa.add_movies(['Dune', 'Dune2', '007', 'Batman', 'Barbie']))  # 5
    #
    # print(custi_3.subscribe(tup))  # SUCCESS
    # print(custi_3.find_movie('Arielle'))    # {'TUplus'}
    # custi_3.print_bill()
    # # #################
    # # Kosten von Eve:
    # # TUplus: 7.95
    # # -----------
    # # Summe: 7.95
    #
    # print(custi_1.subscribe(gpa))  # SUCCESS
    # print(custi_2.subscribe(gpa))  # SUCCESS
    # print(custi_2.subscribe(tup))  # SUCCESS
    # print(custi_4.subscribe(gpa))  # SUCCESS
    # custi_2.print_bill()
    # # #################
    # # Kosten von Bob:
    # # TUplus: 7.95
    # # Genüsslicher Popcorn Abend: 9.98
    # # -----------
    # # Summe: 17.93
    # custi_4.print_bill()
    # # #################
    # # Kosten von Fahrenheit:
    # # Genüsslicher Popcorn Abend: 9.98
    # # -----------
    # # Summe: 9.98
    # print(custi_2.find_movie('007'))    # {'Genüsslicher Popcorn Abend', 'TUplus'}
    #
    # print(gpa.add_movies(['Arielle', 'Dune', 'LOTR', 'Jaws']))  # 3
    # print(tup.add_movies(['Arielle', 'Dune']))  # 1
    # print(gpa.get_advertisement())
    # # ==##Genüsslicher Popcorn Abend##==
    # # Wir bieten 8 Filme für nur 9.98GELD monatlich!
    # print(tup.get_advertisement())
    # # ==##TUplus##==
    # # Wir bieten 7 Filme für nur 7.95GELD monatlich!
    #
    # sec = Service('Secundus', 5.55)
    # print(sec.add_movies(['Barbie', 'Pirates', 'Zombies', 'Crocks']))  # 4
    # print(custi_4.subscribe(sec))  # SUCCESS
    # print(custi_3.subscribe(tup))  # ERR_ALREADY_SUBSCRIBED
    # print(custi_5.subscribe(sec))  # SUCCESS
    # print(gpa.get_advertisement())
    # # ==##Genüsslicher Popcorn Abend##==
    # # Wir bieten 8 Filme für nur 9.98GELD monatlich!
    # print(tup.get_advertisement())
    # # ==##TUplus##==
    # # Wir bieten 7 Filme für nur 7.95GELD monatlich!
    # print(sec.get_advertisement())
    # # ==##Secundus##==
    # # Wir bieten 4 Filme für nur 5.55GELD monatlich!
    # custi_1.print_bill()
    # # #################
    # # Kosten von Alice:
    # # Genüsslicher Popcorn Abend: 9.98
    # # -----------
    # # Summe: 9.98
    # custi_2.print_bill()
    # # #################
    # # Kosten von Bob:
    # # Genüsslicher Popcorn Abend: 9.98
    # # TUplus: 7.95
    # # -----------
    # # Summe: 17.93
    # custi_3.print_bill()
    # # #################
    # # Kosten von Eve:
    # # TUplus: 7.95
    # # -----------
    # # Summe: 7.95
    # custi_4.print_bill()
    # # #################
    # # Kosten von Fahrenheit:
    # # Genüsslicher Popcorn Abend: 9.98
    # # Secundus: 5.55
    # # -----------
    # # Summe: 15.530000000000001
    # custi_5.print_bill()
    # # #################
    # # Kosten von Gustav:
    # # Secundus: 5.55
    # # -----------
    # # Summe: 5.55
    #
    # print(gpa.adjust_service(3))  # True
    # custi_1.print_bill()
    # # #################
    # # Kosten von Alice:
    # # Genüsslicher Popcorn Abend: 12.98
    # # -----------
    # # Summe: 12.98
    # custi_2.print_bill()
    # # #################
    # # Kosten von Bob:
    # # TUplus: 7.95
    # # Genüsslicher Popcorn Abend: 12.98
    # # -----------
    # # Summe: 20.93
    # custi_3.print_bill()
    # # #################
    # # Kosten von Eve:
    # # TUplus: 7.95
    # # -----------
    # # Summe: 7.95
    # custi_4.print_bill()
    # # #################
    # # Kosten von Fahrenheit:
    # # Genüsslicher Popcorn Abend: 12.98
    # # Secundus: 5.55
    # # -----------
    # # Summe: 18.53
    # custi_5.print_bill()
    # # #################
    # # Kosten von Gustav:
    # # Secundus: 5.55
    # # -----------
    # # Summe: 5.55
    #
    # print(custi_5.subscribe(tup))  # SUCCESS
    # print(custi_5.find_movie('Barbie'))     # {'Secundus', 'TUplus'}
    # print(custi_5.find_movie('Crocks'))     # {'Secundus'}


# -------------
# Aufgabe 4
# -------------

# -- Aufgabe 4.1

# Beispielfunktionen:

# Ist n in O(0.5*n)?
# Antwort: Ja. Für c = 2 und n_0 = 0 gilt: Für alle n >= n0 gilt: n <= c * 0.5 * n (insbesondere n = n),
#                                          also f(n) <= c * g(n), da f(n) = n und g(n) = 0.5*n

# Ist (n^3)/10 + n^2 - 7 in O(n)?
# Antwort: Nein. Für jede beliebige Konstante c lässt sich ein n1 finden, ab dem
#          (n^3)/10 + n^2 - 7 > c*n für alle n >= n1 gilt (was der Definition von "in O(n)"
#          genau widerspricht).
#          Genauer: für alle n welche (n^2)/10 + n - 7/n > c erfüllen; es ist offensichtlich
#                   dass (n^2)/10 + n - 7/n mit steigendem n wächst, während c konstant ist.

# // Ende Beispielfunktionen


# 1) 3^3 * n + 2000^2                     in O(n):
# Antwort: TODO
# Begründung: TODO

# 2) 4 * n^3 * n + (n/2)^2 + 2*n          in O(n^3)?
# Antwort: TODO
# Begründung: TODO

# 3) 2 * log(n) + 7                       in O(n)?
# Antwort: TODO
# Begründung: TODO

# 4) 100 * n^15 + 24 * n^3 - 2 * n^2      in O(2^n)?
# Antwort: TODO
# Begründung: TODO


# -- Aufgabe 4.2:
# Beispielfunktion:
# 24*n + 2*log(n)
# Kleinste asymptotische obere Schranke: O(n)
# Begründung: Für c = 100 gilt: 24*n + 2*log(n) <= 100*n ab bestimmten n0, z.B. ab
#                n > 2 [bis hierher Minimalantwort; mögliche Ergänzung:]
#                Gilt da n >= log(n) für n >= 1: Daraus folgt 2*n >= 2*log(n).
#                Daraus folgt 24*n + 2*log(n) <= 24*n + 2*n = 26*n <= 100*n
#                [Ableitung/Begründung nicht notwendig, Angabe von c und n0 reicht;
#                n0 und c müssen auch nicht die kleinsten möglichen Werte sein, sondern
#                können der Definition entsprechend beliebig gewählt werden]


# 1) 9 * n + (n/3)^2 - 27 * log(n)
# Kleinste asymptotische obere Schranke: TODO
# Begründung: TODO


# 2) (2^5 * n^3)/(2*n^4) + 3 * log(n) - 2024
# Kleinste asymptotische obere Schranke: TODO
# Begründung: TODO


# 3) 3 * n * 14 * log(n) * 0.5 * n^2 - 2 * n^3 - 1701
# Kleinste asymptotische obere Schranke: TODO
# Begründung: TODO


if __name__ == '__main__':
    # exercise1()
    # exercise2()
    # exercise3()
    # streaming_service_scenario()
    pass