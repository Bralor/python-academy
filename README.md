Minula [lekce#03](https://github.com/Bralor/python-academy/tree/lekce03)

<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lekce 04
## Dulezite odkazy
- [Portal Engeto.com](https://engeto.com/)
- [Python academy, repozitar](https://github.com/Bralor/python-academy)
- [Walrus operator](https://realpython.com/lessons/assignment-expressions/)

## Co nas dnes ceka?
Doposud jsme se snazili kazdy udaj zadat/vypisovat rucne. Kazde oznameni v 
kodu melo svuju prislusny radek. Ode dneska se budeme snazit zapis trochu 
automatizovat. Probereme spolecne prvni typ smycek/cyklus v Pythonu.
Bude to tzv. cyklus _while_, o kterem se budeme podrobneji bavit a naucime se 
ho pouzivat.

## Nakupni kosik 
V ramci dnesni hodiny se budeme snazit vytvorit virtualni nakupni kosik, do
ktereho budeme moci jako zakaznik vkladat zbozi z nabidky. Nas kosik bude umet
vypisovat celkovou hodnotu zbozi v kosiku a soucasne ukazovat, co je jeho 
obsahem.

## Ukazka
Po spusteni by mel program vypadat nasledovne:
```bash
$ ./nakupni_kosik
```
Cela ukazka z terminalu: 
```bash
VITEJTE V NASEM VIRTUALNIM OBCHODE!
========================================
VYBERTE SI Z NASEHO ZBOZI:
========================================
{'banan': 30,
 'chleb': 20,
 'jablko': 10,
 'jogurt': 10,
 'maso': 100,
 'mleko': 30,
 'pomeranc': 15}
========================================
VYBERTE ZBOZI: banan
VYBERTE ZBOZI: mleko
VYBERTE ZBOZI: pomeranc 
VYBERTE ZBOZI: exit 
========================================
{'banan': 30, 'mleko': 30, 'pomeranc': 15}
========================================
CENA CELKEM: 75 CZK
Vystup by na konci lekce mohl vypadat nasledovne:
```
## Co budeme potrebovat? 
- python 3.8! (kvuli novemu operatoru)
- text. editor
- [podminky](https://github.com/Bralor/python_academy/tree/master/lesson02#podminkovy-zapis)
- [slovnik](https://github.com/Bralor/python_academy/tree/master/lesson03#slovnik)

## Muzeme zacit!
<p align="center">
  <img src="https://media.giphy.com/media/GSrZUFaPs7yCs/source.gif" width="300" height="300">
</p>

Nejprve si vytvorime novy soubor pro dnesni lekci. Po te nakopirujeme zadane
udaje, se kterymi budeme chtit pracovat.

```python
KOSIK = {}
ODDELOVAC = "=" * 40
POTRAVINY = {
    "mleko": 30,
    "maso": 100,
    "banan": 30,
    "jogurt": 10,
    "chleb": 20,
    "jablko": 10,
    "pomeranc": 15,
}
```
## Vypiseme uvodni text
Na uvod nam bude stacit vypsat, ze kterych potravin zakaznik muze vybirat. Plus
oddelovaci lemovany uvodni text. Prvni cast by mohla vypadat nasledovne:
```python
# II. KROK
# Vypiseme nabidku a oddelime
print(ODDELOVAC)
print("VITEJTE V NASEM VIRTUALNIM OBCHODE!")
print(ODDELOVAC)
print("VYBERTE SI Z NASEHO ZBOZI:")
print(ODDELOVAC)
pprint(POTRAVINY)
print(ODDELOVAC)
```
Kdyz se koukame na promennou __ODDELOVAC__, zacina byt malicko napadna. Proto
se dneska naucime pouzivat atribut funkce __print__. Tim bude _end_. Jde o
volitelny atribut, ktery neni nutne zadavat. Slouzi hlavne k tomu, abychom na 
konec toho, co chceme zobrazit mohli doplnit libovolny znak/znaky.

__Ukazka__:
```python
print("Ahoj, ze 4. lekce!", end="\n##################")
```

## Takze...
Nyni muzeme prvni vystupni sekci doplnit o nas novy atribut __end__.
```python
print("VITEJTE V NASEM VIRTUALNIM OBCHODE!", end=f"\n{ODDELOVAC}")
print("VYBERTE SI Z NASEHO ZBOZI:", end="\n{ODDELOVAC}")
pprint(POTRAVINY)
print(ODDELOVAC)
```

## Chceme vybrat zbozi
Nyni se budeme snazit vybrat 3 polozky z promenne _POTRAVINY_ a pridat je do
promenne _KOSIK_.

### Nejprve potrebuje vstup...
Abychom meli moznost si vybrat, musime vyuzit funkce __input__:
```python
vyber_potravinu = input("VYBERTE ZBOZI: ")
``` 
### ...Vlozime do kosiku...
Jakmile jsme vybrali zbozi, musime jej vlozim do promenne __KOSIK__:
```python
KOSIK[vyber_potravinu] = POTRAVINY.get(vyber_potravinu, "NENI SKLADEM")
```
### ...Vypisime cenu
Jakmile je potravina v seznamu, zjistime cenu a vypiseme ji:
```python
print(f"CELKEM: {sum(KOSIK.values())} CZK")
```

## Trochu obtiznejsi varianta
Jakmile se nam podari cela procedura zapsat. Vyzkousejme si to cele zopakovat
pro vyber 4 polozek ze zadaneho vyberu.

__Mozne reseni__:
```python
vyber1 = input("VYBERTE ZBOZI c.1: ")
vyber2 = input("VYBERTE ZBOZI c.2  ")
vyber3 = input("VYBERTE ZBOZI c.3: ")

KOSIK[vyber1] = POTRAVINY.get(vyber1, "NENI SKLADEM")
KOSIK[vyber2] = POTRAVINY.get(vyber2, "NENI SKLADEM")
KOSIK[vyber3] = POTRAVINY.get(vyber3, "NENI SKLADEM")

print(ODDELOVAC)
print(KOSIK)
print(ODDELOVAC)
print(f"CELKEM: {sum(KOSIK.values())} CZK")
``` 

## Citite prsty?
Predchozi krok byl jeste unosny. Trochu.. Predstavme si ale, ze se budeme
snazit zapsat desitky nebo stovky polozek. Tady uz by situace, kdy budu udaje
opakovane vkladat, zapisovat do slovniku a nasledne jej scitat a vypisovat
neprehledna.

## Jak to obejit?
Na stesti v Pythonu existuje neco, co nam opakovani, takovych kroku zajisti. Je
to prave _cyklus_, nebo take _smycka_. Tedy proces, ktery probiha opakovane. V
ramci dnesni lekce se seznamime s prvnim typem smycek.

## while cyklus
Jak uz jmeno prozradi, oznameni teto smycky se schovava za klicovym slovem
__while__. Popiseme si, jak __while__ funguje:
```python
while <podminka>:
    # provadej toto pokud je podminka pravdiva (TRUE)
# pokracuj dal, pokud smycka skoncila
```
### Podminka
V zahlavi si muzeme vsimnout pojmu _podminka_. Je to tak, ze smycka probiha,
pokud podminka v zahlavi vraci boolean hodnotu _True_. Jakmile dostane _False_,
cyklus skonci.

### -> True
Pokud nam podminka vraci __True__, probiha ten kod, ktery je odsazeny hned pod
zahlavim. Tedy v nasem vzoru cast:
```python
    # provadej toto pokud je podminka pravdiva (TRUE)
```
Vsimnete si urcite povinneho odsazeni.

### -> False
Jakmile nam ale podminka v zahlavi vrati _False_. Cela smycka se ukonci a
nasleduje kod za ni. Tedy:
```python
# pokracuj dal, pokud smycka skoncila
```

# Cheatsheet s priklady
# While cyklus
Je to jeden z [cyklu](https://engeto.com/cs/kurz/online-python-akademie/studium/y1BTUUW1Q12bjKt1MGVJRw/rozsireni-sekvenci-smycka-while/smycka-while/princip-while) v Pythonu, ktery umoznuje opakovat libovolnou cast naseho kodu. Opet je slovo *while* nejaky rezervovany pojem, ktery Pythonu rozezna.
```
```
Priklad:
```
x = 0

>>> while x < 10:
...     print(f"x={x}; {x}<10, v poradku!")
...     x = x + 1
... 
x=0; 0<10, v poradku!
x=1; 1<10, v poradku!
x=2; 2<10, v poradku!
x=3; 3<10, v poradku!
x=4; 4<10, v poradku!
x=5; 5<10, v poradku!
x=6; 6<10, v poradku!
x=7; 7<10, v poradku!
x=8; 8<10, v poradku!
x=9; 9<10, v poradku!

```
# While + else
While cyklus ma spoustu ze sve podstaty spolecne s podminkovym zapisem. Mimo struktury zapisu napr. *else*. Pokud se podminka v zahlavi vyhodnoti jako NEPRAVDIVA, potom se nevykonava kod v odsazenem bloku po zahlavi, ale v prave *else*.
```
>>> x = 0
>>> while x < 10:
...     print(f"x={x}; {x}<10, v poradku!")
...     x = x + 1
... else:
...     print(f"x=10; 10==10, cyklus konci!")
... 
x=0; 0<10, v poradku!
x=1; 1<10, v poradku!
x=2; 2<10, v poradku!
x=3; 3<10, v poradku!
x=4; 4<10, v poradku!
x=5; 5<10, v poradku!
x=6; 6<10, v poradku!
x=7; 7<10, v poradku!
x=8; 8<10, v poradku!
x=9; 9<10, v poradku!
x=10; 10==10, cyklus konci!
```

# Nekonecny cyklus
Jednou z moznosti, kterou *while* smycka nabizi je zapsani [nekonecne](https://engeto.com/cs/kurz/online-python-akademie/studium/jSauyS9oTWW2PX_0PL9PZw/rozsireni-sekvenci-smycka-while/smycka-while/preruseni-while-break) smycky.
Jak by smycka vypadat nemela:
```
>>> x = 0
>>> while x < 10:
...     print(f"x={x}; {x}<10, v poradku!")
x=0; 0<10, v poradku!
x=0; 0<10, v poradku!
x=0; 0<10, v poradku!
x=0; 0<10, v poradku!
...
<ctrl+C --> ukonci>
```
Jak vytvorit nekonecnou smycku, ktera ma ucel:
```
>>> cislo = 2
>>> prepinac = True
>>> while prepinac:
...     cislo = cislo ** cislo
...     kontrola = input("PRO UKONCENI NAPIS 'q': ")
...     if kontrola == "q":
...             prepinac = False
...     else:
...             print(cislo)
... 
PRO UKONCENI NAPIS 'q': 
4
PRO UKONCENI NAPIS 'q': 
256

```
# Break + continue
V ramci pouziti smycek muzeme vyuzivat dvou ohlasenich uvnitr smycky.
1. [break](https://engeto.com/cs/kurz/online-python-akademie/studium/jSauyS9oTWW2PX_0PL9PZw/rozsireni-sekvenci-smycka-while/smycka-while/preruseni-while-break) - pri cteni odsazeneho bloku narazim na toto ohlaseni a smycku ukoncim
2. continue - ... vracim se opet do zahlavi a zacinam dalsi cyklus
Priklad BREAK:
```
>>> while cislo < 100:
...     cislo = cislo + 2
...     if cislo == 14:
...             break
...     else:
...             print(cislo)
... 
2
4
6
8
10
12
```
Priklad CONTINUE:
```
>>> cislo = 0
>>> while cislo < 100:
...     cislo = cislo + 3
...     if cislo % 15 == 0:
...             print(f"NASOBEK 15ti! Cislo --> {cislo}")
...             continue
...     else:
...             print(cislo)
... 
3
6
9
12
NASOBEK 15ti! Cislo --> 15
18
21
24
27
NASOBEK 15ti! Cislo --> 30
33
36
39
42
NASOBEK 15ti! Cislo --> 45
48
51
54
57
NASOBEK 15ti! Cislo --> 60
63
66
69
72
NASOBEK 15ti! Cislo --> 75
78
81
84
87
NASOBEK 15ti! Cislo --> 90
93
96
99
102

```

# Walrus (prirazovaci) operator
Prirazovaci operator, nebo prirazovaci vyraz je v Pythonu pomerne nova zalezitost. Jeho jmeno je odvozene od symbolu jejichz kombinace pripomina mroze. Jeho ucel spociva ve zkraceni definice promenne a jejiho pouziti do jedne konstrukce (formy zapisu).
```
>>> while ((dotaz:=input("VLOZ CISLO: ")).isnumeric()):
...     print(dotaz)
... 
VLOZ CISLO: 1
1
VLOZ CISLO: 2
2
VLOZ CISLO: 3
3
VLOZ CISLO: 4
4
VLOZ CISLO: a
>>>

```

Pokracovat na Lekci#05
