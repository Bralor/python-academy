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
DOSTUPNE OPERACE: 
-------------------------
+|-|*|/|prum|^
-------------------------
OPERACE ('q'- konec): ^
CISLO 1: 2
CISLO 2: 5
-------------------------
2 ^ 5 = 32
-------------------------
DOSTUPNE OPERACE: 
-------------------------
+|-|*|/|prum|^
-------------------------
OPERACE ('q'- konec): q
Doufam, ze se Vam kalkulacka libila! ^.^
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


def uvodni_text(text: "str") -> "str":
    "Uvodni text pred zacatkem cyklu"
    print(f"KALKULACKA".center(50), end=f"\n{ODDELOVAC}\n")

```
Nyni muzeme vyzkouset jak se nas program bude chovat po teto uprave. Vsimnete
si pouziti anotaci u funkce. Jednak jejich __parametru__, jednak vracene
__promenne__.
```
jmeno_funkce.__annotations__
```
Timto zpusobem si mohu nechat zobrazit moje anotace.

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
