def welcome():
    print ("Vitajte vo filtri chemických prvkov!")

def read_file():
    zoznam = []
    return zoznam

def define_rules():
    print ("Teraz vložte ale aspoň jedno pravidlo, ktoré sa použije pri triedení zoznamu: ")
    pravidla = input()
    return pravidla

def algoritmus(zoznam, pravidla):
    vytriedeny_zoznam = []
    for item in zoznam:
        if item in pravidla: #dodefinovat!
            vytriedeny_zoznam.append(item)
        else:
            pass
    return f"Vytriedený zoznam podľa pravidiel {pravidla} je: {vytriedeny_zoznam}"