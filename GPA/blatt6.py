# -*- coding: utf-8 -*-
# GPA 2025

import datetime


# -------------
# Aufgabe 1
# -------------


def things_in_space():
    space_probes = {
        "Voyager 1": {
            "mission": {"launch": 1977},
            "visited": ['Jupiter', 'Io', 'Europa', 'Ganymede', 'Callisto', 'Titan', 'Tethys', 'Saturn', 'Mimas',
                        'Enceladus', 'Rhea', 'Hyperion'],
            "launch_mass": 815,
            "launch_site": "Cape Canaveral",
            "launch_rocket": "Titan IIIE",
            "operator": 'NASA'

        },
        "Voyager 2": {
            "mission": {"launch": 1977},
            "visited": ['Callisto', 'Ganymede', 'Europa', 'Amalkthea', 'Jupiter', 'Io',
                        'Iapetus', 'Hyperion', 'Titan', 'Helene', 'Dione', 'Calypso', 'Mimas', 'Pandora', 'Saturn',
                        'Atlas', 'Enceladus', 'Janus', 'Epimetheus', 'Telesto', 'Tethys', 'Rhea', 'Phobe',
                        'Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Uranus',
                        'Neptun', 'Galtea', 'Larissa', 'Proteus', 'Triton'],
            "launch_mass": 721.9,
            "launch_site": "Cape Canaveral",
            "launch_rocket": "Titan IIIE",
            "operator": 'NASA'
        },
        "Galileo": {
            "mission": {"launch": 1989, "end": 2003},
            "visited": [],
            "destination": 'Jupiter',
            "launch_mass": 721.9,
            "launch_site": "Kennedy Space Center",
            "launch_rocket": "Space Shuttle",
            "operator": 'NASA'
        },
        "Rosetta": {
            "mission": {"launch": 2004, "end": 2016},
            "destination": 'Komet 67P',  # Korrekt aber zu lange: 'Komet 67P/Tschurjumow-Gerassimenko'
            "operator": 'ESA',
            "launch_mass": 3000,
            "launch_site": "Centra Spatial Guyanais",
            "launch_rocket": "Ariane 5",
        },
        "Mars Climate Orbiter": {
            "mission": {"launch": 1998, "failed": 1999},
            "destination": 'Mars',
            "operator": 'NASA',
            "launch_mass": 638,
            "launch_site": "Cape Canaveral",
            "launch_rocket": "Delta II",
        },
        "Danuri": {
            "mission": {"launch": 2022},
            "destination": 'Mond',
            "operator": 'KARI',
            "launch_mass": 678,
            "launch_site": "Cape Canaveral",
            "launch_rocket": "Falcon 9",
        },
        "Beresheet": {
            "mission": {"launch": 2019, "failed": 2019},
            "destination": 'Mond',
            "operator": 'AIA',
            "launch_mass": 585,
            "launch_site": "Cape Canaveral",
            "launch_rocket": "Falcon 9",
        },
        "Chandrayaan-2": {
            "mission": {"launch": 2019},
            "destination": 'Mond',
            "operator": 'ISRO',
            "launch_mass": 3850,
            "launch_site": "Satish Dhawan Space Centre",
            "launch_rocket": "GSLV Mk III",
        },
        "Chang’e 5": {
            "mission": {"launch": 2020, "end": 2021},
            "destination": 'Mond',
            "operator": 'CNSA',
            "launch_mass": 8250,
            "launch_site": "Kosmodrom Wenchang",
            "launch_rocket": "Langer Marsch 5",
        },
        "Akatsuki": {
            "mission": {"launch": 2010, "end": 2024},
            "destination": 'Venus',
            "operator": 'JAXA',
            "launch_mass": 480,
            "launch_site": "Tanegashima Space Center",
            "launch_rocket": "H-2",
        },
        "Stardust": {
            "mission": {"launch": 1999, "end": 2011},
            "destination": 'Wild 2',
            "visited": ['5535 Annefrank', 'Wild 2', 'Erde', 'Tempel 1'],
            "operator": 'NASA',
            "launch_mass": 385,
            "launch_site": "Cape Canaveral",
            "launch_rocket": "Delta II",
        },
        "Cassini": {
            "mission": {"launch": 1997, "end": 2017},
            "destination": 'Saturn',
            "visited": ['Venus', '(2685) Masursky', 'Jupiter', 'Phoebe', 'Titan',
                        'Enceladus', 'Daphnis', 'Hyperion', 'Tethys'],
            "operator": 'NASA',
            "launch_mass": 2523,
            "launch_site": "Cape Canaveral",
            "launch_rocket": "Titan IV",
        },
        "JUICE": {
            "mission": {"launch": 2023},
            "destination": 'Jupiter',
            "operator": 'ESA',
            "launch_mass": 6070,
            "launch_site": "Centra Spatial Guyanais",
            "launch_rocket": "Ariane 5",
        }
    }

    # Die Masse (beim Start) der schwersten Sonde:
    # Erwartete Ausgabe:
    # 8250
    highest_mass = 0
    for probe_details in space_probes.values():
        mass = probe_details['launch_mass']
        if mass > highest_mass:
            highest_mass = mass
            # print(f"found new max: {highest_mass}")

    print(highest_mass)

    print()

    # Eine Menge set() mit allen Zielen von Sonden in Variable destinations speichern und ausgeben
    # Erwartete Ausgabe (Reihenfolge unbestimmt)
    # {'Venus', 'Komet 67P', 'Saturn', 'Mond', 'Wild 2', 'Mars', 'Jupiter'}
    destinations = set()
    for val in space_probes.values():
        # print(val)
        if "destination" in val.keys():
            # print(val["destination"])
            if val["destination"] not in destinations:
                destinations.add(val["destination"])
    print(destinations)

    print()

    # Für jede Sonde, die ihre Mission erfolgreich abgeschlossen hat eine Zeile mit
    # Name: Missionsdauer
    # Die Zeilen sind aufsteigend sortiert nach den Namen der Sonden
    # Erwartete Ausgabe:
    # Akatsuki: 14
    # Cassini: 20
    # Chang’e 5: 1
    # Galileo: 14
    # Rosetta: 12
    # Stardust: 12
    for key,val in space_probes.items():
        # print(key,val)
        if "end" in val['mission']:
            print(f"{key}: {val['mission']['end'] - val['mission']['launch']}")


    print()

    # Neues Dictionary mit Planetennamen als Schlüssel.
    # Jedem Planeten, der Ziel einer Sonde ist, wird ein Dictionary zugeordnet.
    # Dieses enthält einen Eintrag für jede Sonde, deren Ziel der Planet ist.
    # Der Schlüssel dieses Eintrags ist der Name der Sonde, und der zugeordnete
    # Wert ein Dictionary mit den Schlüsseln 'start', 'rocket' und 'agency',
    # welche die entsprechenden Werte der Sonde enthalten.
    # Erwartetes Ergebnis (Hinweis zur Ausgabe: zur besseren Lesbarkeit wurde die Ausgabe hier
    #  formatiert - die "normale" Ausgabe in einer einzigen Zeile ist ausreichend!)
    # {'Mars': {
    #           'Mars Climate Orbiter': {
    #               'start': 1998,
    #               'rocket': 'Delta II',
    #               'agency': 'NASA'}},
    #  'Venus': {
    #           'Akatsuki': {
    #               'start': 2010,
    #               'rocket': 'H-2',
    #               'agency': 'JAXA'}},
    #  'Jupiter': {
    #           'Galileo': {
    #               'start': 1989,
    #               'rocket': 'Space Shuttle',
    #               'agency': 'NASA'},
    #          'JUICE': {
    #               'start': 2023,
    #               'rocket': 'Ariane 5',
    #               'agency': 'ESA'}}
    # }
    planets = {'Merkur', 'Venus', 'Erde', 'Mars', 'Jupiter', 'Uranus', 'Neptun'}
    # TODO: Lösung hier
    destination_details = {}

    for probe_name, probe_data in space_probes.items():
        if "destination" in probe_data:
            current_planet = probe_data["destination"]
            if current_planet in planets:
                if current_planet not in destination_details:
                    destination_details[current_planet] = {}

                start = probe_data['mission']['launch']
                rocket = probe_data['launch_rocket']
                agency = probe_data['operator']

                # Erstelle das innere Dictionary für die Sonde und weise es zu
                destination_details[current_planet][probe_name] = {
                    'start': start,
                    'rocket': rocket,
                    'agency': agency
                }

    print(destination_details)


