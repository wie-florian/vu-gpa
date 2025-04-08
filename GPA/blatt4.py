# -*- coding: utf-8 -*-
# GPA 2025


# -------------
# Aufgabe 1
# -------------


# TODO: sum_up(begin, end)


# TODO: add_digits(expression)


# TODO: divide_by_seven(begin, end)


# TODO: biggest_char(line)


def exercise1():
    print('\n\n#### AUFGABE 1:')
    # print('\n--- sum_up')
    # print(sum_up(3, 4))
    # print(sum_up(-3, 3))
    # print(sum_up(2, 2))
    # print(sum_up(-4, 8))
    # TODO: auch wenn es die Angabe nicht explizit fordert:
    #       überlegen Sie, ob es weitere sinnvolle Testfälle gibt, die bislang nicht abgedeckt wurden

    print('\n--- add_digits')
    # print(add_digits(''))
    # print(add_digits('+3+2+1'))
    # print(add_digits('+9-3+8+7'))
    # print(add_digits('-4-4+5-0'))
    # TODO: auch wenn es die Angabe nicht explizit fordert:
    #       überlegen Sie, ob es weitere sinnvolle Testfälle gibt, die bislang nicht abgedeckt wurden

    print('\n--- divide_by_seven')
    # print(divide_by_seven(5, 5))
    # print(divide_by_seven(1, 6))
    # print(divide_by_seven(-7, 7))
    # print(divide_by_seven(2, 65))
    # TODO: auch wenn es die Angabe nicht explizit fordert:
    #       überlegen Sie, ob es weitere sinnvolle Testfälle gibt, die bislang nicht abgedeckt wurden

    print('\n--- biggest_char')
    # print(biggest_char('a'))
    # print(biggest_char('aA'))
    # print(biggest_char('12'))
    # print(biggest_char('abcdefg'))
    # print(biggest_char('ABcDEF'))
    # print(biggest_char('You thought that through'))
    # TODO: auch wenn es die Angabe nicht explizit fordert:
    #       überlegen Sie, ob es weitere sinnvolle Testfälle gibt, die bislang nicht abgedeckt wurden


# -------------
# Aufgabe 2
# -------------


# TODO: enclose(values)


# TODO: extract(seq)


# TODO: find_first_average(candidates, goal)


def exercise2():
    print('\n\n#### AUFGABE 2:')
    print('\n--- enclose:')
    # print(enclose([3, 2, 1, 6, 5, 4]))            # [1, 3, 2, 1, 6, 5, 4, 6]
    # print(enclose(['a']))                         # ['a', 'a', 'a']
    # print(enclose([1, 2, 0, 0, 4, 5]))            # [0, 1, 2, 0, 0, 4, 5, 5]
    # print(enclose([[], [3], [1, 1, 5]]))          # [[], [], [3], [1, 1, 5], [3]]
    # TODO: eigene Aufrufe (wie zuvor: nicht zwingend vorgeschrieben,
    #   aber überlegen Sie, ob weitere Testfälle nützlich sein könnten

    print('\n--- extract:')
    # print(extract([1, 2, 3, 4, 5]))               # (1, 1, 3, 1, 5)
    # print(extract((1, 2, 3, 4)))                  # (1, 1, 3, 0, 4)
    # print(extract('abc'))                         # ('a', 0, 'b', 0, 'c')
    # print(extract(('G', [1, 2], 5, 'P', 2, 5, 'A')))  # ('G', 2, 'P', 2, 'A')
    # TODO: eigene Aufrufe (wie zuvor: nicht zwingend vorgeschrieben,
    #   aber überlegen Sie, ob weitere Testfälle nützlich sein könnten

    print('\n--- find_first_average:')
    # print(find_first_average([1, 1, 1, 1, 1, 1], 1))      # [0, 1, 1, 1]
    # print(find_first_average([1, 4, 2, 1, 1.5, 1], 1.5))  # [2, 2, 1, 1.5]
    # print(find_first_average([2, 2, 2], 2))               # [0, 2, 2, 2]
    # print(find_first_average([4, 3, 3, 3], 3))            # [1, 3, 3, 3]
    # print(find_first_average([1, 1, 1, 1, 1, 1], 3))      # [-1]
    # print(find_first_average([1, 1], 1))                  # [-1]
    # TODO: eigene Aufrufe (wie zuvor: nicht zwingend vorgeschrieben,
    #   aber überlegen Sie, ob weitere Testfälle nützlich sein könnten


