# -*- coding: utf-8 -*-
# GPA 2024


# -------------
# Aufgabe 1
# -------------


# TODO: sum_much_smaller_numbers(bottom, target)
def sum_much_smaller_numbers(bottom, target):
    if bottom**2 <= target:
        return bottom + sum_much_smaller_numbers(bottom + 1, target)
    else:
        return 0

# TODO: sum_up(start, end, skip)
def sum_up(start, end, skip):
    if start > end:
        return 0
    if start % 7 == 0 and skip > 0:
        return sum_up(start + 1, end, skip - 1)
    else:
        return start + sum_up(start + 1, end, skip)


# TODO: reach_it(goal, a, b)
def reach_it(goal, a, b, current=0, count=0, add_next='a'):
    if current >= goal:
        return count
    if add_next == 'a':
        return reach_it(goal, a, b, current + a, count + 1, 'b')
    else:
        return reach_it(goal, a, b, current + b, count + 1, 'a')

# TODO: move_to_end(line, char)
def move_to_end(line, char):
    if not line:
        return ''
    if line[0] == char:
        return move_to_end(line[1:], char) + char
    else:
        return line[0] + move_to_end(line[1:], char)

def exercise1():
    print('#### AUFGABE 1:')
    print('\nsum_much_smaller_numbers:')
    print(sum_much_smaller_numbers(1, 25))    # 15
    print(sum_much_smaller_numbers(6, 36))    # 6
    print(sum_much_smaller_numbers(6, 35))    # 0
    print(sum_much_smaller_numbers(1, 1000))  # 496
    print(sum_much_smaller_numbers(25, 5))    # 0
    # TODO: eigene Aufrufe (die vorgegebenen Aufrufe decken einige wichtige Fälle ab,
    #                       weitere Tests können aber sinnvoll sein)

    print('\nsum_up:')
    print(sum_up(1, 20, 1))   # 203
    print(sum_up(1, 20, 0))   # 210
    print(sum_up(0, 20, 1))   # 210
    print(sum_up(1, 20, 2))   # 189
    print(sum_up(1, 32, 10))  # 458
    print(sum_up(-7, 7, 1))   # 7
    # TODO: eigene Aufrufe (die vorgegebenen Aufrufe decken einige wichtige Fälle ab,
    #                       weitere Tests können aber sinnvoll sein)

    print('\nreach_it:')
    print(reach_it(6, 2, 3))      # 3
    print(reach_it(24, 2, 3))     # 10
    print(reach_it(100, 10, 20))  # 7
    print(reach_it(100, 20, 10))  # 7
    print(reach_it(70, 7, 3))     # 14
    print(reach_it(7, 10, 2))     # 1
    print(reach_it(2, 2, 1))      # 1
    # # TODO: eigene Aufrufe (die vorgegebenen Aufrufe decken einige wichtige Fälle ab,
    # #                       weitere Tests können aber sinnvoll sein)
    #
    print('\nmove_to_end:')
    print(move_to_end('Hoalolo', 'o'))                        # 'Hallooo'
    print(move_to_end('a,a,a,...der Winter der ist d', 'a'))  # ',,,...der Winter der ist daaa'
    print(move_to_end('oioioioioioioi', 'o'))                 # 'iiiiiiiooooooo'
    print(move_to_end('tut sich nix', '1'))                   # 'tut sich nix'
    print(move_to_end('alle ! stellen sich hinten an', '!'))  # 'alle stellen sich hinten an!'
    # # TODO: eigene Aufrufe (die vorgegebenen Aufrufe decken einige wichtige Fälle ab,
    # #                       weitere Tests können aber sinnvoll sein)
    #
# -------------
# Aufgabe 2
# -------------


# TODO: reverse_between(values, start, end)
def reverse_between(values, start, end):
    new_values = values[:start] + values[start:end+1][::-1] + values[end+1:]
    return new_values


# TODO: smallest_members(seqs)
def smallest_members(seqs):
    new_seqs = [ ]
    for i in seqs:
        new_seqs.append(min(i))
    return new_seqs


# TODO: find_available_seats(seats, n)
def find_available_seats(seats, n):
    counter = 0
    i = 0
    for j in seats:
        if j == '.':
            counter += 1
            if counter == n:
                return i - n + 1
        else:
            counter = 0
        i += 1
    return -1