def exercise1():
    print('## Aufgabe 1\n')
    things_in_space()


# -------------
# Aufgabe 2
# -------------


def current_time() -> str:
    """
    returns the current date and time formatted as YYYY-MM-DD HH:MM:SS
    Can be used to create the logfiles

    :return:
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def parse_coffee_line(line: str) -> int:
    """
    reads from a log-line for coffee made the number of times the coffee
    was brewed

    :param line: a line from the logfile for a "coffee-made" event
    :return: number of infusions for this coffee
    """
    return int(line[line.index('(') + 1:line.index(')')])


def log_maintenance_task(task: str) -> str:
    timestamp = current_time()
    log_entry = f"[{timestamp}]: {task}\n"

    try:
        with open('blatt6_Beispieldateien/maintenance.log', 'a', encoding='utf-8') as file:
            file.write(log_entry)
    except Exception as e:
        print(f"Fehler beim Schreiben in maintenance.log: {e}")

    return current_time()


def read_log() -> dict:
    log_data = {
        'water refill': 'noch nie',
        'beans refill': 'noch nie',
        'last decalc': 'noch nie',
        'coffees made': 0,
        'water': -1,
        'beans': -1,
        'since decalc': -1
    }

    try:
        with open('blatt6_Beispieldateien/maintenance_2.log', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                return log_data

    except Exception as e:
        print(f"Fehler beim Lesen von maintenance.log oder Datei nicht vorhanden: {e}")
        log_data['water refill'] = 'read error'
        log_data['beans refill'] = 'read error'
        log_data['last decalc'] = 'read error'
        return log_data

    for line in lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue

        timestamp_in_line = cleaned_line[1:20]

        if 'beans refill' in cleaned_line:
            log_data['beans refill'] = timestamp_in_line
        if 'water refill' in cleaned_line:
            log_data['water refill'] = timestamp_in_line
        if 'decalcify' in cleaned_line:
            log_data['last decalc'] = timestamp_in_line
        if 'coffee made' in cleaned_line:
            try:
                log_data['coffees made'] += parse_coffee_line(cleaned_line)
            except ValueError:
                print(f"Warnung: Konnte 'coffee made' Zeile nicht parsen: {cleaned_line}")

    last_valid_line = ""
    for i in range(len(lines) - 1, -1, -1):
        line_content = lines[i].strip()
        if line_content:
            last_valid_line = line_content
            break

    if 'switched off (' in last_valid_line and last_valid_line.endswith(')'):
        start_index = last_valid_line.find('switched off (') + len('switched off (')
        details_part = last_valid_line[start_index:-1]

        parts = details_part.split('; ')
        try:
            log_data['water'] = int(parts[0].split(': ')[1])
            log_data['beans'] = int(parts[1].split(': ')[1])
            log_data['since decalc'] = int(parts[2].split(': ')[1])
        except (IndexError, ValueError) as parse_error:
            print(
                f"Warnung: Konnte 'switched off' Zeile nicht vollständig parsen: {last_valid_line} - {parse_error}")
            log_data['water'] = -1
            log_data['beans'] = -1
            log_data['since decalc'] = -1
            print("Kaffeemaschine wurde nicht korrekt abgeschalten (oder Log-Formatproblem).")

        else:
            print("Kaffeemaschine wurde nicht korrekt abgeschalten (Formatfehler in Log).")

    elif lines:
        print("Kaffeemaschine wurde nicht korrekt abgeschalten.")

    return log_data







class CoffeeMachine:

    def __init__(self):
        self.beans = 30
        self.water = 200
        self.since_decalc = 0
        self.last_antical, self.last_beans, self.last_water = 'NULL', 'NULL', 'NULL'
        self.coffees_made = - 1

    def print_main_menu(self, started):
        print(f'## Hallo, hier das Neueste von deiner Kaffeemaschine (ohne Pause seit {started})')
        print('=== Status: ')
        print(f'    Bohnen: {self.beans / 1000} kg')
        print(f'    Wasser: {self.water / 1000} l')
        if self.since_decalc >= 3:
            print(f'    HINWEIS! Maschine sollte entkalkt werden!')
        print()
        print('=== (Hauptmenü) Deine Möglichkeiten:')
        print(f'[kaffee] Kaffee machen (already {self.coffees_made} made)')
        print(f'[bohnen] Kaffeebohnen nachfüllen (last refill: {self.last_beans})')
        print(f'[wasser] Wasser nachfüllen (last refill: {self.last_water})')
        print(f'[entkalken] Maschine entkalken (last: {self.last_antical})')
        print('[quit] Maschine ausschalten')

    def perform_action(self, choice):
        if choice.lower() == 'wasser':
            self.refill_water()
        elif choice.lower() == 'bohnen':
            self.refill_beans()
        elif choice.lower() == 'kaffee':
            self.make_coffee()
        elif choice.lower() == 'entkalken':
            self.decalc()
        elif choice.lower() == 'quit':
            print('Dankeschön und auf Wiedersehen!')
        else:
            print('.. Sorry, das sagt mir jetzt nichts.')

    def refill_water(self):
        added = int(input('Wie viele ml Wasser füllst du nach? '))
        added = min(added, 1000 - self.water)
        self.water = self.water + added
        self.last_water = log_maintenance_task(f'water refill ({added}ml)')

    def refill_beans(self):
        added = int(input('Wie viel g Bohnen füllst du nach? '))
        added = min(added, 450 - self.beans)
        self.beans = self.beans + added
        self.last_beans = log_maintenance_task(f'beans refill ({added}g)')

    def decalc(self):
        print('-- Entkalkungsvorgang läuft ... abgeschlossen.')
        self.since_decalc = 0
        self.last_antical = log_maintenance_task('decalcify')

    def make_coffee(self):
        strength = int(input('Bitte die Stärke wählen: 1) schwach [15g], 2) mittel [30g], 3) stark [45g]')) * 15
        if self.beans < strength:
            print('Nicht genug Bohnen! Abbruch! Abbruch!!')
        else:
            self.beans -= strength
            print('Mahle Bohnen: Bruiiiiii, grrrrrrrr, chk')
            size = int(
                input('Bitte die Kaffeegröße wählen: 1) klein [75ml], 2) mittel [150ml], 3) groß [225ml]'))
            made = 0
            for i in range(size):
                if self.water > 75:
                    print('Brühe ...', end=' ')
                    self.water -= 75
                    made += 1
                else:
                    print('Leider nicht genug Wasser für den nächsten Brühvorgang.')
                    break
            log_maintenance_task(f'coffee made ({made})[water: {made * 75}; beans: {strength}]')
            self.coffees_made += made
            print('Kaffee ist fertig - bitte entnehmen.')
            self.since_decalc += 1

    def switch_on(self) -> str:
        print('Genussvoller Profi Aufguss starting ... done')
        infos = read_log()
        self.last_antical = infos['last decalc']
        self.last_beans = infos['beans refill']
        self.last_water = infos['water refill']
        self.coffees_made = infos['coffees made']
        self.water = infos['water'] if infos['water'] >= 0 else 200
        self.beans = infos['beans'] if infos['beans'] >= 0 else 30
        self.since_decalc = infos["since decalc"] if infos['since decalc'] > 0 else 0
        return log_maintenance_task('switched on')

    def switch_off(self):
        current = log_maintenance_task(
            f'switched off (water: {self.water};beans: {self.beans};decalc: {self.since_decalc})')
        print(f'Schalte ab, Zeit: {current}')

    def run(self):
        started = self.switch_on()
        choice = ''
        while choice.lower() != 'quit':
            self.print_main_menu(started)
            choice = input('Deine Auswahl: ')
            self.perform_action(choice)
        self.switch_off()


def coffee_machine():
    """
    can be used to run the coffee machine (interactively)
    :return:
    """
    machine = CoffeeMachine()
    machine.run()


def exercise2():

    # test log_maintenance_task:
    print(log_maintenance_task('Test1'))

    print(log_maintenance_task('Test2'))
    print(log_maintenance_task('decalcify'))
    print(log_maintenance_task('beans refill (500g)'))
    print(log_maintenance_task('coffee made (2)[water: 150; beans: 30]'))
    print(log_maintenance_task('switched off (water: 50;beans: 450;decalc: 1)'))

    # test read_log
    print(read_log())

    # obiger Aufruf besitzt unterschiedliche Rückgaben abhängig vom Inhalt von maintenance.log:
    # ohne dass maintenance.log existiert:
    # {'water refill': 'read error', 'beans refill': 'read error', 'last decalc': 'read error',
    #  'coffees made': -1, 'water': -1, 'beans': -1, 'since decalc': -1}

    # mit maintenance.log als maintenance.log:
    # {'water refill': '2025-04-16 15:15:43', 'beans refill': '2025-04-16 15:15:58',
    #  'last decalc': '2025-04-16 15:16:00', 'coffees made': 18, 'water': 764,
    #  'beans': 70, 'since decalc': 0}

    # mit maintenance_2.log als maintenance.log:
    # {'water refill': '2025-04-01 12:00:21', 'beans refill': 'noch nie',
    #  'last decalc': 'noch nie', 'coffees made': 4, 'water': -1,
    #  'beans': -1, 'since decalc': -1}

    # mit maintenance_3.log als maintenance.log:
    # {'water refill': 'noch nie', 'beans refill': 'GPA!!GPA!!GPA!!GPA!',
    #  'last decalc': 'noch nie', 'coffees made': 0, 'water': 120,
    #  'beans': 1200, 'since decalc': 17}

    # mit maintenance_4.log als maintenance.log:
    # {'water refill': 'noch nie', 'beans refill': 'noch nie',
    #  'last decalc': 'noch nie', 'coffees made': 0, 'water': -1,
    #  'beans': -1, 'since decalc': -1}


# -------------
# Aufgabe 3
# -------------


class Restaurant:
    def __init__(self, name: str, menu_price: int, daily_portions: int):
        self.name = name
        self.menu_price = menu_price
        self.daily_portions = daily_portions
        self.available_portions = daily_portions
        self.cuisines = set()

    def reset_menus(self) -> None:
        self.available_portions = self.daily_portions

    def food_left(self) -> bool:
        return self.available_portions >= 1

    def add_cuisine(self, cuisine: str) -> None:
        self.cuisines.add(cuisine)

    def adjust_price(self, change: int) -> bool:
        if (self.menu_price + change) > 0:
            self.menu_price += change
            return True
        return False

    def offers(self, cuisine: str) -> bool:
        return cuisine in self.cuisines

    def sell_menus(self, amount: int) -> int:
        if amount < 0:
            return 0

        if self.available_portions >= amount:
            sold_amount = amount
        else:
            sold_amount = self.available_portions

        self.available_portions -= sold_amount
        return sold_amount

    def print_status(self) -> None:
        print(f"** {self.name} **")
        if self.food_left():
            print(f" Menüs übrig: {self.available_portions}")
            print(f" Preis: {self.menu_price}")
            if self.cuisines:
                sorted_cuisines = sorted(list(self.cuisines))
                print(f" Wir bieten: {', '.join(sorted_cuisines)}")
            else:
                print(" Wir bieten: (noch keine Küchen spezifiziert)")
        else:
            print(" * HEUTE LEIDER SCHON AUSVERKAUFT! *")



class Foodie:
    def __init__(self, name: str, budget: int, default_amount: int):
        self.name = name
        self.budget = budget
        self.default_amount = default_amount
        self.watchlist = set()

    def watch_restaurant(self, restaurant: Restaurant) -> None:
        self.watchlist.add(restaurant)

    def increase_budget(self) -> None:
        self.budget += 2

    def buy_menus(self, restaurant: Restaurant, amount: int = -1) -> bool:
        if amount < -1:
            return False

        portions_to_buy = 0
        if amount == -1:
            portions_to_buy = self.default_amount
        else:
            portions_to_buy = amount

        if portions_to_buy <= 0:
            return True

        sold_portions = restaurant.sell_menus(portions_to_buy)
        return sold_portions == portions_to_buy

    def list_options(self, cuisine: str = None) -> None:
        print(f"Hallo {self.name}!")
        print("Das sind deine Optionen:")

        options_found = False
        sorted_watchlist_restaurants = sorted(list(self.watchlist), key=lambda r: r.name)

        for r in sorted_watchlist_restaurants:
            if cuisine is None or r.offers(cuisine):
                options_found = True
                print(f"== {r.name}:", end="")
                if r.menu_price > self.budget:
                    print(" **ZU TEUER**")
                else:
                    print()

                if r.food_left():
                    print(f" ** {r.available_portions} Menüs um {r.menu_price} Euro verfügbar.")
                else:
                    print(" ** AUSVERKAUFT **")
                print()

        if not options_found and cuisine is not None:
            print(f"Leider keine Restaurants auf deiner Watchlist, die '{cuisine}' anbieten.")
        elif not options_found and not self.watchlist:
            print("Deine Watchlist ist noch leer.")


def exercise3() -> None:
    print('\n\n## Aufgabe 3:')
    gpa = Restaurant('Grob Püriertes Aufgetautes', 5, 6)
    gpa.print_status()

    print(gpa.offers('Italienisch'))
    gpa.add_cuisine('Chinesisch')
    gpa.add_cuisine('Libanesisch')
    print(gpa.offers('Italienisch'))
    print(gpa.offers('Chinesisch'))
    print(gpa.sell_menus(2))
    gpa.print_status()

    print(gpa.adjust_price(-6))
    print(gpa.adjust_price(1))
    gpa.print_status()

    print(gpa.food_left())
    print(gpa.sell_menus(5))
    print(gpa.food_left())
    gpa.reset_menus()
    gpa.print_status()

    print('\n\n===== FOODIE:')
    obelix = Foodie('Obelix', 5, 3)
    obelix.list_options()

    obelix.watch_restaurant(gpa)
    obelix.watch_restaurant(gpa)
    obelix.list_options()

    print(obelix.buy_menus(gpa, 1))
    print(obelix.buy_menus(gpa))
    print(obelix.buy_menus(gpa))
    obelix.list_options()

    obelix.increase_budget()
    obelix.list_options()

    gpa.reset_menus()
    wurst = Restaurant('Mizitants Würstelstand', 2, 12)
    obelix.watch_restaurant(wurst)
    wurst.add_cuisine('Wurst')
    obelix.list_options('Libanesisch')
    obelix.list_options('Wurst')


def lunch_scenario():
    print('\n##OFFICE LUNCH:\n')
    rest = Restaurant('R - das Restaurant', 4, 4)
    rest.add_cuisine('Thai')
    rest.add_cuisine('Wiener Küche')
    rest.add_cuisine('Burger')
    pizza = Restaurant('Pizza, Pasta, Perfekt', 5, 7)
    pizza.add_cuisine('Italien')
    burgers = Restaurant('Burgers and Stuff', 6, 8)
    burgers.add_cuisine('Mexiko')
    burgers.add_cuisine('Burger')
    burgers.add_cuisine('US Style')
    fishnchips = Restaurant('England Finest', 7, 15)
    fishnchips.add_cuisine('English')
    fishnchips.add_cuisine('Indian')
    fishnchips.add_cuisine('Pakistan')

    rest.print_status()
    # ** R - das Restaurant **
    #  Menüs übrig: 4
    #  Preis: 4
    #  Wir bieten: Thai, Burger, Wiener Küche
    pizza.print_status()
    # ** Pizza, Pasta, Perfekt **
    #  Menüs übrig: 7
    #  Preis: 5
    #  Wir bieten: Italien
    burgers.print_status()
    # ** Burgers and Stuff **
    #  Menüs übrig: 8
    #  Preis: 6
    #  Wir bieten: Burger, US Style, Mexiko
    fishnchips.print_status()
    # ** England Finest **
    #  Menüs übrig: 15
    #  Preis: 7
    #  Wir bieten: Indian, English, Pakistan

    print('1: ========================')

    ceo = Foodie('Mr. Manager', 25, 4)
    jan = Foodie('Janet (Accounting)', 7, 1)
    bob = Foodie('Bob', 5, 2)
    maria = Foodie('Maria (CFO)', 3, 3)
    mario = Foodie('Mario', 4, 1)

    ceo.watch_restaurant(rest)
    ceo.watch_restaurant(pizza)
    ceo.watch_restaurant(burgers)

    jan.watch_restaurant(fishnchips)
    jan.watch_restaurant(pizza)

    bob.watch_restaurant(pizza)
    bob.watch_restaurant(fishnchips)

    maria.watch_restaurant(rest)
    maria.watch_restaurant(burgers)
    maria.watch_restaurant(pizza)

    mario.watch_restaurant(pizza)

    maria.list_options()
    # Hallo Maria (CFO)!
    # Das sind deine Optionen:
    # == Pizza, Pasta, Perfekt: **ZU TEUER**
    # ** 7 Menüs um 5 Euro verfügbar.
    #
    # == R - das Restaurant: **ZU TEUER**
    # ** 4 Menüs um 4 Euro verfügbar.
    #
    # == Burgers and Stuff: **ZU TEUER**
    # ** 8 Menüs um 6 Euro verfügbar.

    ceo.list_options()
    # Hallo Mr. Manager!
    # Das sind deine Optionen:
    # == Pizza, Pasta, Perfekt:
    # ** 7 Menüs um 5 Euro verfügbar.
    #
    # == R - das Restaurant:
    # ** 4 Menüs um 4 Euro verfügbar.
    #
    # == Burgers and Stuff:
    # ** 8 Menüs um 6 Euro verfügbar.

    print(ceo.buy_menus(rest))              # True
    print(ceo.buy_menus(burgers, 1)) # True
    maria.list_options()
    # Hallo Maria (CFO)!
    # Das sind deine Optionen:
    # == Pizza, Pasta, Perfekt: **ZU TEUER**
    # ** 7 Menüs um 5 Euro verfügbar.
    #
    # == R - das Restaurant: **ZU TEUER**
    #  ** AUSVERKAUFT **
    #
    # == Burgers and Stuff: **ZU TEUER**
    # ** 7 Menüs um 6 Euro verfügbar.

    print('2: ========================')
    jan.list_options()
    # Hallo Janet (Accounting)!
    # Das sind deine Optionen:
    # == Pizza, Pasta, Perfekt:
    # ** 7 Menüs um 5 Euro verfügbar.
    #
    # == England Finest:
    # ** 15 Menüs um 7 Euro verfügbar.

    print(mario.buy_menus(pizza, 3))  # True
    print(maria.buy_menus(pizza, 6))  # False
    print(burgers.sell_menus(4))              # 4

    burgers.print_status()
    # ** Burgers and Stuff **
    #  Menüs übrig: 3
    #  Preis: 6
    #  Wir bieten: Burger, US Style, Mexiko
    pizza.print_status()
    # ** Pizza, Pasta, Perfekt **
    #  * HEUTE LEIDER SCHON AUSVERKAUFT! *

    print('3: ========================')
    print(pizza.food_left())        # False
    pizza.reset_menus()
    print(bob.buy_menus(pizza))     # True
    pizza.print_status()
    # ** Pizza, Pasta, Perfekt **
    #  Menüs übrig: 5
    #  Preis: 5
    #  Wir bieten: Italien

    print(fishnchips.offers('Seafood')) # False
    fishnchips.add_cuisine('Seafood')
    fishnchips.adjust_price(3)
    print(fishnchips.offers('Seafood'))
    jan.list_options()
    # Hallo Janet (Accounting)!
    # Das sind deine Optionen:
    # == Pizza, Pasta, Perfekt:
    # ** 5 Menüs um 5 Euro verfügbar.
    #
    # == England Finest: **ZU TEUER**
    # ** 15 Menüs um 10 Euro verfügbar.
    jan.increase_budget()
    jan.list_options()
    # Hallo Janet (Accounting)!
    # Das sind deine Optionen:
    # == Pizza, Pasta, Perfekt:
    # ** 5 Menüs um 5 Euro verfügbar.
    #
    # == England Finest: **ZU TEUER**
    # ** 15 Menüs um 10 Euro verfügbar.

    print('4: ========================')
    ceo.watch_restaurant(fishnchips)
    ceo.list_options()
    # Hallo Mr. Manager!
    # Das sind deine Optionen:
    # == Burgers and Stuff:
    # ** 3 Menüs um 6 Euro verfügbar.
    #
    # == R - das Restaurant:
    #  ** AUSVERKAUFT **
    #
    # == Pizza, Pasta, Perfekt:
    # ** 5 Menüs um 5 Euro verfügbar.
    #
    # == England Finest:
    # ** 15 Menüs um 10 Euro verfügbar.
    print(fishnchips.sell_menus(7))     # 7
    jan.increase_budget()
    jan.list_options()
    # Hallo Janet (Accounting)!
    # Das sind deine Optionen:
    # == Pizza, Pasta, Perfekt:
    # ** 5 Menüs um 5 Euro verfügbar.
    #
    # == England Finest:
    # ** 8 Menüs um 10 Euro verfügbar.

    print(fishnchips.sell_menus(9))     # 8
    print(fishnchips.food_left())
    mario.list_options()
    #

    print('5: ========================')
    print(pizza.sell_menus(3))      # 3
    ceo.list_options('Burger')
    # Hallo Mr. Manager!
    # Das sind deine Optionen:
    # == R - das Restaurant:
    #  ** AUSVERKAUFT **
    #
    # == Burgers and Stuff:
    # ** 3 Menüs um 6 Euro verfügbar.
    maria.list_options('Seafood')
    # Hallo Maria (CFO)!
    # Das sind deine Optionen:
    jan.list_options('Italien')
    # Hallo Janet (Accounting)!
    # Das sind deine Optionen:
    # == Pizza, Pasta, Perfekt:
    # ** 2 Menüs um 5 Euro verfügbar.


# -------------
# Aufgabe 4
# -------------

# -- Aufgabe 4.1

# Beispielfunktionen:

# Ist n in O(0.5*n)?
# Hinweis: hier gilt f(n) = n und g(n) = 0.5*n,  dass f(n) <= c * g(n)
# Antwort: Ja. Für c = 2 und n_0 = 0 gilt: Für alle n >= n0 gilt: n <= c * 0.5 * n (insbesondere n = n)

# Ist (n^3)/10 + n^2 - 7 in O(n)?
# Antwort: Nein. Für jede beliebige Konstante c lässt sich ein n1 finden, ab dem
#          (n^3)/10 + n^2 - 7 > c*n für alle n >= n1 gilt (was der Definition von "in O(n)"
#          genau widerspricht).
#          Genauer: für alle n welche (n^2)/10 + n - 7/n > c erfüllen; es ist offensichtlich
#                   dass (n^2)/10 + n - 7/n mit steigendem n wächst, während c konstant ist.

# // Ende Beispielfunktionen


# 1) 2^n - n^5 + 2 * n^3 - 2025          in O(n^6):
# Antwort: Nein
# Begründung: 2^n wächst deutlich schneller (exponentiell) als n^6 anwachsen kann (polynomial)
# Für jedes c>0 wird es ein n > n_0 geben für dass gilt 2^n - n^5 + 2 * n^3 - 2025 >= c * n^6


# 2) n^3 + 2^(10) * n                    in O(n^4)?
# Antwort: Ja
# Begründung: n^4 wird immer schneller als n^3 anwachsen, während der zweite term 2^(10) nur eine große Zahl auf
# ein n multipliziert wird. Somit wird ein c existieren, für welches gilt: c * n_0^4 >= n^3 + 2^(10) * n


# 3) n * log^2(n) + 20^4                 in O(n^3)?
# Antwort: Ja
# Begründung: n^3 hat ein polynomielles Wachstum und wird somit größer als n * log^2(n)


# 4) (n^2)/n + n^2 * n - 30 * n          in O(n^2)?
# Antwort: Nein
# Begründung: Das Wachstum von n^2 ist geringer als jenes von n^2 * n = n^3.


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

# // Ende Beispielfunktion


# 1) 5 * n * log(n+3) - 12 * n + 6
# # Kleinste asymptotische obere Schranke: O(n * log(n))
# Begründung: c=11 und n_0 = 5


# 2) 2^3 * n * n + 42 - 8 * n^2
# Kleinste asymptotische obere Schranke: O(1)
# Begründung: c=42, n_0 = 0 oder 1


# 3) 14 * n^3 + 10^5 * log_2(n) + 2 * n^2 * 2 * n^2
# Kleinste asymptotische obere Schranke: O(n^4)
# Begründung: c = 19 und n_0 = 32


if __name__ == '__main__':
    # exercise1()
    # exercise2()       # testcases for log_maintenance_task and read_log
    # coffee_machine()  # run the coffee machine
    # exercise3()       # smaller testcases for single methods
    # lunch_scenario()  # bigger scenario for Restaurants and Foodies
    pass
