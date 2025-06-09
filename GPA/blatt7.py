# -*- coding: utf-8 -*-
# GPA 2025

# 3.6.2025 (10:00): Korrektur von func_2(): statt "_ in amount" jetzt korrekt "_ in range(amount)"

from deque import Deque
from stack import Stack


# -------------
# Aufgabe 1
# -------------


def exercise1():
    points = [[0, 0, 0, 1], [100, 200, 320], [1000], [999, 502, 707], [301, 202]]
    # points aufsteigend nach Länge der Einträge sortieren und ausgeben
    # Erwartete Ausgabe: [[1000], [301, 202], [100, 200, 320], [999, 502, 707], [0, 0, 0, 1]]
    points.sort(key=len)
    print(points)

    # points Absteigend nach Spannweite (= Differenz zwischen größten und kleinsten Eintrag) der Einträge sortieren
    # Erwartete Ausgabe: [[999, 502, 707], [100, 200, 320], [301, 202], [0, 0, 0, 1], [1000]]
    def list_range(sublist):
        if not sublist:
            return 0
        return max(sublist) + min(sublist)

    points.sort(key=list_range)
    print(points)


    # Der erste Wert jedes Tupels ist der Name einer Stadt in Österreich, der zweite
    # Wert die Einwohnerzahl (gerundet auf 5000 Einwohner)
    # source: Statstik Austria, Stand 2024
    cities = [('Leonding', 30_000),
              ('Feldkirch', 35_000),
              ('Tulln', 15_000),
              ('Baden', 25_000),
              ('Wels', 65_000),
              ('Krems', 25_000),
              ('Villach', 65_000),
              ('Dornbirn', 50_000),
              ('Leoben', 25_000),
              ('Kapfenberg', 20_000),
              ]

    # Neue Liste mit selben Einträgen, absteigend sortiert nach Einwohnerzahl (bei gleicher Einwohnerzahl nach Name),
    # erstellen und ausgeben.
    # Erwartete Ausgabe:
    # [('Wels', 65000), ('Villach', 65000), ('Dornbirn', 50000), ('Feldkirch', 35000), ('Leonding', 30000), ('Leoben', 25000), ('Krems', 25000), ('Baden', 25000), ('Kapfenberg', 20000), ('Tulln', 15000)]
    cities_sorted = list(cities)
    cities_sorted.sort(key=lambda city: city[0], reverse=True)

    cities_sorted.sort(key=lambda city: city[1], reverse=True)
    print(cities_sorted)

    # Freiwillig: Städte mit gleicher Einwohnerzahl aufsteigend nach Namen sortieren.
    # Erwartete Ausgabe:
    # [('Villach', 65000), ('Wels', 65000), ('Dornbirn', 50000), ('Feldkirch', 35000), ('Leonding', 30000), ('Baden', 25000), ('Krems', 25000), ('Leoben', 25000), ('Kapfenberg', 20000), ('Tulln', 15000)]
    cities_sorted2 = list(cities)
    cities_sorted2.sort(key=lambda city: city[0], reverse=False)

    cities_sorted2.sort(key=lambda city: city[1], reverse=True)
    print(cities_sorted2)


    students = {
        "Alice": {"beginn": 2019, "ende": 2025},
        "Bob": {"beginn": 2013},
        "Charlie": {"beginn": 2020, "pause": 3},
        "Dave": {"beginn": 2016, "ende": 2022},
        "Eve": {"beginn": 2018, "ende": 2023, "pause": 2},
        "Fritz": {"beginn": 2021},
        "Gustav": {"beginn": 2020, "ende": 2025}
    }

    # bisherigen Studiendauer ist: ende (heuer falls noch nicht abgeschlossen) - beginn - pause (0 falls nicht pausiert)
    # Liste mit den Namen der Studierenden, aufsteigend sortiert nach der (bisherigen) Studiendauer
    # Erwartete Ausgabe:
    # ['Charlie', 'Eve', 'Fritz', 'Gustav', 'Alice', 'Dave', 'Bob']
    aktuelles_jahr = 2025

    def studiendauer_berechnen(student_data):
        beginn = student_data.get('beginn', None)
        ende = student_data.get('ende', aktuelles_jahr)
        pause = student_data.get('pause', 0)
        return ende - beginn - pause

    student_list = list(students.keys())
    sorted_student_list = sorted(student_list, key= lambda name: studiendauer_berechnen(students[name]))
    print(sorted_student_list)

