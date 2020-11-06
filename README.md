➡ [vratit se na treti lekci](https://github.com/Bralor/python-academy/tree/lekce03)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 4⃣ Python akademie
### 🗒 Dulezite odkazy
- [Python Academy, Engeto](https://engeto.com/)
- [Walrus operator, dokumentace](hhttps://www.python.org/dev/peps/pep-0572/)
---

### 🗒 Obsah lekce
1. Ukazka ulohy
2. Vstupni data
3. Uvodni vypisovani
4. While cyklus
5. Nekonecna smycka
6. Walrus operator
---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si ctvrtou lekci jako **zip**](https://github.com/Bralor/python-academy/archive/lekce04.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **kosik** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
  <summary> Vstupni data</summary>

---

</details>

---

<details>
  <summary> Uvodni vypisovani</summary>

---

</details>

---

<details>
  <summary> While cyklus</summary>

---

</details>

---

<details>
  <summary> Nekonecna smycka</summary>

---

</details>

---

<details>
  <summary> Walrus operator</summary>

---

</details>

---

➡ [pokracovat na dalsi (05) lekci](https://github.com/Bralor/python-academy/tree/lekce05)

## Co nas dnes ceka?
Doposud jsme se snazili kazdy udaj zadat rucne. Kazde oznameni v
kodu melo svuj prislusny radek. Ode dneska se budeme snazit zapis trochu
automatizovat. Probereme spolecne prvni typ smycek v Pythonu. Bude to
tzv. cyklus `while`, o kterem se budeme podrobneji bavit a naucime se
ho pouzivat.

## Nakupni kosik
V ramci dnesni hodiny se budeme snazit vytvorit virtualni nakupni kosik, do
ktereho budeme moci jako zakaznik vkladat zbozi z nabidky. Nas kosik bude umet
vypisovat celkovou hodnotu zbozi v kosiku a soucasne ukazovat, jaky je jeho
obsah.

## Ukazka
Po spusteni by mel program vypadat nasledovne:
```bash
$ ./nakupni_kosik
```
Cela ukazka z terminalu: 
```
VITEJTE V NASEM VIRTUALNIM OBCHODE!
========================================
VYBERTE SI Z NASEHO ZBOZI:
========================================
POTRAVINA: pomeranc,    CENA: 15
POTRAVINA: jablko,      CENA: 10
POTRAVINA: chleb,       CENA: 20
POTRAVINA: jogurt,      CENA: 10
POTRAVINA: banan,       CENA: 30
POTRAVINA: maso,        CENA: 100
POTRAVINA: mleko,       CENA: 30
========================================
VYBERTE ZBOZI: maso
VYBERTE ZBOZI: maso
*MASO* NENI SKLADEM!
VYBERTE ZBOZI: mleko
VYBERTE ZBOZI: banan
VYBERTE ZBOZI: jablko
VYBERTE ZBOZI: exit
========================================
        KOSIK JE PLNY! UKONCUJI
========================================
          CELKOVA CENA: 170,-
========================================
```

## Co budeme potrebovat? 
- python 3.8! (kvuli novemu operatoru)
- text. editor
- [podminky](https://github.com/Bralor/python_academy/tree/master/lesson02#podminkovy-zapis)
- [slovnik](https://github.com/Bralor/python_academy/tree/master/lesson03#slovnik)

## Muzeme zacit!
<p align="center">
  <img src="https://media.giphy.com/media/GSrZUFaPs7yCs/giphy-downsized.gif" width="300" height="300">
</p>
Nejprve si vytvorime novy soubor pro dnesni lekci. Po te nakopirujeme zadane
udaje, se kterymi budeme chtit pracovat.

```python
""" Lekce #4 - Uvod do programovani, nakupni kosik """

KOSIK = {}
ODDELOVAC = "=" * 40
POTRAVINY = {
    "mleko": [30, 5],
    "maso": [100, 1],
    "banan": [30, 10],
    "jogurt": [10, 5],
    "chleb": [20, 5],
    "jablko": [10, 10],
    "pomeranc": [15, 10]
}
```
### Vypiseme uvodni text
Na uvod nam bude stacit vypsat, ze kterych potravin zakaznik muze vybirat. Plus
oddelovaci lemovany uvodni text. Prvni kus kodu by mohl vypadat nasledovne:
```python
print(ODDELOVAC)
print("VITEJTE V NASEM VIRTUALNIM OBCHODE!")
print(ODDELOVAC)
print("VYBERTE SI Z NASEHO ZBOZI:")
print(ODDELOVAC)
print(POTRAVINY)
print(ODDELOVAC)
```
Kdyz se koukame na promennou `ODDELOVAC`, zacina byt malicko napadna. Proto
se dneska naucime pouzivat nepovinny atribut funkce `print`. Tim bude `end`.
Jde o volitelny atribut, ktery neni nutne zadavat. Slouzi hlavne k tomu,
abychom na konec toho, co chceme zobrazit mohli doplnit libovolny znak/znaky.
```python
print("Ahoj, ze 4. lekce!", end="\n##################\n")
```
Nyni muzeme prvni vystupni sekci doplnit o nas novy atribut `end` a upravit
tak nasi druhou sekci kodu:
```python
print("VITEJTE V NASEM VIRTUALNIM OBCHODE!", end=f"\n{ODDELOVAC}\n")
print("VYBERTE SI Z NASEHO ZBOZI:", end=f"\n{ODDELOVAC}\n")
pprint(POTRAVINY) # nelze pouzivat *end* u `pprint`
print(ODDELOVAC)
```

## Vybirame zbozi
Nyni se budeme snazit vybrat 3 polozky z promenne `POTRAVINY` a pridat je do
promenne `KOSIK`.

### Nejprve potrebuje vstup...
Abychom meli moznost si vybrat, musime vyuzit funkce `input`:
```python
vyber_potravinu = input("VYBERTE ZBOZI: ")
```
Jakmile jsme vybrali zbozi, musime jej vlozim do promenne `KOSIK` spolecne
s jeho cenou (pouze cenou):
```python
KOSIK[vyber_potravinu] = POTRAVINY[vyber_zbozi][0]
```
Jakmile je potravina v seznamu, zjistime cenu a vypiseme ji:
```python
print(f"CELKEM: {sum(KOSIK.values())} CZK")
```

### Trochu obtiznejsi varianta
Jakmile se nam podari cela procedura zapsat. Vyzkousejme si to cele zopakovat
pro vyber 4 polozek ze zadaneho vyberu.
```python
vyber1 = input("VYBERTE ZBOZI c.1: ")
vyber2 = input("VYBERTE ZBOZI c.2: ")
vyber3 = input("VYBERTE ZBOZI c.3: ")
vyber4 = input("VYBERTE ZBOZI c.4: ")

KOSIK[vyber1] = POTRAVINY[vyber1][0]
KOSIK[vyber2] = POTRAVINY[vyber2][0]
KOSIK[vyber3] = POTRAVINY[vyber3][0]
KOSIK[vyber4] = POTRAVINY[vyber4][0]

print(ODDELOVAC)
print(KOSIK, end=f"\n{ODDELOVAC}\n")
print(f"CELKEM: {sum(KOSIK.values())} CZK", end=f"\n{ODDELOVAC}\n")
```

### Citite prsty?
Predchozi krok byl jeste unosny. Trochu.. Predstavme si ale, ze se budeme
snazit zapsat desitky nebo stovky polozek. Tady uz by situace, kdy budu udaje
opakovane vkladat, zapisovat do slovniku a nasledne jej scitat a vypisovat
neprehledna.

### Jak to obejit?
Na stesti v Pythonu existuje neco, co nam opakovani, takovych kroku zajisti. Je
to prave __cyklus__. Tedy proces, ktery probiha opakovane. V ramci dnesni lekce
se seznamime s prvnim typem smycek.

## While cyklus
Jak uz jmeno prozradi, oznameni teto smycky se schovava za klicovym slovem
`while`. Popiseme si, jak `while` funguje:
```python
while <podminka>:
    # provadej toto pokud je podminka pravdiva (TRUE)
# pokracuj dal, pokud smycka skoncila
```
### Podminka
V zahlavi si muzeme vsimnout pojmu __podminka__. Je to tak, ze smycka probiha,
pokud podminka v zahlavi vraci boolean hodnotu `True`. Jakmile dostane `False`,
cyklus skonci.

### True
Pokud nam podminka vraci `True`, probiha ten kod, ktery je odsazeny hned pod
zahlavim. Tedy v nasem vzoru cast:
```python
    # provadej toto pokud je podminka pravdiva (TRUE)
```
Vsimnete si povinneho odsazeni.

### False
Jakmile nam ale podminka v zahlavi vrati `False`. Cela smycka se ukonci a
nasleduje kod za ni. Tedy:
```python
# pokracuj dal, pokud smycka skoncila
```

### Jednoducha ukazka
Pojdme spolecne mrknout na `while` cyklus v praxi:
```python
x = 0

while x < 10:
    print(f"x={x}; {x}<10, v poradku!")
    x = x + 1

print(f"x={x}; {x}=10, konec smycky, pokracujeme...")
```

## Vyzkousejme while!
Na zaklade toho, co jsme se pred chvili o `while` cyklus rekli, pojdme
upravit nas kod:
```python
while len(KOSIK) < 4:
    vyber_zbozi = input(f"VYBERTE ZBOZI ('q' -> KONEC): ")
    KOSIK[vyber_zbozi] = POTRAVINY[vyber_zbozi][0]
```
Ted uz staci jen dopsat vypocet celkove ceny nakupu. Muzeme pokracovat v kodu
pod smyckou nebo pouzit podminkovou vetev `else`.
```python
while <podminka>:
    <proved pokud podminka -> True>
else:
    <proved pokud podminka -> False>
```
Takze do `else` vetve nasi smycky doplnime vypocet ceny a zobrani obsahu.
```python
else:
    print(ODDELOVAC)
    print("KOSIK JE PLNY! UKONCUJI", end=f"\n{ODDELOVAC}\n")
    print(KOSIK, end=f"\n{ODDELOVAC}\n")
    print(f"CENA CELKEM: {sum(KOSIK.values())} CZK", end=f"\n{ODDELOVAC}\n")
```

### Proc jenom 4 polozky?
Dalsi otazkou zamysleni, je vyber maximalniho poctu polozek pro kosik. Ukoncit
po 3, 4, 5 polozkach? Nechat jej neomezeny? Jak tedy nakup ukoncit? 

### Dokdy podminka probiha?
Na uvod ke smycce `while` jsme si rekli, ze smycka bezi tak dlouho, dokud
podminka vraci `True`. Co kdyz ale explicitne zapisu, ze ma podminka ma
hodnotu `True`?
```python
x = 0

while x < 10:
    print(f"x={x}; {x}<10, v poradku!")

x=0; 0<10, v poradku!
x=0; 0<10, v poradku!
x=0; 0<10, v poradku!
x=0; 0<10, v poradku!
...
<ctrl+C --> ukonci>
```
Muze se mi stat, ze pokud podminku postavim nevhodne, tak vytvorim nekonecnou
smycku. Pripadne tedy muzu mit vytvoreni nekonecne smycky umyslne, potom ale
potrebuji ohlaseni, ktere je schopne prubeh ukoncit.
```python
cislo = 2
prepinac = True

while prepinac:
    cislo = cislo ** cislo
    kontrola = input("PRO UKONCENI NAPIS 'q': ").lower()

    if kontrola == "q":
            prepinac = False
    else:
            print(cislo)
```

### Nase nova nekonecna smycka!

<p align="center">
  <img src="https://media.giphy.com/media/qVVVfmHDMBZug/source.gif" width="300" height="300">
</p>

Nyni pojdme upravit nas kod tak, aby bylo mozne vkladat polozky do nakupniho
kosiku tak dlouho, jak jen uzivatel bude potrebovat.
```python
pokracovat = True                                                               
                                                                                
while pokracovat:                                                               
    vyber_zbozi = input(f"VYBERTE ZBOZI ('q' -> KONEC): ")                      
                                                                                
    if vyber_zbozi == "q":                                                      
        pokracovat = False                                                      
    else:                                                                       
        KOSIK[vyber_zbozi] = POTRAVINY[vyber_zbozi][0]

else:
    print(ODDELOVAC)
    print("KOSIK JE PLNY! UKONCUJI", end=f"\n{ODDELOVAC}\n")
    print(KOSIK, end=f"\n{ODDELOVAC}\n")
    print(f"CENA CELKEM: {sum(KOSIK.values())} CZK", end=f"\n{ODDELOVAC}\n")
```
Je nutne doplnit radny system v podminkove vetvi, jinak nebude funkcionalita
naseho programu dostatecne stabilni.
1. Hlidam si ukonceni programu
2. Hlidame jestli je uzivatelem zadane zbozi ve slovniku `POTRAVINY`
3. Pokud je vsechno predchozi vyhodnoceno `False`, ukladame.

### Co kdyz se spletu?
Muze se stat, ze jako uzivatelem napiseme polozku (jeji jmeno), ktere nebude
skladem, nebo se jen prepiseme. Jak to opravit?
```python
while pokracovat:
    vyber_zbozi = input(f"VYBERTE ZBOZI ('q' -> KONEC): ")

    if vyber_zbozi == "q":
        pokracovat = False
    elif vyber_zbozi not in POTRAVINY.keys():
        print(f"*{vyber_zbozi}* NEMAME SKLADEM!")
    else:
        KOSIK[vyber_zbozi] = POTRAVINY[vyber_zbozi][0]
```

### Ukoncit nebo ne?
Vhodnejsi bude zuzitkovat nasi smycku a misto vypinani celeho kodu, bude
upozorneni, ze nastala chyba a cekat na novy vstup.

### Jak se vratim k smycce?
Pokud je interpret Pythonu u cteni sady kodu, ktera nasleduje po zahlavi, musim
pouzit specialni syntaxi pro preruseni.

### Continue, ohlaseni
Casto se muze hodit vraceni se k podmince smycky a jeji opetovne spusteni.
Ukazeme si to na konkretnim prikladu:
```python
cislo = 0
veta = "Příliš žluťoučký kůň úpěl ďábelské ódy"

while cislo < len(veta):
    pismeno = veta[cislo]

    if pismeno in "říšžťčýůňúěďáéó":
        cislo = cislo + 1
        continue  # zakomentuj pro vysvetleni

    print(pismeno)
    cislo = cislo + 1
```
V nasem prikladu chceme vypisovat pouze pismena, ktera nemaji diakritiku
(neobsahuji hacky a carky). Pokud takove pismeno v nasi promenne `VETA` najdu,
zamerne jej preskocim pomoci ohlaseni `continue`.

### Break, ohlaseni
Podobne ale muze nastat situace, kdy nase smycka na neco narazi a v takovem
pripade chceme cyklus uplne ukoncit.
```python
cislo = 0
veta = "Příliš žluťoučký kůň úpěl ďábelské ódy"

while cislo < len(veta):
    pismeno = veta[cislo]

    if pismeno in "říšžťčýůňúěďáéó":
        cislo = cislo + 1
        break  # zakomentuj pro vysvetleni

    print(pismeno)
    cislo = cislo + 1

else:
    print("Preskakuji `else` vetev")

print("Pokracuji!")
```
Ve druhem prikladu prochazim nasi vetu symbol za symbolem, jako v predchozi
variante a pokud narazim na symbol s diakritikou, smycku ukoncim. Muzete si
vsimnout, ze preskakuji i vetev `else`. Proto je potreba na to pri psani
myslet.

### Doplnime nas kod
Ted, kdyz vime jaka dalsi ohlaseni pro smycky mame k dispozici, pojdme doplnit
nas program. Chceme overit, jestli vybrane zbozi je mezi klici promenne 
`ZBOZI`. Pokud ano, doplnim do `KOSIK`. Pokud ne, vypisu oznameni a
pokracuji dalsi smyckou.

## Walrus operator (Python3.8+!)
Dalsi moznosti jak nas kod upravit je pomoci specialniho
operatoru, tzv. __prirazovaciho__ operatoru (z angl. _walrus operator_).
```python
DATA = dict()

while ((dotaz:=input("JMENO? "))):
    DATA[dotaz] = dotaz.isalpha()
```
### Zkusime zkratit zadavani zbozi
Ted, kdyz tusime jak prirazovaci operator funguje, jej zkusime doplnit do
naseho kodu.
```python
while (vyber_zbozi := input("VYBERTE ZBOZI: ")) != 'q':
    if vyber_zbozi not in POTRAVINY.keys():
        print(f"*{vyber_zbozi}* NEMAME SKLADEM!")
    else:
        KOSIK[vyber_zbozi] = POTRAVINY[vyber_zbozi][0]
else:
    ...
```
Zapis se nam podstatne zkrati, podminka pro zadani potraviny a ukonceni nakupu
se nam presune do zahlavi `while` cyklu.

## Lepsi vypis v uvodu
Pomoci smycky bychom mohli vylepsit zapis v uvodu. Dovedete to?

### Dalsi smycka
Reseni spociva v pouziti dalsi (separatni smycky v uvodu). Nez ji ale zapiseme
podivejme se jaky datovy typ je promenna `POTRAVINY`. Jde o slovnik, takze
abychom jej mohli prochazet, budeme potrebovat metodu `pop`/`popitem`. Ty
bohuzel puvodni slovnik promazou, takze si schvalne vytvorime jeho kopii.
```python
TABULKA = POTRAVINY.copy()
```
Staci pouzit metodu pro slovniky `copy()`, ktera nam zajisti vytvoreni
duplicitniho slovniku.
```python
while TABULKA:
    radek_potravina = TABULKA.popitem()
    print(f"POTRAVINA: {radek_potravina[0]},\tCENA: {radek_potravina[1][0]}")
```

### Co jednotlive kusy zbozi?
Napada vas jak vyresit problem, kdy bude chtit vlozit opakovane nejakou
potravinu do kosiku? Jak na to? 

### Musime pocitat
V zadani mame jako hodnotu seznam. Ten vzdy obsahuje:
1. __I. index__ -> cenu
2. __II. index__ -> pocet na sklade

### Nejprve podminky
Musime rozsirit nase podminky, aby odecitani zbozi bylo provadeno automaticky.
```python
while (vyber_zbozi := input("VYBERTE ZBOZI: ")) != 'q':
    if vyber_zbozi not in POTRAVINY.keys():
        print(f"*{vyber_zbozi}* NEMAME SKLADEM!")

    elif vyber_zbozi not in KOSIK and POTRAVINY[vyber_zbozi][1] > 0:
        KOSIK[vyber_zbozi] = [
            POTRAVINY[vyber_zbozi][0],
            1
        ]

    elif vyber_zbozi in KOSIK and POTRAVINY[vyber_zbozi][1] > 0:
        KOSIK[vyber_zbozi][1]  = KOSIK[vyber_zbozi][1] + 1
        POTRAVINY[vyber_zbozi][1] = POTRAVINY[vyber_zbozi][1] - 1

    elif POTRAVINY[vyber_zbozi][1] == 0:
        print(f"*{vyber_zbozi.upper()}* NENI SKLADEM!")
    ...
```
Podle nasich podminek nyni program zohledni, jestli je jeste zbozi skladem nebo
nikoliv.

### Nove vypocet ceny
No a na zaver doplnim jeste posledni `while` cyklus, ktery mi secte celkovou
```python
...
else:
    print(ODDELOVAC)
    print("KOSIK JE PLNY! UKONCUJI".center(40, " "), end=f"\n{ODDELOVAC}\n")
    index, vysledek = 0, 0

    while index != len(muj_kosik:=list(KOSIK.values())):
        zbozi = muj_kosik[index]
        cena, pocet = zbozi[0], zbozi[1]
        vysledek += cena * pocet
        index += 1

    else:
        print(
            f"CELKOVA CENA: {vysledek},-".center(40, " "),
            end=f"\n{ODDELOVAC}\n"
        )

```

Pokracovat na [Lekci#05](https://github.com/Bralor/python-academy/tree/lekce05)
 
