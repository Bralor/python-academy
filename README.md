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

## Dnesni ukol
V dnesni lekci se budeme bavit o potencialnich chybach uvnitr naseho kodu. Kdy
se mohou objevit, co znamenaji a jak s nimi pracovat. V bodech:
1. __Typy__ chyb
2. __Vyjimky__
3. __try/except__
4. __Debuggovani__

## Zkontroluj vstupni data
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

## Co s nimi?
1. Syntakticke chyby je nutne odstranit --> debugovat
2. Logicke chyby (+ behove chyby) je mozne hlidat --> error handling

## Vyjimka
Nicmene s chybami se pocita, a proto je s nimi v Pythonu zachazeno jako s
nejakymi objekty. Programatori jsou casto presvedceni, ze v jejich programech
se chyba objevi jen zridka, tudiz je hromadne oznacuji jako __vyjimky__. Vyjimka
je opet nejaky situace, ktera nastane, pokud se pri vykonavani programu objevi
nejaka chyba a nebo je nejaka cast zkratka podezrela (warning).

## Zachazeni s chybami
S logickymi chybami si lze poradit. Na celou operaci existuje opet presne
popsana skladba, kterou muzeme odchytavat jednotlive chyby, nebo skupinu chyb.

Teorie:
```
try:
    <neco_co_chceme_vyzkouset>

except <jmeno_vyjimky>:
    <toto_se_stane_pokud_dostaneme_vyjimku>
```

Priklad:
```
def input_int() -> int:
    while True:
        try:
            x = int(input("VLOZTE CELE CISLO: "))
            break
        except ValueError:
            print("Neni cele cislo, zkuste znovu...")
    return x

print(f"\nZADALI JSTE CISLO: {input_int()} ")
```

## Vice vetvi *except*
Chyby muzeme specifikovat pomoci vice vyjimek (pripadne doplnit/zkratit aliasem)

Priklad:
```
try:
    <neco_co_chceme_vyzkouset>

except <jmeno_vyjimky1>:
    <toto_se_stane_pokud_dostaneme_vyjimku1>

except <jmeno_vyjimky2>:
    <toto_se_stane_pokud_dostaneme_vyjimku2>
```

## Vetev *else*
Pokud nedojde k vyhodnoceni ve vetvi _try_ s vyjimkou. Proved vetev *else*

Priklad:
```
try:
    <neco_co_chceme_vyzkouset>

except <jmeno_vyjimky1>:
    <toto_se_stane_pokud_dostaneme_vyjimku1>

except <jmeno_vyjimky2>:
    <toto_se_stane_pokud_dostaneme_vyjimku2>

else:
    <toto_proved_pokud_nedostaneme_vyjimku>
```

## Vetev *finally*
At uz vyhodnoceni bude s vyjimkou ci bez ni, proved to, co obsahuje vetev *finally*.

Priklad:
```
try:
    <neco_co_chceme_vyzkouset>

except <jmeno_vyjimky>:
    <toto_se_stane_pokud_dostaneme_vyjimku>

finally:
    <toto_proved_pokazde>
```
