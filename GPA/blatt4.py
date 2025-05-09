# -*- coding: utf-8 -*-
# GPA 2025


# -------------
# Aufgabe 1
# -------------


def sum_up(begin, end):
    # Basisfall: Wenn begin größer als end ist, ist die Summe 0.
    if begin > end:
        return 0
    # Rekursiver Schritt: Berechne Term und addiere zur Summe des restlichen Intervalls.
    else:
        return (3 * begin - 2) + sum_up(begin + 1, end)


def add_digits(expression):
    # Basisfall: Wenn expression leer ist return 0
    if expression == '':
        return 0
    # Rekursion: verwandle erste zwei zeichen in int und addiere zur nächsten iteration ohne diesen zeichen
    else:
        return int(expression[0:2]) + add_digits(expression[2:])


def divide_by_seven(begin, end):
    # Basisfall: Wenn begin > end gibt | zurück. Für leere Erbenisse und am Ende
    if begin > end:
        return '|'
    # Rekursion 1: Wenn Zahl durch 7 teilbar -> gib sie zurück und mache neuen durchlauf mit nächster zahl
    if begin % 7 == 0:
        return f"|{begin}{divide_by_seven(begin + 1, end)}"
    # Rekursion 2: Wenn Zahl nicht durch 7 teilbar -> Rekursion mit nächster Zahl
    elif begin % 7 != 0:
        return f"{divide_by_seven(begin + 1, end)}"


def biggest_char(line):
    # Basisfall: Wenn line nur ein Zeichen hat gib es doppelt zurück
    if len(line) == 1:
        return line[0] + line[0]
    else:
        # Rekursiver Schritt: Erneuter Aufruf der Funktion ohne das erste Zeichen.
        rest = biggest_char(line[1:])
        # Vergleich zwischen dem ersten Zeichen `line[0]` und dem größten Zeichen vom Rest `rest[0]`
        if line[0] > rest[0]:
            # Wenn das erste Zeichen größer ist, kommt es an den Anfang der Zeile.
            return line[0] + line
        else:
            # Andernfalls wird das neue größte Zeichen vorne an die Zeile gestellt.
            return rest[0] + line


def exercise1():
    print('\n\n#### AUFGABE 1:')
    print('\n--- sum_up')
    print(sum_up(3, 4))
    print(sum_up(-3, 3))
    print(sum_up(2, 2))
    print(sum_up(-4, 8))
    print(sum_up(5, 1))

    print('\n--- add_digits')
    print(add_digits(''))
    print(add_digits('+3+2+1'))
    print(add_digits('+9-3+8+7'))
    print(add_digits('-4-4+5-0'))
    print(add_digits('+3+2+1'))

    print('\n--- divide_by_seven')
    print(divide_by_seven(5, 5))
    print(divide_by_seven(1, 6))
    print(divide_by_seven(-7, 7))
    print(divide_by_seven(2, 65))
    print(divide_by_seven(5, -8))
    print(divide_by_seven(7, 7))

    print('\n--- biggest_char')
    print(biggest_char('a'))
    print(biggest_char('aA'))
    print(biggest_char('12'))
    print(biggest_char('abcdefg'))
    print(biggest_char('ABcDEF'))
    print(biggest_char('You thought that through'))
    print(biggest_char(' '))
    print(biggest_char('1'))


# -------------
# Aufgabe 2
# -------------


def enclose(values):
    # Starte liste mit kleinstem Wert
    # Kann hier gestartet werden, da veränderbar
    list = [min(values)]

    # Fügt jedes Zeichen von values an die Liste an
    for val in values:
        list.append(val)

    # Fügt den höchsten wert hinzu
    list.append(max(values))

    return list

def extract(seq):
    n = len(seq)    # Länge der Sequenz
    v = n // 2      # Index für den mittleren Wert
    count1 = v - 1  # Wie viel ist zwischen 1. und v.
    count2 = n - v -2   # Wie viel ist zwischen n. und v.

    # Tuple wird direkt im return erstellt/zurückgegeben
    return seq[0], count1, seq[v], count2, seq[-1]


