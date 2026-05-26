"""autor: Zuzana Bodri
Tento program slúži na filtrovanie chemických prvkov podľa zadaných pravidiel.
Program načíta zoznam chemických prvkov z JSON súboru, umožní užívateľovi zadať pravidlá a následne vytriedi zoznam podľa týchto pravidiel.
Pôvod zoznamu: https://jsonlint.com/datasets/elements"""

import json

def welcome():
    print ("Vitajte vo filtri chemických prvkov!")

def read_file(source):
    with open(source, encoding = "utf-8") as file:
        zoznam = json.load(file)
    return zoznam

def define_rules():
    print ("Teraz vložte skupenstvo prvku, pri normálnych podmienkach, ktoré sa použije pri triedení zoznamu: \n- pevné skupenstvo (s) \n- kvapalné skupenstvo (l) \n- plynné skupenstvo (g)")
    pravidla = input().lower().strip()
    if pravidla in ["s", "l", "g"]:
        if pravidla == "s":
            return "Solid"
        elif pravidla == "l":
            return "Liquid"
        elif pravidla == "g":
            return "Gas"
    else:
        print("Neplatné skupenstvo. Prosím, zadajte jedno z uvedených.")
        return define_rules()


def algoritmus(zoznam, pravidla):
    vytriedeny_zoznam = []
    for item in zoznam["elements"]:
        if (item["phase"] == pravidla):
            vytriedeny_zoznam.append(item)
        else:
            pass
    print (f"Prvky, ktoré sú v skupenstve: {pravidla} :\n {vytriedeny_zoznam}")


welcome ()
zoznam = read_file ("elements.json")
pravidla = define_rules ()
algoritmus (zoznam, pravidla)