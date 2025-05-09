# -*- coding: utf-8 -*-
# GPA 2025

# 2025-05-06: Die Zeile 272: print(f'## Steine übrig: Player 1: [{pieces['1']}]  Player 2: [{pieces['2']}]\n')
#             funktioniert nur in sehr neuen Python Versionen (3.13). Wir haben sie durch eine ersetzt,
#             die auch in älteren geht (pieces["1"] bzw pieces["2"]).

import random


# -------------
# Aufgabe 1
# -------------


def delete_direct_repeats(values: list) -> list:
    end = []
    print(f"values: {values}")
    if len(values) == 1:
        end.append(values[0])
        return end
    else:
        first = values[0]
        second = values[1]
        print(f"first: {first}, second: {second}")
        if first == second:
            return delete_direct_repeats(values[1:])
        else:
            end.append(first)
            print(f"end: {end}")
            return delete_direct_repeats(values[1:])



# TODO: 1.2: balance(load: list[int | float], begin: int, end: int) -> None


# TODO: 1.3: collect(elements: list[tuple[str, int]], position: int, forbidden: set[int]) -> tuple[str, int]


def exercise1() -> None:
    # TODO: weitere Testfälle bei Bedarf bitte einfügen
    print('\n -- delete_direct_repeats')
    print(delete_direct_repeats([1, 2, 2, 4, 3, 3, 3, 2]))
    print(delete_direct_repeats(['a', 'a', 'a']))
    print(delete_direct_repeats([7, 7, 4, 7, 7, 7]))
    print(delete_direct_repeats([4.0]))
    print(delete_direct_repeats([[1], [], []]))

    print('\n -- balance')
    load1 = [0, 4]
    # balance(load1, 0, 1)
    print(load1)
    load2 = [0, -3, 1]
    # balance(load2, 0, 2)
    print(load2)
    load3 = [1, 2, 9, 10]
    # balance(load3, 0, 3)
    print(load3)
    load4 = [1, 2, 9, 10]
    # balance(load4, 0, 2)
    print(load4)
    load5 = [0, 9, 9]
    # balance(load5, 1, 1)
    print(load5)

    print('\n -- collect')
    # print(collect([('Welt', 1), ('Hallo', 2), ('schnöde', 0), ('!', 4)], 1, set()))
    # print(collect([('Welt', 1), ('Hallo', 2), ('schnöde', 0), ('!', 4)], 1, {0}))
    # print(collect([('Welt', 1), ('Hallo', 2), ('schnöde', 0), ('!', 4)], 0, {0}))
    # print(collect([('a,b,c', 0), ('b', 3), ('a', 1), ('c', 4)], 2, set()))
    # print(collect([('a,b,c', 0), ('b', 3), ('a', 1), ('c', 4)], 0, set()))


# -------------
# Aufgabe 2
# -------------


# Aufgabe a)
def fun_with_rivers() -> None:
    country_codes = {
        'AUT': 'Österreich',
        'DNK': 'Dänemark',
        'DEU': 'Deutschland',
        'CHE': 'Schweiz',
        'UKR': 'Ukraine',
        'POL': 'Polen',
        'ITA': 'Italien',
        'NLD': 'Niederlande',
        'SVK': 'Slowakei',
        'BGR': 'Bulgarien',
        'CZE': 'Tschechische Republik'
    }

    rivers = {
        'Donau': ['DEU', 'AUT', 'SVK', 'HUN', 'HRV', 'SRB', 'BGR', 'ROU', 'MDA', 'UKR'],
        'Elbe': ['CZE', 'DEU'],
        'Rhein': ['CHE', 'LIE', 'AUT', 'DEU', 'FRA', 'NLD'],
        'Po': ['ITA'],
        'Inn': ['CHE', 'AUT', 'DEU'],
        'Ebro': ['ESP']
    }

    # Die Namen aller Länder (in country_codes) die auf 'en' enden, durch ', ' getrennt, in einer Zeile
    # alphabetisch aufsteigend sortiert:
    # Erwartete Ausgabe:
    # Bulgarien, Italien, Polen
    # TODO implementieren

    # Alle Flüsse in rivers, die durch mehr als drei Länder fließen ausgeben.
    # Eine Zeile pro Fluss im Format
    # Flussname: (Anzahl der Länder)
    # Erwartete Ausgabe (Reihenfolge beliebig):
    # Donau (10)
    # Rhein (6)
    # TODO implementieren

    # Liste der Länder durch welche die Donau fließt in der ursprünglichen Reihenfolge.
    # Für in country_code definierte Länder wird der Name verwendet, für die anderen
    # '(???)'. Ausgabe in einer Zeile durch ' -> ' getrennt.
    # Erwartete Ausgabe (in dieser Reihenfolge):
    # Deutschland -> Osterreich -> Slowakei -> (???) -> (???) -> (???) -> Bulgarien -> (???) -> (???) -> Ukraine
    # TODO implementieren

    # Anzahl der verschiedenen Länder, durch die Flüsse in rivers fließen, sowie die Anzahl der davon in
    # country_codes definierten Länder.
    # Erwartete Ausgabe (wichtig sind die Zahlen, nicht die genaue Formulierung):
    # Die Flüsse fließen durch 17 verschiedene L¨ ander.
    # 9 davon kennen wir.
    # TODO: implementieren

    # Alle Flüsse in rivers die durch Österreich fließen, durch '~~' getrennt in einer Zeile ausgeben.
    # Erwartete Ausgabe (Reihenfolge beliebig):
    # Donau~~Rhein~~Inn
    # TODO: implementieren


