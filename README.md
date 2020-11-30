➡ [vratit se na sestou lekci](https://github.com/Bralor/python-academy/tree/lekce06)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 7⃣ Python akademie
###  Dulezite odkazy
- [Portal Engeto.com](https://engeto.com/)
- [Seznamova komprehence](http://howto.py.cz/cap08.htm#10)
- [Ternarni operator](https://book.pythontips.com/en/latest/ternary_operators.html)
- [Python, dokumentace zabudovanych funkci](https://docs.python.org/3/library/functions.html)
- [Collections, standartni modul](https://docs.python.org/3/library/collections.html#collections.Counter)
- [Type hints, napovidani u funkci](https://www.python.org/dev/peps/pep-0484/)
---

###  Obsah lekce
1. Ukazka ulohy
2. Funkce, prace vice funkci
3. Jmenna prostredi v Pythonu
4. Funkcni ramce
5. Type hint, napovidani
6. Typy argumentu
---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si sedmou lekci jako **zip**](https://github.com/Bralor/python-academy/archive/lekce07.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **upravene_udaje** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
  <summary>🎹 Funkce, prace vice funkci</summary>

</details>

---

<details>
  <summary>📊 Jmenna prostredi v Pythonu</summary>

</details>

---

<details>
  <summary>🎎 Funkcni ramce</summary>

</details>

---

<details>
  <summary>💬 Type hint, napovidani</summary>

</details>

---

<details>
  <summary>👽 Typy argumentu</summary>

</details>

---

<details>
  <summary>🚧 Procvicovani na doma</summary>

</details>

---
➡ [pokracovat na osmou lekci](https://github.com/Bralor/python-academy/tree/lekce08)


## Co nas dneska ceka?
Ucelem dnesni lekce je rozsirit znalosti o funkcich v Pythonu. V minule lekci
jsme si rekli neco o funkcich na uvod. Vsechno jsme si overili na nasi prvni
definovane funkci. Dnes nas ceka:
1. Pouziti vice funkci
2. Jmenna prostredi (namespaces)
3. Ramce funkci (function scopes)
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
VYBER MATEMATICKOU OPERACI: abs
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
    uvodni_text()


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
# Globalni jmenne prostredi
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
Pokud bych mel lokalnich prostredi vic, melo by kazde svoje vlastni jmenne
prostredi.

### Ramce v Pythonu
Aby byl Python schopen dohledat konrektni promennou, existuji na to 4 typy
prostredi (hierarchie):
1. Zabudovana jmena (built-in) - napr. `def`, `str`, `sum`
2. Globalni (global scope) - napr. promenne v souboru
3. Uzavrene prostredi (enclosing scope) - funkce uvnitr funkce
4. Lokalni prostredi (local scope) - napr. parametry funkci, promenne ve funkci

### Priklad uzavreneho prostredi
Mame tu na ukazku jeden pohled na uzavrenou funkci (funkci uvnitr funkce):
```python
def vnejsi_func(em):
    mail = em.split("@")
    def vnitrni_func():
            return mail[1].split(".")
    domena, *zbytek = vnitrni_func()
    return domena
```
Pokud zavolame funkci `vnejsi_func` s argumentem `matous@matous.cz`, ziskame
samotnou domenu. Pokud ale budu chtit pouzit vnitrni funkci `vnitrni_func`,
Python nas nenecha.

### Proc to?
Nasledujici priklad nam objasni, proc vubec vsechna ta jmenna prostredi a
ramcove celky musime resit:
```python
JMENO = "Matous"

def func():
    print(JMENO)
```
Pokud spustime tuto funkci, vypise nas interpret hodnotu `Matous`.
```python
def func():
    JMENO = "Lukas"

print(JMENO)
```
Ale pokud zapiseme tuto funkci a budeme chtit pouzit `print` a vypsat promennou
`JMENO`, dostaneme `NameError`. V podstate si staci pamatovat,
ze __globalni__ promenne jsou viditelne v celem nasem kodu. Zatim co
__lokalni__ promenne jsou viditelne pouze v prostredi, ve kterem vznikly.

### Z toho vyplyva?
Pokud volame z lokalniho jmenneho prostredi promennou z globalniho jmenneho
prostredi, Python ji umi naleznout, ale obracene to neplati.

### Zaverem k hierarchii
Pokud tedy Python hleda promennou, postupuje nasledovne:
1. Nejprve prohlizi __lokalni__ jmenne prostredi (napr. ve funkci)
2. Pokud nenajde, pokracuje do __globalniho__ prostredi (v nasem souboru)
3. Pokud nenajde, pokracuje do __built-in__ prostredi (predefinovane)
4. Pokud nenajde, nasleduje `NameError`

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

## Jak zapisovat parametry?
Variant pro zadavani parametru do funkce je cela skala:
1. Podle pozice
2. Podle __klice__
3. __Defaultni__ parametr
4. __*args__ (list, tuple)
5. __**kwargs__ (slovnik)

### Co se nam hodi?
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
Jakmile budeme mit hotovou cast, kde promenne `x1`, `x2` ukladame z funkce,
musime doplnit funkci `vyber_cisla`:
```python
def vyber_cisla() -> "tuple":
    return float(input("x1: ")), float(input("x2: "))
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
def zakladni_operace(x: "float", y: "float", op: "str") -> "float":
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
    uvodni_text()

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
        print(ODDELOVAC)
        print("UKONCUJI...")
        exit()
```
A uplne posledni detail na zaver by mel osetrit scenar, kdy uzivatel zada jiny
vstup nez mame v nabidce:
```python
    else:
        print(ODDELOVAC)
        print(f"*{op}* NENI V NABIDCE")
```
Tim by byl nas program kalkulacka kompletni!

Pokracovat na [lekci#08](https://github.com/Bralor/python-academy/tree/lekce08)