# -------------
# Aufgabe 2
# -------------

# Beispielfunktion:
# obere Schranke: O(n^2)
# Begründung: 2 verschachtelte Schleifen welche über jeweils n Elemente laufen => n*n
def example_func(n: int) -> None:
    for i in range(n):
        for j in range(n):
            print(i, ':', j)


# ==== Ende Beispielfunktion


# -- Funktionen ohne Listen


# obere Schranke: O(n^4)
# Begründung: 2 verschachtelte Schleifen, die äußere läuft n^2 mal und die innere ebenso, wenn i klein ist -> n^2 * n^2 = n^4
def func_1(n):
    for i in range(1, n ** 2 + 1):
        for j in range(i, n ** 2 + 1):
            print(f'({i},{j})')


# obere Schranke: O(log(n))
# Begründung: Die Funktion teilt val immer durch 10  und ist somit proportional zu der Anzahl an Ziffern von n == log_{10}(n)
def func_2(n):
    amount = 0
    val = n
    while val > 0:
        i = val % 10
        if i % 3 == 0:
            amount += 1
        val = val // 10
    for _ in range(amount):
        print('_', end=' ')
    print()
    return amount


# obere Schranke: O(10n) == O(n)
# Begründung: Äußere Schleife läuft immer 10 mal, die innere n-mal, somit ist die innere die dominante für die Schranke
def func_3(n):
    count = 0
    for i in range(10):
        for j in range(n):
            count += 1
    return count


# obere Schranke: O(n^2)
# Begründung: Äußere Schleife läuft n mal, die innere läuft n + n*n, also n^2 mal
def func_4(n):
    k = n
    for i in range(n):
        k += n
    curval = 1
    cursum = 0
    for j in range(k):
        cursum += curval
        curval *= -1
    return cursum


# ---- Funktionen mit Listen