# Aufgabe b)
def top_donors(donations: list[tuple[str, tuple[int, ...]]]) -> dict[str, list[int]]:
    # TODO: implementieren
    pass


def get_personal_total(aggregated_donations: dict, name: str) -> int:
    # TODO: implementieren
    pass


def exercise2() -> None:
    print('\n\n####### EXERCISE 2:')
    print('\n---- fun with rivers:')
    fun_with_rivers()

    print('\n---- top_donors:')
    dict_a = top_donors([('Alice', (200, 300)), ('Bob', (10, 10, 10)), ('Eve', (20, 50)),
                         ('Alice', (1000,)), ('Bob', (300, 300))])
    print(dict_a)
    # Erwartet: {'Alice': [200, 300, 1000], 'Bob': [10, 10, 10, 300, 300], 'Eve': [20, 50]}

    dict_b = top_donors([('GPA', (100, 100, 100)), ('GPA', (100, 100, 100)), ('GPA', (100, 100, 101)),
                         ('GPA', (150, 50, 101))])
    print(dict_b)
    # Erwartet: {'GPA': [100, 100, 100, 100, 100, 100, 100, 100, 101, 150, 50, 101]}

    print(top_donors([('A', (100, 100)), ('B', (100,))]))
    # Erwartet: {'A': [100, 100], 'B': [100]}

    print(top_donors([('Dagobert', ())]))
    # Erwartet: {'Dagobert': []}

    print(top_donors([]))
    # Erwartet: {}

    print('\n---- get_personal_total:')
    dict_a = {'Alice': [200, 300, 1000], 'Bob': [10, 10, 10, 300, 300], 'Eve': [20, 50]}
    dict_b = {'GPA': [100, 100, 100, 100, 100, 100, 100, 100, 101, 150, 50, 101]}
    print(get_personal_total(dict_a, 'Alice'))  # Erwartet: 1500
    print(get_personal_total(dict_a, 'Bob'))  # Erwartet: 630
    print(get_personal_total(dict_b, 'Alice'))  # Erwartet: -1
    print(get_personal_total(top_donors([('Alice', (0,))]), 'Alice'))  # Erwartet: 0
    print(get_personal_total(dict(), 'Bob'))  # Erwartet: -1


# -------------
# Aufgabe 3
# -------------


# TODO: direkt in TUWEL lösen -- keine Abgabe in dieser Datei


# -------------
# Aufgabe 4
# -------------


# Annahme: rechteckiges Spielfeld
def print_board(board: list[list[str]]) -> None:
    """
    Prints the current status of the game

    :param board: a rectangular list of lists, i.e. all lists in board have the same length
    """
    rows = ['|'.join(board[r]) for r in range(len(board))]
    seps = '-' * (2 * len(board) - 1)
    print(f'\n{seps}\n'.join(rows))


def get_desaster(desasters: list[tuple], board: list[list[str]]) -> tuple:
    """
    Decides if desaster struck.
     If yes, it returns a row, column or square hit by the desaster.
     If  no, it returns the tuple (False, )

    Has two modes:
        in random mode (selected by having desasters == None), all choices are made randomly
        in predefined mode (selected by desaster being a list), the decision is taken (and removed)
          from the list. If the list is empty, then no desaster occurred.

    :param desasters:
    :param round:
    :param board:
    :return:
    """
    if desasters is None:
        # random desaster
        if random.random() < 0.25:
            kind = random.choice(['row', 'column'])
            if kind == 'row':
                return kind, random.choice(list(range(0, len(board))))
            elif kind == 'column':
                return kind, random.choice(list(range(0, len(board[0]))))
        else:
            return (False,)
    elif len(desasters) > 0:
        return desasters.pop(0)
    else:
        return (False,)