def find_first_average(candidates, goal):
    if len(candidates) < 3:
        return [-1]

    upper = goal + 0.00001
    lower = goal - 0.00001
    tag = True

    for i in range(len(candidates)):
        avg = sum(candidates[i:i+3]) / 3
        if lower <= avg <= upper:
            tag = False
            return [i, candidates[i], candidates[i+1], candidates[i+2]]
    if tag:
        return [-1]

    return [-1]


def find_first_average_recursive(candidates, goal, index=0):
    if len(candidates) < 3:
        return [-1]
    if index > len(candidates) - 3:
        return [-1]

    upper = goal + 0.00001
    lower = goal - 0.00001

    avg = sum(candidates[index:index + 3]) / 3
    if lower <= avg <= upper:
        return [index, candidates[index], candidates[index + 1], candidates[index + 2]]
    else:
        return find_first_average_recursive(candidates, goal, index + 1)




def exercise2():
    print('\n\n#### AUFGABE 2:')
    print('\n--- enclose:')
    print(enclose([3, 2, 1, 6, 5, 4]))            # [1, 3, 2, 1, 6, 5, 4, 6]
    print(enclose(['a']))                         # ['a', 'a', 'a']
    print(enclose([1, 2, 0, 0, 4, 5]))            # [0, 1, 2, 0, 0, 4, 5, 5]
    print(enclose([[], [3], [1, 1, 5]]))          # [[], [], [3], [1, 1, 5], [3]]
    print(enclose([True, False]))
    print(enclose([(1,0), (2,0), (3,0)]))

    print('\n--- extract:')
    print(extract([1, 2, 3, 4, 5]))               # (1, 1, 3, 1, 5)
    print(extract((1, 2, 3, 4)))                  # (1, 1, 3, 0, 4)
    print(extract('abc'))                         # ('a', 0, 'b', 0, 'c')
    print(extract(('G', [1, 2], 5, 'P', 2, 5, 'A')))  # ('G', 2, 'P', 2, 'A')
    print(extract((True,False,1,True)))                         # (True,1,1,0,True)
    print(extract([1, 1, 1, 1, 1]))                             # (1, 1, 1, 1, 1)
    print(extract([1, "a", True, 2.5, [1, 2]]))                 # (1, 1, True, 1, [1, 2])
    print(extract([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))   # ([1, 2], 1, [5, 6], 1, [9, 10])


    print('\n--- find_first_average:')
    print(find_first_average([1, 1, 1, 1, 1, 1], 1))      # [0, 1, 1, 1]
    print(find_first_average([1, 4, 2, 1, 1.5, 1], 1.5))  # [2, 2, 1, 1.5]
    print(find_first_average([2, 2, 2], 2))               # [0, 2, 2, 2]
    print(find_first_average([4, 3, 3, 3], 3))            # [1, 3, 3, 3]
    print(find_first_average([1, 1, 1, 1, 1, 1], 3))      # [-1]
    print(find_first_average([1, 1], 1))                  # [-1]
    print(find_first_average([], 5))                      # [-1]
    print(find_first_average([1,2,3,4,5,6,7,8,9], 8))     # [6, 7, 8, 9]
    print(find_first_average([-1,-2,-3,-4], -3))               # [1, -2, -3, -4]
    print(find_first_average([1,2.5,3], 2.16666))         # [0, 1, 2.5, 3]
    print(find_first_average([1,2.5,3], 2.1666))         # [-1]


# -------------
# Aufgabe 3
# -------------


def split(values, threshold):
    # initialisiere eine smaller und eine larger liste
    # liste hat bereits 0 als counter drin, wenn die liste anschließend befüllt wird kann
    # 0 mit der anzahl and items überschrieben werden
    smaller = [0]
    larger = [0]

    # checked jedes Zeichen in values und vergleicht es mit threshold
    # wenn kleiner kommt es in die liste smaller und wenn größer in die liste larger
    for v in values:
        if v < threshold:
            smaller.append(v)
        elif v >= threshold:
            larger.append(v)

    # zählt die objekte in den listen abzüglich des counters
    smaller[0] = len(smaller) - 1
    larger[0] = len(larger) - 1

    # gibt das tuple aus smaller und larger zurück
    return smaller, larger


def winners(games):
    # initialisiere ein set für winners
    winners = set()

    # für jedes game in games wird iteriert
    for game in games:
        # struktur des game objekt wird vorgegeben
        team1, points1, points2, team2 = game
        # der gewinner wird ermittelt und in winners hinzugefügt
        if points1 > points2:
            winners.add(team1)
        elif points1 < points2:
            winners.add(team2)

    # gibt das winners set zurück
    return winners


def shared_by_all(values, *collections):
    # Erstelle eine Liste aus allen collections welche mehr als 3 Einträge haben
    valid_collections = [col for col in collections if len(col) >= 3]
    # print(f"Values: {values}")
    # print(valid_collections)

    # Wenn valid_collections leer ist, wird das set aus values zurückgegeben
    if not valid_collections:
        return set(values)

    # Starte set für "shared", wo alles hineinkommt, was in allen collections vorkommt.
    shared = set()
    # Für jeden value in values
    for value in values:
        # initialisiere eine flag, die bestimmt ob value in allen vorkommt oder nicht.
        is_shared = True
        # Prüft jede collection in valid_collections, nach einander
        for collection in valid_collections:
            # Wenn value nicht in der zu testenden collection aus valid_collections ist, wird die flag auf false gesetzt
            if value not in collection:
                is_shared = False
        # wenn für den value die flag nie auf False gesetzt wurde, so wurde er in allen valid_collections gefunden
        # und in das set "shared" hinzugefügt
        if is_shared:
            shared.add(value)
        # vorteil vom set ist, wenn ein value öfter vorkommt wird er nur einmal hinzugefügt und nicht
        # so oft wie er in values vorkommt

    return shared



def top_donors(donations):
    donors = set()

    for donators in donations:
        donation = 0
        donor, amounts = donators
        for amount in amounts:
            donation += amount
        if donation > 500 or len(amounts) > 2:
            donors.add((donor, donation, len(amounts)))

    return donors


def exercise3():
    print('\n\n#### AUFGABE 3:')
    print('\n--- split:')
    print(split([1, 7, 3, 9, 10], 5))                                  # ([2, 1, 3], [3, 7, 9, 10])
    print(split({'ich', 'will', 'aber', 'nicht'}, 'mama'))             # ([2, 'ich', 'aber'], [2, 'will', 'nicht'])
    print(split((['N', 'C', 'C'], ['-'], ['1701']), ['enterprise']))   # ([3, ['N', 'C', 'C'], ['-'], ['1701']], [0])
    print(split('Na Na Na', 'a'))                                      # ([5, 'N', ' ', 'N', ' ', 'N'], [3, 'a', 'a', 'a'])
    print(split([], 2025))                                             # ([0], [0])
    print(split(['a','Rest'], 'Test'))  # ([1, 'Rest'], [1, 'a'])
    print(split(['Na Na Na'], ''))  # ([0], [1, 'Na Na Na'])

    print('\n--- winners:')
    print(winners([('AUT', 0, 9, 'ESP'), ('ENG', 1, 0, 'GER'), ('GER', 7, 1, 'BRA'), ('ITA', 0, 0, 'ARG')]))
                                # Erwartet: {'ESP', 'GER', 'ENG'}
    print(winners({('A', 1, 2, 'AA'), ('BBB', 3, 2, 'BB'), ('A', 0, 0, 'C')}))    # {'BBB', 'AA'}
    print(winners(set()))                                                         # set()

    print(winners([('A', 1, 0, 'B'), ('A', 2, 0, 'C')]))  # {'A'}
    print(winners([('A', 0, 1, 'B'), ('A', 0, 2, 'C')]))  # {'B', 'C'}
    print(winners([('A', 1, 1, 'B'), ('C', 2, 2, 'D')]))  # set()
    print(winners([('A', 1, 0, 'A')]))                      # {'A'}


    print('\n--- shared_by_all:')
    print(shared_by_all({1, 2, 3, 4}, {1, 3}, {2, 3, 4}, [2, 4, 5]))                      # {2, 4}
    print(shared_by_all('Hallo', {1, 3}, 'hello', ('l', 'o', 'p')))                       # {'o', 'l'}
    print(shared_by_all([(1,), (2,)], [(1,), tuple(), (2,)], ((3,), (2,), (1,)), 'na'))   # {(1,), (2,)}
    print(shared_by_all('Singapore', 'ja', {1, 2}, [[], []]))                             # {'e', 'i', 'n', 'S', 'g', 'o', 'p', 'a', 'r'}

    print(shared_by_all({1, 2, 3}, {4, 5, 6}))  # {} - Keine gemeinsamen Elemente
    print(shared_by_all("abc", "abef", "acd"))  # {'a'}
    print(shared_by_all({1, 'a', 2}, ['a', 1, 3], (2, 'a')))  # {1, 'a'}
    print(shared_by_all(set(), set(), set()))  # set()


    print('\n--- top_donors:')
    print(top_donors([('Alice', (200, 300)), ('Bob', (10, 10, 10)), ('Eve', (20, 50)), ('Alice', (1000,)), ('Bob', (300, 300))]))
                            # Erwartet: {('Bob', 600, 2), ('Alice', 1000, 1), ('Bob', 30, 3)}
    print(top_donors([('GPA', (100, 100, 100)), ('GPA', (100, 100, 100)), ('GPA', (100, 100, 101)), ('GPA', (150, 50, 101))]))
                            # Erwartet: {('GPA', 300, 3), ('GPA', 301, 3)}
    print(top_donors({('A', (100, 100)), ('B', (100,))}))     # set()

    print(top_donors([('Alice', (0,0,0,0))]))  # keine spende aber 4 mal → {('Alice', 0, 1)}
    print(top_donors([('David', ())]))  # Leere Spendenliste -> set()
    print(top_donors([]))  # Leere Eingabe -> set()



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
    queues[qid].append(impatience)
    return


def time_passes(queues):
    for queue in queues:
        for person in range(len(queue)):
            queue[person] += 1
    pass


def serve_snacks(queues, qid):
    for person in range(len(queues[qid])):
        if queues[qid][person] > 10:
            queues[qid][person] -= 10
        elif queues[qid][person] <= 10:
            queues[qid][person] = 0
    pass


def split_most_impatient_queue(queues):
    ungeduld_score = -1
    queue_imp = -1

    for i, queue in enumerate(queues):
        queue_ungeduld = sum(queue)
        if queue_ungeduld > ungeduld_score:
            ungeduld_score = queue_ungeduld
            queue_imp = i

    if queue_imp != -1 and len(queues[queue_imp]) > 1:
        queue_to_split = queues[queue_imp]
        mid_index = len(queue_to_split) // 2
        first_half = queue_to_split[:mid_index]
        second_half = queue_to_split[mid_index:]

        queues[queue_imp] = first_half
        queues.append(second_half)

    pass


def customer_finished(queues, qid):
    if len(queues[qid]) != 0:
        item = queues[qid].pop(0)
        return item
    else:
        return -1


def cut_lines(queues, max_length):
    sent_home = []
    for queue in queues:
        if len(queue) > max_length:
            sent_home.append(queue[max_length:])
            queue[:] = queue[:max_length]
    if sent_home == []:
        sent_home = [-1]
    return sent_home


def throws_tantrum(queues, position):
    qid, pos = position
    queues[qid][pos] += 5

    if pos+1 in range(len(queues[qid])):
        queues[qid][pos+1] += 2
    if pos-1 in range(len(queues[qid])):
        queues[qid][pos-1] += 2
    if qid-1 in range(len(queues)) and pos in range(len(queues[qid-1])):
        queues[qid-1][pos] += 2
    if qid+1 in range(len(queues)) and pos in range(len(queues[qid+1])):
        queues[qid+1][pos] += 2

    pass


def long_distance_chat(queues, pos, from_qid, to_qid):
    counter = 0
    queue_range = range(from_qid+1, to_qid)
    for qid in queue_range:
        if pos in range(len(queues[qid])):
            queues[qid][pos] += 2
            counter += 1
    return counter


def exercise4():
    print('\n\n## Aufgabe 4:')

    print('\n-- person arrives:')
    queues1 = [[4, 3, 9, 12], [], [3, 6, 12, 24]]
    print(queues1)
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
    # exercise1()
    # exercise2()
    # exercise3()
    exercise4()