# Filter chemických prvkov

Tento repozitár slúži pre študijné účely. 
Algoritmus vznikol na základe úlohy, viď nižšie ***Task description***.
Ako zoznam som si zvolila voľne sťažiteľný [JSON dataset chemických prvkov](https://jsonlint.com/datasets/elements) (obsahuje len výber chemických prvkov, nie celý zoznam!).

### Task description:
Prosím napište algoritmus (jazyk volný), který ze seznamu vytřídí prvky podle nějakých pravidel, včetně příkladu takového pravidla. Tzn. ať je tam sekce, kam se doplní konkrétní pravidla, prvky budou někde mimo v seznamu, který algoritmus projde a smaže hodnoty, které neprošly pravidly. Prosím o instrukci jak spustit a kde najdeme algoritmus.

### Popis algoritmu:
Tento program slúži na filtrovanie chemických prvkov podľa zadaných pravidiel. Program načíta zoznam chemických prvkov z JSON súboru, umožní užívateľovi zadať pravidlá a následne vytriedi zoznam podľa týchto pravidiel.

## Hlavné ciele:
- samostatná sekcia pre logiku pravidiel oddelená od samotnej metódy algoritmus
- dataset oddelený
- škálovateľnosť pre prípadné doplnenie ďalších pravidiel
- upevniť si prácu s JSON, cykly while a for, modularita
- precvičiť si písanie testov (unittest)

## Instructions:
1.  Naklonujte si repozitár
2.  Uistite sa, že máte nainštalovaný Python (vs 3.8 alebo novšia)
3.  Spustite skript "algoritmus.py" cez terminál, napr. vo VS Code