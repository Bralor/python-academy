Minula [lekce#10](https://github.com/Bralor/python-academy/tree/lekce10)

<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lekce 11
## Dulezite odkazy
- Portal [Engeto.com](https://engeto.com/)
- Python Academy [repozitar](https://github.com/Bralor/python-academy)
- [Generator](https://mockaroo.com/) nahodnych dat (testovacich dat)

## Dnesni ukol
Dnes se budeme bavit o dalsich typech souboru, se kterymi muzeme v ramci
Pythonu pracovat. Povime si neco o formatu, jehoz hlavnim ucelem je snadny
prenos dat (tedy [JSON](#important-links)) a tabulkovem formatu (tedy
[CSV](#important-links)). V bodech:
1. json
2. csv

## Prevodnik json2csv
Ukolem pro dnesek je napsat program, ktery bude umet prevadet `JSON`
na `CSV` (moznost doplnit i obracene). Na uvod dostaneme `JSON` s
fiktivnimi udaji zamestnancu, ktere budeme chtit ukladat do `CSV`. Logicky
chceme usporadat strukturu programu nasledovne:

## Ukazka na uvod
Spustime skript v adresari:
```
$ python hlavni.py <do-csv> <puvodni.json>
```
Dostaneme nasledujici vystup:
```

```

## Co budeme potrebovat?
- python 3.6+
- text. editor
- [for smycky](https://github.com/Bralor/python-academy/tree/lekce05)
- [funkce v Pythonu](https://github.com/Bralor/python-academy/tree/lekce06)
- [prace s text. soubory](https://github.com/Bralor/python-academy/tree/lekce08)
- [handlovani chyb](https://github.com/Bralor/python-academy/tree/lekce09)
- [importovani](https://github.com/Bralor/python-academy/tree/lekce10)

## Co nejdriv
Do pracovniho adresare si nakopirujeme vstupni `ORIG.json` soubor. Dale si
otevreme novy soubor, ktery pojmenujeme `hlavni.py`:
```python
# hlavni.py
#!/usr//bin/python3.8
"""Lekce #11 - Uvod do programovani, csv/json - hlavni funkce"""
```
Bodove by mela struktura obsahovat tyto kroky:
```python

# hlavni funkce musi rozpoznat scenar       -> hlavni()
    # potom nacist obsah                    -> nacti_obsah()
    # upravit jej na prislusny format       -> uprav_text()
    # zapsat                                -> zapis()

```

## Spousteni
Prvni vec, co nas skript v ramci souboru `hlavni.py` musi vysetrit je, jaky
typ souboru budeme zapisovat. Chceme soubor spoustet nasledovne:
```
$ python hlavni.py to-csv <jmeno_souboru>
```
Takze nejprve nahrajeme modul `sys` a pouzijeme funkcionalitu spousteni s
argumenty:
```python
...
import sys


def hlavni() -> None:
    if prevod == "do-csv":
        print("Nacitam obsah!")
        print("Zpracovavam...")
        print("Zapisuji obsah")


if __name__ == "__main__":
    prevod = sys.argv[1]
    hlavni()
```
Na zacatek staci jednotlive funkce nahradit pouhymi vystupy z funkci `print`.

## Nacitame!
Nacitani souboru `.txt` uz ovladame. Dneska nam to ale stacit nebude.

## Json (~javaScript object notation)
Ucelne zjednoduseny format, urceny pro prenos dat. Snadno citelny, lehce
formatovatelny. Velice podobny Pythonovskemu slovniku, ale ma svoji
charakteristickou sadu pravidel:
1. Co neni `str`, to je prevedeno na `str`
2. `True` namapovano na `'true'` (`False` na `'false'`)
3. `None` namapovano na `null`

## Prace s json-em
Nez vubec zacneme s json-em pracovat, musime importovat balik `json` (standartne
k dispozici). Vytvorime si novy soubor `pomocne.py`:
```python
# pomocne.py
#!/usr/bin/python3.8
"""Lekce #12 - Uvod do programovani, csv/json - pomocne funkce"""
import json
```
Obecne se pri praci s json-em mluvi o _serialization/deserialization_. Nam bude
stacit proste __cist/zapsat__ (podobne jako u `.txt` souboru):
```python
udaje {
    "polobuh: {
        "jmeno": "Chuck Norris",
        "kliky": "vsechny"
    }
}
```

### Zapis
Nejprve budeme chtit slovnik `udaje` zapsat jako `.json` soubor:
```python
with open("novy_json.json", "w") as zapis_js:
    json.dump(udaje, zapis_js)
```
Pro zapis pouzijeme funkci `dump`. Ta potrebuje nasledujici:
1. __promennou__ s udaji k zapsani
2. __jmeno__ souboru, kam `promennou` zapiseme

### Cteni
Ted, kdyz mame nas prvni json zapsany na disku, jej otevreme:
```python
with open("novy_json.json", "r") as cteni_js:
    udaje = json.load(cteni_js)
```
Pote staci vypsat promennou `udaje`.

### Dalsi argumenty
1. __indent__ - odsadi zapsany `json` o N mist
2. __sort\_keys__ - seradi klice

### dump/dumps, load/loads
Opatrne na jmena funkci. `dump/load` zapisuje(cte) `json` do(z) souboru.
Kdyz pouziju `dumps/loads`, tak zapisuji(ctu) retezec pro vypisovani s `print`,
parsovani, aj.

## Nacitame
Nejprve pojdme dopsat do souboru `pomocne.py` funkci, ktera nacita obsah ruznych
json-u:
```python
# pomocne.py
...

def nacti_json(soubor: str, mod: str = "r") -> dict:
    try:
        with open(soubor, mod) as cteni:
            obsah = json.load(cteni)

    except FileNotFoundError:
        print(f"SOUBOR: {soubor} NEEXISTUJE!")

    else:
        return obsah
```
Nasledne dopiseme volani funkce `nacti_json` do souboru `hlavni.py`:
```python
# hlavni.py
...

from pomocne import nacti_json


def hlavni() -> None:
    if prevod == "do-csv":
        nacteny_json = nacti_json("ORIG.json")
        print(f"JSON: {nacteny_json}")

        print("Zpracovavam...")
        print("Zapisuji obsah")

...
```
## Upravime obsah
Z naseho puvodniho souboru `json` jsme jiz udelali slovnik. Nyni jej chceme
zredukovat, protoze nas zajimaji jen tyto klice:
1. __first\_name__
2. __last\_name__
3. __email__
Proto musime nyni napsat funkci, ktera vytvori novy slovnik, ktery bude mit
unikatni jmeno klice a tyto tri hodnoty:
```
novy_slovnik = {
    "id_1":{"jmeno": "Matous", "prijmeni": "Holinka", "email": "matous@matous"},
    ...
}
```
Definujeme novou funkci do souboru `pomocne.py`:
```python
# pomocne.py
...

def uprav_obsah(data: dict) -> dict:
    """
    Zredukujeme puvodni slovnik 'data' pouze na 3 klice:
        1. jmeno
        2. prijmeni
        3. email

    Ulozime do noveho slovniku a vracime jej
    """
    upravene_udaje = {}

    for index, slovnik in enumerate(data, 1):
        upravene_udaje[f"id_{index}"] = {
            "jmeno": slovnik["first_name"],
            "prijmeni": slovnik["last_name"],
            "email": slovnik["email"]
        }
    return upravene_udaje
```
Pote pouzijeme funkci `uprav_obsah` v souboru `hlavni.py`:
```python
# hlavni.py
...
from pomocne import nacti_json, uprav_obsah


def hlavni() -> None:
    if prevod == "do-csv":
        nacteny_json = nacti_json("ORIG.json")
        print(f"JSON: {nacteny_json}")

        zkracene_udaje = uprav_obsah(nacteny_json)
        print("ZKRACENE: {zkracene_udaje}")

        print("Zapisuji obsah")

...
```

## Zapisujeme!
Nyni, kdyz jsme si nacetli udaje z `json` a zpravili jejich obsah, muzeme nova
data ukladat do `csv`.

## Csv (~ comma-separated values)
Tedy format zalozeny na hodnotach obecne oddelenych oddelovacem, psany v jistem
dialektu. Zakladni stavebni jednotkou jsou bunky (MS Excel), ktere jsou
situovany do radku a sloupcu.

## Prace s csv
Nejprve nahrajeme modul `csv`, abychom mohli pouzivat vse, co obsahuje.
Zakladni dva procesy, ktere muzeme provadet jsou:
1. __Cteni__ souboru `csv`
2. __Zapis__ do souboru `csv`
Udaje na procvicovani:
```python
zahlavi = ["jmeno", "prijmeni", "vek"]
osoba1 = ["Matous", "Holinka", "28"]
osoba2 = ["Petr", "Svetr", "27"]

osoba3 = {"jmeno": "Matous", "prijmeni": "Holinka", "vek": 28}
osoba4 = {"jmeno": "Petr", "prijmeni": "Svetr", "vek": 27}
```

### Zapis do souboru
Tak jako u `txt` a `json` vyuzijeme funkcionality kontext. manazeru. Prakticky
muzeme pro zapis pouzit funkci `writer`, se kterou muzeme zapsat seznamy aj.
Nebo `DictWriter`, kdy zapisujeme udaje ulozene ve slovnicich.

### writer
Nejprve zkusime ulozit seznamy:
```python
import csv

with open("prvni_csv.csv", mode="w") as csv_f:
    zapisovac = csv.writer(csv_f, delimiter=',')

    zapisovac.writer(zahlavi)
    zapisovac.writer(osoba1)
    zapisovac.writer(osoba2)
```
Nakonec v aktualnim adresari zkontrolujeme soubor `prvni_csv.csv`.
```python
# eventualni reseni
    ...
    zapisovac.writerows((zahlavi, osoba1, osoba2))
```

### DictWriter
Soucasne muzeme ukladat do `csv` take slovniky:
```python
import csv

with open("treti_csv.csv", mode="w") as csv_f:
    zahlavi = osoba3.keys()
    zapisovac = csv.DictWriter(csv_f, fieldnames=zahlavi)

    zapisovac.writeheader()
    zapisovac.writerow(osoba3)
    zapisovac.writerow(osoba4)
```
Opet muzeme pouzit variantu `writerows`.

### Cteni ze souboru
Analogicky k procesu zapisovani funguje proces cteni ze souboru `csv`. Tentokrat
pomoci:
1. Funkce __reader__ (seznamy)
2. Funkce __DictReader__ (slovniky)
```python
import csv

with open("treti_csv.csv", mode="r") as csv_f:
    cteni = csv.DictReader(csv_f, delimiter=",")

    for radek in cteni:
        print(f"RADEK: {radek}")
```

## Ulozime slovnik
Pomoci funkci v modulu `csv` muzeme ulozit udaje v nasi promenne
`zkracene_udaje`. Doplnime proto soubor `pomocne.py` o novou definici funkce:
```python
# pomocne.py
import csv
...
def zapis_csv(soubor: str, udaje: dict) -> None:
    try:
        with open(soubor, mode="w", newline="") as csv_f:
            zahlavi = udaje["id_1"].keys()
            zapisovac = csv.DictWriter(csv_f, fieldnames=zahlavi)

            zapisovac.writeheader()
            for zamestnanec in udaje:
                zapisovac.writerow({
                    "jmeno": udaje[zamestnanec]["jmeno"],
                    "prijmeni": udaje[zamestnanec]["prijmeni"],
                    "email": udaje[zamestnanec]["email"]
                })
    except KeyError:
        print("NESPRAVNY HODNOTA PRO SLOVNIK")
```
Doplnime jeste soubor `hlavni.py`, kde funkci `zapis_csv` zavolame:
```python
# hlavni.py
...
from pomocne import nacti_json, uprav_obsah, zapis_csv
...
def hlavni() -> None:
    if prevod == "do-csv":
        nacteny_json = nacti_json()
        zkracene_udaje = uprav_obsah(nacteny_json)
        zapis_csv("vystupni.csv", zkracene_udaje)
...
```
Dalsi variantou jak ulohu vylepsit je doplnit podminkovou vetev pro prevedeni
`csv` souboru do `json`(soucasne doplnit potrebne funkce).

Pokracovat na [Lekci#12](https://github.com/Bralor/python-academy/tree/lekce12)

