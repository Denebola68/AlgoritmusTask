print ("Vložte zoznam, jednotlivé prvky zoznamu musia byť oddelené čiarkou a medzerou: ")
zoznam = input()

print ("Teraz vložte ale aspoň jedno pravidlo, ktoré sa použije pri triedení zoznamu. Pravidlá musia být oddelené čiarkou a medzerou: ")
pravidla = input()

def algoritmus(zoznam, pravidla):
    vytriedeny_zoznam = []
    for item in zoznam:
        if item in pravidla: #dodefinovat!
            vytriedeny_zoznam.append(item)
        else:
            pass
    return f"Vytriedený zoznam podľa pravidiel {pravidla} je: {vytriedeny_zoznam}"