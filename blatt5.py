# -*- coding: utf-8 -*-
# GPA 2024
import copy


# -------------
# Aufgabe 1
# -------------


# TODO: 1.1: main_event(contestants: list[tuple[str, int]]) -> list[str]
def main_event(contestants: list[tuple[str, int]]) -> list[str]:



# TODO: 1.2: cheapest_design(offers: list[tuple]) -> tuple

# TODO: 1.3: closest(values: list[tuple[int, int]]) -> list[int]


def exercise1() -> None:
    # TODO: Testfälle bitte hier einfügen
    pass


# -------------
# Aufgabe 2
# -------------


def relocate(trains: dict, source: str, target: str) -> bool:
    # TODO: implementieren
    pass


def exercise2() -> None:
    carriage_types = {
        'E': 'Speisewagen',
        'F': '1.Klasse Wagen',
        'K': 'Familienwagen',
        'L': 'Liegewagen',
        'N': '2.Klasse Wagen',
        'R': 'Ruhewagen',
        'S': 'Schlafwagen'
    }

    trains = {
        'RJ01': ['F', 'R', 'E', 'N', 'N', 'M', 'N', 'K'],
        'NJ01': ['S', 'S', 'S', 'E', 'L', 'L', 'L', 'N', 'N'],
        'BlingBling': ['F', 'F', 'F', 'F', 'E', 'F', 'F', 'F', 'R'],
        'IC01': ['N', 'N', 'N', 'N']
    }

    orient_express = ['A', 'C', 'E', 'I', 'K', 'L', 'R', 1, ('F', 'S')]

    # Aufgabe a)

    # Die Namen aller Wagen-Typen, durch '|--|' getrennt, in einer Zeile, alphabetisch aufsteigend sortiert:
    # Erwartete Ausgabe:
    # 1.Klasse Wagen|--|2.Klasse Wagen|--|Familienwagen|--|Liegewagen|--|Ruhewagen|--|Schlafwagen|--|Speisewagen
    # TODO implementieren

    # Für jedes Element in orient_express '(Ah!)' ausgeben, wenn das Element ein Schlüssel in
    # carriage_types ist, und '(Oh?)' sonst. Ausgabe in einer Zeile durch '-' getrennt
    # in der Reihenfolge der Einträge in orient_express.
    # Erwartete Ausgabe (in dieser Reihenfolge):
    # (Oh?)-(Oh?)-(Ah!)-(Oh?)-(Ah!)-(Ah!)-(Ah!)-(Oh?)-(Oh?)
    # TODO implementieren

    # Zu jedem Zug in trains die Länge des Zuges (= Anzahl der Wagen) ausgeben.
    # Eine Zeile pro Zug im Format
    # Zugname: Länge
    # Erwartete Ausgabe (Reihenfolge beliebig):
    # RJ01: 8
    # NJ01: 9
    # BlingBling: 9
    # IC01: 4
    # TODO implementieren

    # Für den Zug 'RJ01' in trains: Eine Liste erstellen, die zu jedem Wagen dessen vollständigen
    # Namen enthält, wenn der Typ als Schlüssel in carriage_types auftritt, sonst
    # '(Unbekannt)' für den Wagen.
    # Die Reihenfolge der Einträge der Liste ist die selbe Reihenfolge wie in carriage_type.
    # Liste ausgeben.
    # Erwartete Ausgabe (in dieser Reihenfolge, aber in einer Zeile):
    # ['1.Klasse Wagen', 'Ruhewagen', 'Speisewagen', '2.Klasse Wagen', '2.Klasse Wagen', '(Unbekannt)',
    #  '2.Klasse Wagen', 'Familienwagen']
    # TODO implementieren

    # Aufgabe b)
    ex_d1 = {'train1': ['N'], 'train2': ['E'], 'train3': []}

    res = relocate(ex_d1, 'train1', 'train2')  # 'N' von 1 nach 2: True
    print(res, ex_d1)
    res = relocate(ex_d1, 'train2', 'train3')  # 'N' von 2 nach 3: True
    print(res, ex_d1)
    res = relocate(ex_d1, 'train1', 'train2')  # nichts passiert, weil 1 leer: False
    print(res, ex_d1)
    res = relocate(ex_d1, 'train3', 'train')   # nichts passiert, weil 'train' nicht existiert: False
    print(res, ex_d1)
    res = relocate(ex_d1, 'train', 'train1')   # nichts passiert, weil 'train' nicht existiert: False
    print(res, ex_d1)
    # zwei zusätzliche, positive Tests (nicht am PDF)
    res = relocate(trains, 'IC01', 'NJ01')     # True
    print(res, trains)
    res = relocate(trains, 'IC01', 'RJ01')     # True
    print(res, trains)