# -------------
# Aufgabe 3
# -------------


# TODO: split(values, threshold)


# TODO: winners(games)


# TODO: shared_by_all(values, *collections)


# TODO: top_donors(donations)


def exercise3():
    print('\n\n#### AUFGABE 3:')
    print('\n--- split:')
    # print(split([1, 7, 3, 9, 10], 5))                                  # ([2, 1, 3], [3, 7, 9, 10])
    # print(split({'ich', 'will', 'aber', 'nicht'}, 'mama'))             # ([2, 'ich', 'aber'], [2, 'will', 'nicht'])
    # print(split((['N', 'C', 'C'], ['-'], ['1701']), ['enterprise']))   # ([3, ['N', 'C', 'C'], ['-'], ['1701']], [0])
    # print(split('Na Na Na', 'a'))                                      # ([5, 'N', ' ', 'N', ' ', 'N'], [3, 'a', 'a', 'a'])
    # print(split([], 2025))                                             # ([0], [0])
    # TODO: eigene Aufrufe (wie zuvor: nicht zwingend vorgeschrieben,
    #          aber überlegen Sie, ob weitere Testfälle nützlich sein könnten

    print('\n--- winners:')
    # print(winners([('AUT', 0, 9, 'ESP'), ('ENG', 1, 0, 'GER'), ('GER', 7, 1, 'BRA'), ('ITA', 0, 0, 'ARG')]))
                                # Erwartet: {'ESP', 'GER', 'ENG'}
    # print(winners({('A', 1, 2, 'AA'), ('BBB', 3, 2, 'BB'), ('A', 0, 0, 'C')}))    # {'BBB', 'AA'}
    # print(winners(set()))                                                         # set()
    # TODO: eigene Aufrufe (wie zuvor: nicht zwingend vorgeschrieben,
    #          aber überlegen Sie, ob weitere Testfälle nützlich sein könnten

    print('\n--- shared_by_all:')
    # print(shared_by_all({1, 2, 3, 4}, {1, 3}, {2, 3, 4}, [2, 4, 5]))                      # {2, 4}
    # print(shared_by_all('Hallo', {1, 3}, 'hello', ('l', 'o', 'p')))                       # {'o', 'l'}
    # print(shared_by_all([(1,), (2,)], [(1,), tuple(), (2,)], ((3,), (2,), (1,)), 'na'))   # {(1,), (2,)}
    # print(shared_by_all('Singapore', 'ja', {1, 2}, [[], []]))                             # {'e', 'i', 'n', 'S', 'g', 'o', 'p', 'a', 'r'}
    # TODO: eigene Aufrufe (wie zuvor: nicht zwingend vorgeschrieben,
    #          aber überlegen Sie, ob weitere Testfälle nützlich sein könnten

    print('\n--- top_donors:')
    # print(top_donors([('Alice', (200, 300)), ('Bob', (10, 10, 10)), ('Eve', (20, 50)), ('Alice', (1000,)), ('Bob', (300, 300))]))
                            # Erwartet: {('Bob', 600, 2), ('Alice', 1000, 1), ('Bob', 30, 3)}
    # print(top_donors([('GPA', (100, 100, 100)), ('GPA', (100, 100, 100)), ('GPA', (100, 100, 101)), ('GPA', (150, 50, 101))]))
                            # Erwartet: {('GPA', 300, 3), ('GPA', 301, 3)}
    # print(top_donors({('A', (100, 100)), ('B', (100,))}))     # set()
    # TODO: eigene Aufrufe (wie zuvor: nicht zwingend vorgeschrieben,
    #          aber überlegen Sie, ob weitere Testfälle nützlich sein könnten


