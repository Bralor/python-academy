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
nekolika souboru.
1. Moduly, v Pythonu
2. Baliky, v Pythonu
3. Proces importovani v Pythonu
4. Standartni moduly
5. Moduly tretich stran
6. if \_\_name\_\_ == "\_\_main\_\_", konstrukce

## Vytvareni souboru
Budeme v situaci, kdy dostaneme jako vstupni udaj textovy soubor. V tomto
souboru jsou jmena a jejich pripony. Za pomoci tohoto souboru budeme chtit
vytvorit skutecne soubory (staci prazdne) do uzivatelem zadaneho adresare.

## Ukazka na uvod
Spustime skript v adresari:
```
$ ./soubory_z_txt
```
A dostaneme nasledujici vystup, pokud jsme adresar se soubory jeste nevytvorili:
```
<USPECH>
Vytvarim /home/mholinka/projects/python_academy/lesson11/pokus/outlook_2016.pptx
Vytvarim /home/mholinka/projects/python_academy/lesson11/pokus/icon_53456.jpg
Vytvarim /home/mholinka/projects/python_academy/lesson11/pokus/summary_2019.pptx
...
```
...pripadne takovy vystup, pokud slozka jiz existuje.
```
<NEUSPECH>
ADRESAR JIZ EXISTUJE! (/home/mholinka/projects/python_academy/lesson11/pokus)
SOUBORY NELZE VYTVORIT! VRACENA HODNOTA --> False
```

#Spousteni:
#```
#$ python <jmeno_souboru> "<prazdna_slozka>" "<txt_s_jmeny>"  # obecne
#$ python hlavni.py "/home/mholinka/projects/python_academy/lesson11/pokus" "/home/mholinka/projects/python_academy/lesson11/jmena_souboru.txt"
#```


## Co budeme potrebovat?
- python 3.6+
- text. editor/IDE
- [for smycky](https://github.com/Bralor/python-academy/tree/lekce05)
- [funkce v Pythonu](https://github.com/Bralor/python-academy/tree/lekce06)
- [prace s text. soubory](https://github.com/Bralor/python-academy/tree/lekce08)
- [handlovani chyb](https://github.com/Bralor/python-academy/tree/lekce09)

## Postup
Do pracovniho adresare si nakopirujeme vstupni textovy soubor, se kterym
budeme chtit pracovat `jmena_souboru.txt`. Dale si otevreme novy soubor,
ktery pojmenujeme `hlavni.py` a dalsi soubor `pomocne`.
```python
#!/usr/bin/python3
"""Lekce #11 - Uvod do programovani, importovani - hlavni"""
```
Pro pomocne funkce vytvorime dalsi soubor:
```
#!/usr/bin/python3
"""Lekce #11 - Uvod do programovani, importovani - pomocne"""
```
Jakmile mame oba soubory otevrene, nachystame si hlavni body pro `hlavni.py`:
```python
# hlavni.py

def hlavni() -> None:
    # volani funkce pro nahrati souboru
    # volani funkce vytvoreni souboru
```
...a hlavni body pro soubor `pomocne.py`:
```python
# pomocny.py

# Funkce pro nahrani souboru
# Funkce pro vytvoreni souboru
```
Takze nas soubor `pomocne.py` by mohl zacit nasledovne:
```python
def nacti_soubor(soubor: str, mod: str = "r") -> list:
    print(f"Nacitam soubor: {soubor}")

def vytvor_soubor(jmeno_soubor: str, abs_cesta: str) -> None:
    print(f"Vytvarim soubor: {jmeno_soubor}")
```
Nez si ale zacneme importovat pojdme si o importovani neco rict.

## Na uvod 
### Modul
V podstate jde o soubor s priponou ".py". Obsahuje promenne, funkce, aj. Tak
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
Pokud se importovanych objektu vice, je vhodne dbat na mnozstvi aliasu, aby byl
ctenar naseho kodu schopen dohledat dany objekt.

Doplnime importovani do naseho souboru `hlavni.py`:
```python
# hlavni.py
from pomocne import nacti_soubor, vytvor_soubor

def hlavni() -> None:
    nacti_soubor("soubor.txt")
    vytvor_soubor("zamestnanci.csv", "/home/Documents")


hlavni()
```

### Balik
Je cela sbirka modulu (tedy *.py* souboru) umistena ve spolecnem adresari,
ktery ma navic jistou hierarchii. Uvnitr adresare najdeme soubor:
1. [__\_\_init\_\_.py__](#important-links)
2.  __\_\_pycachce\_\_.py__

### init
Oznacuji adresare na disku, ktere Python pouziva jako baliky.

### pycache
To je soubor, ktery vznika kdyz spoustime kod a interpret jej zkompiluje na
__bytecode__ a schova je do toho adresare. Ucel je spustit program, co mozna
nejrychleji (za predpokladu, ze jej neupravime).
```python
from <package> import <modul>   # obecne
from collections import List    # konkr. priklad
```

## Souhrn
Dulezite poznamky k modulum/balikum v ramci Pythonu:
1. Nemusim jej opakovane zapisovat
2. Muzu jej pouzivat na ruznych mistech (v souborech)
3. Kod je prehlednejsi

## Importovani, obecne
Pokud chci modul pouzit, musim jej nejprve _importovat_. Cela procedura hledani
modulu nebo baliku probiha nasledovne:
1. Python kontroluje jestli neni modul jiz nacteny
2. Pokud neni, [hleda](#important-links) jej:
2. V built-in modulech
4. V aktualnim adresari
5. Pomoci `sys.path`
6. `ModulNotFoundError` -> soubor nenalezen
7. Kompilace + spusteni -> soubor nalezen
```python
import sys
sys.modules         # slovnik s zabudovanymi moduly
sys.path            # adresare, kde algorytmus hleda
```

## Moduly tretich stran
Pro praci s moduly tretich stran muzeme pracovat v __terminalu__ nebo primo v
__editoru__:

### Terminal
Vytvorim si virtualni pracovni prostredi:
```
python3 -m venv <jmeno_prostredi>     # obecne
python3 -m venv python_academy        # priklad
```
Aktivuji moje pracovni virtualni prostredi:
```
source <jmeno_prostredi>/bin/activate       # obecne
source python_academy/bin/activate          # v nasem pripade
```
Jakmile prostredi aktivujeme, muzeme si vsimnout kulate zavorky na zacatku
radku s jmenem prostredi uvnitr.
```
(python_academy) matous@matous:~/$ deactivate   # ukoncim virt. prostredi
matous@matous:~/projects/python_academy        # -> jmena prostredi nevidim
```
__Pozn.__ Pro ukonceni prace ve virtualnim prostredi staci napsat prikaz
`deactivate`.

Najdu modul, ktery se mi hodi. Bud mame vime, co hledame, pripadne pouzijeme
[pypi.org](https://pypi.org).

Stahuji + instaluji (pomoci [pipu](#important-links) -> package installer):
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