# -------------
# Aufgabe 3
# -------------


def cuddling_numbers_v1(values: list[int]) -> list[int]:
    max_dist = -1, -1
    for i in range(len(values) - 3):
        diff = abs(max(values[i:i + 3]) - min(values[i:i + 3]))
        if diff >= max_dist[0]:
            max_dist = diff, i
    return values[i: i + 3]


def cuddling_numbers_v2(values: list[int]) -> list[int]:
    max_dist = -1, -1
    for i in range(len(values) - 3):
        diff = abs(max(values[i:i + 3]) - min(values[i:i + 3]))
        if diff >= max_dist[0]:
            max_dist = diff, i
    return values[max_dist[1]: max_dist[1] + 3]


def cuddling_numbers_v3(values: list[int]) -> list[int]:
    result = values[:3]
    for i in range(0, len(values) - 2, 3):
        cur_vals = values[i:i + 3]
        if abs(max(cur_vals) - min(cur_vals)) > abs((max(result) - min(result))):
            result = cur_vals
    return result


def cuddling_numbers_v4(values: list[int]) -> list[int]:
    best_i, max_diff = 0, 0
    for i in range(1, len(values) - 1):
        if values[i + 1] - values[i - 1] > max_diff:
            best_i, max_diff = i - 1, values[i + 1] - values[i - 1]
    return values[best_i:][:3]


def cuddling_numbers_v5(values: list[int]) -> list[int]:
    diffs = [abs(max(values[i:i + 3]) - min(values[i:i + 3])) for i in range(0, len(values) - 3)]
    return values[diffs.index(max(diffs)):][:3]


def cuddling_numbers_v6(values: list[int]) -> list[int]:
    diffs = [abs(max(values[i:i + 3]) - min(values[i:i + 3])) for i in range(0, len(values) - 2)]
    return values[diffs.index(max(diffs)):][:3]