def player_input(player: str, board: list[list[str]]) -> tuple[int, int]:
    print(f'Spieler {player} mit der ruhigen Hand, wohin mit der Figur?')
    row, col = -1, -1
    # TODO: Eingabe absichern, dass es zu keinen Abstürzen kommt
    row = int(input(f'Welche Zeile? (0-{len(board) - 1})> '))  # darf nicht verändert werden
    col = int(input(f'Welche Spalte? (0-{len(board[0]) - 1})> '))  # darf nicht verändert werden
    # TODO: vernünftigen Error werfen
    # TODO: überprüfen, ob es sich bei der Eingabe um ein gültiges freies Feld handelt (siehe Angabe) - falls nicht: Exception erzeugen
    return row, col


def clear_row(board: list[list[str]], rid: int) -> tuple[int, int]:
    # TODO: implementieren
    return -1, -1


def clear_column(board: list[list[str]], cid: int) -> tuple[int, int]:
    cnt = {'1': 0, '2': 0, ' ': 0}
    # TODO: implementieren
    return cnt['1'], cnt['2']


def run_game(rows: int, columns: int, start_pieces: int, rounds: int, desasters: list = None) -> None:
    board = [[' '] * columns for _ in range(rows)]
    pieces = {'1': start_pieces, '2': start_pieces}
    player = '1'
    max_rounds = rounds
    rounds_played = 0
    print_board(board)
    while rounds_played < 2 * max_rounds and pieces['1'] > 0 and pieces['2'] > 0:
        # TODO: Fehlerbehandlung falscher Eingaben
        row, col = player_input(player, board)
        # TODO: Das ausgewählte Feld in board auf den Wert von "player" setzen
        pieces[player] -= 1     # Die Anzahl der Steine des aktuellen player um 1 reduzieren
        print_board(board)      # Spielstand nach Zug
        rounds_played += 1
        desaster = get_desaster(desasters, board)
        if len(desaster) > 1:
            print(f'\n======\n -- !! UHOH - Desaster struck: {desaster} !!\n')
            fallen = 0, 0
            if desaster[0] == 'row':
                fallen = clear_row(board, desaster[1])
            elif desaster[0] == 'column':
                fallen = clear_column(board, desaster[1])
            pieces['1'] += fallen[0]            # Steine zurückgeben
            pieces['2'] += fallen[1]
            print_board(board)                  # Spielstand nach Desaster
        player = '2' if player == '1' else '1'  # Spielerwechsel
        print(f'## Steine übrig: Player 1: [{pieces["1"]}]  Player 2: [{pieces["2"]}]\n')

    print('\n #### SPIEL IST AUS ######')
    if pieces['1'] > pieces['2']:
        print('Player 2 hat gewonnen - die Letzten werden die Ersten sein.')
    elif pieces['1'] == pieces['2']:
        print('Unentschieden! Na sowas, gleich nochmal!')
    else:
        print('Player 1 hat gewonnen - kein Wunder bei dem Namen.')


def test_player_input() -> None:
    board_input = [[' ', ' ', '1'],
                   [' ', '2', '1'],
                   ['2', '2', '2']]
    try:
        player_input('X', board_input)
    except ValueError as val_error:
        print(f'VALUE ERROR: {val_error}')


