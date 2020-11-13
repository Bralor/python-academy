➡ [vratit se na prvni lekci](https://github.com/Bralor/python-academy/tree/lekce01)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 2⃣ Python akademie
### 🗒 Dulezite odkazy
- [Engeto.com](https://engeto.com/cs/)
- [Python Academy, Git](https://engeto.com/cs/kurz/git-zaklady-pro-uzivatele/lekce)
- [Python Academy, zaciname!](https://engeto.com/cs/kurz/python-academy/studium/SpmtH-mVRY6zPL9alhruMQ/home-set-up/basics-of-command-line)
- [Python, dokumentace zabudovanych funkci](https://docs.python.org/3/library/functions.html)
---

### 🗒 Obsah lekce
1. Ukazka ulohy
2. Doplnime ulohu z [prvni lekce]()
3. Python, prace
4. Boolean
5. Podminkovy zapis
6. Ukonceni kodu
7. Metody datovych typu
---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si druhou lekci jako **zip**](https://github.com/Bralor/python-academy/archive/lekce02.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **destinatio_p2** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

## Rozsirime zadani naseho programu
Budeme chtit vytvorit soupis lokalit, ktere pokud uzivatel vybere, dostane slevu.

```python
SLEVY = ("Olomouc", "Svitavy")
```

## Prvni podminka
Prvnim krokem, u ktereho bude potreba rozhodovat, je samotne cislo lokality.
Chceme v podstate zabranit tomu, aby uzivatel zadal takove cislo, ktere nemame
na vyber. Tedy cokoliv mensiho nez 1 a vetsi nez 6.

Obecne:
```python
por_cislo = int(input("Vyberte cislo lokality: "))
# Promenna *por_cislo* > 0 a *por_cislo* <= 6 
```
## Pravda nebo ne?
Abychom byli schopni rozlisit, co je v Pythonu pravda a neni, budeme se muset
seznamit s datovym typem _boolean_. Je to dalsi typ jako byl retezec, desetinne
cislo, atd. Castence spada pod _integer_ (tedy specialne hodnoty 1 a 0). V
Pythonu je ale casteji oznacujeme textovym popiskem __True(1)__ a __False(0)__.
Jejich ucelem je rozhodovat v testovaci procedure, zda-li je nejaky vyraz
[pravdivy](https://engeto.com/cs/kurz/online-python-akademie/studium/9roGO2_ITGaLbq-X-KGT7w/rozhodujeme/datovy-typ-boolean/co-je-to-boolean)
nebo ne.

Ukazka:
```python
bool(1)  # True
bool(0)  # False
```

## Logicke operatory
Boolean hodnoty souvisi s pouzitim [logickych operatoru](https://engeto.com/cs/kurz/online-python-akademie/studium/rh38CL2fRmmOBqJt312GOA/rozhodujeme/datovy-typ-boolean/logicke-operace):
1. __and__
2. __or__
3. __not__

```python
bool(True and True)     # True, viz. tabulka zadani
bool(True and False)    # False
bool(False and False)  # False

bool(True or True)      # True
bool(True or False)     # True
bool(False or False)     # False

bool(not True)      # False
bool(not False)     # True
```

## Podminkovy zapis
Pro pouziti
[podminkoveho zapisu](https://engeto.com/cs/kurz/online-python-akademie/studium/EBuXiFdpSKK96n6Eds4cgA/rozhodujeme/python-rozhoduje/podminky-if)
musime dodrzet nasledujici kroky:
1. Klicove slovo __if__
2. Vytvorit __bool()__ test
3. Radek ukoncit dvojteckou __:__
4. Nasledujici radek psat _odsazeny_

Ukazka __if-else__:
```python
A = 10_000
B = 15_000

if A > B:
    print("PRAVDA! A je mensi nez B")           # Vypis toto, pokud je bool -> True
else:
    print("NENI PRAVDA! A neni vetsi nez B")    # Vypis toto, pokud je bool -> False
```

## Zapiseme prvni podminku
<p align="center">
  <img src="https://media.giphy.com/media/l2Je57ilZJPzNkeXK/source.gif" width="300" height="300">
</p>

Takze pomoci teorie o podminkovem zapise v nasem souboru vytvorime prvni
podminku:
```python
por_cislo = int(input("Vyberte cislo lokality: "))

if por_cislo < 1 or por_cislo > 6:
    print("Vami vybrane cislo neni v nabidce, ukoncuji")
    # ukoncuji
else:
    destinace = SEZNAM_MEST[por_cislo - 1]
    cena = SEZNAM_CEN[por_cislo - 1]
    print(f"DESTINACE: {destinace}")
    print(ODDELOVAC)
```

## Jak ukoncime program? 
Pokud uzivatel nejakou podminku pri zadavani nesplni, chceme automaticky
program ukoncit. Budeme pouzivat tzv. _ukoncovaci oznameni_. Jde o formu
ukonceni prubehu naseho souboru. V Pythonu je vic moznosti jak ukonceni
vyvolat (__quit()__/__exit()__).(pozn. oba tyto prikazy vychazi ze stejneho
principu) 

__Priklad__:
```python
...
if por_cislo < 1 or por_cislo > 6:
    print("Vami vybrane cislo neni v nabidce, ukoncuji")
    exit()
    ...
```

## Aplikujeme prepocet slev
Po poradovem cislu chceme aplikovat vypocet mozne slevy. Nejprve je nutne
zjistit, jestli se konkretni lokalita nachazi v destinacich se zlevnenym
jizdnym.

### Overeni clenstvi
Jde o formu dotazu, kdy se ptame, jestli je nejaky udaj
[soucasti](https://engeto.com/cs/kurz/online-python-akademie/studium/tR_PX2qoQw68kXQKe1q1fg/zaciname-s-pythonem-datove-typy/operace-se-sekvencemi/pritomnost-prvku-membership-test)
sekvence jako je retezec, seznam, tuple. Klicovym pojmem v tomto overovani
je __in__.

__Priklad__:
```bash
"Matous" in ["Matous", "Marek", "Lukas", "Jan"]  # True
```

## Zapiseme dalsi podminku
Nase varianta se slevou bude vypada nasledovne:
```python
if destinace in SLEVY:
    cena_po_sleve = 0.75 * cena
else:
    cena_po_sleve = cena
```


## Overime jmeno a prijmeni
Nyni se chceme ujistit, ze symboly zadane do promennych *jmeno* a *prijmeni*
jsou slozene pouze z pismen. Pokud chceme podobnym zpusobem pracovat s
retezci, muzeme se podivat, jestli nami hledane upravy nezahrnuji
stavajici _metody retezcu_.

Kde hledat jmena metod:
```bash
help(str)  # Napoveda pro retezce
```

Vystup:
```
...
 |  isalpha(...)
 |      S.isalpha() -> bool
 |      
 |      Return True if all characters in S are alphabetic
 |      and there is at least one character in S, False otherwise.
 |  
...
```
Obecne pouziti metod (nejen pro retezce):
```python
<jmeno_promenne><.><jmeno_metody><()>
```

__Priklad__:
```bash
"matous".isalpha()      # True
"m@tous".isalpha()      # False
"mat0us".isalpha()      # False
```

Takze muzeme dopsat overovaci cast k promennym __jmeno__ a __prijmeni__:
```python
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")

if jmeno.isalpha() and prijmeni.isalpha():
    print(f"JMENO: {jmeno}, PRIJMENI: {prijmeni}")
    print(ODDELOVAC)
else:
    print("Jmeno a prijmeni musi obsahovat pouze pismena, ukoncuji")
    exit()
```

## Overeni veku
Dalsi podminkovy zapis bude overovat vek potencialniho uzivatele, abychom
zamezili pouzivani mladsim 18ti let.

__Obecne__:
```
<aktualni_rok>-<vek> > 18
```

__Dopiseme__:
```python
AKT_ROK = 2020
vek = int(input("ROK NAROZENI: "))

if (AKT_ROK - vek) >= 18:
    print(f"Pokracuji...")
    print(ODDELOVAC)
else:
    print("Nase sluzby mohou vyuzivat pouze osoby starsi 18 let, ukoncuji")
    exit()
```

## Kontrola emailove adresy
Pro kontrolu emailu bude stacit zjistit, jestli zadany email obsahuje symbol zavinace (*@*). Tudiz se ptam, jestli promenna neobsahuje konkretni [symbol](###-overeni-clenstvi).

__Dopiseme__:
```python
email = input("EMAIL: ")

if "@" in email:
    print("Email v poradku, pokracuji...")
    print(ODDELOVAC)
else:
    print("Nepodporovany format emailu, ukoncuji")
    exit()
```

## Kontrola hesla
Kontrola hesla bude komplikovanejsi. Aby bylo heslo platne, bude muset
splnovat nasledujici:
1. Musi byt delsi nez 8 symbolu
2. Musi obsahovat pismena
3. Musi obsahovat cislice

### Vestavena funkce __len()__
Jde o preddefinovanou funkci, ktera slouzi k [pocitani prvku](https://engeto.com/cs/kurz/online-python-akademie/studium/MCDGtwdxTn2GMv5sfPvXQA/zaciname-s-pythonem-datove-typy/operace-se-sekvencemi/zjisteni-delky-lenght) v udaji.

Priklad:
```python
len("matous")           # 6
len(["a", "b", "c"])    # 3
```

Prvni cast podminky:
```python
if len(heslo) >= 8 ...
```

### Pismena a cislice
Za timto ucelem opet prohledame dostupne [metody](#kontrola-jmeno-a-prijmeni)

### Nektere metody retezcu
Jde o metody, ktere nam pomahaji/usnadnuji praci s retezci.
1. __S.isalpha()__ --> vraci True, pokud jsou vsechny znaky v __S__ pismena
2. __S.isnumeric()__ --> vraci False, pokud jsou vsechny znaky v __S__ ciselne

__Priklad__:
```bash
"Matous".isalpha()      # True
"M@tous".isalpha()      # False
"Mat0us".isalpha()      # False
"7350".isalpha()        # False
"7350".isnumeric()      # True
```

__Doplnime__:
```python
if len(heslo) >= 8 and not heslo.isalpha() and not heslo.isnumeric():
    print("Heslo v poradku")
    print(ODDELOVAC)
    print("UZIVATEL: " + jmeno)
    print("DESTINACE: " + destinace)
    print("CENA(cil:" + destinace + "): " + str(cena_po_sleve))
    print(f"Jizdenku posleme na Vasi emailovou adresu: {email}")

else:
    print(
    """
    Tvoje heslo je spatne zadane:
	1. Musi obsahovat alespon 8 znaku,
	2. Musi obsahovat pismena,
    3. Musi obsahovat cislice
    """
    )
```

## Slozitejsi podminkova vetev
Nami zapsane podminkove vetve byly pomerne strucne. Prakticky se muze stat,
ze budeme potrebovat rozhodovaci proces delsi nez proste __bud__ a __nebo__.

Ukazka __if-elif-else__:
```python
METRO = False               # bool
POCET_OBYVATEL = 374_734    # integer

if POCET_OBYVATEL < 100_000:
    print("Jde o male mesto")

elif POCET_OBYVATEL < 300_000:
    print("Jde o velke mesto")

elif POCET_OBYVATEL == 374_734 and METRO == False:
    print("Jasne BRNO!")
```

Pokracovat na [Lekci#03](https://github.com/Bralor/python-academy/tree/lekce03)