def run_tests(functions: list, testcases: list[tuple[list[int], list[int]]]) -> None:
    """
    Function provided to check if sufficient test-coverage has been reached.
    The evaluation of your testcases is written as output -- please check the output.

    You don't need to call this function explicitly, there exists already a call in
    the function exercise3(). Just fill the list with testcases in exercise3().

    You don't need to understand the implementation of this function - but there's no
    harm in checking it's source code.

    :param functions: A list of functions the testcases should be run against. Already set correctly
        when called from exercise3()
    :param testcases: The list of testcases, each testcase is a tuple of two lists: the first being
        the input to the testcase, the second the expected result.
    :return:
    """
    passed = [set() for _ in range(len(functions))]
    print('Ausgabe:\n'
          'Testfall <Nr>: "ok" oder "FAILED" [<input>: <berechnetes Ergebnis> (<erwartetes Ergebnis>)]')
    for idx, func in enumerate(functions):
        print(f'\n#### Funktion: {func.__name__}')
        for vidx, (value, expected) in enumerate(testcases):
            try:
                res = func(value)
                print(f'Testfall {vidx + 1}: {"ok" if expected == res else "FAILED"} [{value}: {res} ({expected})]')
                if res == expected:
                    passed[idx].add(f'TF {vidx + 1}')
            except Exception as e:
                print(f'Testfall {vidx + 1}: CRASHES with EXCEPTION')
    print()
    all_improved = True
    reintroduced_error = False
    failed = set()
    all_tcs = {f'TF {i}' for i in range(1, len(testcases) + 1)}
    for idx, ok in enumerate(passed[:-1]):
        diff = passed[idx + 1].difference(ok)
        if len(diff) == 0:
            all_improved = False
        print(f'Failed auf {functions[idx].__name__} aber ok auf {functions[idx + 1].__name__}: '
              f'{"ok" if diff else "MISSING"} ({diff})')
        if ok.difference(passed[idx + 1]).intersection(failed):
            print(f'{functions[idx + 1].__name__} führt bereits ausgebesserten Fehler wieder ein: '
                  f'{ok.difference(passed[idx + 1]).intersection(failed)}')
            reintroduced_error = True
        failed.update(all_tcs.difference(ok))

    print('\n ### ZUSAMMENFASSUNG:')
    print(f'Jede Funktion bessert einen Fehler ihrer Vorgängerin aus: {"ja" if all_improved else "NEIN (ACHTUNG!)"}')
    print(f'Mindestens eine Funktion führt einen Fehler wieder ein, der zuvor schon ausgebessert wurde: '
          f'{"ja" if reintroduced_error else "NEIN (ACHTUNG!)"}')


def exercise3():
    # Definiert die Liste der Funktionen, auf denen die Testfälle laufen sollen.
    # Am besten unverändert lassen.
    implementations = [cuddling_numbers_v1,
                       cuddling_numbers_v2,
                       cuddling_numbers_v3,
                       cuddling_numbers_v4,
                       cuddling_numbers_v5,
                       cuddling_numbers_v6
                       ]

    # Jeder Testcase besteht aus einem zweistelligen Tupel:
    #        an erster Stelle steht der Input (eine Liste mit mindestens 3 Einträgen),
    #        an zweiter Stelle das erwartete Ergebnis (eine Liste mit 3 Elementen)
    # Beispiel: ([1, 1, 1, 1, 1, 1, 1, 1, 100], [1, 1, 100])

    # TODO: Geben Sie in dieser Liste Ihre Testfälle an
    testcases = []

    # Diese Funktion ruft die Implementierungen auf den Testfällen auf und überprüft die geforderten Bedingungen.
    run_tests(implementations, testcases)


# -------------
# Aufgabe 4
# -------------


# TODO: Parameter überprüfen und Ausnahmen auslösen
def reverse_between(seq: tuple, start: int, end: int) -> tuple:
    return seq[:start] + seq[start:end + 1][::-1] + seq[end + 1:]


def exercise4() -> None:
    # Werte der Variablen dürfen nicht verändert werden!
    the_good_values = [((0, 1, 2, 3, 4, 5, 6, 7), 2, 5),
                       (('ich', 'gehe', 'hin', 'da'), 2, 3),
                       ((0, 1, 2), 0, 1),
                       (('G', 'P', 'A'), 1, 1),
                       (('a', 's', 'l', 'm', 'b', 'e', 's', 'e'), 2, 6)]
    the_bad_values = [((0, 1, 2), '0', 1),
                      (('G', 'P', 'A'), 1, '1'),
                      (['ich', 'gehe', 'hin', 'da'], 2, 3),
                      ('klappt nicht', 2.0, '5'),
                      (['klappt auch nicht'], 2, (5,)),
                      (tuple(), 0, 0),
                      (('G', 'P', 'A'), -1, 1),
                      (('G', 'P', 'A'), 2, 1),
                      (('G', 'P', 'A'), 2, 3),
                      (('G', 'P', 'A'), 2, 3.0)
                      ]
    the_ugly_values = []  # all values are beautiful
    result = ''

    for arg in the_good_values + the_bad_values:
        # TODO: Aufruf so gestalten dass Ausnahmen abgefangen werden und
        #  die Fehlermeldungen ausgegeben werden. Das Programm darf beim
        #  Ausführen der Funktion nicht abstürzen, und muss sämtliche
        #  Einträge der Liste bad_values durchlaufen (nicht nach dem ersten
        #  abbrechen)
        # result = reverse_between(*arg)     # Zeile reaktivieren sobald dies sicher möglich ist
        print('PASSED:', 'Testcase:', arg, 'Result:', result)