# -------------
# Aufgabe 4
# -------------


def visualize_queues(queues):
    """
    Expects a list of lists of integer values. Prints one row for each
    nested list. The row starts with a name for the list, and then
    has the values of the list separated by a space.
    To work as intended, all numbers must be in the range [-9;99]
    """
    qname = 'Schalter'
    print('-' * len(qname))
    for idx, line in enumerate(queues):
        print(f'{qname} {idx}:', end=' ')
        for person in line:
            print(f'{person:02}', end=' ')
        print()
    print()


def person_arrives(queues, qid, impatience):
    # TODO: Fügen Sie Ihre Implementierung hier ein
    pass


def time_passes(queues):
    # TODO: Fügen Sie Ihre Implementierung hier ein
    pass


def serve_snacks(queues, qid):
    # TODO: Fügen Sie Ihre Implementierung hier ein
    pass


def split_most_impatient_queue(queues):
    # TODO: Fügen Sie Ihre Implementierung hier ein
    pass


def customer_finished(queues, qid):
    # TODO: Fügen Sie Ihre Implementierung hier ein
    return -1


def cut_lines(queues, max_length):
    # TODO: Fügen Sie Ihre Implementierung hier ein
    return 0


def throws_tantrum(queues, position):
    # TODO: Fügen Sie Ihre Implementierung hier ein
    pass


def long_distance_chat(queues, pos, from_qid, to_qid):
    # TODO: Fügen Sie Ihre Implementierung hier ein
    return 0


