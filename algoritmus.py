"""autor: Zuzana Bodri
Tento program slúži na filtrovanie chemických prvkov podľa zadaných pravidiel.
Program načíta zoznam chemických prvkov z JSON súboru, umožní užívateľovi zadať pravidlá a následne vytriedi zoznam podľa týchto pravidiel.
Pôvod zoznamu: https://jsonlint.com/datasets/elements"""
# importy: 
import json

# Úvodné funkcie:
def welcome():
    print ("Vitajte vo filtri chemických prvkov!")

# Načítanie JSONu s chemickými prvkami
def read_file(source):
    with open(source, encoding = "utf-8") as file:
        zoznam = json.load(file)
    return zoznam

# Pravidla pre triedenie:

    # Pravidlo 1:.

    # Výber skupenstva užívatelom
def rule_phase_choice():
    phase_conversion = {"s": "Solid", "l": "Liquid", "g": "Gas"}

    while True:
        print ("Teraz vložte skupenstvo prvku, pri normálnych podmienkach, ktoré sa použije pri triedení zoznamu: \n- pevné skupenstvo (s) \n- kvapalné skupenstvo (l) \n- plynné skupenstvo (g)")
        skupenstvo = input().lower().strip()
        if skupenstvo in phase_conversion:
            return phase_conversion[skupenstvo]
        else:
            print ("Neplatný vstup, zadejte prosím 's', 'l' nebo 'g'.")



    # Filter podľa skupenstva, porovnava hodnotu v zoznamu s hodnotou zadanou uživatelom
def rule_phase_match(item, phase_choice):
    return item.get("phase") == phase_choice


    # Pravidlo 2 a dalšie pravidlá zde, kdyby :)
    
#__________________________________________________________________________

# Cyklus cez zoznam, aplikácia pravidla pre jednotlivé itemy v slovníku a vytvorenie zoznamu fittujúcich hodnôt:
def algoritmus(zoznam, vybrane_pravidlo, kriterium):
   # POZNÁMKA: I keď zadanie znelo "...,který algoritmus projde a smaže hodnoty",
   # rozhodla som sa postavit funkciu  na vytvorení prázdneho zoznamu, kde sa uložia vyhovujúce položky původného zoznamu.
   # Tím som sa chcela vyhnúť mazaniu položiek zoznamu, cez ktorý prechádza cyklus.
   filtered_elements = []
   for item in zoznam["elements"]:
        if vybrane_pravidlo(item, kriterium) is True:
            filtered_elements.append(item)
   print (f"Zoznam prvkov, ktoré odpovídají zadanému pravidlu: {filtered_elements}")

#_________________________________________________________________________


welcome ()
zoznam = read_file ("elements.json")
phase_choice = rule_phase_choice()
algoritmus (zoznam, rule_phase_match, phase_choice)