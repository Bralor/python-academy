Minula lekce[lekce#01](https://github.com/Bralor/python-academy/tree/lekce01)

<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lekce 02
## Dulezite odkazy
- [Python Academy, lekce](https://engeto.com/cs/kurz/python-academy/lekce)
- [Python Academy, muj repozitar](https://github.com/Bralor/python-academy)
- [Python Academy, muj repozitar, lekce#01](https://github.com/Bralor/python-academy/tree/lekce01)

## Co nas dnes ceka?
V navaznosti na minulou lekci se budeme snazit nas program (Destinatio) zdokonalit. Soucasti naseho vylepsovani bude patrit teorie k boolean hodnotam, logickym operatorum a zaklady k podminkovemu zapisu.

## Co bude vysledkem?
Po spusteni by mel program vypadat nasledovne (nebo viz. demo):
```bash
$ destinatio
```
Dostaneme nasledny vypis:
```bash
===================================
Vitejte u nasi aplikace Destinatio!
===================================

1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180

===================================
Vyberte cislo lokality: 3
DESTINACE: Olomouc
===================================
JMENO: Matous
PRIJMENI: Holinka
JMENO: Matous, PRIJMENI: Holinka
===================================
ROK NAROZENI: 1992
Pokracuji...
===================================
EMAIL: matous@matous.cz
Email v poradku, pokracuji...
===================================
HESLO: panpes738
Heslo v poradku
===================================
UZIVATEL: Matous
DESTINACE: Olomouc
CENA(cil:Olomouc): 90.0
Jizdenku posleme na Vasi emailovou adresu: matous@matous.cz
```

## Co budeme potrebovat?
- Python 3.6+
- textovy editor (dle uvazeni/doporuceni)
- vystup z [prvni lekce](https://github.com/Bralor/python-academy/blob/lekce01/destinatio_p1.py)
- vytvorit si novy soubor ve svem pracovnim adresari

## Pokracujeme s kodem!

<p align="center">
  <img src="https://media.giphy.com/media/XbV2l8rk7wGKbQlpPM/source.gif" width="300" height="300">
</p>

Otevreme nas novy pracovni soubor a vlozime zapis z posledni lekce.

## Rozsirime zadani naseho programu
Budeme chtit vytvorit soupis lokalit, ktere pokud uzivatel vybere, dostane slevu.

```python
SLEVY = ("Olomouc", "Svitavy")
```

## Prvni podminka
Prvnim krokem, u ktereho bude potreboa rozhodovat, je samotne cislo lokality. Chceme v podstate zabranit tomu, aby uzivatel zadal takove cislo, ktere nemame na vyber. Tedy cokoliv mensiho nez 1 a vetsi nez 6.

Obecne:
```python
por_cislo = int(input("Vyberte cislo lokality: "))
# Promenna *por_cislo* > 0 a *por_cislo* <= 6 
```
## Pravda nebo ne?
Abychom byli schopni rozlisit, co je v Pythonu pravda a neni, budeme se muset seznamit s datovym typem _boolean_. Je to dalsi typ jako byl retezec, desestinne cislo, atd. Castence spada pod _integer_ (tedy specialne hodnoty 1 a 0). V Pythonu je ale casteji oznacujeme textovym popiskem __True(1)__ a __False(0)__. Jejich ucelem je rozhodovat v testovaci procedure, zda-li je nejaky vyraz [pravdivy](https://engeto.com/cs/kurz/online-python-akademie/studium/9roGO2_ITGaLbq-X-KGT7w/rozhodujeme/datovy-typ-boolean/co-je-to-boolean) nebo ne.


## Logicke operatory
Bool hodnoty souvisi s pouzitim logickych operatoru:
-[and](https://engeto.com/cs/kurz/online-python-akademie/studium/rh38CL2fRmmOBqJt312GOA/rozhodujeme/datovy-typ-boolean/logicke-operace)
-or
-not

## Podminkovy zapis
Pro pouziti [podminkoveho zapisu](https://engeto.com/cs/kurz/online-python-akademie/studium/EBuXiFdpSKK96n6Eds4cgA/rozhodujeme/python-rozhoduje/podminky-if) musime dodrzet nasledujici kroky:
1. Klicove slovo _if_
2. Vytvorit bool() test
3. Radek ukoncit dvojteckou
4. Nasledujici radek psat odsazeny

Priklad I.:
```
A = 10_000
B = 15_000

if A > B:
    print("PRAVDA! A je mensi nez B")  # True
else:
    print("NENI PRAVDA! A neni vetsi nez B")  # False
```

Priklad II.:
```
METRO = False               # bool
POCET_OBYVATEL = 374_734    # integer

if POCET_OBYVATEL < 100_000:
    print("Jde o male mesto")

elif POCET_OBYVATEL < 300_000:
    print("Jde o velke mesto")

elif POCET_OBYVATEL == 374_734 and METRO == False:
    print("Jasne BRNO!")

```

## Ukoncovaci oznameni
Jde o formu ukonceni prubehu naseho souboru. V Pythonu je vic moznosti jak ukonceni vyvolat (quit()/exit()). Vice info v odkazu na uvod.

Priklad:
```
VEK = 19

if VEK > 18:
    print("USPECH! Pokracuji...")
else:
    print("NEUSPECH! Ukoncuji...")
    exit()
```
## Overovani clenstvi
Jde o dotazovaci strukturu, kdy se ptame jestli je nejaky udaj [soucasti](https://engeto.com/cs/kurz/online-python-akademie/studium/tR_PX2qoQw68kXQKe1q1fg/zaciname-s-pythonem-datove-typy/operace-se-sekvencemi/pritomnost-prvku-membership-test) sekvence jako je string, list, tuple. Klicovym pojmem v tomto overovani je _in_.

Priklad:
```
>>> "Matous" in ["Matous", "Marek", "Lukas", "Jan"]
True
```

## Nektere metody retezcu
Jde o metody, ktere nam pomahaji/usnadnuji praci s retezci.
1. S.isalpha() --> vraci True, pokud jsou vsechny znaky v S pismena
2. S.isnumeric() --> vraci False, pokud jsou vsechny znaky ciselne

Priklad:
```
>>> "Matous".isalpha()
True
>>> "M@tous".isalpha()
False
>>> "Mat0us".isalpha()
False
>>> "7350".isalpha()
False
>>> "7350".isnumeric()
True

```

## len()
Jde o preddefinovanou funkci, ktera slouzi k [pocitani prvku](https://engeto.com/cs/kurz/online-python-akademie/studium/MCDGtwdxTn2GMv5sfPvXQA/zaciname-s-pythonem-datove-typy/operace-se-sekvencemi/zjisteni-delky-lenght) v udaji.

Priklad:
```
>>> len("Matous")
6
>>> len(["zena", "ruze", "pisen", "kost"])
4
```