# obere Schranke: O(n^2)
# Begründung: die äußere Schleife läuft n/2 mal, das if statement erstellt immer eine Kopie der ersten Hälfte der Schleife, und sucht dann, im schlimmsten Fall ist die Suche proportional zu n
# Außen n/2 -> O(n), Innen O(n) --> Gesamt O(n^2)
def func_l1(values: list[int]) -> list[int]:
    result = []
    i = len(values) // 2
    while i < len(values):
        if values[i] in values[:len(values) // 2]:
            result.append(values[i])
        i += 1
    return result


# obere Schranke: O(n)
# Begründung: alle Operationen sind recht einfach, nur das erstellen der Tupel, welche n-mal abläuft (Länge der liste)
def func_l2(first: list) -> list[tuple]:
    if len(first) < 10 ** 10:
        return [(first[i], first[-i]) for i in range(len(first))]
    else:
        return []


# obere Schranke: O(n log(n))
# Begründung: while halbiert step jedes mal --> log, in der Schleife muss count die gesamte Liste durchlaufen --> n
def func_l3(values: list[int]) -> int:
    step = len(values) // 2
    idx = step
    while step > 0:
        step //= 2
        if values.count(values[idx]) < 2:
            idx -= step
        else:
            idx += step
    return values[idx]


# obere Schranke: O(2^n)
# Begründung: weil in der for-schleife result = result + result, so verdoppelt sich result bei jedem durchlauf, da es
# sich um strings und keine Zahlen handelt, wird dadurch jedesmal ein neuer string erstellt
def func_l4(values: str):
    n = len(values)
    result = values[:1]
    for i in range(n):
        result = result + result
    result += '!'
    return result.find('!')


def exercise2():
    pass


# -------------
# Aufgabe 3
# -------------


def can_beat(cards: list[tuple[str, int]], given: tuple[str, int]) -> bool:
    given_color, given_value = given[0], given[1]
    n = len(cards)

    # Suche index der ersten karte mit der gegebenen Farbe, wegen der Reihenfolge, ist dies die Karte mit dem höchsten wert für diese farbe sein.
    low = 0
    high = n - 1
    first_color_idx = -1

    while low <= high:
        mid = (low + high) // 2
        mid_card_color = cards[mid][0]

        if mid_card_color < given_color:
            low = mid + 1
        elif mid_card_color > given_color:
            high = mid - 1
        else:
            first_color_idx = mid
            high = mid - 1

    if first_color_idx == -1:
        return False

    # Wir haben den first_color_idx (höchster Wert für diese Farbe) -> überprüfen obWert höher als gegebener Wert
    if cards[first_color_idx][1] > given_value:
        return True
    else:
        return False


def exercise3():
    # Verwenden Sie bitte diese Funktion, wenn Sie Ihre Implementierung testen möchten.
    cards_1 = [('blau', 2), ('rot', 9), ('rot', 5), ('rot', 4), ('rot', 2), ('rot', 0)]
    cards_2 = [('blau', 12), ('blau', 8), ('blau', 5), ('blau', 2), ('rot', 9), ('rot', 5), ('rot', 4), ('rot', 2),
               ('rot', 0)]

    print(can_beat(cards_1, ('rot', 4)))  # True
    print(can_beat(cards_1, ('rot', 3)))  # True
    print(can_beat(cards_1, ('rot', 9)))  # False
    print(can_beat(cards_1, ('rot', 22)))  # False
    print(can_beat(cards_1, ('blau', 1)))  # True
    print(can_beat(cards_1, ('blau', 2)))  # False
    print(can_beat(cards_1, ('grün', 0)))  # False
    print(can_beat(cards_1, ('schwarz', 0)))  # False
    print(can_beat(cards_1, ('a', 0)))  # False

    print(can_beat(cards_2, ('grün', 3)))  # False
    print(can_beat(cards_2, ('blau', 8)))  # True
    print(can_beat(cards_2, ('blau', 9)))  # True
    print(can_beat(cards_2, ('blau', 12)))  # False
    print(can_beat(cards_2, ('rot', 8)))  # True
    print(can_beat(cards_2, ('rot', 9)))  # False


# -------------
# Aufgabe 4
# -------------


# Annahme: len(values) >= 1
def min_before(values: list[int]) -> list[int]:
    return [min(values[:i]) for i in range(1, len(values))]


# Laufzeit der gegebenen Funktion: O(n^2)


# Annahme: len(values) >= 1
def min_before_linear(values: list[int]) -> list[int]:
    result = []
    current_overall_min = values[0]

    for i in range(1, len(values)):
        result.append(current_overall_min)
        current_overall_min = min(current_overall_min, values[i])

    return result


# kurze Begründung für lineare Laufzeit:
# Die Funktion durchläuft die Eingabeliste 'values' genau einmal mit einer einfachen 'for'-Schleife.
# In jeder Iteration werden nur konstante Operationen ausgeführt.


def exercise4():
    test_cases = [
        [5, 9, 2, 4, 1, 8, 2],
        [10, 20, 30, 40, 50],
        [50, 40, 30, 20, 10],
        [7],
        [1, 1, 1, 1, 1],
        [-1, -5, 0, 10, -20]
    ]

    print("--- Aufgabe 4 Tests ---")
    for values in test_cases:
        result_original = min_before(values)
        result_linear = min_before_linear(values)

        print(f"Input: {values}")
        print(f"min_before (original): {result_original}")
        print(f"min_before_linear (linear): {result_linear}")
        print(f"Results match   : {result_original == result_linear}\n")


# -------------
# Aufgabe 5
# -------------


# Welche der folgenden Buchstabenfolgen können mittels einer Sequenz von Stack-Operationen
# erzeugt werden in welcher die Buchstaben in aufsteigender Reihenfolge auf den Stack gelegt werden?

# A B C D E F

# 1: C B A D F E
# Möglich: ja
# Sequenz der Operationen oder Begründung warum nicht möglich:
# push(A)
# push(B)
# push(C)
# pop()
# pop()
# pop()
# push(D)
# pop()
# push(E)
# push(F)
# pop()
# pop()

# 2: C D F E A B
# Möglich: nein
# Sequenz der Operationen oder Begründung warum nicht möglich:
# push(A)
# push(B)
# push(C)
# pop()
# push(D)
# pop()
# push(E)
# push(F)
# pop()
# pop()
# nun kann nur noch B und nicht zuerst A ausgegeben werden

# 3: D C B E A F
# Möglich: ja
# Sequenz der Operationen oder Begründung warum nicht möglich:
# push(A), push(B), push(C), push(D), pop(), pop(), pop(), push(E), pop(), pop(), push(F), pop()

# b)
# Welche der folgenden Sequenzen können durch die in der Angabe
# beschriebenen Deque-Operationen aus einer Deque mit dem Inhalt
#  a b c d e f
# erzeugt werden?

# 1: a f e c b d
# Möglich: nein
# Sequenz der Operationen oder Begründung warum nicht möglich:
# delete_first(), delete_last(), delete_last(), nun b,c,d -> c nicht als nächstes möglich

# 2: f e a d c b
# Möglich: ja
# Sequenz der Operationen oder Begründung warum nicht möglich:
# delete_last(), delete_last(), delete_first(), delete_last(), delete_last(), delete_first(),


# -------------
# Aufgabe 6
# -------------


class QueueTODOs:

    def __init__(self):
        self.__queue = Deque()

    def __len__(self) -> int:
        return len(self.__queue)

    def add_todo(self, task: str) -> None:
        self.__queue.add_last(task)

    def do_todo(self) -> str | None:
        if not self.__queue.is_empty():
            return self.__queue.delete_first()
        else:
            return None

    def reduce_load(self, max_load: int) -> list[str]:
        dropped = []
        while len(self.__queue) > max_load:
            dropped.append(self.__queue.delete_last())
        return dropped


class StackTODOs:
    def __init__(self):
        self.__todos = Stack()

    def __len__(self) -> int:
        """Gibt die aktuelle Anzahl der Aufgaben im Stack zurück."""
        return len(self.__todos)

    def add_todo(self, task: str) -> None:
        """Fügt eine neue Aufgabe zum Stack hinzu (LIFO)."""
        self.__todos.push(task)

    def do_todo(self) -> str | None:
        """
        Bearbeitet die nächste Aufgabe vom Stack (LIFO).
        Gibt die Aufgabe zurück oder None, wenn der Stack leer ist.
        """
        if not self.__todos.is_empty():
            try:
                return self.__todos.pop()
            except Empty: # Sollte nicht passieren, da is_empty() geprüft wird, aber zur Sicherheit.
                return None
        else:
            return None

    def reduce_load(self, max_load: int) -> list[str]:
        """
        Reduziert die Anzahl der Aufgaben im Stack auf max_load,
        indem die zuletzt hinzugefügten Aufgaben entfernt werden (LIFO).
        Gibt eine Liste mit den entfernten Aufgaben zurück.
        """
        dropped = []
        while len(self.__todos) > max_load:
            try:
                dropped.append(self.__todos.pop())
            except Empty: # Sollte nicht passieren, da len() > max_load
                break # Wenn der Stack plötzlich leer ist, breche ab.
        return dropped



def exercise6():
    todos = StackTODOs()
    print(todos.do_todo())
    todos.add_todo('Aufgabe 1')
    todos.add_todo('Aufgabe 2')
    todos.add_todo('Aufgabe 3')
    todos.add_todo('Aufgabe 4')
    todos.add_todo('Aufgabe 5')
    print(len(todos))
    print(todos.reduce_load(3))
    print(len(todos))
    print(todos.do_todo())
    print(len(todos))
    print(todos.do_todo())
    print(todos.do_todo())
    print(todos.do_todo())
    print(len(todos))


# -------------
# Aufgabe 7
# -------------


class Employee:
    __LIFO_KEYWORD = 'lifo'  # Klassenvariable für 'LIFO' Stringvergleich (case-insensitive)
    __DEFAULT_EMPTY_NAME = 'John/Jane Doe'  # Standardname für leere Namen

    def __init__(self, name: str, management_level: int, organizes_work: str):
        self.__name = name
        self.__management_level = management_level

        # Initialisiere __todos basierend auf organizes_work
        if organizes_work.lower() == Employee.__LIFO_KEYWORD:
            self.__todos = StackTODOs()
        else:
            self.__todos = QueueTODOs()

    def get_name(self) -> str:
        """
        Gibt den Namen der Person zurück. Ist der Name leer, wird ein Default-Name zurückgegeben.
        """
        if self.__name:
            return self.__name
        else:
            return Employee.__DEFAULT_EMPTY_NAME

    def assign_task(self, task: str) -> None:
        """Fügt den übergebenen String als neue Aufgabe zur Sammlung der ToDos hinzu."""
        self.__todos.add_todo(task)

    def completes_task(self) -> None:
        """
        Erzeugt eine Ausgabe abhängig davon, ob die Person noch offene Aufgaben hat, oder nicht.
        """
        task = self.__todos.do_todo()
        if task is None:
            print(f"{self.get_name()} hat gerade leider nichts zu tun - kein Fortschritt.")
        else:
            print(f"{self.get_name()} hat folgende Tätigkeit abgeschlossen: {task}")

    def workload(self, clearance: int) -> str:
        """
        Gibt eine Beschreibung des Workloads der Person zurück.
        Der Detailgrad hängt vom übergebenen Berechtigungslevel 'clearance' ab.
        """
        current_load = len(self.__todos)
        if clearance > self.__management_level:
            return f"{current_load} Aufgaben"
        else:
            if current_load < 2:
                return 'LOW'
            elif 2 <= current_load <= 3:
                return 'MEDIUM'
            else:  # current_load >= 4
                return 'HIGH'

    def peek_colleague(self, colleague) -> None:
        """
        Erzeugt eine Ausgabe zum Workload einer Kollegin, wie ihn die aufrufende Person sehen darf.
        """
        # Abruf der Workload des Kollegen mit dem Management-Level der aktuellen Person als Clearance
        colleague_workload_info = colleague.workload(self.__management_level)

        # Abruf des Namen des Kollegen über dessen get_name Methode
        colleague_name = colleague.get_name()

        # Abruf des Namen der aufrufenden Person (self) über deren get_name Methode
        my_name = self.get_name()

        print(f"[{my_name}]: Workload von {colleague_name} ist {colleague_workload_info}")


def exercise7():
    donna = Employee('Donna', 5, 'FIFO')
    michael = Employee('Michael', 10, 'LIFO')
    pepper = Employee('Pepper', 10, 'FIFO')
    dwight = Employee('Dwight', 2, 'LIFO')
    ryan = Employee('Ryan', 3, 'LIFO')
    bernd = Employee('Bernd', 5, 'LIFO')
    ulf = Employee('Ulf', 2, 'FIFO')
    doe = Employee('', 1, 'FIFO')

    print(donna.get_name())     # Donna
    print(doe.get_name())       # John/Jane Doe

    michael.assign_task('Rechnung erstellen')
    michael.assign_task('Kunden kontaktieren')
    ulf.assign_task('Kaffee kochen')
    ulf.assign_task('Kekse kaufen')
    donna.assign_task('Meeting vorbereiten')
    donna.assign_task('Tagesordnung erstellen')
    pepper.assign_task('Dampf machen')
    ulf.assign_task('Briefmarken kaufen')
    ryan.assign_task('Antrag durchlesen')
    ryan.assign_task('Antrag ablehnen')
    ulf.assign_task('Meetingraum putzen')
    ryan.assign_task('Schreibtisch aufräumen')
    pepper.assign_task('Streit schlichten')
    donna.assign_task('Anrufbeantworter einschalten')
    ulf.assign_task('Fenster öffnen')

    print('Donna Workload(5):', donna.workload(5))      # Donna Workload(5): MEDIUM
    print('Donna Workload (6):', donna.workload(6))     # Donna Workload (6): 3 Aufgaben
    print('Ryan Workload (5):', ryan.workload(5))       # Ryan Workload (5): 3 Aufgaben
    print('Bernd Workload (5):', bernd.workload(5))     # Bernd Workload (5): LOW
    print('Dwight Workload (11):', dwight.workload(11)) # Dwight Workload (11): 0 Aufgaben
    print('Dwight Workload (0):', dwight.workload(0))   # Dwight Workload (0): LOW

    pepper.peek_colleague(ulf)          # [Pepper]: Workload von Ulf ist 5 Aufgaben
    pepper.peek_colleague(michael)      # [Pepper]: Workload von Michael ist MEDIUM
    doe.peek_colleague(ulf)             # []: Workload von Ulf ist HIGH
    ulf.peek_colleague(dwight)          # [Ulf]: Workload von Dwight ist LOW
    pepper.peek_colleague(dwight)       # [Pepper]: Workload von Dwight ist 0 Aufgaben

    donna.completes_task()  # Donna hat folgende Tätigkeit abgeschlossen: Meeting vorbereiten
    donna.completes_task()  # Donna hat folgende Tätigkeit abgeschlossen: Tagesordnung erstellen
    donna.completes_task()  # Donna hat folgende Tätigkeit abgeschlossen: Anrufbeantworter einschalten
    donna.completes_task()  # Donna hat gerade leider nichts zu tun - kein Fortschritt.

    ryan.completes_task()   # Ryan hat folgende Tätigkeit abgeschlossen: Schreibtisch aufräumen
    ryan.completes_task()   # Ryan hat folgende Tätigkeit abgeschlossen: Antrag ablehnen
    ryan.completes_task()   # Ryan hat folgende Tätigkeit abgeschlossen: Antrag durchlesen
    ryan.completes_task()   # Ryan hat gerade leider nichts zu tun - kein Fortschritt.
    ryan.completes_task()   # Ryan hat gerade leider nichts zu tun - kein Fortschritt.

    pepper.peek_colleague(ryan) # [Pepper]: Workload von Ryan ist 0 Aufgaben
    pepper.peek_colleague(ulf)  # [Pepper]: Workload von Ulf ist 5 Aufgaben
    dwight.peek_colleague(ulf)  # [Dwight]: Workload von Ulf ist HIGH
    ulf.completes_task()        # Ulf hat folgende Tätigkeit abgeschlossen: Kaffee kochen
    ulf.completes_task()        # Ulf hat folgende Tätigkeit abgeschlossen: Kekse kaufen
    dwight.peek_colleague(ulf)  # [Dwight]: Workload von Ulf ist MEDIUM
    doe.peek_colleague(pepper)  # []: Workload von Pepper ist MEDIUM


def the_office():
    # Neue Mitarbeiter und deren Arbeitsweise
    pam = Employee('Pam', 3, 'FIFO')
    jim = Employee('Jim', 4, 'LIFO')
    angela = Employee('Angela', 5, 'LIFO')
    creed = Employee('Creed', 1, 'FIFO')

    print(f"Neue Mitarbeiter: {pam.get_name()}, {jim.get_name()}, {angela.get_name()}, {creed.get_name()}")

    # Aufgaben zuweisen
    pam.assign_task('Kundenanruf beantworten')
    pam.assign_task('E-Mails sortieren')
    pam.assign_task('Termine koordinieren')
    pam.assign_task('Beschwerde bearbeiten')

    jim.assign_task('Präsentation vorbereiten')
    jim.assign_task('Bericht schreiben')
    jim.assign_task('Neue Software testen')

    angela.assign_task('Budget prüfen')
    angela.assign_task('Mitarbeitergespräche führen')
    angela.assign_task('Strategie planen')
    angela.assign_task('Jahresbericht abschließen')
    angela.assign_task('Bonusverteilung genehmigen')

    creed.assign_task('Pflanzen gießen')

    print(f"{pam.get_name()} Workload(3): {pam.workload(3)}")
    print(f"{jim.get_name()} Workload(5): {jim.workload(5)}")
    print(f"{angela.get_name()} Workload(5): {angela.workload(5)}")
    print(f"{creed.get_name()} Workload(0): {creed.workload(0)}")

    jim.peek_colleague(pam)
    angela.peek_colleague(jim)
    pam.peek_colleague(creed)

    pam.completes_task()
    jim.completes_task()
    angela.completes_task()
    creed.completes_task()

    print(f"\n{pam.get_name()} Workload(3): {pam.workload(3)}")
    print(f"{jim.get_name()} Workload(5): {jim.workload(5)}")
    print(f"{angela.get_name()} Workload(5): {angela.workload(5)}")
    print(f"{creed.get_name()} Workload(0): {creed.workload(0)}")

    pam.completes_task()
    pam.completes_task()
    angela.completes_task()
    angela.completes_task()
    angela.completes_task()

    print(f"{pam.get_name()} Workload(3): {pam.workload(3)}")
    print(f"{jim.get_name()} Workload(5): {jim.workload(5)}")


if __name__ == "__main__":
    # exercise1()
    # exercise2()
    # exercise3()
    # exercise4()
    # exercise6()
    # exercise7()
    # the_office()
