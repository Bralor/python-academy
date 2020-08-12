Minula [lekce#07](https://github.com/Bralor/python-academy/tree/lekce07)

<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lesson 08
## Dulezite odkazy
- Portal [Engeto.com](https://engeto.com/)
- Python Academy [repozitar](https://github.com/Bralor/python-academy)
- [Anotace](https://www.python.org/dev/peps/pep-3107/) v Pythonu
- Generator [nahodnych slov](https://randomwordgenerator.com/) (max. 50)
- [Formatovani](https://realpython.com/python-string-formatting/) retezcu

## Co nas dneska ceka?
Hlavnim cilem dnesni lekce bude prace s __textovymi soubory__ pomoci Pythonu.
Dale si povime neco vic k __formatovani retezcu__. Tuto problematiku jsme
jiz castecne nacnuli, ale dneska zabrousime do detailu. V bodech:
1. Prace s .txt soubory
2. Kontextovy manazer
3. Formatovaci vyraz
4. Formatovaci metoda
5. f-strings

## Obesenec
Dalsim ukolem bude napsat v Pythonu hru v prikazovem radku. Hra se jmenuje
__obesenec__. Opet se budeme snazit aplikovat maximum z nove ziskanych
teoretickych znalosti.

## Ukazka na zacatek
Spustime skript v nasem adresari:
```
$ ./obesenec
```
Vystup muzeme vypadat nasledovne:
```
KOD
```

## Co budeme potrebovat?
- python 3.6.9+
- text. editor
- while smycky
- for smycky
- funkce v Pythonu

## Co nejdriv?

<p align="center">
  <img src="https://media.giphy.com/media/i34oXbluCO0G4/giphy-downsized.gif" width="300" height="300">
</p>

## Otevreme novy soubor
Otevreme pracovni adresar pro dnesni lekci a nakopirujeme do nej soubor se
slovy (`slova.txt`). Potom klasicky vytvorime soubor, kam budeme zapisovat nasi
hru (__obesenec__).
```python
#!/usr/bin/python3
"""Lekce #8 - Uvod do programovani, obesenec"""
```

## Ridici funkce
Aplikujeme podobnou mechaniku jako v minule lekci, tedy na zacatek vytvorime
hlavni ridici funkci `main()`.
```python
def main() -> None:
    "Hlavni ridici funkce nasi hry"
```
Nez zavolame hlavni funkci, zkusime si predstavit jednotlive kroky nasi hry,
ktere budou zapotrebi.
```python
def main() -> None:
    "Hlavni ridici funkce nasi hry"
    print("Pridavam hrace")
    print("Vybirame slovo")
    print("Schovavam slovo")

    i = 1

    while i < 5:  # apple
        print(f"Kolo: {i}")
        i += 1
    else:
        print("Konec hry!")

main()
```
Nakonec nasi hlavni funkci `main()` s jednotlivymi `print()` funkcemi spustime.
Kdyz se podivame na aktualni kod, muzeme rict, ze co `print()`, to jedna dilci
funkce.

## Pridame hrace
Prvni funkce bude obstaravat jmeno hrace:
```python
def pridej_hrace() -> str:
    return input("ZADEJTE JMENO HRACE: ")
```
A nasledne volani teto funkce z nasi hlavni funkce `main()`:
```python
def main() -> None:
    "Hlavni ridici funkce nasi hry"
    hrac = pridej_hrace()
    print("Vybirame slovo")
    print("Schovavam slovo")

    i = 1

    while i < 5:  # apple
        print(f"Kolo: {i}")
        i += 1
    else:
        print("Konec hry!")
```
Tim mame jmeno hrace ulozene v promenne `hrac` a muzeme jej pouzit pozdeji.

## Vybirame slovo
Doted jsme udaje schovavali v retezcich, tuplech, seznamech, aj. Dnes si
ukazeme jak muzeme hodnoty ziskat i z textovych souboru pomoci Pythonu.

### Prace se soubory
Abychom mohli s textovymi soubory pracovat, musime je nejprve
[otevrit](https://docs.python.org/3/library/functions.html#open):
```
moje_slova = open("slova.txt", "r")
```
Jelikoz se nachazime v adresari, kde tento soubor (__slova.txt__) skutecne mame,
muzeme jeho obsah otevrit. Dale si vsimnete `"r"`, ktery symbolizuje spusteni
rezimu pro cteni.

### Cteme udaje
Ted mame soubor nacteny, potrebujeme jej precist:
```
obsah_txt = moje_slova.read()
```
Pomoci metody `read()` si muzeme precist cely obsah souboru. Ted si muzeme
vypsat promennou `obsah_txt`:
```
'arrival\neffort\nfact\nanxiety\nhousing...
```
Vidime, ze jsem dostal ponekud nerozdeleny retezec. Pokud vime, ze jsou udaje
umistene na radcich pod sebou, muzeme zkusit metodu `readlines()`:
```
muj_txt.close()
muj_txt = open("slova.txt", "r")
obsah = muj_txt.readlines()
print(obsah)
```
Po kazdem zpracovani textu je nutne nacteny soubor ukoncit pomoci metody
`close()`, aby nam nezustal v pameti.

### Opatrne
Pokud precteme obsah souboru pomoci `read()`/`readlines()`, pomyslny kurzor
ukazujici aktualni polohu v textovem souboru se presune na posledni pozici.
Takze pri dalsim cteni, ziskame prazdny retezec nebo seznam:
```
obsah = muj_txt.readlines()
print(obsah)
[]
```
Kurzor muzeme posunout pomoci prikazu `seek()`, kdy do kulate zavorky nastavime
pozici, na ktere jej chceme nastavit:
1. __seek(0)__ - pro zacatek souboru
2. __seek(0, 2)__ - pro konec souboru

Pokud potrebuji zjistit, kde se v souboru aktualne nachazim, pouziju metodu
`tell()`.

### Kontextovy manazer
Je zapis s klicovym slovem `with` na zacatku definice. Je dobry prave kvuli
svoji syntaxi:
1. __otevri__ objekt
2. __zpracuj__ jej
3. __zavri__ objekt
Takze pri nasi manipulaci se souborem nemusime myslet na to, jestli jsme jej
ukoncili nebo ne:
```
with open("slova.txt", "r") as muj_txt:
    obsah_txt = muj_txt.readlines()
```
Zapis je kratsi a soucasne neztrati na citelnosti. Doplnime nyni nasi funkci
pro vyber slova:
```python
def vyber_slovo(soubor) -> str:
    with open(soubor, "r") as txt:
        slova = txt.readlines()
    return slova[0].strip()
```
Dalsim krokem bude vybrane slovo ulozit do promenne a vypsat si jej:
```python
    ...
    vybrane_slovo = vyber_slovo("slova.txt")
    print(f"HLEDANE SLOVO: {vybrane_slovo}")
    ...
```
Jak ale muzeme zajistit, abychom pokazde vybrali nahodne slovo?

## Modul random
Na moduly a jejich vyuziti jeste rec prijde. Nam ted staci pouze vyuziti
jednoho:
```python
def vyber_slovo(soubor) -> str:
    import random
    with open(soubor, "r") as txt:
        slova = txt.readlines()
    return random.choice(slova).strip()
```
Klicovyum slovem `import` oznamim interpretu, ze potrebuji nahrat modul
`random`. Nakonec pri vraci pouziju metodu `choice()`, kterou zajistim, ze si
vyberu pseudonahodny retezec z puvodniho seznamu `slova`. Opatrne presuneme
`strip()`, abychom jej aplikovali na retezec, ne seznam.

## Schovani slova
Jakmile je slovo vybrane, musime jej pro uzivatele schovat. Zvolime si akorat
symbol, ktery se bude zobrazovat misto jednotlivych slov:
```python
def schovej_slovo(slovo: str) -> list:
    "Nahradime pismena symbolem `_` a soucasne vypocitame pokusy"
    return ["_"] * len(slovo), 1.3 * len(slovo)
```
Je dost mozne, ze druhy udaj, tedy pocet pokusu bude desetinne cislo. Pouzijeme
proto funkci `round()`, abychom jej zaokrouhlili:
```python
    ...
    return ["_"] * len(slovo), round(1.3 * len(slovo), 0)
```
Jeste doplnime volani nasi nove funkce:
```python
    ...
    tajne_slovo, pokusy = schovej_slovo(vybrane_slovo)
    print(f"SCHOVANE SLOVO: {tajne_slovo}")
```
Jeste je mozne doplnit vypis slova pomoci metody `join()`

## Stav hry
Nyni, kdyz mame vsechny udaje pohromade, muzeme zacit upravovat cyklus, uvnitr
ktereho bude nase hra probihat.

### Delka hry
V promenne `pokusy` je ulozena hodnota, ktera stanovuje, kolikrat muze
hrac hadat, doplnime proto cyklus:
```python
    while pokusy:
        print(f"Kolo: X")
        pokusy -= 1
```
Dalsim krokem by mel byt vypis na zacatku kola. Tudiz definujeme novou funkci:
```python
def vypis_hry(hrac: str, stav: str, zbyva: int) -> None:
    # zprava
    # oddelovac
    # vypis
```
Jak ale zpravu radne naformatovat?

## Formatovani retezcu
V Pythonu muzeme retezce formatovat zpravidla tremi zpusoby:
1. Formatovaci __vyraz__, %-formatting
2. Formatovaci __metoda__, str.format()
3. F-string

### Formatovaci vyraz
Jde o prapuvodni formatovani v Pythonu, ktera je soucasti od sameho zacatku:
```
JMENO = "Lukas"
VEK = 26
"Ahoj, jmenuji se %s a je mi %d let" % (JMENO, VEK)
```
Dneska se jiz oficialne nedoporuje pouzivat, jelikoz casto selhava, prip.
nespravne zobrazuje tuply nebo slovniky. Soucasne se samotne vypisovani stava
az prilis podrobne.

### Formatovaci metoda
Od verze Pythonu 2.6 mame k dispozici dalsi zpusob pro formatovani:
```
JMENO = "Eliska"
VEK = 25
"Ahoj, jmenuji se {} a je mi {} let" .format(JMENO, VEK)
```
Pouziti je mene upovidane, nicmene pokud bych chtel vypsat vice promennych,
porad by byl tento zpusob pomerne narocny na vypisovani.

### F-string
Od verze Pythonu 3.6 mame k dispozici dalsi metodu pro formatovani:
```
JMENO = "Lucie"
VEK = 27
f"Ahoj, jmenuji se {JMENO} a je mi {VEK} let"
```
Syntaxe je velice strucna ale rozhodne ne na ukor citelnosti. Zvlada ruzne
platne operace v Pythonu i volani funkci. Akorat u slovniku pamatovat, ze
pokud pouziju napr. dvojite uvozovky u retezce, potom vnitrni musim psat jako
jednoduche, abych ty puvodni predcasne neukoncoval.

### Je to na vas
Vyberte si zpusob formatovani, ktery se vam nejvice hodi a pojdme jej pouzit:
```python
def vypis_hry(hrac: str, stav: str, zbyva: int) -> None:
    zprava = f"HRAC: {hrac} | STAV: {stav} | ZBYVA TAHU: {zbyva}"
    oddelovac = len(zprava) * "-"
    print(oddelovac, zprava, oddelovac, sep="\n")
```
Nova funkce, ktera zajisti informativni vypisovat se sklada ze tri casti:
1. __Zprava__, kterou vypisuji
2. __Oddelovac__
3. __print__
```python
    ...
    while pokusy:
        vypis_hry(hrac, tajne_slovo, pokusy)
```
Jeste pripiseme volani nasi nove funkce, kam doplnime prislusne argumenty.

## Tah hrace
Na pocatku kazdeho kola, jakmile se se vypise stav pomoci funkce `vypis_hry()`,
bude hrac volit pismeno:
```python
def vyber_pismena() -> str:
    return input("HADEJ PISMENO: ")
```
Funkci definujeme ale zatim ji nebudeme volat.

## Overeni tahu
Dalsi funkce, souvisejici s predchozi funkci `vyber_pismena`, je posouzeni,
jestli se pismeno doopravdy nachazi v tajnem slove:
```python
def overeni_pismena(pism: str, slovo: str, stav: str) -> None:
    for index, pismeno in enumerate(slovo):
        if pismeno in pism:
            slovo[index] = pism
```
Principem je zkontrolovat jedno pismeno za druhym, jestli nesedi k pismenu,
ktere hrac tipoval. Do teto funkce zadame dva parametry:
1. __Pismeno__, ktere zvolil hrac
2. __Slovo__, ktere hada hrac

## Dalsi a dalsi kolo
Predchozi funkce jsme jen definovali a nyni je pouzijeme. Vsechny tyto dilci
funkce, ktere se opakuji v kazdem kole sdruzime pod jednu vetsi:
```python
def hraci_kolo(hrac: str, pokusy: str, slovo: str) -> None:
    vypis_hry(hrac, slovo, pokusy)
    hadani = vyber_pismena()
    overeni_pismena(hadani, slovo)
```
Finalni volani teto funkce uvnitr smycky doplnime nasledovne:
```python
    while pokusy:
        hraci_kolo(hrac, pokusy, tajne_slovo)
        pokusy -= 1
```
Nakonec jeste po kazdem kole snizime hodnotu promenne `pokusy`.

## Zaver hry
Nakonec zbyva posoudit posledni, a to podminku, zda hrac vyhraje, pripadne
prohraje:
```python
def ukonceni_hry(hrac: str, stav: str, pokusy: int) -> bool:
    if "_" not in stav:
        vypis_hry(hrac, slovo, pokusy)
        print(f"VYBORNE, {hrac}, UHADL JSI!")
        exit()
    elif "_" in stav and pokusy == 0:
        print(f"PROHRALS, {hrac}, TREBA PRISTE!")
        exit()
```
Pokracovat na [lekci#09](https://github.com/Bralor/python-academy/tree/lekce09)


