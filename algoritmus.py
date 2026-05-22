"""autor: Zuzana Bodri
Tento program slúži na filtrovanie chemických prvkov podľa zadaných pravidiel.
Program načíta zoznam chemických prvkov z JSON súboru, umožní užívateľovi zadať pravidlá a následne vytriedi zoznam podľa týchto pravidiel."""

import json

def welcome():
    print ("Vitajte vo filtri chemických prvkov!")

def read_file(source):
    with open(source, encoding = "utf-8") as file:
        zoznam = json.load(file)
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
    print (f"Prvky, ktoré zodpovedajú pravidlám {pravidla} sú:\n {vytriedeny_zoznam}")


welcome ()
read_file ("elements.json")