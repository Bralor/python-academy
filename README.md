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
- [Built-in funkce](https://docs.python.org/3/library/functions.html)
- [Zkraceny zapis](https://docs.python.org/2.0/ref/augassign.html)
- Dalsi vyuziti [hvezdicky](https://note.nkmk.me/en/python-tuple-list-unpack/)

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
UDAJE = '''
byt0001,55m1,Olomouc,ul.Heyrovského,
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

1.__print()__
2.__input()__
3.__sum()__
4.__sorted()__

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
__umocnovani()__ a do kulate zavorky zadame dve vstupni hodnoty, jak rika jeji
popisek:
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
def preved_udaj(vstup: str) -> str:
    """'byt 0001' -> funkce: preved_test -> '1+1'"""
    return "1+1" if vstup == "byt 0001" else "Neplatny udaj!"
```

## Spojime nas kod
V tomto okamziku jsme v pozici, kdy mame upravujici funkci a vstupni udaje.
Musime proto tyto dve casti propojit. Zadany text je retezec, a proto jej
musime upravit, nez jej budeme pouzivat ve funkci.

### Rozdelime text
Vidime, ze kus textu, ktery potrebujeme, je na kazdem radku:
```
...
byt 0003,42 m2,Olomouc,ul.Nešverova,
byt 0002,55 m2,Olomouc,ul.Dělnická,
byt 0004,59 m2,Olomouc,ul.Zirmova,
byt 0007,92 m2,Olomouc,ul.Nová Ulice,
byt 0002,52 m2,Olomouc,ul.Nová Ulice,
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

Posledni casti v nasem kodu bude rozdele radky pridat do libovolneho datoveho
typu, ktery se nam hodi nejvice.
```python
jednotlive_udaje = []

for radek in UDAJE.split("\n"):
    if radek != "":
        jednotlive_udaje.append(radek)
```

## Prirazovani vice promennych
Ve druhe casti, budeme potrebovat ziskat oznaceni bytu. Tedy prvni cast radku:
```
...
byt 0003,... ,
byt 0002,... ,
byt 0004,... ,
byt 0007,... ,
byt 0002,... ,
...
```
Co budeme muset zmenit?

### Jednoduche prirazeni promenne
Pomoci znamenka *=* vytvorim cestu do pameti pocitace. Takze promenna potom
funguje jako nejaky ukazatel/odkaz.

__Priklad__:
```
JMENO = "Matous"
```
### Vicenasobne prirazeni
Neni nutne prirazovat na jednom radku pouze jedne promenne. Pro takove pripady
existuje specialni zapis:
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
1.  __oznaceni__,
2. __plocha__,
3. __mesto__,
4. __ulice__
```python
    ...
    if radek != "":
        ozn, plocha, mesto, ulice = radek.split(",", maxsplit=3)
```

### Potrebujeme zbytek?
Jiste jste si polozili otazku, jestli je opravdu nutne, rozdelovat text na
tolik oddilu, kdyz prakticky potrebujeme pouze __oznaceni__. Pomoci
rozbalovaciho operatoru _*_ si muzeme usetrit vypisovani.
```
STREDNI_ROD = ("mesto", "more", "kure", "staveni")
v1, *zbytek = STREDNI_ROD
print(zbytek)  # ["more", "kure", "staveni"]
```
Uz jsme si o vyuziti tohoto symbolu nekolikrat povidali. Jejim dalsim vyuzitim
muzeme [rozbalovat](#dulezite-odkazy) datove typy jako seznamy a tuply.
```python
    ...
    ozn, *zbytek_dat = radek.split(",", maxsplit=1)
    ...
```

## Overime pocet
Kazdy udaj, ktery bude prevedeny na novy format zapisu chceme evidovat. V
podstate overime, ze pocet udaju, ktere jsme na zacatku meli, sedi s poctem
uprav.

### Pocitadlo
Klasicky zapis pro pocitani ve smycce jsme si uz ukazovali:
```python
i = 73
i = i + 1
print(i)  # 74
```
### Zkraceny zapis
V Pythonu dale existuje forma [zkraceneho zapisu](#dulezite-odkazy). Neplati
pouze pro _scitani_ ale i pro dalsi operace (odcitani, nasobeni, aj.). Jde o
podobny proces, jako obycejne prirazeni, jenom misto vytvoreni noveho objektu
a jeho prirazeni k hodnote se zmeni stary objekt.
```python
i += 1; print(i)
75
```

## Zavolame nasi funkci
Nyni, kdyz jsme schopni extrahovat oznaceni bytu (promenna __ozn__), muzeme
pouzit nasi funkci! Jak jsem v uvodu naznacil, abychom definovanou funkci mohli
pouzit, musime ji _zavolat_.

### Ale kdy volat?
Musime najit vhodne misto, kde funkci pouzit/zavolat. Pomoc k vyreseni teto
otazky muze byt vstup do funkce, tzv. _parametr_:
```python
def jmeno_funkce(parametr) -> None:
    ...
```
Vsimneme si, ze jako parametr si do funkce prejeme vkladat jednotliva oznaceni.
Proto bude vhodne funkci zavolat, az promennou __ozn__ definujeme.
```python
    ... 
    if radek != "":
            ozn, *zbytek_dat = radek.split(",", maxsplit=1)
            upravene = prevadec(ozn)
            ...
```
Jelikoz ve funkci __prevadec__ pouzivame __return__, musime hodnotu vracenou z
funkce ulozit do nejake promenne.

### Doplnime scitani
Doplnime nasi funkci dalsi funkcionalitu. Zajistime, ze bude pocitat,
jednotlive upravy. Tedy, pokud dojde ze zmene, vrati 1 a pokud ne, vrati 0.
```python
...
    return ("1+1", 1) if vstup == "byt 0001" else ("Nic", 0)
    ...
```
Funkce nam v tento okamzik v obou variantach vraci tupl se dvema udaji. Proto
budeme muset upravit i zapisovani techto hodnot do promennych.
```python
        ...
        udaj, pocet = prevadec(ozn)
        upravene += pocet
        ...
```

## Spojime udaje
V tento moment vsechno bezi jak na dratkach. Dalsim krokem bude spojeni noveho
udaje a zbytku radku (promenna __zbytek_dat__).

### Dalsi metoda?!
Ano, pokud potrebujeme spojit retezce, pak nam prijde vhod metoda retezcu
_join()_. Jak ji ale pouzivat:
```python
STREDNI_ROD = ("mesto", "more", "kure", "staveni")
", ".join(STREDNI_ROD)
```
Do uvozovek napisu, cim chci jednotlive udaje spojit a tesne za uvozovky
nalepim metodu pomoci tecky. Do kulatych zavorek potom zapiseme promennou,
jejichz hodnoty chci spojovat.
```python
        ...
        zbytek_dat = ",".join(zbytek_dat)
        ...
```
V tuto chvili mame tedy pospojovane udaje z puvodniho __zbytek_dat__.

### A jeste jednou
Jakmile mame nove ulozenou promennou __zbytek_dat__, spojime tuto promennou a
promennou __udaj__.
```python
        ...
        jednotlive_udaje.append(",".join((udaj, zbytek_dat)))
        ...
```
Nyni mame zpet seznam, ktery obsahuje prevedene oznaceni do citelne podoby i
zbytek udaju na radku. Nicmene v zatim prevadime pouze jeden typ oznaceni.

## Rozsirime funkci
Abychom mohli opravovat vsechny typy bydleni, musime funkci ukazat nas slovnik
__PREVOD_UDAJU__. Takze jej vlozime jako argument, do volani funkce a soucasne
mu nachystame promennou do definice funkce.
```python
def prevadec(vstup: str, prevodnik: dict) -> tuple:
    return (prevodnik.get(vstup, None), 1) if vstup in prevodnik else (None, 0)
```
V tuto chvili pomoci metody __get__ nahradime vsechny potencialni pripady, ktere
mohou nastat.

## Vracime vysledek
Posledni vec, kterou dopiseme bude podminka. Ta overi, jestli jsou prevedena
vsechna data a pokud ano, vypiseme je. Pokud nebude podminka splnena, vysledek
netiskneme.
```python
...
if upravene == len(UDAJE.split("\n")) - 2:
    print(jednotlive_udaje)
else:
    print("Prevod neprobehl uspesne. Zkontroluj udaje!")

```

Pokracovat na [Lekci#07](https://github.com/Bralor/python-academy/tree/lekce07)