# -------------
# Aufgabe 5
# -------------


def neighbour_majority(board: list[list[str]], position: tuple[int, int]) -> str:
    # TODO: Funktion implementieren
    return '-'  # TODO: Zeile kann verändert/angepasst werden


def count_fields(board: list[list[str]]) -> dict[str, int]:
    # TODO: Funktion implementieren
    return {'X': 0, 'O': 0}  # TODO: Zeile kann verändert/angepasst werden


def print_board(board: list[list[str]]) -> None:
    """
    Visualizes the state of the game given in board by printing the board on the console.

    board is supposed to be a list of lists of strings (either the empty string or single character strings).
    The output consists of one line for each list in board, with each line containing one column for each entry
    of that list. Rows are separated by rows of '-', and colums are separated by '|'.
    :param board: The current state of the game as a list of lists of strings
    :return: None
    """
    rows = ['|'.join(board[r]) for r in range(len(board))]
    seps = '-' * (2 * len(board) - 1)
    print(f'\n{seps}\n'.join(rows))


def fill(board: list[list[str]]) -> list[list[str]]:
    """
    Creates a board representing the final state of the game after the empty fields have been assigned.

    Creates a copy of board and fills X or O into those empty positions where the symbol is present in the
    majority of neighbouring positions. Cells for which neither X nor O is present in more neighbouring
    cells in board than the other mark are left empty.
    This copy is returned.

    :param board: A list of lists of strings
    :return: A new list of lists of strings
    """
    result = copy.deepcopy(board)
    for ridx, row in enumerate(board):
        for cidx, field in enumerate(row):
            if field not in ('X', 'O'):
                symb = neighbour_majority(board, (ridx, cidx))
                if symb in ('X', 'O'):
                    result[ridx][cidx] = symb
    return result


def query_move(player_name: str, board: list[list[str]]) -> tuple[int, int]:
    """
    Dialog to aks a user to enter a field for their next move.

    Asks the user for a position on the board to pick as their next move. If an invalid choice
    (no valid integer, not on the board or an already occupied position) is entered, a ValueError
    exception is raised.

    :param player_name: Name of the player to be asked for their move
    :param board: List of lists of strings representing the board with the already occupied positions
    :return: Indices describing row and column of the selected field.
    """
    print(f'Erhabenes Wesen {player_name}, welches Feld möchten Sie als nächstes für sich beanspruchen?')
    asking = True
    row, col = -1, -1
    while asking:
        try:
            row = int(input(f'Welche Zeile ist genehm? (0-{len(board) - 1})> '))
            col = int(input(f'Und welche Spalte hat Ihr (unglaublicher) Intellekt gewählt? (0-{len(board) - 1})> '))
            asking = False
        except ValueError:
            print('Es tut mir schrecklich leid, aber könnte es sein, dass die Eingabe kein gültiger Integer war?')
    if not 0 <= row < len(board):
        raise ValueError('Ich bin untröstlich, aber ich kann diese Zeile am Spielfeld nicht finden!')
    if not 0 <= col < len(board):
        raise ValueError('Ich bin nicht würdig: Ich kann diese Spalte am Spielfeld nicht finden!')
    if board[row][col] != ' ':
        raise ValueError('Dieses Feld ... ich weiß nicht, wie ich es sagen soll ... ich fürchte, das ist schon belegt')
    return row, col


