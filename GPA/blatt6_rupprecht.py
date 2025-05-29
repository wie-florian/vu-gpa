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
    # TODO: Lösung hier
    highest_mass = 0
    for val in space_probes.values():
        if val["launch_mass"] > highest_mass:
            highest_mass = val["launch_mass"]
    print(highest_mass)

    print()

    # Eine Menge set() mit allen Zielen von Sonden in Variable destinations speichern und ausgeben
    # Erwartete Ausgabe (Reihenfolge unbestimmt)
    # {'Venus', 'Komet 67P', 'Saturn', 'Mond', 'Wild 2', 'Mars', 'Jupiter'}
    # TODO: Lösung hier
    destinations = set()
    for val in space_probes.values():
        if "destination" in val.keys():
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
    # TODO: Lösung hier
    for key,val in space_probes.items():
        if "end" in val["mission"].keys():
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
    for key,val in space_probes.items():
        if "destination" in val.keys():
            if val["destination"] in planets:
                if val["destination"] not in destination_details.keys():
                    destination_details[val["destination"]] = {}
                destination_details[val["destination"]][key] = {
                    "start" : val["mission"]["launch"],
                    "rocket" : val["launch_rocket"],
                    "agency" : val["operator"]
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
    # TODO: implementieren
    try:
        with open("blatt6_Beispieldateien/maintenance.log", "a") as f:
            f.write(f"[{current_time()}]: {task}\n")
            print("written")
            f.close()
    except Exception as e:
        print(f"Logging failed: {e}")
    
    return current_time()


def read_log() -> dict:
    # TODO: implementieren
    try:
        with open("blatt6_Beispieldateien/maintenance.log", "r") as f:
            content = list(f)
            f.close()
    except Exception as e:
        print(f"maintenance.log wasn't read correctly or missing: {e}")
        return {
            'water refill': 'read error',
            'beans refill': 'read error',
            'last decalc': 'read error',
            'coffees made': -1,
            'water': -1,
            'beans': -1,
            'since decalc': -1
        }
    op = {}
    op["coffees made"] = 0
    for i,line in enumerate(content):
        try:
            match line[23]:
                case "s":
                    pass
                case "c":
                    op["coffees made"] += parse_coffee_line(line)
                case "d":
                    op["last decalc"] = line[1:20]
                case "w":
                    op["water refill"] = line[1:20]
                case "b":
                    op["beans refill"] = line[1:20]
                case _:
                    raise Exception
        except Exception as e:
            print(f"Having trouble reading line {i}: {e}")
    if "switched off" in line:
        line_content = line[line.index('(') + 1:line.index(')')].split(";")
        op["water"] = int(line_content[0][7:])
        op["beans"] = int(line_content[1][7:])
        op["since decalc"] = int(line_content[2][8:])
    else:
        print("Coffee machine wasn't closed correctly")
        op["water"] = -1
        op["beans"] = -1
        op["since decalc"] = -1
    for key in {"water refill","beans refill","last decalc"}:
        if key not in op.keys():
            op[key] = "noch nie"
    return op


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
    
    def __init__(self, name, menu_price, daily_portions):
        self.name = name
        self.menu_price = menu_price
        self.daily_portions = daily_portions
        self.available_portions = daily_portions
        self.cuisines = set()
        
    def reset_menus(self):
        self.available_portions = self.daily_portions
        
    def food_left(self):
        return True if self.available_portions > 0 else False
    
    def add_cuisine(self,cuisine):
        self.cuisines.add(cuisine)
        
    def adjust_price(self,change):
        if self.menu_price + change > 0:
            self.menu_price += change
            return True
        else:
            return False
        
    def offers(self,cuisine):
        return True if cuisine in self.cuisines else False
    
    def sell_menus(self,amount):
        amount = self.available_portions if amount > self.available_portions else amount
        self.available_portions -= amount
        return amount
    
    def print_status(self):
        print(f"|----{self.name}----|\nWir bieten:")
        if self.available_portions > 0:
            for c in self.cuisines:
                print(f" - {c}")
            print(f"zu einem sagenhaften Preis von nur\n   {self.menu_price}€")
            print(f"Kommen Sie schnell - nur noch {self.available_portions} Portionen")
        else:
            print("Gut aber aus\nKommen Sie morgen wieder")


class Foodie:
    
    def __init__(self,name,budget,default_amount):
        self.name = name
        self.budget = budget
        self.default_amount = default_amount
        self.watchlist = set()
        
    def watch_restaurant(self,restaurant):
        self.watchlist.add(restaurant)
        
    def increase_budget(self):
        self.budget += 2
        
    def buy_menus(self,restaurant,amount=-1):
        if amount >= -1:
            amount = self.default_amount if amount == -1 else amount
            if amount > restaurant.available_portions:
                amount = restaurant.available_portions
                amount = self.budget // restaurant.menu_price if self.budget // restaurant.menu_price < amount else amount
                op = False
            else:
                if amount > self.budget // restaurant.menu_price:
                    amount = self.budget // restaurant.menu_price
                    op = False
                else:
                    op = True
            self.budget -= amount * restaurant.menu_price
            restaurant.sell_menus(amount)
            return op
        else:
            return False
        
    def list_options(self,cuisine=None):
        if len(self.watchlist) == 0:
            print("Ohne Restaurants auf der Watchlist wird eine Empfehlung schwer...")
            return
        print(f"Foodie {self.name}, du hast folgende Optionen:")
        counter = 0
        for restaurant in self.watchlist:
            if cuisine in restaurant.cuisines or cuisine == None:
                counter += 1
                print()
                restaurant.print_status()
                if restaurant.menu_price > self.budget:
                    print("**VIEL ZU TEUER**")
        if counter == 0:
            print()
            print(f"Keine Ergebnisse für '{cuisine}', solche fancy Restaurants gibt es hier nicht!")


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
# Antwort: nein
# Begründung: 2^n steigt stärker als n^6


# 2) n^3 + 2^(10) * n                    in O(n^4)?
# Antwort: ja
# Begründung: für c=1 und n0=0 gilt n^3+1024n <= n^4


# 3) n * log^2(n) + 20^4                 in O(n^3)?
# Antwort: ja
# Begründung: fpr c=2.5 und n0=40 gilt n*(log10(n))^2+20^4 <= c*n^3


# 4) (n^2)/n + n^2 * n - 30 * n          in O(n^2)?
# Antwort: nein
# Begründung: n^3 wächst immer schneller als n^2


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
# Kleinste asymptotische obere Schranke: O(n^2)
# Begründung: TODO


# 2) 2^3 * n * n + 42 - 8 * n^2
# Kleinste asymptotische obere Schranke: O(42.1)
# Begründung: TODO


# 3) 14 * n^3 + 10^5 * log_2(n) + 2 * n^2 * 2 * n^2
# Kleinste asymptotische obere Schranke: O(n^5)
# Begründung: TODO


if __name__ == '__main__':
    exercise1()
    exercise2()       # testcases for log_maintenance_task and read_log
    #coffee_machine()  # run the coffee machine
    exercise3()       # smaller testcases for single methods
    lunch_scenario()  # bigger scenario for Restaurants and Foodies
    pass