def exercise4():
    ## Testfälle für clear_row:
    print('\n\n### CLEAR ROW')
    board_r = [[' ', '1', '2', '1'], ['1', ' ', '2', ' '], [' ', ' ', '2', ' ']]
    print(clear_row(board_r, 1))
    print(board_r)
    # Rückgabe: (1, 1)
    # board_r: [[' ', '1', '2', '1'], [' ', ' ', ' ', ' '], [' ', ' ', '2', ' ']]

    print(clear_row(board_r, 0))
    print(board_r)
    # Rückgabe: (2, 1)
    # board_r: [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', '2', ' ']]

    print(clear_row(board_r, 1))
    print(board_r)
    # Rückgabe: (0, 0)
    # board_r: [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', '2', ' ']]

    print(clear_row(board_r, 2))
    print(board_r)
    # Rückgabe: (0, 1)
    # board_r: [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]

    ## Testfälle für clear_column:
    print('\n\n### CLEAR COLUMN')
    board_c = [['1', ' ', '2', '1', '2'], [' ', ' ', ' ', ' ', ' '], ['2', ' ', '1', ' ', '1'],
               [' ', '2', '1', '2', '1']]
    print(clear_column(board_c, 1))
    print(board_c)
    # Rückgabe: (0, 1)
    # board_c: [['1', ' ', '2', '1', '2'], [' ', ' ', ' ', ' ', ' '], ['2', ' ', '1', ' ', '1'], [' ', ' ', '1', '2', '1']]

    print(clear_column(board_c, 4))
    print(board_c)
    # Rückgabe: (2, 1)
    # board_c: [['1', ' ', '2', '1', ' '], [' ', ' ', ' ', ' ', ' '], ['2', ' ', '1', ' ', ' '], [' ', ' ', '1', '2', ' ']]

    print(clear_column(board_c, 0))
    print(board_c)
    # Rückgabe: (1, 1)
    # board_c: [[' ', ' ', '2', '1', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', '1', ' ', ' '], [' ', ' ', '1', '2', ' ']]

    print(clear_column(board_c, 1))
    print(board_c)
    # Rückgabe: (0, 0)
    # board_c: [[' ', ' ', '2', '1', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', '1', ' ', ' '], [' ', ' ', '1', '2', ' ']]

    desasters_0 = [
        (False,),
        ('row', 0),
        ('column', 1),
        (False,),
        ('row', 2),
        (False,),
        (False,),
        ('row', 2),
        (False,),
        (False,)
    ]
    # Den Ablauf zu folgendem Aufruf finden Sie am PDD Aufgabenblatt5.pdf
    run_game(3, 4, 3, 6, desasters_0)

    print()
    print()

    desasters_1 = [
        (False,),
        (False,),
        (False,),
        ('column', 2),
        (False,),
        ('row', 3),
        ('column', 5),
        (False,),
        (False,),
        (False,),
        ('row', 3),
        ('row', 4),
        ('column', 2),
        (False,),
    ]

    # Den Ablauf zu folgendem Ablauf finden Sie in den Kommentaren unter dem Aufruf.
    run_game(5, 7, 5, 7, desasters_1)

    #   0|1|2|3|4|5|6
    # ---------------
    # 0: | | | | | |
    # ---------------
    # 1: | | | | | |
    # ---------------
    # 2: | | | | | |
    # ---------------
    # 3: | | | | | |
    # ---------------
    # 4: | | | | | |
    # Spieler 1 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 9
    # Welche Spalte? (0-6)> 4
    # Hihi, das ist aber keine gültige Zeile am Spielfeld!
    # Spieler 1 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 3
    # Welche Spalte? (0-6)> 2
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: | | | | | |
    # ---------------
    # 1: | | | | | |
    # ---------------
    # 2: | | | | | |
    # ---------------
    # 3: | |1| | | |
    # ---------------
    # 4: | | | | | |
    # ## Steine übrig: Player 1: [4]  Player 2: [5]
    #
    # Spieler 2 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 1
    # Welche Spalte? (0-6)> 5
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: | | | | | |
    # ---------------
    # 1: | | | | |2|
    # ---------------
    # 2: | | | | | |
    # ---------------
    # 3: | |1| | | |
    # ---------------
    # 4: | | | | | |
    # ## Steine übrig: Player 1: [4]  Player 2: [4]
    #
    # Spieler 1 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 0
    # Welche Spalte? (0-6)> 1
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | | | | |2|
    # ---------------
    # 2: | | | | | |
    # ---------------
    # 3: | |1| | | |
    # ---------------
    # 4: | | | | | |
    # ## Steine übrig: Player 1: [3]  Player 2: [4]
    #
    # Spieler 2 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 1
    # Welche Spalte? (0-6)> 2
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | |2| | |2|
    # ---------------
    # 2: | | | | | |
    # ---------------
    # 3: | |1| | | |
    # ---------------
    # 4: | | | | | |
    #
    # ======
    #  -- !! UHOH - Desaster struck: ('column', 2) !!
    #
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | | | | |2|
    # ---------------
    # 2: | | | | | |
    # ---------------
    # 3: | | | | | |
    # ---------------
    # 4: | | | | | |
    # ## Steine übrig: Player 1: [4]  Player 2: [4]
    #
    # Spieler 1 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 4
    # Welche Spalte? (0-6)> 0
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | | | | |2|
    # ---------------
    # 2: | | | | | |
    # ---------------
    # 3: | | | | | |
    # ---------------
    # 4:1| | | | | |
    # ## Steine übrig: Player 1: [3]  Player 2: [4]
    #
    # Spieler 2 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 3
    # Welche Spalte? (0-6)> 2
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | | | | |2|
    # ---------------
    # 2: | | | | | |
    # ---------------
    # 3: | |2| | | |
    # ---------------
    # 4:1| | | | | |
    #
    # ======
    #  -- !! UHOH - Desaster struck: ('row', 3) !!
    #
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | | | | |2|
    # ---------------
    # 2: | | | | | |
    # ---------------
    # 3: | | | | | |
    # ---------------
    # 4:1| | | | | |
    # ## Steine übrig: Player 1: [3]  Player 2: [4]
    #
    # Spieler 1 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 3
    # Welche Spalte? (0-6)> 2
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | | | | |2|
    # ---------------
    # 2: | | | | | |
    # ---------------
    # 3: | |1| | | |
    # ---------------
    # 4:1| | | | | |
    #
    # ======
    #  -- !! UHOH - Desaster struck: ('column', 5) !!
    #
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | | | | | |
    # ---------------
    # 2: | | | | | |
    # ---------------
    # 3: | |1| | | |
    # ---------------
    # 4:1| | | | | |
    # ## Steine übrig: Player 1: [2]  Player 2: [5]
    #
    # Spieler 2 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 2
    # Welche Spalte? (0-6)> 4
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | | | | | |
    # ---------------
    # 2: | | | |2| |
    # ---------------
    # 3: | |1| | | |
    # ---------------
    # 4:1| | | | | |
    # ## Steine übrig: Player 1: [2]  Player 2: [4]
    #
    # Spieler 1 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 3
    # Welche Spalte? (0-6)> 6
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | | | | | |
    # ---------------
    # 2: | | | |2| |
    # ---------------
    # 3: | |1| | | |1
    # ---------------
    # 4:1| | | | | |
    # ## Steine übrig: Player 1: [1]  Player 2: [4]
    #
    # Spieler 2 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 4
    # Welche Spalte? (0-6)> 4
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | | | | | |
    # ---------------
    # 2: | | | |2| |
    # ---------------
    # 3: | |1| | | |1
    # ---------------
    # 4:1| | | |2| |
    # ## Steine übrig: Player 1: [1]  Player 2: [3]
    #
    # Spieler 1 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 1
    # Welche Spalte? (0-6)> 2
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | |1| | | |
    # ---------------
    # 2: | | | |2| |
    # ---------------
    # 3: | |1| | | |1
    # ---------------
    # 4:1| | | |2| |
    #
    # ======
    #  -- !! UHOH - Desaster struck: ('row', 3) !!
    #
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | |1| | | |
    # ---------------
    # 2: | | | |2| |
    # ---------------
    # 3: | | | | | |
    # ---------------
    # 4:1| | | |2| |
    # ## Steine übrig: Player 1: [2]  Player 2: [3]
    #
    # Spieler 2 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 3
    # Welche Spalte? (0-6)> 1
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | |1| | | |
    # ---------------
    # 2: | | | |2| |
    # ---------------
    # 3: |2| | | | |
    # ---------------
    # 4:1| | | |2| |
    #
    # ======
    #  -- !! UHOH - Desaster struck: ('row', 4) !!
    #
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | |1| | | |
    # ---------------
    # 2: | | | |2| |
    # ---------------
    # 3: |2| | | | |
    # ---------------
    # 4: | | | | | |
    # ## Steine übrig: Player 1: [3]  Player 2: [3]
    #
    # Spieler 1 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 4
    # Welche Spalte? (0-6)> 3
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | |1| | | |
    # ---------------
    # 2: | | | |2| |
    # ---------------
    # 3: |2| | | | |
    # ---------------
    # 4: | | |1| | |
    #
    # ======
    #  -- !! UHOH - Desaster struck: ('column', 2) !!
    #
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1: | | | | | |
    # ---------------
    # 2: | | | |2| |
    # ---------------
    # 3: |2| | | | |
    # ---------------
    # 4: | | |1| | |
    # ## Steine übrig: Player 1: [3]  Player 2: [3]
    #
    # Spieler 2 mit der ruhigen Hand, wohin mit der Figur?
    # Welche Zeile? (0-4)> 1
    # Welche Spalte? (0-6)> 0
    #   0|1|2|3|4|5|6
    # ---------------
    # 0: |1| | | | |
    # ---------------
    # 1:2| | | | | |
    # ---------------
    # 2: | | | |2| |
    # ---------------
    # 3: |2| | | | |
    # ---------------
    # 4: | | |1| | |
    # ## Steine übrig: Player 1: [3]  Player 2: [2]
    #
    #
    #  #### SPIEL IST AUS ######
    # Player 2 hat gewonnen - die Letzten werden die Ersten sein.


if __name__ == '__main__':
    exercise1()
    # exercise2()
    # test_player_input()
    # exercise4()
