Minula [lekce#09](https://github.com/Bralor/python-academy/tree/lekce09)

<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lesson 10
## Dulezite odkazy
- Portal [Engeto.com](https://engeto.com/)
- Python Academy [repozitar](https://github.com/Bralor/python-academy)
- Soubor [\_\_init\_\_.py](https://pythontips.com/2013/07/28/what-is-__init__-py/)
- Hledani [modulu](https://docs.python.org/3/tutorial/modules.html#the-module-search-path)
- Instalator balicku [pip](https://pypi.org/project/pip/)
- [Pycharm importing](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)
- [Name == '__main__'](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)

## Dnesni ukol
Cilem dnesni lekce je povedet si vic o modulech. Rozlisovat mezi moduly a
baliky. Umet nacist nejenom moduly standartni ale i moduly tretich stran a
s tim problematika souvisejici. Dale se budeme snazit rozdelit nasi praci do
nekolika souboru. Celkem tedy projedeme:
1. __Moduly__, v Pythonu
2. __Baliky__, v Pythonu
3. __Proces importovani__ v Pythonu
4. __Standartni__ moduly a baliky
5. Moduly a baliky __tretich stran__
6. if \_\_name\_\_ == "\_\_main\_\_", konstrukce

## Vytvareni souboru
Budeme v situaci, kdy dostaneme jako vstupni udaj textovy soubor
[`jmena_souboru.txt`](https://github.com/Bralor/python-academy/blob/lekce10/jmena_souboru.txt)
. V tomto souboru jsou jmena a jejich pripony. Za pomoci tohoto souboru budeme
chtit vytvorit skutecne soubory (staci prazdne) do uzivatelem zadaneho adresare.

## Ukazka na uvod
Spustime skript v adresari:
```
$ python hlavni.py jmena_souboru.txt vystupni_adresar 
```
A dostaneme nasledujici vystup, pokud jsme adresar se soubory jeste nevytvorili:
```
VYTVARIM: /home/matous/projects/python-academy/vystupni_soubory/rofl.gif
HOTOVO!
VYTVARIM: /home/matous/projects/python-academy/vystupni_soubory/paths.png
HOTOVO!
VYTVARIM: /home/matous/projects/python-academy/vystupni_soubory/icon_53333.jpg
HOTOVO!
...
```

## Co budeme potrebovat?
- python 3.6+
- text. editor/IDE
- [for smycky](https://github.com/Bralor/python-academy/tree/lekce05)
- [funkce v Pythonu](https://github.com/Bralor/python-academy/tree/lekce06)
- [prace s text. soubory](https://github.com/Bralor/python-academy/tree/lekce08)
- [handlovani chyb](https://github.com/Bralor/python-academy/tree/lekce09)

## Pro zacatek
Do pracovniho adresare si nakopirujeme vstupni textovy soubor
`jmena_souboru.txt`. Dale si otevreme novy soubor, ktery pojmenujeme
`hlavni.py` na jehoz uvod zapiseme:
```python
#!/usr/bin/python3
"""Lekce #11 - Uvod do programovani, importovani - hlavni"""
```
Pro pomocne funkce vytvorime dalsi soubor `pomocne.py`:
```python
#!/usr/bin/python3
"""Lekce #11 - Uvod do programovani, importovani - pomocne"""
```

## Jak budeme postupovat
Jakmile mame oba soubory otevrene, nachystame si hlavni body pro `hlavni.py`:
```python
# hlavni.py

# hlavni funkce
    # volani funkce pro nahrati souboru
    # volani funkce pro vytvoreni noveho adresare
    # volani funkce vytvoreni souboru
```
...a hlavni body pro soubor `pomocne.py`:
```python
# pomocne.py

# Funkce pro nahrani souboru
# Funkce pro vytvoreni adresare
# Funkce pro vytvoreni souboru
```

## Prvni krucky
Nasi soubor `hlavni.py` muzeme doplnit o definice funkce `hlavni()`:
```python
# hlavni.py

def hlavni() -> None:
    # volani funkce pro nahrati souboru
    # volani funkce pro vytvoreni noveho adresare
    # volani funkce vytvoreni souboru
```
V souboru `pomocne.py` muzeme doplnit definice funkci s kratkou `print()`
funkci:
```python
# pomocne.py

def nacti_soubor(soubor: str) -> None:
    print(f"NACITAM SOUBOR: {soubor}")

def vytvor_adresar(jmeno: str) -> None:
    print(f"VYTVORIM ADRESAR: {jmeno}")

def vytvor_soubor(jmeno_soubor: str) -> None:
    print(f"VYTVARIM SOUBOR: {jmeno_soubor}")
```
Jde o jednoduchou abstrakci toho, jak by mely oba soubory spolupracovat. Pozdeji
funkcim doplnime radny kod.

## Modul v Pythonu
V podstate jde o soubor s priponou __.py__. Obsahuje promenne, funkce, aj. Tak
jak jsme psali kod doposud.
```python
import <muj_modul>      # obecne
import os               # konkretni priklad
```
Dale muzeme _importovat_ pomoci ohlaseni `from ... import ...`:
```python
from pprint import pprint
```
Je mozne doplnit i __alias__ pomoci klicoveho slova `as`:
```python
from pprint import pprint as pp
```
Pokud je importovanych objektu vice, je vhodne dbat na mnozstvi aliasu, aby byl
ctenar naseho kodu schopen dohledat dany objekt.

### Doplnime nasi ulohu
Doplnime importovani funkci ze souboru `pomocne.py` do naseho souboru
`hlavni.py` a funkce ve spravnem poradi zavolame:
```python
# hlavni.py
from pomocne import nacti_soubor, vytvor_adresar, vytvor_soubor

def hlavni() -> None:
    nacti_soubor("soubor.txt")
    vytvor_adresar("vystupni soubory")
    vytvor_soubor("zamestnanci.csv")

hlavni()
```
Po doplneni oznameni o importovani muzeme spustit soubor `hlavni.py`.

## Balik v Pythonu
Je cela sbirka modulu (tedy *.py* souboru) umistena ve spolecnem adresari,
ktery ma navic jistou hierarchii. Prikladem muze byt standartni balik Pythonu
`json`. Uvnitr adresare s balikem najdeme:
1. [__init.py__](#important-links)
2.  __pycache__
3. Nekolik ruznych __modulu__

### init
Oznacuji adresare na disku, ktere Python pouziva jako baliky.

### pycache
To je slozka, ktera vznika kdyz spoustime kod a interpret jej zkompiluje na
__bytecode__. Nasledne schova zkompilovany kod do tohoto adresare. Ucel je
spustit program, co mozna nejrychleji (za predpokladu, ze jej neupravime).
```python
from <package> import <modul>   # obecne
from json import dumps          # konkr. priklad
```

## Souhrn
Dulezite poznamky k modulum/balikum v ramci Pythonu:
1. Nemusim jej opakovane zapisovat
2. Muzu jej pouzivat na ruznych mistech (v souborech)
3. Kod je prehlednejsi

## Hledani modulu/baliku
Cela procedura hledani modulu ci baliku probiha nasledovne:
1. Python kontroluje jestli neni modul jiz nacteny
2. Pokud nenajde, [hleda](#important-links) jej nejprve pomoci `sys.modules`
3. Pokud nenajde, hleda jej v aktualnim adresari
4. Pokud nenajde, hleda jej v `sys.path`
5. Pokud nenajde, `ModulNotFoundError`
6. Pokud najde, kompilovani + spusteni

## Nacitani souboru
Prvni funkce, kterou chceme definovat je `nacti_soubor()`:
```python
# pomocne.py

def nacti_soubor(soubor: str, mod: str = "r") -> list: 
    try:
        with open(soubor, mod) as txt:
            obsah = txt.readlines()

    except FileNotFoundError:
        print(f"SOUBOR: {soubor} NEEXISTUJE!")

    else:
        return obsah
```
Nasledne doplnime nas soubor `hlavni.py`:
```python
# hlavni.py

def hlavni() -> None:
    jmena = nacti_soubor("jmena_souboru.txt")
    print(f"JMENA: {jmena}")


hlavni()
```

## Vytvoreni prazdne slozky
Dalsi vec, ktere chceme zabranit, aby se nam soubory vytvorily primo
do pracovni slozky. Budeme je chtit umistit do specialni slozky. Nejprve
chceme overit, jestli slozka, kterou chceme vytvorit, neexistuje:
```
os.path.isdir(<jmeno_slozky>)
```
Pomoci modulu `os` muzeme pouzit metodu `isdir()`. Ta vraci `True`, pokud je
zadane jmeno opravdu adresar (podobne funguje `isfile()`):
```python
# pomocne.py
import os

def hlavni() -> None:
    jmena = nacti_soubor(jmena_souboru)
    if not os.path.isdir(jmeno_adresare):
        pass

    else:
        print(f"SLOZKA: {jmeno_adresare} EXISTUJE!")

jmena_souboru = "jmena_souboru.txt"
jmeno_adresare = "vystup"
hlavni()
```
Timto zajistime, ze pokud slozka jiz existuje, muzeme ji pouzit. Pokud ne,
vytvorime novou. Novou prazdnou slozku opet vytvorime pomoci modulu `os`.
Pomoci funkce `mkdir` muzeme specifikovat jmeno adresare do kulate zavorky:
```
os.mkdir(<jmeno>)
```
Funkci v `pomocne.py` definujeme takhle:
```python
# pomocne.py

def vytvor_adresar(jmeno: str) -> None:
    os.mkdir(jmeno)
```
Z funkce si necham vratit promennou `jmeno`, ktera obsahuje ulozeny `str` se
jmenem. Soucasne pouzijeme `getcwd()` funkci, ktera nam vypise absolutni
cestu k aktualnimu pracovnimu adresari (neni povinne).

## Jak vytvorim soubor
Nyni se podivame na funkci `vytvor_soubor()`. K tomu abychom vytvorili soubor
potrebujeme dve veci:
1. __Jmeno__ souboru
2. __Absolutni cestu__ pro umisteni nebo __jmeno__ slozky

Rekneme tedy, ze chceme vytvorit soubor `tabulky.csv` do aktualniho pracovniho
adresare:
```
abs_cesta = "/home/absolutni/cesta/lekce10/"
jmeno = "tabulky.csv"
```
Takze pomoci pseudokodu bude prikaz vypadat nasledovne:
```python
novy_soubor = abs_cesta + jmeno

with open(novy_soubor, "w") as soub:
    ...
```

### Skutecna funkce
Nejprve musime v souboru `hlavni.py` spojit absolutni cestu do pracovni slozky
a jmeno cilove slozky:
```
os.path.join(<abs_cesta>, <cil_adresar>)
```
Definujeme funkci v souboru `pomocne.py`:
```python
...
def vytvor_soubor(jmeno_so: str) -> None:
    if not os.path.isfile(jmeno_so):
        with open(jmeno_so, "w") as soub:
            print(f"VYTVARIM: {jmeno_so}")
        print("HOTOVO!")

    else:
        print(f"SOUBOR: {jmeno_so} EXISTUJE!")
```
Po te doplnime funkci `hlavni` v souboru `hlavni.py`:
```python
# hlavni.py
import os

from pomocne import nacti_soubor
from pomocne import vytvor_adresar
from pomocne import vytvor_soubor


def hlavni() -> None:
    jmena = nacti_soubor(jmena_souboru)

    if not os.path.isdir(jmeno_adresare):
        vytvor_adresar(jmeno_adresare)
        vytvor_soubor(os.path.join(jmeno_adresare, jmena[0])

    else:
        print(f"SLOZKA: {jmeno_adresare}, EXISTUJE!")
    

jmena_souboru = sys.argv[1]
jmeno_adresare = sys.argv[2]
hlavni()
```

## Existujici soubory
Muze nastat situace, kdy existuje nejenom adresar `vystup` ale i nektere soubory
v nem. Proto je nutne situaci osetret vsestrannejsi funkci:
```python
# pomocne.py
...
def vytvor_vsechny_soubory(vsechna_jm: list, jmeno_adresare: str) -> None:
    for jmeno in vsechna_jm:
        vytvor_soubor(
            os.path.join(os.path.abspath(jmeno_adresare), jmeno.strip()))
```
Predchozi kod je nova funkce do souboru `pomocne.py`. Nyni importujeme a
zavolame tuto funkci uvnitr soubor `hlavni.py`:
```python
# hlavni.py
import os

from pomocne import nacti_soubor
from pomocne import vytvor_adresar
from pomocne import vytvor_vsechny_soubory


def hlavni() -> None:
    jmena = nacti_soubor(jmena_souboru)

    if not os.path.isdir(jmeno_adresare):
        vytvor_adresar(jmeno_adresare)
        vytvor_vsechny_soubory(jmena, jmeno_adresare)

    else:
        print(f"SLOZKA: {jmeno_adresare}, EXISTUJE!")
        vytvor_vsechny_soubory(jmena, jmeno_adresare)
    

jmena_souboru = sys.argv[1]
jmeno_adresare = sys.argv[2]
hlavni()
```

## Moduly tretich stran
Pro praci s moduly tretich stran muzeme pracovat v __terminalu__ nebo primo v
__editoru__:

### Terminal
Vytvorim si virtualni pracovni prostredi:
```
python3 -m venv <jmeno_prostredi>     # obecne
```
Aktivuji moje pracovni virtualni prostredi:
```
source <jmeno_prostredi>/bin/activate       # obecne
```
Jakmile prostredi aktivujeme, muzeme si vsimnout kulate zavorky na zacatku
radku s jmenem prostredi uvnitr.
```
(jmeno_prostredi) matous@matous:~/$ deactivate   # ukoncim virt. prostredi
matous@matous:~/projects/python_academy        # -> jmena prostredi nevidim
```
Najdu modul, ktery se mi hodi. Bud vime, co hledame, pripadne pouzijeme
[pypi.org](https://pypi.org). Stahuji + instaluji (pomoci
[pipu](#important-links) -> package installer):
```
pip install requests-html       # instalace
pip uninstall requests-html     # odstraneni
```
Zkontroluji, ktere moduly mam pro svuj aktualni projekt dostupne a zapisu je
do .txt souboru:
```
pip freeze > requirements.txt
```

### Pycharm
- [Spustime](#important-links) Pycharm a otevreme projekt
- -> Settings
- -> Project: <jmeno_projektu>
- -> Project interpreter
- Vedle tabulky nahore + vpravo je symbol *+*
- Vyhledame modul/balik

## if __name__ == "__main__"
Konstrukce, ktera nam umozni bezkonfliktne [importovat](#important-links)
soubory i jejich obsah a pritom nedojde ke spusteni celeho souboru. Takze pokud
spoustim __.py__ soubor, ulozim do promenne `__name__` hodnotu `__main__`.
Naopak pokud soubor importuji, tato situace nenastane.
```python
def hlavni():
    print("Spoustim hlavni funkci()")
    print("Volani prvni funkce...")
    funkce_1()
    print("Volani druhe funkce...")
    funkce_2()
    print("Volani treti funkce...")
    funkce_3()


def funkce_1():
    print("Spousteni prvni funkce...")


def funkce_2():
    print("Spousteni druhe funkce...")


def funkce_3():
    print("Spousteni treti funkce...")
```
Pokud soubor importuji (.py!) nastavi hodnotu `__name__` jako jmeno souboru.
```python
if __name__ == "__main__":
    print("Spousteni pres importovani")
    hlavni()
else:
    print("Naimportovano!")
```

## Jak toho vyuzit
Mrkneme se na nas program. Nebylo by prijmnejsi zadavani jmena textoveho souboru
se jmeny zadat rucne? Pripadne jmeno slozky pro nase soubory? Pomoci modulu
`sys` si muzeme upravit nas program:
```python
# hlavni.py
import sys

...

if len(sys.argv) != 3:
    print("POUZITI: python hlavni.py <txt_soubor> <jmeno_adresare>")

else:
    jmena_souboru = sys.argv[1]
    jmeno_adresare = sys.argv[2]
    hlavni()
```
Cely soubor `hlavni.py` pak bude vypadat nasledovne:
```python
import os
import sys

from pomocne import nacti_soubor
from pomocne import vytvor_adresar
from pomocne import vytvor_vsechny_soubory


def hlavni() -> None:
    jmena = nacti_soubor(jmena_souboru)

    if not os.path.isdir(jmeno_adresare):
        vytvor_adresar(jmeno_adresare)
        vytvor_vsechny_soubory(jmena, jmeno_adresare)

    else:
        print(f"SLOZKA: {jmeno_adresare}, EXISTUJE!")
        vytvor_vsechny_soubory(jmena, jmeno_adresare)


if len(sys.argv) != 3:
    print("POUZITI: python hlavni.py <txt_soubor> <jmeno_adresare>")

else:
    jmena_souboru = sys.argv[1]
    jmeno_adresare = sys.argv[2]
    hlavni()
```

Pokracovat na [Lekci#11](https://github.com/Bralor/python-academy/tree/lekce11)