# TODO: balance_passengers(left, right)
def balance_passengers(left, right):
    n_swaps = 0
    for i in range(len(left)):
        if i % 2 == 0:
            if left[i] < right[i]:
                left[i], right[i] = right[i], left[i]
                n_swaps += 1
        else:
            if left[i] > right[i]:
                left[i], right[i] = right[i], left[i]
                n_swaps += 1
    return n_swaps



def exercise2():
    print('\n\n#### AUFGABE 2:')
    # TODO: Ihre Aufrufe der Funktionen aus Aufgabe 2 hier
    print('\nreverse_between:')
    print(reverse_between((0, 1, 2, 3, 4, 5, 6, 7), 2, 5))      # (0, 1, 5, 4, 3, 2, 6, 7)
    print(reverse_between(('ich', 'gehe', 'hin', 'da'), 2, 3))  # ('ich', 'gehe', 'da', 'hin')
    print(reverse_between((0, 1, 2), 0, 1))                     # (1, 0, 2)
    print(reverse_between(('G', 'P', 'A'), 1, 1))               # ('G', 'P', 'A')
    print(reverse_between(reverse_between(('a', 's', 'l', 'm', 'b', 'e', 's', 'e'), 2, 6), 4, 5))
                                                             # Erwartet: ('a', 's', 's', 'e', 'm', 'b', 'l', 'e')
    # TODO: eigene Aufrufe
    print(reverse_between('leben', 0,4)) # nebel


    print('\nsmallest_members:')
    print(smallest_members([[4, 0, 4], 'hallo', (1, 0, 0)]))      # [0, 'a', 0]
    print(smallest_members(('0', [0], (0.1, -0.1, 7))))           # ['0', 0, -0.1]
    print(smallest_members((('ich', 'du', 'GPA'), ['!', '?'])))   # ['GPA', '!']
    print(smallest_members([]))                                   # []
    # TODO: eigene Aufrufe
    print(smallest_members([[1, 2, 3, 4, 5, 6, 0, 8, 9], '32109']))     # [0, '0']


    print('\nfind_available_seats:')
    print(find_available_seats('I ... Batman!', 3))                   # 2
    print(find_available_seats([0, '.', '.', 3, '.', '.', '.'], 4))   # -1
    print(find_available_seats([0, '.', '.', 3, '.', '.', '.'], 3))   # 4
    print(find_available_seats([0, '.', '.', 3, '.', '.', '.'], 2))   # 1
    print(find_available_seats(('.', '.', 'x'), 1))                   # 0
    print(find_available_seats('...', 4))                             # -1
    print(find_available_seats(('.', '..', '.'), 4))                  # -1
    print(find_available_seats([], 1))                                # -1
    # # TODO: eigene Aufrufe
    print(find_available_seats(['.', 'x', 'why', '.', '.', '.'], 3)) # 3

    print('\nFilter Maps by type:')
    print('\nbalance_passengers:')
    left = [0, 0, 0, 0, 0]
    right = [1, 1, 1, 1, 1]
    swaps = balance_passengers(left, right)
    print(left, right, swaps)                    # [1, 0, 1, 0, 1] [0, 1, 0, 1, 0] 3

    left = ['Batman', 'Thanos', 'Asterix']
    right = ['Robin', 'Avengers', 'Obelix']
    swaps = balance_passengers(left, right)
    print(left, right, swaps)                    # ['Robin', 'Avengers', 'Obelix'] ['Batman', 'Thanos', 'Asterix'] 3
    swaps = balance_passengers(left, right)
    print(left, right, swaps)                    # ['Robin', 'Avengers', 'Obelix'] ['Batman', 'Thanos', 'Asterix'] 0

    left = ['S', 't', 'o', 'rt', '!']
    right = ['S', 't', 'a', 'p', '!']
    swaps = balance_passengers(left, right)
    print(left, right, swaps)                    # ['S', 't', 'o', 'p', '!'] ['S', 't', 'a', 'rt', '!'] 1
    # TODO: eigene Aufrufe
    left = ['Bravo', 'Berta', 'Bernd']
    right = ['Alpha', 'Alex', 'Anton']
    swaps = balance_passengers(left, right)
    print(left, right, swaps)                   # ['Bravo', 'Alex', 'Bernd'] ['Alpha', 'Berta', 'Anton'] 1