def exercise4():
    print('\n\n## Aufgabe 4:')

    print('\n-- person arrives:')
    queues1 = [[4, 3, 9, 12], [], [3, 6, 12, 24]]
    person_arrives(queues1, 0, 2)
    print(queues1)
    # visualize_queues([[4, 3, 9, 12, 2], [], [3, 6, 12, 24]])
    person_arrives(queues1, 2, 48)
    print(queues1)
    # visualize_queues([[4, 3, 9, 12, 2], [], [3, 6, 12, 24, 48]])
    person_arrives(queues1, 1, 1)
    print(queues1)
    # visualize_queues([[4, 3, 9, 12, 2], [1], [3, 6, 12, 24, 48]])

    print('\n-- time_passed:')
    q2 = [[], [0, 0, 2, 3, 50], [25, 12, 5], [], [1]]
    q3 = [[]]
    time_passes(q2)
    print(q2)
    # visualize_queues([[], [1, 1, 3, 4, 51], [26, 13, 6], [], [2]])
    time_passes(q2)
    print(q2)
    # visualize_queues([[], [2, 2, 4, 5, 52], [27, 14, 7], [], [3]])
    time_passes(q3)
    print(q3)
    # visualize_queues([[]])

    print('\n-- serve_snacks:')
    q4 = [[14], [1, 10, 11, 20], [], [5, 15, 25]]
    serve_snacks(q4, 0)
    print(q4)
    # visualize_queues([[4], [1, 10, 11, 20], [], [5, 15, 25]])
    serve_snacks(q4, 1)
    print(q4)
    # visualize_queues([[4], [0, 0, 1, 10], [], [5, 15, 25]])
    serve_snacks(q4, 1)
    print(q4)
    # visualize_queues([[4], [0, 0, 0, 0], [], [5, 15, 25]])
    serve_snacks(q4, 1)
    print(q4)
    # visualize_queues([[4], [0, 0, 0, 0], [], [5, 15, 25]])
    serve_snacks(q4, 2)
    print(q4)
    # visualize_queues([[4], [0, 0, 0, 0], [], [5, 15, 25]])
    serve_snacks(q4, 3)
    print(q4)
    # visualize_queues([[4], [0, 0, 0, 0], [], [0, 5, 15]])
    serve_snacks(q4, 3)
    print(q4)
    # visualize_queues([[4], [0, 0, 0, 0], [], [0, 0, 5]])

    print('\n-- split_most_impatient_queue:')
    q5 = [[2, 7, 3], [10, 5], [8, 7], [2, 2, 2, 2]]
    q6 = [[], [0, 0, 0]]
    split_most_impatient_queue(q5)
    print(q5)
    # visualize_queues([[2, 7, 3], [10], [8, 7], [2, 2, 2, 2], [5]])
    split_most_impatient_queue(q5)
    print(q5)
    # visualize_queues([[2, 7, 3], [10], [8], [2, 2, 2, 2], [5], [7]])
    split_most_impatient_queue(q5)
    print(q5)
    # visualize_queues([[2], [10], [8], [2, 2, 2, 2], [5], [7], [7, 3]])
    split_most_impatient_queue(q5)
    print(q5)
    # visualize_queues([[2], [10], [8], [2, 2, 2, 2], [5], [7], [7, 3]])
    split_most_impatient_queue(q6)
    print(q6)
    # visualize_queues([[], [0, 0, 0]])

    print('\n-- customer_finished:')
    q7 = [[1, 2, 3], [4], [5, 6]]
    print(customer_finished(q7, 0))
    print(q7)
    # visualize_queues([[2, 3], [4], [5, 6]])
    print(customer_finished(q7, 1))
    print(q7)
    # visualize_queues([[2, 3], [], [5, 6]])
    print(customer_finished(q7, 1))
    print(q7)
    # visualize_queues([[2, 3], [], [5, 6]])
    print(customer_finished(q7, 2))
    print(q7)
    # visualize_queues()
    print(customer_finished(q7, 0))
    print(q7)
    # visualize_queues()

    print('\n-- cut_lines:')
    q8 = [[1, 2, 3, 4, 5], [0], [], [10, 11, 12]]
    print(cut_lines(q8, 3))
    print(q8)
    # visualize_queues([[1, 2, 3], [0], [], [10, 11, 12]])
    print(cut_lines(q8, 3))
    print(q8)
    # visualize_queues([[1, 2, 3], [0], [], [10, 11, 12]])
    print(cut_lines(q8, 2))
    print(q8)
    # visualize_queues([[1, 2], [0], [], [10, 11]])
    print(cut_lines(q8, 0))
    print(q8)
    # visualize_queues([[], [], [], []])

    print('\n-- throws_tantrum:')
    q9 = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1]]
    throws_tantrum(q9, (1, 1))
    print(q9)
    # visualize_queues([[1, 3, 1], [3, 6, 3], [1, 3, 1], [1, 1]])
    throws_tantrum(q9, (2, 2))
    print(q9)
    # visualize_queues([[1, 3, 1], [3, 6, 5], [1, 5, 6], [1, 1]])
    throws_tantrum(q9, (0, 0))
    print(q9)
    # visualize_queues([[6, 5, 1], [5, 6, 5], [1, 5, 6], [1, 1]])

    print('\n-- long_distance_chat:')
    q10 = [[1, 1, 1, 1], [1, 1], [1, 1, 1], [1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    print(long_distance_chat(q10, 1, 1, 5))
    print(q10)
    # visualize_queues([[1, 1, 1, 1], [1, 1], [1, 3, 1], [1, 3], [1, 3, 1, 1], [1, 1, 1, 1]])
    print(long_distance_chat(q10, 2, 0, 4))
    print(q10)
    # visualize_queues([[1, 1, 1, 1], [1, 1], [1, 3, 3], [1, 3], [1, 3, 1, 1], [1, 1, 1, 1]])
    print(long_distance_chat(q10, 3, 0, 4))
    print(q10)
    # visualize_queues([[1, 1, 1, 1], [1, 1], [1, 3, 3], [1, 3], [1, 3, 1, 1], [1, 1, 1, 1]])


# -------------
# Main
# -------------

if __name__ == '__main__':
    exercise1()
    exercise2()
    exercise3()