Minula [lekce#08](https://github.com/Bralor/python-academy/tree/lekce08)

<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lesson 09
## Dulezite odkazy
- Portal [Engeto.com](https://engeto.com/)
- Python Academy [repozitar](https://github.com/Bralor/python-academy)
- [Anotace](https://www.python.org/dev/peps/pep-3107/) v Pythonu
- [Generator](https://mockaroo.com/) nahodnych dat (testovacich dat)
- Oficialni [dokumentace pdb](https://docs.python.org/3/library/pdb.html?highlight=pdb)

## Dnesni ukol
V dnesni lekci se budeme bavit o potencialnich chybach uvnitr naseho kodu. Kdy
se mohou objevit, co znamenaji a jak s nimi pracovat. V bodech:
1. __Typy__ chyb
2. __Vyjimky__
3. __try/except__
4. __Debuggovani__

## Zkontroluj vstupni data #1
Nas dnesni program bude mit za ukol kontrolat datove typy, ktere do nej nacteme.
Budeme chtit vedet, jestli vstupni udaje obsahuji pouze hodnoty, ktere lze
prevadet na celociselne udaje (integer), prip. jestli data neobsahuji nejake
nezadouci typy (nelze prevest na integer).

## Ukazka na uvod
Spustime skript v tomto adresari:
```python
$ ./kontrola_udaju 
```
A dostaneme nasledujici vystup:
```
781523 --> OK, pokracuji...
---------------------------------------
240598 --> OK, pokracuji...
---------------------------------------
799662 --> OK, pokracuji...
---------------------------------------
NEKONVERTOVATELNE --> mmnnoo, ValueError
---------------------------------------
503937 --> OK, pokracuji...
---------------------------------------
268824 --> OK, pokracuji...
---------------------------------------
...
```

## Co budeme potrebovat?
- Python 3.6+
- text. editor/IDE
- soubor __cisla.txt__
- [while smycky](https://github.com/Bralor/python-academy/tree/lekce04)
- [for smycky](https://github.com/Bralor/python-academy/tree/lekce05)
- [funkce v Pythonu](https://github.com/Bralor/python_academy/tree/lekce06)
- [prace s text. soubory](https://github.com/Bralor/python_academy/tree/lekce08)

## Zacneme s ulohou

<p align="center">
  <img src="https://media.giphy.com/media/idouiA9eH3Ad0pj3ci/giphy.gif" width="480" height="270">
</p>

## Chyby v Pythonu
Chyby udela prakticky kazdy. Mohou zpusobit selhani naseho programu nebo
minimalne nebude fungovat tak, jak ocekavame.

## Jake mame chyby?
Nejprve je vhodne udelat se v tom vsem poradek:

### Syntakticke chyby
Jde o prohresek proti pravidlum skladebnich predpisu jazyka Python.
```python
def scitac-a,b:
    return a + b
```
Prohresek je jasny. Definoval jsem funkci spatnym zpusobem. Spravne ma syntaxe
vypadat nasledovne:
```python
def scitac(a: int, b: int) -> int:
    return a + b
```

### Behove chyby
Chyby, ktere se projevi az pri prekladani naseho kodu (delim nulou, pouzivam
neco, co jeste neexistuje).
```python
def vrat_polovinu(cislo: int) -> float:
    return float(cislo / 2)
```
Kratka funkce, ktera vrati polovinu z hodnoty, ktera do funkce vstupuje:
```python
cisla = (1, 5)
cisla = (1, 5, 8, 9, 10, 22)
cisla = (1, 5, 8, 9, 10, 22, "a", 50)

for cislo in cisla:
    vrat_polovinu(cislo)
```
Vidim, ze pro prvni dva tuply funkce splnuje nase ocekavani. Ale u tretiho
tuplu nastane neocekavana situace. V prubehu dojde k selhani.

### Logicke chyby
Kod funguje, ale jinak, nez ocekavame.
```python
x = 3
y = 5

prumer = x + y / 2
```
Pokud chceme ziskat spravnou hodnotu, musime vlozit scitance do zavorek.

## Souhrn
Pokud tedy resime __typ__ chyb, bavime se o:
1. Syntakticke chyby
2. Behova chyby
3. Logicke chyby

## Zacneme s ukolem
Opet si do pracovniho adresare nakopirujeme soubor s hodnotami:
```
cisla.txt
```
Dale vytvorime novy soubor:
```
kontrola_cisel.py
```
Na uvod muzeme doplnit nekolik udaju, se kterymi zacneme pracovat:
```python
#!usr/bin/python3
"""Lekce #9 - Uvod do programovani, kontrola cisel"""

def hlavni() -> None:
    pass


hlavni()
```

## Co dal?
Udaje mame v externim souboru, takze prvni krok je jeho nacteni:
```python
def hlavni() -> None:
    # otevrit soubor a nacist udaje uvnitr
    ...
```
Vytvorime funkci `nacitani_udaju()`, ktera bude mit na starost tyto body:
1. __Otevreni__ souboru
2. __Precteni__ obsahu
3. __Zavreni__
```python
def nacitani_udaju(soubor: str, rezim="r") -> str:
    with open(soubor, rezim) as txt:
        return txt.readlines()
```
Nezapomenme doplnit volani tento funkce, to funkce `hlavni()`.

## Prevadime..
Udaje mame nactene, takze je muzeme upravit a ulozit jako `int`:
```python
def hlavni() -> None:
    nactene_udaje = nacitani_udaju("cisla.txt")
    # prevest na 'int'
    ...
```
Nejprve nase funkce, ktera to bude mit cele na starost:
```python
def preved_udaje(data: list) -> None:
    prevedeno = set()

    for udaj in data:
        udaj = udaj.strip()
        prevedeno.add(int(udaj))
        print(f"PREVEDENO: {udaj}")

    return prevedeno
```
Pote jeste zavolat prave vytvorenou funkci:
```python
def hlavni() -> None:
    nactene_udaje = nacitani_udaju("cisla.txt")
    preved_udaje(nactene_udaje)
```

## Pojdme cely proces vyzkouset
Vidime, ze kus kodu probehl jak mel. Ale v jistem bode nas kode zkolaboval.
Pote vratil vyjimku pojmenovanou `ValueError`. Muzeme s jistotou rict, ze
program chvili bezel, ale uprostred behu selhal. S jakym typem chyby jsme
se setkali?

## Co s tim?
1. Syntakticke chyby je nutne odstranit --> __debugovat__
2. Logicke chyby (+ behove chyby) je mozne hlidat --> __error handling__

## Error handling
Neboli jak s chybami __zachazet__. S chybami se pocita, a proto je s nimi
v Pythonu zachazeno jako s nejakymi objekty. Programatori jsou casto
presvedceni, ze v jejich programech se chyba objevi jen zridka, tudiz je
hromadne oznacuji jako __vyjimky__. Vyjimka je opet nejaky situace, ktera
nastane, pokud se pri vykonavani programu objevi nejaka chyba a nebo je nejaka
cast zkratka podezrela (warning).

### Zachazeni s chybami
S logickymi chybami si lze poradit. Na celou operaci existuje opet presne
popsana skladba, kterou muzeme odchytavat jednotlive chyby, nebo skupinu chyb.
```python
try:
    <neco_co_chceme_vyzkouset>

except <jmeno_vyjimky>:
    <toto_se_stane_pokud_dostaneme_vyjimku>
```
Vic si ukazeme na prakticke ukazce:
```python
def vloz_cislo() -> int:
    try:
        x = int(input("VLOZTE CELE CISLO: "))
        return x

    except ValueError:
        print("NENI MOZNE PREVEST NA INT")
```
Pokud uzivatek vlozi jiny datovy typ nez takovy, ktery jde prevest na
celociselny typ `integer`, vrati se nam vypis z bloku `except`.

### Vice moznosti
Chyby muzeme specifikovat pomoci vice vyjimek:
```python
try:
    <neco_co_chceme_vyzkouset>

except <jmeno_vyjimky1>:
    <toto_se_stane_pokud_dostaneme_vyjimku1>
```
Pokud mame vice vyjimek, ktere mohou nastat, staci je pripsat:
```python
except <jmeno_vyjimky2>:
    <toto_se_stane_pokud_dostaneme_vyjimku2>
```
Pokud nedojde k vyhodnoceni ve vetvi __try__ s vyjimkou, proved vetev __else__:
```python
else:
    <toto_proved_pokud_nedostaneme_vyjimku>
```
At uz vyhodnoceni bude s vyjimkou ci bez ni, proved to, co obsahuje vetev
__finally__.
```python
finally:
    <toto_proved_pokazde>
```
### Vysledek
Takze cela procedura pro overeni muze vypadat nasledovne:
```python
try:
    <neco_co_chceme_vyzkouset>

except <jmeno_vyjimky1>:
    <toto_se_stane_pokud_dostaneme_vyjimku1>

except <jmeno_vyjimky2>:
    <toto_se_stane_pokud_dostaneme_vyjimku2>

else:
    <toto_proved_pokud_nedostaneme_vyjimku>

finally:
    <toto_proved_pokazde>
```

## Nyni vsechno aplikujeme
Dost prakticky nelze pouzit vetsinou vsechno. Ale my se nyni pokusime
zapsat kazdou vetev z `try/except/else/finally`:

### try/except
Nejprve proces, kdy chceme neco overit:
```python
    for udaj in data:
        try:
            udaj = int(udaj.strip())
```
Nyni doplnime vyjimku, ktera se nam v prubehu spusteni naseho programu
objevila:
```python
        except ValueError:
            print(f"NELZE PREVEST --> {udaj}")
```
V praxi je samozrejme mozne doplnit __vyjimek__ vice.

### else/finally
Doplnime __else__, tedy vetev, na kterou prijde rada, pokud __try__ nevyvodi
zadnou vyjimku:
```python
        else:
            print(f"{udaj} --> OK, POKRACUJI..")
            prevedeno.add(udaj)
```
Nakonec doplnime vetev s __finally__, ktera se spusti v kazdem pripade:
```python
        finally:
            print("-" * 39)
```
Nyni muzeme program opet spustit a meli bychom dostat vystup stejny, jako
v ukazce na uvod.

## Debuggovani
Predstavme si situaci. Nas vedouci nam zada ukol, zpracovat textovy soubor s
udaji. Chceme jej cely projit a naformatovat vystup jako `Udaj1, Udaj2, ...`
(pocatecni pismeno velke, zbytek malym pismem a oba udaje oddelene carkou).
Udaju je hromada a rekne, ze jakmile dojdeme po vyraz `quit`, chceme hledani
ukoncit.

## Ukazka druha
Spustime druhy soubor:
```
$ ./kontrola_mest
```
Jakmile spustime druhy soubor, chceme vystup zakonceny nasledovne:
```
...
Vatican City,Vatican City
Venezuela,Caracas
Vietnam,Hanoi
Yemen,Sana'A
Zambia,Lusaka
Zimbabwe,Harare
```

## Druhy ukol
Nejprve si sepsat strukturu naseho kodu. Tedy jednotlive body, co by mel kod
delat:
```python
# nacist udaje ze souboru
# projit vsechny udaje
# u kazdeho provest zmenu
```
Prakticky uvod muze vypadat nasledovne:
```python
def nacti_soubor(soubor: str, mod: str = "r") -> list:
    # nacist udaje ze souboru

def prepis_udaje(nacteny_soubor: list) -> None:
    # cyklus
        # zmena udaje
```
Vsechno potom dusledne zavolat a spustit.

## Dopiseme zadani
Uz zname princip `try/except`, takze jej rovnou pouzijeme:
```python
def nacti_soubor(soubor: str, mod: str = "r") -> list:
    try:
        with open(soubor, mod) as txt:
            obsah = txt.readlines()
        return obsah

    except FileNotFoundError:
        print("SOUBOR NELZE NAJIT")
```
K tomy dopiseme funkci `prepis_udaje()`, ktera bude prochazet radek po radku
a kazdy udaj v nasi promenne `obsah` rozdeli do novych promennych `zeme` a
`mesto`. Nakonec je vypiseme s velkym pocatecnim pismenem.
```python
def prepis_udaje(nacteny_soubor: list) -> None:
    for udaj in nacteny_soubor:
        try:
            udaj = udaj.strip()
        except AttributeError:
            print(f"NELZE STRIPOVAT TYP {type(udaj)}")
        else:
            if "quit" in udaj.lower():
                return
            zeme, mesto = udaj.split(",")
            mesto = mesto.strip()
            zeme = zeme.strip()

            print(zeme.title(), mesto.title(), sep=",")
```
Obe funkce pak zavolame. Treba v ridici funkci `main()`.

## Jak zacit s debuggovanim?
Nejlepsim zpusobem jak overit, jestli nas kod funguje jak ma, je spustit jej.
Cim vice ruznych variant spusteni vyzkousim, tim mene chyb objevime pozdeji.
Presto se muze stat, ze vsechny moznosti dostatecne neosetrime.

## print()/vars()
Nejjednodusi zpusobem, kterym zacit je vypisovat konkretni vystupy pomoci
funkce `print()`. Dalsi moznosti je zabudovana funkce `vars()`, ktera extrahuje
hodnoty nasich lokalnich promennych:
```python
def ukazka_vrs(*args) -> None:
    print(vars())
```
Nejprve zkusime nasi funkci `ukazka_vrs()` pro `1, 2, 3` a pote pro seznam
`["a", "b", "c"]`.

## pdb
Debugovat pomoci zabudovanych funkci muze byt napomocne, ale casto potrebujeme
silnejsi kalibr. Vetsina textovych editoru ma vlastni __debugger__. My si ale
povime neco o standartnim debuggeru pojmenovanem __pdb__.

## Spoustime Pdb
__Pdb__ je modul v pythonu, ktery nas pusti do interaktivniho prohlizece prubehu
naseho kodu. Spustime nas kod s __pdb__ nasledovne:
```
python3 -m pdb <jmeno_souboru>.py
```
Dostaneme se do interaktivniho profilu uvnitr terminalu:
```bash
> /home/matous/projects/python-academy/debugging_mesta.py(2)<module>()
-> """Lekce #10 - Uvod do programovani, debugging"""
(Pdb)
```

## Dostupne prikazy
Na uvod si muzeme vypsat napovedu:
```
(Pdb) ?
```
Pripadne specifickou napovedu pro prave vypsane prikazy:
```
(Pdb) ? step
```
Chceme prochazet nas kod krok za krokem, jak si jej bude spoustet interpret.
Takze pouzijeme `step`.

## Popojedeme
Co se stane behem prvnich kroku?
1. __Nactu__ definice
2. __Najdu__ volani
3. __Spustim__ funkci
4. __Spoustim__ obsah teto volane funkce

## Na co se zamerit?
Idealne na misto, ktere nasi funkci ukoncuje. Tedy posledni radek, nebo nejaka
podminka. Obvykle u `return` ohlaseni, pokud je k dispozici.
```python
    ...
            print(f"NELZE STRIPOVAT TYP {type(udaj)}")
        else:
            if "quit" in udaj.lower():
                return
            zeme, mesto = udaj.split(",")
    ...
```
V nasem kodu `return` mame, takze nastavime sledovani radku, na kterem se
klicove slovo nachazi.
```
(Pdb) b 22
```
Pomoci `b` nastavim tzv. _breakpoint_, coz je klicovy prvek modulu `pdb`, ktery
nam nastavi v kodu misto, na ktere pokud v prubehu kodu narazim, tak jej
zastavim.
```
(Pdb) c
```
Necham __pdb__ dal prochazet s prikazem `continue`, at dojde na konec, pripadne
k `breakpointu`.

## Zaznam
Meli bychom ziskat nasledujici vystup:
```
Denmark,Copenhagen
Djibouti,Djibouti (City)
Dominica,Roseau
Dominican Republic,Santo Domingo
> /home/matous/projects/python-academy/debugging_mesta.py(22)prepis_udaje()
-> return
```
Prubeh se zastavil na radku 22, na nasem `breakpointu`. Pojdme si vypsat obsah
promenne `udaj`:
```
(Pdb) p udaj
```
Ten by nam mohl aspon trochu objasnit, proc se spustila podminka predcasne:
```
(Pdb) p udaj
'ECUADOR, QUITO'
```
Cast vyrazu obsahuje __quit__. Tim padem neni mozne nase udaje proverit vsechny,
protoze funkce `prepis_udaje()` skonci predcasne. Takze se pustime do
opravovani.
```python
    ...
    if "quit" == udaj.lower():
        return
```
Ted by mel nas kod probehnout az do konce, jak jsme videli v
[ukazce](#-ukazka-druha).

## Zaverem
Ucelne se snazime psat vice testu a overovani, abychom debugovani predchazeli.
Pokud ale neni jina moznost, muze nam pomoci jedna z vyse zminenych metod:
1. __Spustit__ kod pro vice scenaru
2. __print()/vars()__
3. Modul __pdb__
4. Debugger v __ide__ (v PyCharm)

Pokracovat na [Lekci#10](https://github.com/Bralor/python-academy/tree/lekce10)

