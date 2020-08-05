Minula [lekce#06](https://github.com/Bralor/python-academy/tree/lekce06)

<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lesson 07
## Dulezite odkazy
- Portal [Engeto.com](https://engeto.com/)
- Python Academy [repozitar](https://github.com/Bralor/python-academy)
- [Anotace](https://www.python.org/dev/peps/pep-3107/) v Pythonu

## Co nas dneska ceka?
Ucelem dnesni lekce je rozsirit znalosti o funkcich v Pythonu. V minule lekci
jsme si rekli neco o funkcich na uvod. Vsechno jsme si overili na nasi prvni
definovane funkci. Dnes nas ceka:
1. Pouziti vice funkci
2. Namespaces
3. Scopes
4. Anotace funkci
5. Typy argumentu
 
## Kalkulacka
Ulohou pro dnesni lekci bude napsat vlastni __kalkulacku__. Tady se budeme
snazit pochopit, jak spolu muzou funkce vzajemne komunikovat a predavat si
informace.

## Ukazka na zacatek
Spustime skript v nasem adresari:
```
$ ./kalkulacka
```
Vystup muzeme vypadat nasledovne:
```
          VITEJTE U PROGRAMU KALKULACKA           
==================================================
               + | - | * | / | abs                
==================================================
VYBER MATEMATICKOU OPERACI: +
==================================================
x1: 123
x2: 326
==================================================
x1 + x2: 123.0 + 326.0 = 449.0
==================================================
               + | - | * | / | abs                
==================================================
VYBER MATEMATICKOU OPERACI: prum
==================================================
VLOZTE CISLA ODDELENA CARKOU: 1,2,3,4,
==================================================
RADA CISEL: [1.0, 2.0, 3.0, 4.0], VYSLEDEK: 2.5
==================================================
               + | - | * | / | abs                
==================================================
VYBER MATEMATICKOU OPERACI: q
==================================================
UKONCUJI...
```

## Co budeme potrebovat?
- python 3.6.9+
- text. editor
- [while smycky](https://github.com/Bralor/python_academy/tree/master/lesson04#while-cyklus)
- [for cyklus](https://github.com/Bralor/python_academy/tree/master/lesson05#for-cyklus)
- [funkce](https://github.com/Bralor/python_academy/tree/master/lesson06#funkce)
Potrebne promenne:
```
NABIDKA = "DOSTUPNE OPERACE: "
ODDELOVAC = "-" * 50
```

## Zaciname!

<p align="center">
  <img src="https://media.giphy.com/media/Y5pJPmh9IWMKc/giphy-downsized.gif" width="300" height="300">
</p>

Nejprve si zkopirujeme uvod souboru a zadani, ktere najdete vyse:
```python
#!/usr/bin/python3
"Lekce #7 - Uvod do programovani, kalkulacka"

NABIDKA = "DOSTUPNE OPERACE: "
ODDELOVAC = "=" * 50
```
Naformatujeme jednoduchy uvodni text a vracime jej pomoci `print`:
```python
print("VITEJTE U PROGRAMU KALKULACKA")
print(f"KALKULACKA".center(50), end=f"\n{ODDELOVAC}\n")
print(NABIDKA, end=f"\n{ODDELOVAC}\n")
```

## Vytvorime hlavni funkci
Nejprve vytvorime hlavni funkci, kterou si pojmenujeme `main`. Ta bude mit za
ukol delegovat ukoly dal:
```python
def main() -> None:
    "Hlavni ridici funkce nasi kalkulacky"
    uvodni_text()
```
Budeme chtit cely prubeh opakovat. Prakticky budeme chtit tocit tyto kroky:
1. Uvod do funkce
2. Vyber operace
3. Presmerovani k matematicke operaci a jeji provedeni
```python
    while True:
        # dostupne_operace()
        # zadana_operace()
        # vyber_proces()
```
Tim mame uvod nachystany a muzeme se soustredit na dilci funkce.

## Uvodni text
Nejprve presuneme cast kodu, kterou jsme jiz napsali v uvodu:
```python
...
NABIDKA = "DOSTUPNE OPERACE: "
ODDELOVAC = "=" * 50

print(NABIDKA, end=f"\n{ODDELOVAC}\n")

def main() -> "None":
    "Hlavni ridici funkce nasi kalkulacky"
    uvodni_text(ODDELOVAC)


def uvodni_text(text: "str")-> "str":
    "Uvodni text pred zacatkem cyklu"
    print(f"{text}".center(50), end=f"\n{ODDELOVAC}\n")
```
Nyni muzeme vyzkouset jak se nas program bude chovat po teto uprave. Vsimnete
si pouziti anotaci u funkce. Jednak jejich __parametru__, jednak vracene
__promenne__.
```
jmeno_funkce.__annotations__
```
Timto zpusobem si mohu nechat zobrazit moje anotace.

## Copak to jde?
Vsimneme v nasem soucasnem zapise promenne `ODDELOVAC`. Vidime, ze s ni funkce
pracuje, ale pritom ji nikde do funkce nevkladam, jak je to mozne?

### Namespace
Jde o jmenne prostredi, ktere automaticky funguje na pozadi naseho kodu v
Pythonu. Pomoci techto prostredi v Pythonu spravujeme a uchovavame promenne.
Kazdy soubor, kazda funkce maji vlastni prostredi, aby zabranili potencialni
kolizi se jmeny promennych.
```
# Jedno globalni jmenne prostredi
JMENO = "Matous"
VEK = 45

# namespace = {"JMENO": "Matous", "VEK": 45}
```
Pokud bych mel napriklad funkci, vypadaly by obe prostredi:
```python
EMAIL = "matous@matous.cz"

def ziskej_domenu(mail: "str") -> "str":
    return mail.split("@")[1].split(".")[0]
```
Tentokrat tu mame hned dve jmenna prostredi:
```
# Globalni jmenne prostredi
namespace_1 = {"EMAIL": "matous@matous.cz", "ziskej_domenu": ""}

# Lokalni jmenne prostredi
namespace_2 = {"mail": ""}
```

### Ramce v Pythonu
Aby byl Python schopen dohledat konrektni promennou, existuji na to 4 typy
prostredi (hierarchie):
1. Zabudovana jmena (built-in) - napr. `def`, `str`, `sum`
2. Globalni (global scope) - napr. promenne v souboru
3. Uzavrene prostredi (enclosing scope) - funkce uvnitr funkce
4. Lokalni prostredi (local scope) - napr. parametry funkci, promenne ve funkci



## Dostupne operace
Dalsim krokem bude vypsat operaci, kterymi nase kalkulacka disponuje. Napiseme
proto novou funkci, ktera bude vypisovat tyto informace:
```python
def dostupne_operace(text: 'tuple') -> "str":
    "Vypisovani dostupnych operaci uvnitr cyklu"
    print(f"{' | '.join(text)}".center(50), end=f"\n{ODDELOVAC}\n")
```
Takovouto definici muzeme pouzit za predpokladu, ze zname vstupni promennou.
Pokud ale predem nevime, kolik budeme argumentu, musime na to jinak.

### Pozicni argumenty
Pokud nemame poneti, kolik toho bude nase funkce zpracovavat, muzeme pouzit
pozicni argumenty (`*args`). Jejich pouziti je pomerne snadne:
```
def func(*args) -> "str":
    print(f"{'|'.join(args)}")
```
Pojdme zkusit nasi funkci zavolat se tremi argumenty:
```
func("+", "-", "*")  # +|-|*
```
Nyni s peti argumenty:
```
func("+", "-", "*", "/", "**")  # +|-|*|/|**
```
### Prepiseme funkci `dostupne_operace`
Ted, kdyz umime pozicni argumenty, muzeme prepsat funkci `dostupne_operace`:
```python
def dostupne_operace(*args) -> "str":
    "Vypisovani dostupnych operaci uvnitr cyklu"
    print(f"{' | '.join(args)}".center(50), end=f"\n{ODDELOVAC}\n")
```
Jakmile ji mame vytvorenou, muzeme ji zavolat v nasi hlavni funkci `main`.

## Vyber operace
Jakmile uzivateli vypiseme souhrn vsech dostupnych operaci, muze vybirat:
```python
def vyber_operaci() -> "str":
    return input("VYBER MATEMATICKOU OPERACI: ")
```
Staci pouzit funkci `input`, ktera si uschova vybranou operaci jako `str`.
Jeste dopiseme volani funkce `vyber_operaci` do nasi hlavni funkce `main`:
```python
def main() -> "None":
    "Hlavni ridici funkce nasi kalkulacky"
    uvodni_text(ODDELOVAC)

    dostupne_operace(OPERACE)
    operace = vyber_operaci()
```

## Delegujeme na jine
Jakmile uzivatel vybere operaci, kterou vyzaduje, musime vytvorit dalsi funkci
celek. Zatim mame nasledujici:
```python
    ...
    uvodni_text(ODDELOVAC)

    dostupne_operace(OPERACE)
    operace = vyber_operaci()
    ...
```
Potrebujeme vymyslet neco podobneho:
```python
    ...
    uvodni_text(ODDELOVAC)

    dostupne_operace(OPERACE)
    operace = vyber_operaci()
    # zpracuj operaci -> vstup: promenna 'operace'
        # pokud bude 'operace' = '+' -> spust 'scitani'
        # pokud bude 'operace' = '-' -> spust 'odcitani'
        # pokud bude 'operace' = '/" -> spust 'deleni'
        # ...
```
Takze si muzeme vsimnout jisteho vzoru:
```python
def zpracuj_operaci(operace: "str") -> "none":
    if ...
    elif ...
    elif ...
    else ...
```
Soustredme se prvni jenom na scitani a odcitani. Na zacatek musime vlozit dva
argumenty do nasi funkce `dostupne_operace`. Tim uzivateli umoznime nahled.
Potom vytvorime prvni podminku ve funkci `vyber_operace`:
```python
def vyber_operace(op: "str") -> "none":
    if op == "+":
        x1, x2 = vyber_cisla()
        print(f"x1 + x2: {x1} + {x2} = {x1 + x2}")
```
Jeste musime doplnit nas vystup a potrebne `ODDELOVAC`. Zatim zname uvod k
formatovani pomoci __f-string__. Dale vime o nepovinnem argumentu `end`. Dneska
si ukazeme dalsi nepovinny argument pro funkci `print` a tim je `sep`.

`sep` je zkratka _oddelovac_. Jde o definici symbolu, ktery se ma vkladat mezi
jednotlive promenne, ktere chceme vypsat pomoci funkce `print`.
```
print("NABIDKA", "-------", "+ | -", "-------", sep="\n")
```
Takze zname dalsi zpusob, kterym muzeme formatovat vystup pomoci funkce `print`.

### Pouzijeme v nasi funkci
```python
def vyber_operace(op: "str") -> "none":
    if op == "+":
        x1, x2 = vyber_cisla()
        print(
            ODDELOVAC,
            f"x1 + x2: {x1} + {x2} = {x1 + x2}",
            ODDELOVAC,
            sep="\n"
            )
```
Ted by bylo mozna na miste povedet si neco o prostredich v Pythonu.

### Obdobne dopiseme podminku odcitani
Jde prakticky o stejny zapis, akorat doplnime znamenko `-` do funkce
`dostupne_operace` a dalsi podminku, ktera jej zohledni.
```python
    elif op == "-":
        x1, x2 = vyber_cisla()
        print(
            ODDELOVAC,
            f"x1 - x2: {x1} - {x2} = {x1 - x2}",
            ODDELOVAC,
            sep="\n"
        )
```
Funkci `print` jsem rozdelil na radky po sebe jelikoz by byl zapis moc dlouhy.

## Nez pujdeme dal
Kdyz se na nase prvni dve podminky podivame, muzeme rict, ze pro zakladni
aritmeticke operace bude prubeh vzdy podobny. Prakticky budeme pracovat s
promennymi:
1. __x1__
2. __x2__
3. __znamenko__
Takze by mozna stalo za to setrit zapisem podminek a napsat pro to jinou funkci.
```python
    if op in ("+", "-", "*", "/"):
        x1, x2 = vyber_cisla()
        vysledek = zakladni_operace(x1, x2, op)
        print(
            ODDELOVAC,
            f"x1 {op} x2: {x1} {op} {x2} = {vysledek}",
            ODDELOVAC,
            sep = "\n"
        )
```
Nejprve musime prizpusobit nasemu zapisu podminku v uvodu funkce
`vyber_operace`. Jakmile mame opraveny uvod, muzeme dodelat potrebnou funkci:
```python
def zakladni_operace(x: "float", y: "float", op: "str") -> "str":
    return {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y
    }.get(op)
```
Tato funkce (v kombinaci s volajici podminkou) pro nas obstara reseni vysledku
pro 4 zakladni aritmeticke operace nasi kalkulacky.

## Dalsi operace

<p align="center">
  <img src="https://media.giphy.com/media/vtVpHbnPi9TLa/giphy.gif" width="300" height="300">
</p>

Mame za sebou 4 operace, pojdme zkusit pocitani prumerne hodnoty. Cely postup
by mohl vypadat nasledovne:
```
# Vkladame libovolny pocet cisel
1, 2, 3, 4, 5, 6, 7, 8, 9, 0

# Dostavame prumernou hodnotu
4.5
```
Na zacatek upravime argumentu funkce `dostupne_operace`:
```python
    dostupne_operace("+", "-", "*", "/", "abs")
```
Dale zapiseme spravnou podminku, ktera zajisti, ze se spusti potrebna
funkce:
```python
    elif op in ("abs", "prum", "prumer"):
        rada = vyber_radu_cisel()
        print(
            ODDELOVAC,
            f"RADA CISEL: {rada}, VYSLEDEK: {sum(rada)/len(rada)}",
            ODDELOVAC,
            sep = "\n"
        )
```
A v posledni kroku tohoto bodu sepiseme potrebnou funkci, ktera nam vraci
prevedenou radu cisel:
```python
def vyber_radu_cisel() -> "list":
    rada_cisel = input("VLOZTE CISLA ODDELENA CARKOU: ")
    prevedene = [
        float(cislo.strip())
        for cislo in rada_cisel.split(",")
        if cislo != ""
    ]
    return prevedene
```

## Par uprav nakonec
Aby bylo mozna kalkulacku pouzivat na vice operaci, pridame na uvod nasi funkce
`main` cyklus:
```python
def main() -> "None":
    "Hlavni ridici funkce nasi kalkulacky"
    uvodni_text(ODDELOVAC)

    while True:
        dostupne_operace("+", "-", "*", "/", "abs")
        operace = vyber_operaci()
        vyber_operace(operace)
```
Dalsim krokem bude zpusobem, jakym tuto smycku ukoncit. Nejlepsi bude, kdyz
k nasim podminkam pridame dalsi podminkovou vetev, ktera bude obsahovat funkci
`exit` (pripadne `quit`):
```python
    elif op in ("quit", "exit", "q", "e"):
        print("UKONCUJI...")
        exit()
```
A uplne posledni detail na zaver by mel osetrit scenar, kdy uzivatel zada jiny
vstup nez mame v nabidce:
```python
    else:
        print(f"*{op}* NENI V NABIDCE")
```
Tim by byl nas program kalkulacka kompletni!




## Metoda .join()
Metoda vracejici retezec spojeny preddefinovanym symbolem.

Priklad
```
SLOVA = ['mesto', 'more', 'kure' ,'staveni']
"+++".join(SLOVA)
>>>
'mesto+++more+++kure+++staveni'
```

## Jmenne prostory a.k.a. namespaces
Rikali jsme si, ze promenna je vytvorena, pokud ji priradime hodnotu. Pomoci konceptu [jmennych prostoru](https://engeto.com/cs/kurz/online-python-akademie/studium/cfXXcPh0TTaF8DGihbsP2A/funkcni-ramce-a-vstupy/funkcni-ramce/co-je-to-ramec), tedy namespace evidujeme/spravujeme tyto namapovana jmena promennych a jejich hodnot. V Pythonu obecne ma kazdy balicek, funkce, modul svoje vlastni jmenne, aby zabranilo potencialni kolizi se jmeny promennych.

Teorie:
```
JMENO = "Matous"
VEK = 56

# ilustrace jmenneho prostredi
namespace = {
    "JMENO": "Matous",
    "VEK": 56
}
```
[Priklad](https://engeto.com/cs/kurz/online-python-akademie/studium/gELVr5MdQUy9LQgqXFMKNw/funkcni-ramce-a-vstupy/funkcni-ramce/zmena-built-in-promennych):
```
# built-in sum()
HODNOTY_1 = [1, 2, 4, 8, 16, 32]
HODNOTY_2 = [1, 2, 4, 8, 16, 32, 64]
sum(HODNOTY_1)  # dostanu vystup, ktery secte vsechny cisla v prom.

# moje vlastni promenna sum
sum = 63

# opet potrebuji sum()
sum(HODNOTY_2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable

```
## Prostredi v Pythonu
Aby byla aplikace jmennych prostoru osetrena, muzeme v Pythonu vymezit 4 druhy [prostredi](https://engeto.com/cs/kurz/online-python-akademie/studium/00LmkBYlTIOnTYVXRau8PQ/funkcni-ramce-a-vstupy/funkcni-ramce/built-in-a-globalni-ramec). Jejich rozdeleni je vytvoreno zamerne, aby Python vedel postup, kterym promenne hledat a jak/komu jej zpristupnit.

Rozdeleni LEGB:
1. Zabudovana jmena (built-in scope) - pr. def, str, sum
2. Globalni (global scope) - pr. promenne v ramci souboru
3. Uzavrene prostredi (enclosing scope) - funkce ve funkci
4. Lokalni (local scope) - pr. parametry funkci, promenne ve func

[Priklad](https://engeto.com/cs/kurz/online-python-akademie/studium/lue9xKseQ6OSse_8dK0O5Q/funkcni-ramce-a-vstupy/funkcni-ramce/stejnojmenne-promenne):
```
>>> jmeno = "Marek"
>>> def func1(jm):
...     jmeno = jm
...     print(jmeno)
... 
>>> func1('Matous')
Matous
>>> print(jmeno)
'Marek'
```
