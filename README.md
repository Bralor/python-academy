➡ [vratit se na patou lekci](https://github.com/Bralor/python-academy/tree/lekce05)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 6⃣ Python akademie
###  Dulezite odkazy
- [Portal Engeto.com](https://engeto.com/)
- [Seznamova komprehence](http://howto.py.cz/cap08.htm#10)
- [Ternarni operator](https://book.pythontips.com/en/latest/ternary_operators.html)
- [Python, dokumentace zabudovanych funkci](https://docs.python.org/3/library/functions.html)
- [Collections, standartni modul](https://docs.python.org/3/library/collections.html#collections.Counter)
---

###  Obsah lekce
1. Ukazka ulohy
2. Vstupni udaje
3. Funkce, zabudovane
4. Funkce, uzivatelem definovane
5. Prirazovani hodnot promennym
6. Zkraceny zapis
---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si sestou lekci jako **zip**](https://github.com/Bralor/python-academy/archive/lekce06.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **upravene_udaje** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
  <summary>📥 Vstupni udaje</summary>

  #### 📜 Upravene & scrapovane detaily
  ```python
  UDAJE = """
  byt0001,55m2,Olomouc,ul.Heyrovského,
  byt0003,65m2,Olomouc,ul.Novosadský_dvůr,
  byt0004,75m2,Olomouc,ul.Wolkerova,
  byt0004,68m2,Olomouc,ul.Zikova,
  byt0001,36m2,Olomouc,ul.Nová_Ulice,
  byt0003,46m2,Olomouc,ul.Nové_sady,
  byt0004,75m2,Olomouc,ul.Nová_Ulice,
  byt0003,42m2,Olomouc,ul.Nová_Ulice,
  byt0005,107m2,Olomouc,ul.Nová_Ulice,
  byt0003,74m2,Olomouc,ul.Uničovská,
  byt0003,42m2,Olomouc,ul.Nešverova,
  byt0002,55m2,Olomouc,ul.Dělnická,
  byt0004,59m2,Olomouc,ul.Zirmova,
  byt0007,92m2,Olomouc,ul.Nová_Ulice,
  byt0002,52m2,Olomouc,ul.Nová_Ulice,
  byt0004,76m2,Olomouc,ul.Nová_Ulice,
  byt0002,81m2,Olomouc,ul.Nová_Ulice,
  byt0003,64m2,Olomouc,ul.Za_vodojemem,
  byt0007,113m2,Olomouc,ul.Jihoslovanská,
  byt0005,94m2,Olomouc,ul.Uničovská,
  byt0003,42m2,Olomouc,ul.Rošického,
  byt0003,75m2,Olomouc,ul.Rošického,
  byt0004,48m2,Olomouc,ul.Handského,
  byt0004,68m2,Olomouc,ul.Komenského,
  byt0003,61m2,Olomouc,ul.Jarmily_Glazarové,
  byt0004,39m2,Olomouc,ul.Přichystalova,
  byt0003,70m2,Olomouc,ul.Foerstova,
  byt0005,61m2,Olomouc,ul.Nová_Ulice,
  byt0007,88m2,Olomouc,ul.Nová_Ulice,
  byt0003,92m2,Olomouc,ul.U_cukrovaru,
  byt0003,56m2,Olomouc,ul.U_cukrovaru,
  byt0004,56m2,Olomouc,ul.Paseka,
  byt0002,74m2,Olomouc,ul.Rokycanova,
  byt0007,116m2,Olomouc,ul.U_cukrovaru,
  byt0004,59m2,Olomouc,ul.Řezáčova,
  byt0004,100m2,Olomouc,ul.Libušina,
  byt0003,64m2,Olomouc,ul.Řezáčova,
  byt0001,33m2,Olomouc,ul.Libušina,
  byt0006,87m2,Olomouc,ul.Černá cesta,
  byt0007,95m2,Olomouc,ul.Kaštanová,
  byt0003,74m2,Olomouc,ul.Nová_Ulice,
  byt0003,75m2,Olomouc,ul.Nová_Ulice,
  byt0004,86m2,Olomouc,ul.Hněvotínská,
  byt0002,67m2,Olomouc,ul.Polská,
  byt0007,120m2,Olomouc,ul.Dvořákova,
  byt0004,90m2,Olomouc,ul.Dvořákova,
  byt0004,86m2,Olomouc,ul.Nová Ulice,
  byt0003,75m2,Olomouc,ul.Nešverova,
  byt0001,45m2,Olomouc,ul.Zirmova,
  byt0006,114m2,Olomouc,ul.Přichystalová,
  """

  PREVOD_UDAJU = {
    "byt0001": "1+1",
    "byt0002": "2+1",
    "byt0003": "2+kk",
    "byt0004": "3+1",
    "byt0005": "3+kk",
    "byt0006": "4+1",
    "byt0007": "4+kk",
  }
  ```

</details>

---

<details>
  <summary>👼 Funkce, zabudovane</summary>

  #### ☝ K zapamatovani
  - jako uzivatel je nemusim definovat
  - mohu je primo pouzit (_zavolat_)
  - soupisku vsech najdeme v sekci [odkazy](#dulezite-odkazy)
  - setrime vypisovani
  - zapis je citelnejsi
  - opakovane pouzitelne

  #### ❓ Jak vypada zabudovana funkce
  ```python
  print("Ahoj, vsem!")
  int(input("Zadejte cislo: "))
  ```

</details>

---

<details>
  <summary>🔥 Funkce, uzivatelem definovane</summary>

  #### ☝ K zapamatovani
  - neni soucasti standartni knihovny Pythonu
  - nejprve potrebuji zapsat jeji definici
  - pokud ji chci spustit, musim ji _zavolat_ (pouzit)
  - `def` klicovy vyraz v zahlavi definice
  - `vypocitej_sumu` nasleduje jmeno funkce, budu potrebovat pri spusteni
  - `cisla` v kulate zavorce je parametr funkce (idealne 2, max. 3)
  - pokud jmeno funkce neni dostatecne popisne, zapisu dokumentaci
  - `return` ohlaseni, pokud chci z funkce vratit nejaky udaj
  - `vypocitej_sumu()` spusteni funkce (_volani_)
  - `seznam_cisel` argument funkce, ktery chci pouzit ve funkci

  #### ❓ Jak vypada zabudovana funkce
  ```python
  def jmeno_funkce(parametr_1, parametr_2):
      # odsazeny kod
      # VOLITELNE: vraceni hodnoty
  ```
  **Priklad funkce**
  ```python
  def vypocitej_sumu(cisla):
      """Dokumentace funkce"""
      suma_cisel = list()

      for cislo in cisla:
          suma_cisel = suma_cisel + cislo

      return suma_cisel


  seznam_cisel = [11, 22, 33, 44, 55, 66, 77, 88, 99]
  vysledek = vypocitej_sumu(seznam_cisel)
  print(f"SUMA VSECH CISEL: {vysledek}")
  ```
  **Pozor!** Nas zapis muzeme vylepsit nekolika kroky:
  1. Napovidani datovych typu
  2. Zkraceny zapis
  3. Seznamova komprehence
  4. f-string, volani funkce
  5. Idealne pouzit `sum` funkci 😏

<details>
  <summary>💣Nase prvni funkce</summary>

  #### 🥅 Nas cil
  Nejprve bez funkce. Chceme napsat mechanismus, ktery prevede `byt0001`
  na `1+1`.

  #### 1⃣ Prvni krok
  Nejprve pomocna promenna `udaj_1`:
  ```python
  udaj_1 = "byt0001"
  ```

  #### 2⃣ Control-flow
  Mechanismus, kterym provedu prevedeni:
  ```python
  if udaj_1 in PREVOD_UDAJU.keys():
      udaj_1 = PREVOD_UDAJU[udaj_1]
  ```
  Pokud nebude hodnota ve slovniku, musime myslet na `KeyError`:
  ```python
  else:
      print("NEZNAMY TYP BYTU!")
  ```
  **Pozor!** Nas zapis muzeme vylepsit nekolika kroky:
  1. Odstranit metodu `keys`
  2. Ternarni operator
  3. Metoda slovniku `get`

  #### 3⃣ Pomoci funkce
  Zapiseme pomoci funkce a doplnime pocitani:
  ```python
  def prevodnik_bytu(typ_bytu: str, vzor: dict) -> str:
      """Prevede a zapocita stavajici typ bytu na novy"""
      if typ_bytu in vzor:
          typ_bytu = vzor[typ_bytu]
          return typ_bytu
      else:
          print("NEZNAMY TYP BYTU!")

  vysledny_typ = prevodnik_bytu(udaj_1, PREVOD_UDAJU)
  print(f"PUVODNI: {udaj_1}, NOVY: {vysledny_typ}")
  ```

</details>

</details>

---

<details>
  <summary>🚦 Prirazovani hodnot promennym</summary>

  #### 📜 Nahodne generovany text

</details>

---

<details>
  <summary>🎯 Zkracene prirazovani</summary>

  #### 📜 Nahodne generovany text

</details>

---

➡ [pokracovat na sedmou lekci](https://github.com/Bralor/python-academy/tree/lekce07)


# Python academy, lesson 06
## Dulezite odkazy
- Portal [Engeto.com](https://engeto.com/)
- Python Academy [repozitar](https://github.com/Bralor/python-academy)
- Generator [nahodnych dat](https://mockaroo.com/)
- [Built-in funkce](https://docs.python.org/3/library/functions.html)
- [Zkraceny zapis](https://docs.python.org/2.0/ref/augassign.html)
- Dalsi vyuziti [hvezdicky](https://note.nkmk.me/en/python-tuple-list-unpack/)

## Co nas dnes ceka?
Jsme v pulce nasich setkani, a proto je nacase, povedet si neco o funkcich
v Pythonu. Soucasne se zamerime na prirazeni vice promennych k prislusnym
hodnotam aj.

## Vytvorime si vlastni funkci
Na uvod dostaneme pseudo-data z webu. Jejich aktualni podoba resp. cislovani
je samozrejme nepouzitelne pro bezneho uzivatele. Proto je musime upravit.
Soucasne chceme evidovat pocet prevedenych dat pro zaverecny vystup.

## Ukazka na uvod
Spustime skript v tomto adresari:
```
$ ./uprav_udaje
```
Za predpokladu, ze pocet vstupnich udaju odpovida poctu upravenych udaju, chceme
nasledujici vystup:
```
['1+1,55m2,Olomouc,ul.Heyrovského,',
 '2+kk,65m2,Olomouc,ul.Novosadský_dvůr,',
 '3+1,75m2,Olomouc,ul.Wolkerova,',
 '3+1,68m2,Olomouc,ul.Zikova,',
 '1+1,36m2,Olomouc,ul.Nová_Ulice,',
 '2+kk,46m2,Olomouc,ul.Nové_sady,',
 ...
```

## Co budeme potrebovat?
- python 3.6.9+
- text. editor
- potrebne promenne:
```
UDAJE = '''
byt0001,55m2,Olomouc,ul.Heyrovského,
byt0003,65m2,Olomouc,ul.Novosadský_dvůr,
byt0004,75m2,Olomouc,ul.Wolkerova,
byt0004,68m2,Olomouc,ul.Zikova,
byt0001,36m2,Olomouc,ul.Nová_Ulice,
byt0003,46m2,Olomouc,ul.Nové_sady,
byt0004,75m2,Olomouc,ul.Nová_Ulice,
byt0003,42m2,Olomouc,ul.Nová_Ulice,
byt0005,107m2,Olomouc,ul.Nová_Ulice,
byt0003,74m2,Olomouc,ul.Uničovská,
byt0003,42m2,Olomouc,ul.Nešverova,
byt0002,55m2,Olomouc,ul.Dělnická,
byt0004,59m2,Olomouc,ul.Zirmova,
byt0007,92m2,Olomouc,ul.Nová_Ulice,
byt0002,52m2,Olomouc,ul.Nová_Ulice,
byt0004,76m2,Olomouc,ul.Nová_Ulice,
byt0002,81m2,Olomouc,ul.Nová_Ulice,
byt0003,64m2,Olomouc,ul.Za_vodojemem,
byt0007,113m2,Olomouc,ul.Jihoslovanská,
byt0005,94m2,Olomouc,ul.Uničovská,
byt0003,42m2,Olomouc,ul.Rošického,
byt0003,75m2,Olomouc,ul.Rošického,
byt0004,48m2,Olomouc,ul.Handského,
byt0004,68m2,Olomouc,ul.Komenského,
byt0003,61m2,Olomouc,ul.Jarmily_Glazarové,
byt0004,39m2,Olomouc,ul.Přichystalova,
byt0003,70m2,Olomouc,ul.Foerstova,
byt0005,61m2,Olomouc,ul.Nová_Ulice,
byt0007,88m2,Olomouc,ul.Nová_Ulice,
byt0003,92m2,Olomouc,ul.U_cukrovaru,
byt0003,56m2,Olomouc,ul.U_cukrovaru,
byt0004,56m2,Olomouc,ul.Paseka,
byt0002,74m2,Olomouc,ul.Rokycanova,
byt0007,116m2,Olomouc,ul.U_cukrovaru,
byt0004,59m2,Olomouc,ul.Řezáčova,
byt0004,100m2,Olomouc,ul.Libušina,
byt0003,64m2,Olomouc,ul.Řezáčova,
byt0001,33m2,Olomouc,ul.Libušina,
byt0006,87m2,Olomouc,ul.Černá cesta,
byt0007,95m2,Olomouc,ul.Kaštanová,
byt0003,74m2,Olomouc,ul.Nová_Ulice,
byt0003,75m2,Olomouc,ul.Nová_Ulice,
byt0004,86m2,Olomouc,ul.Hněvotínská,
byt0002,67m2,Olomouc,ul.Polská,
byt0007,120m2,Olomouc,ul.Dvořákova,
byt0004,90m2,Olomouc,ul.Dvořákova,
byt0004,86m2,Olomouc,ul.Nová Ulice,
byt0003,75m2,Olomouc,ul.Nešverova,
byt0001,45m2,Olomouc,ul.Zirmova,
byt0006,114m2,Olomouc,ul.Přichystalová,
'''
```

## Zacneme s ulohou
<p align="center">
  <img src="https://media.giphy.com/media/1pAeSRT0jM7KxY3J4r/giphy.gif" width="480" height="270">
</p>

Vytvorime si v nasem pracovnim adresari novy soubor a do nej vlozime
[udaje](#co-budeme-potrebovat) na zacatek.
```python
#!/usr/bin/python3
"""Lekce #06 - Uvod do programovani, Uprav udaje"""

UDAJE = """
    ...
```

## Jak prevadet
Nejprve musime stanovit pravidla, na zaklade kterych budeme chtit zadany text
upravit.
```python
PREVOD_UDAJU = {
    "byt0001": "1+1",
    "byt0002": "2+1",
    "byt0003": "2+kk",
    "byt0004": "3+1",
    "byt0005": "3+kk",
    "byt0006": "4+1",
    "byt0007": "4+kk",
}
```
Tuto promennou take pouzijeme v nasem kodu.

## Vlastni funkce
Nez je zacneme vubec pouzivat, pojdme si rict, co to _funkce_ vubec je. V
Pythonu je funkce kus kodu, jehoz zamerem je provest jednu souvislou akci, ukol.
Umoznuji pouzivat kus kodu opakovane, na ruznych mistech a tim zachovavaji
vysokou uroven citelnosti kodu.

### Jake mame funkce
Mozna si rikate, ze jsme uz o funkcich mluvili. Python obsahuje
celou sadu
[zabudovanych funkci](https://docs.python.org/3/library/functions.html)
se kterymi jsme se jiz seznamili a jeste se seznamime.

1. __print()__
2. __input()__
3. __sum()__
4. __sorted()__

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
Mame __definovanou__ funkci, ted ji staci jen __pouzit__.

Funkci pouzijeme tak, ze zapiseme jeji jmeno a odpovidajici pocet vstupnich
promennych. Casto pri pouzivani funkce mluvime o jejich _zavolani_. Zavolani
muzete videt na radcich nize:
```
umocnovani(2, 5)  # 32
```
Pokud bychom chteli tuto hodnotu ulozit, musim vracenou hodnotu z funkce schovat
do nejake promenne:
```python
vysledek = umocnovani(2, 5)
print(vysledek)  # 32
```
V nasem priklade chceme provest nasledujici:
```
"byt 0001" -> funkce: preved_test -> "1+1"
```

### Doplnime zapis
Zatim zkusime definovat jednoduchou funkci, podle vzoru
[vyse](#nase-prvni-funkce). Pokud bude vstupem `byt 0001` chceme z funkce
vratit `1+1`. Pokud bude vstupem cokoliv jineho, chceme vratit `Neplatny udaj`.
```python
def prevadec(typ_bytu: str) -> str:
    if typ_bytu == "byt0001":
        return "1+1"
    else:
        return "NEZNAMY TYP BYTU!"
```

## Spojime nas kod
V tomto okamziku jsme v pozici, kdy mame __upravujici funkci__ a
__vstupni udaje__. Musime proto tyto dve casti propojit. Zadany text je retezec,
a proto jej musime upravit, nez jej budeme pouzivat ve funkci.

### Rozdelime text
Vidime, ze kus textu, ktery potrebujeme, je na kazdem radku:
```
...
byt0003,42 m2,Olomouc,ul.Nešverova,
byt0002,55 m2,Olomouc,ul.Dělnická,
byt0004,59 m2,Olomouc,ul.Zirmova,
byt0007,92 m2,Olomouc,ul.Nová Ulice,
byt0002,52 m2,Olomouc,ul.Nová Ulice,
...
```
Prvnim krokem bude rozdelit text na retezce po jednotlivych radcich.
```python
for radek in UDAJE.split("\n"):
    print(radek)
```

Ve vystupu si muzete vsimnout, ze prvni a posledni radek jsou prazdne. Tomu
se chceme vyhnout do budoucna. Jak to provedeme?
```python
...
    if radek != "":
        print(radek)
```
Staci pouze doplnit podminku. Pri nasem rozdelovani metodou __split()__ dojde k
rozdeleni i na zacatku a na konci, kde se nachazi symboly pro novy radek. Proto
mame ve vyslednem textu prazdne radky v uvodu a zaveru.

Posledni casti v nasem kodu bude rozdelene radky pridat do libovolneho datoveho
typu, ktery se nam hodi nejvice.
```python
vysledky = []

for radek in UDAJE.split("\n"):
    if radek != "":
        vysledky.append(radek)
```

## Prirazovani vice promennych
Ve druhe casti, budeme potrebovat ziskat oznaceni bytu. Tedy prvni cast radku:
```
...
byt0003,... ,
byt0002,... ,
byt0004,... ,
byt0007,... ,
byt0002,... ,
...
```
Co budeme muset zmenit?

### Jednoduche prirazeni promenne
Pomoci znamenka __=__ vytvorim cestu do pameti pocitace. Takze promenna potom
funguje jako nejaky ukazatel.

__Priklad__:
```
JMENO = "Matous"
```
### Vicenasobne prirazeni
Neni nutne prirazovat na jednom radku hodnotu pouze jedne promenne. Pro takove
pripady existuje specialni zapis:
```
JMENO1, JMENO2 = "Matous", "Lucie"
print(JMENO1)  # "Matous"
print(JMENO2)  # "Lucie"
```
Python si v podstate na pozadi udela z jmen promennych tuple. Potom k sobe
zacne parovat jednotlive promenne se stejnym indexem.

Ale __opatrne__:
```python
STREDNI_ROD = ("mesto", "more", "kure", "staveni")
v1, v2, v3, v4, v5 = STREDNI_ROD  # ValueError
```

### Rozdelime radek
Kdyz uz tusime jak na to, pojdme si to vyzkouset. Uvnitr smycky, kterou jsme
vytvorili v prvni casti chceme rozdelit promenne:
1.  __oznaceni_bytu__,
2. __plocha__,
3. __mesto__,
4. __ulice__
```python
for radek in UDAJE.split("\n"):
    if radek != "":
        oznaceni_bytu, plocha, mesto, ulice = radek.split(",", maxsplit=3)
```

### Potrebujeme zbytek?
Je opravdu nutne rozdelovat text na tolik oddilu, kdyz prakticky potrebujeme
pouze __oznaceni__. Pomoci rozbalovaciho operatoru __*__ si muzeme usetrit
vypisovani.
```
STREDNI_ROD = ("mesto", "more", "kure", "staveni")
v1, *zbytek = STREDNI_ROD
print(zbytek)  # ["more", "kure", "staveni"]
```
Uz jsme si o vyuziti tohoto symbolu nekolikrat povidali. Jejim dalsim vyuzitim
muzeme [rozbalovat](#dulezite-odkazy) datove typy jako seznamy a tuply.
```python
for radek in UDAJE.split("\n"):
    if radek != "":
        oznaceni_bytu, *zbytek_dat = radek.split(",", maxsplit=1)
    ...
```

## Zavolame nasi funkci
Nyni, kdyz jsme schopni extrahovat oznaceni bytu (promenna `ozn`), muzeme
pouzit nasi funkci! Abych ji pouzili, musime ji __zavolat__. 

### Ale kdy volat?
Musime najit vhodne misto, kde funkci pouzit. Pomoc k vyreseni teto otazky muze
byt vstup do funkce, tzv. _parametr_:
```python
def jmeno_funkce(parametr) -> None:
    ...
```
Pokud funkci definujeme, do zavorky zadavame __parametry__ funkce. Pokud ale
funkci zavolame (tedy pouzivame), do kulate zavorky jiz zapisujeme _argument_.
Tedy skutecnou promennou, kterou budeme pouzivat uvnitr funkce.

Proto bude vhodne funkci zavolat, az promennou `ozn` vytvorime:
```python
for radek in UDAJE.split("\n"):
    if radek != "":
            oznaceni_bytu, *zbytek_dat = radek.split(",", maxsplit=1)
            upraveny_typ = prevadec(oznaceni_bytu)
            ...
```
Jelikoz ve funkci `prevadec` pouzivame `return`, musime hodnotu vracenou z
funkce ulozit do nejake promenne.

## Doplnime scitani
Doplnime nasi funkci dalsi funkcionalitu. Zajistime, ze bude pocitat,
jednotlive upravy. Tedy, pokud dojde ze zmene, vrati 1 a pokud ne, vrati 0.

### Pocitadlo
Klasicky zapis pro pocitani ve smycce jsme si uz ukazovali:
```python
i = 73
i = i + 1
print(i)  # 74
```
### Zkraceny zapis
V Pythonu dale existuje forma [zkraceneho zapisu](#dulezite-odkazy). Neplati
pouze pro __scitani__ ale i pro dalsi operace (odcitani, nasobeni, aj.). Jde o
podobny proces, jako obycejne prirazeni, jenom misto vytvoreni noveho objektu
a jeho prirazeni k hodnote se zmeni stary objekt.
```python
i += 1; print(i)
75
```
### Doplneni funkce
Jaky udaj budeme pricitat pri pouziti funkce, nechame rozhodnout funkci
samotnou.
```python
def preved_udaj(vstup: str) -> str:
    if vstup == "byt0001":
        return "1+1", 1
    else:
        return "Neplatny udaj!", 0
...
```
`return` totiz muze vracet vice nez jeden udaj. V ukazce nam v tento okamzik
v obou variantach vraci tuple se dvema udaji. Jak je zapsat?
```python
vysledek = []
upravene = 0
neupravene = 0

for radek in UDAJE.split("\n"):
    if radek != "":
            ozn, *zbytek_dat = radek.split(",", maxsplit=1)
            upravene_typ, zmena = preved_udaj(ozn)
            upravene += zmena

    else:
        neupravene += 1
```

## Spojime udaje
Dalsim krokem bude spojeni noveho udaje (promenna `upraveny_typ`) a zbytku
radku (promenna `zbytek_dat`).

### Dalsi metoda?!
<p align="center">
  <img src="https://media.giphy.com/media/14ooolmDKfgrO8/giphy-downsized.gif" width="480" height="270">
</p>

Pokud potrebujeme spojit retezce, pak nam prijde vhod metoda retezcu _join()_.
```python
STREDNI_ROD = ("mesto", "more", "kure", "staveni")
", ".join(STREDNI_ROD)
```
Do uvozovek napisu, cim chci jednotlive udaje spojit a tesne za uvozovky
vlozim metodu s teckou. Do kulatych zavorek potom zapiseme promennou,
jejichz hodnoty chci spojovat.
```python
vysledky = []
upravene = 0
neupravene = 0

for radek in UDAJE.split("\n"):
    if radek != "":
            oznaceni_bytu, *zbytek_dat = radek.split(",", maxsplit=1)
            upraveny_typ, zmena = preved_udaj(ozn)
            upravene += zmena

            zbytek_dat = ",".join(zbytek_dat)
    else:
        neupravene += 1
```
V tuto chvili mame tedy pospojovane udaje z puvodniho seznamu `zbytek_dat`.

### A jeste jednou
Jakmile mame nove ulozenou promennou `zbytek_dat`, spojime tuto promennou a
promennou `udaj`.
```python
vysledky = []
upravene = 0
neupravene = 0

for radek in UDAJE.split("\n"):
    if radek != "":
            oznaceni_bytu, *zbytek_dat = radek.split(",", maxsplit=1)
            upraveny_typ, zmena = preved_udaj(ozn)
            upravene += zmena

            zbytek_dat = ",".join(zbytek_dat)
            vysledky.append(",".join((ozn, zbytek_dat)))
    else:
        neupravene += 1
```
Nyni mame zpet seznam, ktery obsahuje prevedene oznaceni do citelne podoby i
zbytek udaju na radku. Nicmene v zatim prevadime pouze jeden typ oznaceni.

## Rozsirime funkci
Abychom mohli opravovat vsechny typy bydleni, musime funkci ukazat nas slovnik
`PREVOD_UDAJU`. Takze jej vlozime jednak jako parametr, jednak jako argument.
```python
def prevadec(typ_bytu: str, vzor: dict) -> str:
    if typ_bytu in vzor:
        return vzor.get(typ_bytu), 1
    else:
        return "NEZNAMY TYP BYTU!", 0
```
V tuto chvili pomoci metody __get__ nahradime vsechny potencialni pripady, ktere
mohou nastat.

## Vracime vysledek
Posledni vec, kterou dopiseme bude podminka. Ta overi, jestli jsou prevedena
vsechna data a pokud ano, vypiseme je. Pokud nebude podminka splnena, vysledek
netiskneme.
```python
...
if upravene == len(UDAJE.split("\n")) - neupravene:
    from pprint import pprint
    pprint(vysledky)
else:
    print("POCET VSTUPNICH UDAJU A PREVEDENYCH UDAJE JE RUZNY!!")
```

Pokracovat na [Lekci#07](https://github.com/Bralor/python-academy/tree/lekce07)