def run_game(size) -> None:
    """
    Main function of the game that controls the whole program.

    :param size: Size of the board (i.e. game is played on a size x size field)
    """
    board = [[' '] * size for _ in range(size)]
    marks = ('X', 'O')
    player = 0
    rounds = 0
    print_board(board)
    while (rounds // 2) < ((size ** 2) / 4):
        # TODO: Fehlerbehandlung falscher Eingaben
        row, col = query_move(marks[player], board)
        # TODO: Das ausgewählte Feld in board auf den Wert von marks[player] setzen
        print_board(board)  # Spieler:innen den aktuellen Spielstand zeigen
        rounds += 1
        player = 1 - player
    # Endstand berechnen
    result_board = fill(board)
    print('\nErgebnis nach "Auffüllen" der Felder:')
    print_board(result_board)
    result = count_fields(result_board)
    # TODO: Zum Ergebnis passende Meldung ausgeben
    print(f'Hurra! Erhabenes Wesen {marks[0]} gewinnt mit {result[marks[0]]}:{result[marks[1]]}. '
          f'Ich bin so froh, dass Sie es sind!')
    print(f'Hurra! Erhabenes Wesen {marks[1]} gewinnt mit {result[marks[1]]}:{result[marks[0]]}. '
          f'Ich bin so froh, dass Sie es sind!')
    print(f'Hurra! Ein gerechtes Unentschieden. Ich bin so froh, dass bei dem Spiel alle gewonnen haben!')


def exercise5() -> None:
    ## Testfälle für neighbour_majority:
    board = [[' ', 'X', 'O', ''], [' ', 'X', ' ', 'X'], [' ', 'O', 'O', ' '], [' ', 'X', 'O', ' ']]
    print_board(board)
    print()
    print(neighbour_majority(board, (0, 0)))  # Ergebnis: X
    print()
    print(neighbour_majority(board, (0, 3)))  # Ergebnis: -
    print()
    print(neighbour_majority(board, (1, 2)))  # Ergebnis: -

    board = [[' ', 'X', 'O', 'O'], [' ', 'X', ' ', 'X'], [' ', 'O', 'O', ' '], ['X', 'X', 'O', ' ']]
    print_board(board)
    print(neighbour_majority(board, (0, 0)))  # Ergebnis: X
    print()
    print(neighbour_majority(board, (1, 2)))  # Ergebnis: -
    print()
    print(neighbour_majority(board, (3, 3)))  # Ergebnis: O
    print()

    board = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', 'O', 'O', ' '], ['X', 'X', 'O', ' ']]
    print_board(board)
    print(neighbour_majority(board, (1, 0)))  # Ergebnis: -
    print()
    print(neighbour_majority(board, (3, 1)))  # Ergebnis: O
    print()

    ## Testfälle für count_fields:
    board = [[' ', 'X', 'O', ''], [' ', 'X', ' ', 'X'], [' ', 'O', 'O', ' '], [' ', 'X', 'O', ' ']]
    print(count_fields(board))  # {'X': 4, 'O': 4}
    board = [[' ', 'X', 'O', 'O'], [' ', 'X', ' ', 'X'], [' ', 'O', 'O', ' '], ['X', 'X', 'O', ' ']]
    print(count_fields(board))  # {'X': 5, 'O': 5}
    board = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', 'O', 'O', ' '], ['X', 'X', 'O', ' ']]
    print(count_fields(board))  # {'X': 2, 'O': 3}
    board = [[' ', 'X', 'O', ''], [' ', 'X', ' ', 'X'], [' ', 'O', 'O', ' '], [' ', 'X', 'O', ' ']]
    print(count_fields(fill(board)))  # {'X': 7, 'O': 6}
    board = [['A', 'A', 'B', 'X'], ['O', 'X', 'R', 'X'], ['O', 'R', 'A', 'B'], ['R', 'X', 'R', 'B']]
    print(count_fields(board))  # {'X': 4, 'O': 2}


if __name__ == '__main__':
    # exercise1()
    # exercise2()
    # exercise3()
    # exercise4()
    # exercise5()
    # run_game(4)
    pass