# -------------
# Aufgabe 3
# -------------


# TODO: name_lengths(values, ending)
def name_lengths(values, ending):
    result_list = [ ]
    z = len(ending)
    for i in values:
        start = len(i) - z
        end = start + z
        if i[start:end] == ending:
            result_list.append(len(i))
    return result_list

# TODO: create_cards(colors, values)
def create_cards(colors, values):
    cards = set()
    for color in colors:
        for value in values:
            card = (color, value)
            cards.add(card)
    return cards

# TODO: grade(results)
def grade(results):
    positiv = set()
    negativ = set()
    nachtest = set()
    for result in results:
        name = result[0]
        scores = result[1:]
        if len(scores) == 1:
            nachtest.add(name)
        elif len(scores) == 2:
            total_score = sum(scores)
            if total_score >= 50:
                positiv.add(name)
            else:
                negativ.add(name)
    return (positiv, negativ, nachtest)

def exercise3():
    print('\n\n#### AUFGABE 3:')
    # TODO: Ihre Aufrufe der Funktionen aus Aufgabe 3 hier
    print('\nname_lengths:')
    print(name_lengths(['Hallo!', 'liebe', 'Studierende'], '!'))                       # [6]
    print(name_lengths(['Hallo!', 'liebe', 'Studierende'], 'e'))                       # [5, 11]
    print(name_lengths(['Aber', 'er', 'mochte', 'Rababer'], 'er'))                     # [4, 2, 7]
    print(name_lengths(['der ', 'schwer', 'wer', 'werde'], 'wer'))                     # [6, 3]
    print(name_lengths(['durchsucht-', 'die Pferdezucht'], 'ucht'))                    # [15]
    print(name_lengths([], 'nix'))                                                     # []
    print(name_lengths(['Verleihnix', 'Troubadix', 'Automatix'], 'us'))                # []
    # TODO: eigene Aufrufe

    print('\ncreate_cards:')
    print(create_cards(['a'], [1]))                 # {('a', 1)}
    print(create_cards([0], ['a', 'b']))            # {(0, 'b'), (0, 'a')}
    print(create_cards(['a', 'b'], [1]))            # {('a', 1), ('b', 1)}
    print(create_cards(['g', 'gp'], ['a', 'pa']))   # {('g', 'pa'), ('gp', 'pa'), ('gp', 'a'), ('g', 'a')}
    uno = create_cards(['rot', 'grün', 'gelb', 'blau'], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(uno)    # see below
    uno_expected = {('grün', 5), ('grün', 8), ('gelb', 0), ('blau', 0), ('rot', 2), ('rot', 8), ('gelb', 3),
                    ('gelb', 9), ('rot', 5), ('gelb', 6), ('blau', 3), ('blau', 6), ('blau', 9), ('grün', 1),
                    ('grün', 7), ('grün', 4), ('rot', 1), ('gelb', 2), ('rot', 4), ('gelb', 5), ('blau', 5),
                    ('rot', 7), ('gelb', 8), ('blau', 2), ('blau', 8), ('grün', 0), ('grün', 3), ('grün', 6),
                    ('grün', 9), ('rot', 0), ('rot', 6), ('gelb', 1), ('gelb', 7), ('rot', 3), ('rot', 9),
                    ('gelb', 4), ('blau', 1), ('blau', 4), ('blau', 7), ('grün', 2)}
    print(uno == uno_expected)                      # True
    # TODO: eigene Aufrufe

    print('\ngrade:')
    sw_studis = [('Luke', 48, 49), ('Lea', 50), ('Han', 24, 25), ('Chewie', 24, 26), ('Obi', 50)]
    st_studis = [('Jean-Luc', 47), ('#1', 23), ('Wesely', 50, 49), ('Geordie', 45, 43), ('Worf', 35, 25)]
    anon = [('1', 23), ('2', 23, 22), ('3', 20), ('4', 28, 10), ('5', 24, 25)]
    print(grade(sw_studis))  # ({'Luke', 'Chewie'}, {'Han'}, {'Lea', 'Obi'})
    print(grade(st_studis))  #  ({'Wesely', 'Worf', 'Geordie'}, set(), {'#1', 'Jean-Luc'})
    print(grade(anon))       # (set(), {'4', '5', '2'}, {'3', '1'})
    print(grade(anon[:1]))   # (set(), set(), {'1'})
    # TODO: eigene Aufrufe


# -------------
# Aufgabe 4
# -------------


def generate_empty_map(size):
    """
    Creates and returns an empty size x size map as list of list integers with all entries set to 0

    :param size: the number of rows and columns (creates a square map) as integer > 0
    """
    return [[0] * size for _ in range(size)]


def possible_moves(position):
    """
    returns a set containing which of the four moves (up - w, right - d, down - s, left - a) are
    currently available to the player, based on its current position.

    right and down are always possible, up and left only if the player is not positioned in the first
    row or column.

    :param position: a pair (row, column) of integers >= 0 representing the current position of the player on the map
    :return: A set containing at least 'd' and 's', and possibly 'w' and 'a'
    """
    moves = {'d', 's'}
    if position[0] > 0:
        moves.add('w')
    if position[1] > 0:
        moves.add('a')
    return moves


def show_help(position):
    """
    Prints the possible actions of the player to the console

    :param position: pair (row, column) of integers >= 0 representing the current position of the player on the map
    """
    moves = possible_moves(position)
    print()
    print('Deine möglichen Züge:')
    if 'w' in moves:
        print('- w: gehe hoch')
    if 'a' in moves:
        print('- a: gehe links')
    print('- s: gehe runter')
    print('- d: gehe rechts')
    print('- map: Die Karte anzeigen')
    print('- quit: Abenteuer beenden')


def gp_adventure(n, treasure_position):
    """
    Main function for our "game".

    :param n: integer > 0 - size of the original map
    :param treasure_position: pair (row, col) of integers with row, col >= 0
    """
    treasure_found = False
    moves = {'w', 'a', 's', 'd'}
    game_map = generate_empty_map(n)
    cur_row, cur_col = n // 2, n // 2
    visit_field(game_map, (cur_row, cur_col))
    show_help((cur_row, cur_col))
    action = input('Was willst du tun?> ').lower()
    while action != 'quit':

        print()
        if action in moves:
            if action in possible_moves((cur_row, cur_col)):
                if action == 'w':
                    cur_row -= 1
                elif action == 'a':
                    cur_col -= 1
                elif action == 's':
                    cur_row += 1
                elif action == 'd':
                    cur_col += 1

                if cur_row >= len(game_map):
                    add_row(game_map)
                elif cur_col >= len(game_map[cur_row]):
                    add_column(game_map)

                if (cur_row, cur_col) == treasure_position:
                    if treasure_found:
                        print('Ja, hier war der Schatz einmal - aber du hast ihn genommen und niemand hat nachgefüllt.')
                    else:
                        print('WOHOOOO! Schatz gefunden! (Wir, ähh, Du bist reich!)')
                        treasure_found = True
                visit_field(game_map, (cur_row, cur_col))

            else:
                print('Dieser Zug ist leider nicht möglich.')

        elif action == 'map':
            print_map(game_map, (cur_row, cur_col), treasure_position)

        print(f'Du stehst auf {cur_row}x{cur_col}', end=' ')
        if game_map[cur_row][cur_col] > 0:
            print(f'(hier warst du schon {game_map[cur_row][cur_col]} mal).')
        else:
            print('(ein bislang unbesuchtes Feld)')
        if treasure_found:
            print('Du hast den Schatz schon gefunden! (Super)')
        else:
            print('Du hast den Schatz leider noch nicht gefunden. (Such!)')
        show_help((cur_row, cur_col))
        action = input('Was willst du tun?> ').lower()

    print('Spiel vorbei. So viele Felder hast du in jeder Spalte besucht:')
    print_map(game_map, (-1, -1), treasure_position)
    print(*col_statistics(game_map), sep='')


def print_map(game_map, cur_pos, treasure_pos):
    # TODO: Fügen Sie Ihre Implementierung hier ein
    pass  # kann anschließend gelöscht werden, Python erlaubt keine leeren Funktionen


def add_row(game_map):
    # TODO: Fügen Sie Ihre Implementierung hier ein
    pass  # kann anschließend gelöscht werden, Python erlaubt keine leeren Funktionen


def add_column(game_map):
    # TODO: Fügen Sie Ihre Implementierung hier ein
    pass  # kann anschließend gelöscht werden, Python erlaubt keine leeren Funktionen


def visit_field(game_map, position):
    # TODO: Fügen Sie Ihre Implementierung hier ein
    pass  # kann anschließend gelöscht werden, Python erlaubt keine leeren Funktionen


def col_statistics(game_map):
    # TODO: Fügen Sie Ihre Implementierung hier ein
    return []


def exercise4():
    print('\n\n#### AUFGABE 4:')
    print('\nprint_map:')
    map1 = [[1, 2, 0],
            [0, 2, 0],
            [0, 2, 0],
            [0, 0, 0]]
    map2 = [[1, 2, 2, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 4, 2, 2],
            [0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0]]
    map3 = [[1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 2, 2, 2, 1]]
    print_map(map1, (2, 1), (3, 2))    # erwartete Ausgabe siehe Angabe
    print()
    print_map(map1, (0, 0), (0, 0))    # erwartete Ausgabe siehe Angabe
    print()
    print_map(map2, (2, 2), (0, 2))    # erwartete Ausgabe siehe Angabe
    print()
    print_map(map3, (3, 2), (10, 11))  # erwartete Ausgabe siehe Angabe
    print()

    print('\nvisit_field:')
    map4 = [[1, 2, 0], [0, 2, 2], [0, 0, 0]]
    visit_field(map4, (2, 0))     # [[1, 2, 0], [0, 2, 2], [1, 0, 0]]
    print(map4)
    visit_field(map4, (2, 0))     # [[1, 2, 0], [0, 2, 2], [2, 0, 0]]
    print(map4)
    visit_field(map4, (0, 0))     # [[2, 2, 0], [0, 2, 2], [2, 0, 0]]
    print(map4)
    visit_field(map4, (1, 2))     # [[2, 2, 0], [0, 2, 3], [2, 0, 0]]
    print(map4)

    print('\nadd_row:')
    map5 = [[1, 1, 1, 1, 1], [4, 4, 4, 4, 4]]
    map6 = [[1, 2], [3, 4]]
    add_row(map5)
    print(map5)                            # [[1, 1, 1, 1, 1], [4, 4, 4, 4, 4], [0, 0, 0, 0, 0]]
    add_row(map6)
    print(map6)                            # [[1, 2], [3, 4], [0, 0]]
    add_row(map6)
    print(map6)                            # [[1, 2], [3, 4], [0, 0], [0, 0]]

    print('\nadd_column:')
    map7 = [[1, 2, 3], [1], [1, 2]]
    add_column(map7)
    print(map7)                            # [[1, 2, 3, 0], [1, 0], [1, 2, 0]]
    add_column(map7)
    print(map7)                            # [[1, 2, 3, 0, 0], [1, 0, 0], [1, 2, 0, 0]]
    add_column(map6)
    print(map6)                            # [[1, 2, 0], [3, 4, 0], [0, 0, 0], [0, 0, 0]]

    print('\ncol_statistics:')
    map8 = [[0, 2, 1, 0, 0], [2, 8, 0, 2, 1], [1, 0, 0, 3, 1], [2, 1, 3, 7, 5]]
    print(col_statistics(map1))              # [1, 3, 0]
    print(col_statistics(map2))              # [2, 2, 3, 1, 1]
    print(col_statistics(map3))              # [6, 4, 1, 1, 1, 1]
    print(col_statistics(map4))              # [2, 2, 1]
    print(col_statistics(map5))              # [2, 2, 2, 2, 2]
    print(col_statistics(map6))              # [2, 2, 0]
    print(col_statistics(map8))              # [3, 3, 2, 3, 3]


if __name__ == '__main__':
    # exercise1()
    # exercise2()
    # exercise3()
    exercise4()
    # gp_adventure(3, (4,4))
