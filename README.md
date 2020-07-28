Minula [lekce#05](https://github.com/Bralor/python-academy/tree/lekce05)

<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

![](../images/engeto.png)
# Python academy, lesson 06
## Dulezite odkazy
- Portal [Engeto.com](https://engeto.com/)
- Python Academy [repozitar](https://github.com/Bralor/python-academy)
- Generator [nahodnych dat](https://mockaroo.com/)
- [Built-in funkce](https://docs.python.org/3/library/functions.html))

## Co nas dnes ceka?
Jsme v pulce nasich setkani, a proto je uz nacase, povedet si neco o funkcich
v Pythonu. Soucasne se zamerime na prirazeni vicero promennych k prislusnym
hodnotam aj.

## Vytvorime si vlastni funkci
Na uvod dostaneme pseudo-data z webu. Jejich aktualni podoba resp. cislovani
je samozrejme nepouzitelne pro bezneho uzivatele. Proto je musime upravit. Data
oznacena v prvnim sloupci jsou nic nerikajici hodnota z weboveho zdroje. My si
tyto hodnoty upravime.

## Ukazka na uvod
Spustime skript v tomto adresari:
```
$ ./uprav_udaje
```
Vystup by na konci lekce mohl vypadat nasledovne:
```
```

## Co budeme potrebovat?
- python 3.6.9+
- text. editor
- potrebne promenne:
```
UDAJE = """
byt 0001,55 m2,Olomouc,ul.Heyrovského,
byt 0003,65 m2,Olomouc,ul.Novosadský dvůr,
byt 0004,75 m2,Olomouc,ul.Wolkerova,
byt 0004,68 m2,Olomouc,ul.Zikova,
byt 0001,36 m2,Olomouc,ul.Nová Ulice,
byt 0003,46 m2,Olomouc,ul.Nové sady,
byt 0004,75 m2,Olomouc,ul.Nová Ulice,
byt 0003,42 m2,Olomouc,ul.Nová Ulice,
byt 0005,107 m2,Olomouc,ul.Nová Ulice,
byt 0003,74 m2,Olomouc,ul.Uničovská,
byt 0003,42 m2,Olomouc,ul.Nešverova,
byt 0002,55 m2,Olomouc,ul.Dělnická,
byt 0004,59 m2,Olomouc,ul.Zirmova,
byt 0007,92 m2,Olomouc,ul.Nová Ulice,
byt 0002,52 m2,Olomouc,ul.Nová Ulice,
byt 0004,76 m2,Olomouc,ul.Nová Ulice,
byt 0002,81 m2,Olomouc,ul.Nová Ulice,
byt 0003,64 m2,Olomouc,ul.Za vodojemem,
byt 0007,113 m2,Olomouc,ul.Jihoslovanská,
byt 0005,94 m2,Olomouc,ul.Uničovská,
byt 0003,42 m2,Olomouc,ul.Rošického,
byt 0003,75 m2,Olomouc,ul.Rošického,
byt 0004,48 m2,Olomouc,ul.Handského,
byt 0004,68 m2,Olomouc,ul.Komenského,
byt 0003,61 m2,Olomouc,ul.Jarmily Glazarové,
byt 0004,39 m2,Olomouc,ul.Přichystalova,
byt 0003,70 m2,Olomouc,ul.Foerstova,
byt 0005,61 m2,Olomouc,ul.Nová Ulice,
byt 0007,88 m2,Olomouc,ul.Nová Ulice,
byt 0003,92 m2,Olomouc,ul.U cukrovaru,
byt 0003,56 m2,Olomouc,ul.U cukrovaru,
byt 0004,56 m2,Olomouc,ul.Paseka,
byt 0002,74 m2,Olomouc,ul.Rokycanova,
byt 0007,116 m2,Olomouc,ul.U cukrovaru,
byt 0004,59 m2,Olomouc,ul.Řezáčova,
byt 0004,100 m2,Olomouc,ul.Libušina,
byt 0003,64 m2,Olomouc,ul.Řezáčova,
byt 0001,33 m2,Olomouc,ul.Libušina,
byt 0006,87 m2,Olomouc,ul.Černá cesta,
byt 0007,95 m2,Olomouc,ul.Kaštanová,
byt 0003,74 m2,Olomouc,ul.Nová Ulice,
byt 0003,75 m2,Olomouc,ul.Nová Ulice,
byt 0004,86 m2,Olomouc,ul.Hněvotínská,
byt 0002,67 m2,Olomouc,ul.Polská,
byt 0007,120 m2,Olomouc,ul.Dvořákova,
byt 0004,90 m2,Olomouc,ul.Dvořákova,
byt 0004,86 m2,Olomouc,ul.Nová Ulice,
byt 0003,75 m2,Olomouc,ul.Nešverova,
byt 0001,45 m2,Olomouc,ul.Zirmova,
byt 0006,114 m2,Olomouc,ul.Přichystalová,
"""
```

## Zacneme s ulohou
<p align="center">
  <img src="https://media.giphy.com/media/1pAeSRT0jM7KxY3J4r/source.mp4" width="300" height="300">
</p>

Vytvorime si v nasem pracovnim adresari novy soubor a do nej vlozime
[udaje](#co-budeme-potrebovat) na zacatek.
```python
#!/usr/bin/python3
"""Lekce #06 - Uvod do programovani, Uprav udaje"""

# I. KROK
UDAJE = """
    ...
```

## Jak prevadet
Nejprve musime stanovit pravidla, na zaklade kterych budeme chtit zadany text
upravit.
```python
PREVOD_UDAJU = {
    "byt 0001": "1+1",
    "byt 0002": "2+1",
    "byt 0003": "2+kk",
    "byt 0004": "3+1",
    "byt 0005": "3+kk",
    "byt 0006": "4+1",
    "byt 0007": "4+kk",
}
```
Tuto promennou take pouzijeme v nasem kodu.

## Vlastni funkce
Nez je zacneme vubec pouzivat, pojdme si rict, co to _funkce_ vubec je. V
Pythonu je funkce kus kodu, jehoz zamerem je provest jednu souvislou akci, ukol.
Umoznuji pouzivat kus kodu opakovane, na ruznych mistech a tim zachovavaji
vysokou uroven citelnosti kodu.

### Jake mame funkce
Mozna si rikate, ze jsme uz o funkcich mluvili. Ano, je to tak. Python obsahuje
celou sadu
[zabudovanych funkci](https://docs.python.org/3/library/functions.html)
se kterymi jsme se jiz seznamili.

1. print()
2. input()
3. sum()
4. sorted()

V takovem pripade mluvime skupine funkci, ktere jsou jiz definovane ve
strukture Pythonu. My je muzeme primo pouzivat.

Dalsi typ funkci, ktere nas budou zajimat zejmena v dnesni casti jsou
__definovane__ funkce. Tedy takove, ktere si budeme muset jako uzivatele
definovat a pouzit.

### Nase prvni funkce
Obecne funkce muze vypadat nasledovne:
```python
def <jmeno_funkce>(<parametry_funkci>):
    <vlastni_kod>
    <ohlaseni vraceni hodnoty>  # volitelne
```

Podivejme se spolecne na prvni funkci:
```python
def umocnovani(cislo: int, exponent: int) -> int():
    """
    Funkce vezme dve cisla. Prvni bude hodnota, druhe exponent. Potom vrati
    cislo umocnene exponentem
    """
    return cislo ** exponent
```
Mame definovanou funkci, ted ji staci jen _pouzit_.

Funkci pouzijeme tak, ze ji _zavolame_. Tedy, ze ji oslovime jejim jmenem
_umocnovani()_ a do kulate zavorky zadame dve vstupni hodnoty, jak rika jeji
popisek. Napriklad:
```
umocnovani(2, 5)  # 32
```

### Doplnime zapis
## Rozdelime radky
## Prirazovani vice promennych
## Vracime vysledek

Pokracovat na [Lekci#07](https://github.com/Bralor/python-academy/tree/lekce07)

# Postup
Opet si otevreme novy soubor *.py* a nakopirujeme sablonu nize:
```
# I. KROK
# Vlozime zadani
XXXX

# II. KROK
# Definujeme vzor, jak chceme *udaje* prevest


# III. KROK
# Prochazime promennou *udaj* jeden radek za druhym
# Ukazat prazdne retezce na zacatku/ konci

# IV. KROK
# Napiseme seznamovou komprehenci s podminkou

# V. KROK
# Potrebujeme promennou *udaje* rozdelit
# ukazka vicenasobneho prirazeni
# Zkracene prirazovani
    # VI. KROK
    # Chybne prirazeni

    # VII. KROK
    # Spravne prirazeni

    # VIII. KROK
    # chceme pouze ic a zbytek
    # rozbalovaci operator

# IX. KROK
# Potrebujeme menit oznaceni bytu za typ bytu
# Uvod do funkci

# X. KROK
# vstupy do funkci
# vystupy funkce


# XI. KROK
# Doplnime smycku s nasi novou funkci

# XII. KROK
# Uvod k modulum
```

# Cheatsheet s priklady
## Promenne
Pomoci znamenka *=* vytvorim cestu [ukazatele](https://engeto.com/cs/kurz/online-python-akademie/studium/3cEZRZUCQVqpU-31RZEfnw/zaciname-s-pythonem-datove-typy/mluvime-s-pythonem/pamatuj-si-informace-promenne) (jmena promenne) na jeho hodnotu.

Priklad:
```
JMENO = "Matous"
```

## Vicenasobne prirazeni jmena promenne
Ovsem neni nutne prirazovat na jednom radku pouze jedno [jmeno promenne](https://engeto.com/cs/kurz/online-python-akademie/studium/gmVpTjfQQnmVcp9g8DKlmA/uvod-do-funkci/promenne-20/string-list).

Priklad:
```
>>> JMENO1, JMENO2 = "Matous", "Lucie"
>>> JMENO1
'Matous'
>>> JMENO2
'Lucie'
```
Ale opatrne:
```
>>> STREDNI_ROD = ("mesto", "more", "kure", "staveni")
>>> v1, v2, v3, v4, v5 = STREDNI_ROD
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 5, got 4)
```

## Rozbalovaci operator *
Pokud nastane kolize s poctem identifikatoru promennych a skutecnymi hodnotami, muzeme si pomoci [hvezdickou](https://engeto.com/cs/kurz/online-python-akademie/studium/UCYPS8T2TVCDmGhv_dB8Vg/uvod-do-funkci/promenne-20/rozbalovani).
Priklad:
```
>>> v1, *zbytek = STREDNI_ROD
>>> v1
'mesto'
>>> zbytek
['more', 'kure', 'staveni']
>>> 
```

## Zkracene prirazovani
Jde o [zkracenou](https://engeto.com/cs/kurz/online-python-akademie/studium/0F6aYvi8RFeXOnqGoDLQ1g/uvod-do-funkci/promenne-20/rozsirene-prirazeni) verzi predpisu u aritmetickych operaci.
Priklad:
```
>>> i = 73
>>> i = i + 1
>>> i
74
>>> i += 1
75
```

## Funkce
[Funkce](https://engeto.com/cs/kurz/online-python-akademie/studium/HHfElw5KQnGOEK4BMEvg8A/uvod-do-funkci/funkce/uvod-do-funkci) je predepsany postup, kdy vezmu libovolny vstup, upravim jej a vracim vystupni hodnotu. S funkcemi v Pythonu jsme se jiz setkali. print(), sorted(), input(), str(). To jsou tzv. zabudovane funkce (built-in). Funkce, ktere mame jiz v Pythonu k dispozici. Dalsi funkce, ktere v Pythonu nemame si musime definovat svepomoci.

Teorie:

Priklad:

## Uvod k modulum
Neni nutne vsechny funkce psat na vlastni pest. Spousty uzitecnych z nich nekdo uz napsal! Ulozil je do tzv. [modulu](https://engeto.com/cs/kurz/online-python-akademie/studium/gY9XxQ32RYiSI1fe_SlmoA/uvod-do-funkci/python-knihovna/zakladni-moduly). Modul je v podstate nejaky soubor Pythonu (.py). K dispozici jsou dva typy modulu. Nas bude zatim zajimat pouze prvni skupina a to jsou predinstalovane moduly.

Teorie:
```
import <jmeno_modulu>
from <jmeno_modulu> import <jmeno_funkce/metody>
from <jmeno_modulu> import <jmeno_funkce/metody> as <alias>
```
