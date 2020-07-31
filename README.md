Minula [lekce#02](https://github.com/Bralor/python-academy/tree/lekce02)

<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lekce 03
## Dulezite odkazy
- [Python Academy, Engeto](https://engeto.com)
- [Python Academy, minula lekce, repozitar](https://github.com/Bralor/python-academy/tree/lekce02)
- [The Shawshank Redemption](https://www.imdb.com/title/tt0111161/?ref_=fn_al_tt_1)
- [The Godfather](https://www.imdb.com/title/tt0068646/?ref_=fn_al_tt_1)
- [The Dark Knight](https://www.imdb.com/title/tt0468569/?ref_=fn_al_tt_1)
- [The Prestige](https://www.imdb.com/title/tt0482571/?ref_=fn_al_tt_1)

## Co nas dneska ceka
V treti lekci se budeme bavit o dvou novych datovych typech, o jejich metodach
a praktickem vyuziti. V ramci celeho tohoto povidani si opet ukazeme radu
nazornych prikladu a jedne souvisle ulohy.

## Co bude vysledkem
Po spusteni by mel program vypadat nasledovne (viz. demo)
```bash
$ ./movies
```

__Komunikace s programem__:
```
============================================================================
                  Vitejte v nasi skromne filmove databazi                   
============================================================================
Mame v nabidce tyto snimky:
['Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'The Prestige']
============================================================================
VYBERTE KATEGORII:
============================================================================ 
              DETAILY FILMU | SPOLECNE | PODMNOZINA | ROZDILNE              
============================================================================
VYBERTE MOZNOST: detaily filmu
============================================================================
VYBERTE FILM: The Dark Knight
{'HODNOCENI': '90/100',
 'HRAJI': ('Christian Bale',
           'Heath Ledger',
           'Aaron Eckhart',
           'Michael Caine',
           'Maggie Gyllenhaal',
           'Gary Oldman',
           'Morgan Freeman',
           'Monique Gabriela',
           'Ron Dean',
           'Cillian Murphy'),
 'JMENO': 'The Dark Knight',
 'REZISER': 'Christopher Nolan',
 'ROK': 2008,
 'STOPAZ': 152}
```

## Co budeme potrebovat?
- Python 3.6+
- textovy editor
- vstupni hodnoty
```python
film1 = {
    'JMENO': 'Shawshank Redemption',
    'HODNOCENI': "93/100",
    'ROK': 1994,
    'REZISER': 'Frank Darabont',
    'STOPAZ': 144,
    'HRAJI': (
        "Tim Robbins",
        "Morgan Freeman",
        "Bob Gunton",
        "William Sadler",
        "Clancy Brown",
        "Gil Bellows",
        "Mark Rolston",
        "James Whitmore",
        "Jeffrey DeMunn",
        "Larry Brandenburg"    
    ),
}

film2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": (
        "Marlon Brando",
        "Al Pacino",
        "James Caan",
        "Richard S. Castellano",
        "Robert Duvall",
        "Sterling Hayden",
        "John Marley",
        "Richard Conte"
    ),
}

film3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": (
        "Christian Bale",
        "Heath Ledger",
        "Aaron Eckhart",
        "Michael Caine",
        "Maggie Gyllenhaal",
        "Gary Oldman",
        "Morgan Freeman",
        "Monique Gabriela",
        "Ron Dean",
        "Cillian Murphy"
    ),
}

film4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": (
        "Hugh Jackman",
        "Christian Bale",
        "Michael Caine",
        "Piper Perabo",
        "Rebecca Hall",
        "Scarlett Johansson",
        "Samantha Mahurin",
        "David Bowie"
    )
}
```

## Prvni krucek
Vytvorime si novy soubor, pojmenujeme jej `movies.py` a zkopirujeme nasledujici
sablonu:
```python
#!/usr/bin/python3
""" Lekce #3 - Uvod do programovani, Movies """
```

### Co je to slovnik?
Jde opet o zabudovany datovy typ v Pythonu, ktery je tvoreny dvojicemi
__klic: hodnota__. Je charakteristickym svym hledanim (nebo taky _mapovanim_)
klicu a jejich hodnot. Od ntice a seznamu se lisi tim, ze neni mozne jej
indexovat za ucelem ziskavat prvky poporade (prvky nejsou razene, tak jak
seznamy). Klice musi byt unikatni, za to hodnoty nemusi. Hodnoty mohou byt
retezce, cisla, seznam, atd.

### Vytvorime slovnik
Zpusobu pro vytvoreni prazdneho slovniku je vice. Dva nejjednodussi priklady:
```python
novy_slovnik = dict()                 # pomoci konstruktoru
novy_slovnik2 = {'Jmeno' : 'Matous'}   # predpis pomoci klice: hodnoty
```

### Prvni cast ulohy
```python
#!/usr/bin/python3
""" Lekce #3 - Uvod do programovani, Movies """

film1 = {}
```

### Vytvorime klice
Indexovat slovniky nemuzeme. Nicmene proces zapisu pomoci hranate zavorky
slouzi k pridani klice a je hodnoty.
```python
<jmeno_slovniku>["jmeno_klice"] = hodnota_klice
```

__Priklad__:
```python
slovnik = {}
slovnik["jmeno"] = "Matous"
slovnik["email"] = "matous@matous.cz"
print(slovnik)
```

Pro ucely nasi ulohy nejprve vytvorime prazdne klice a hodnoty pridame az v
dalsim kroku.

### Druha cast ulohy
```python
film1["JMENO"] = ""
film1["HODNOCENI"] = ""
film1["ROK"] = None
film1["REZISER"] = ""
film1["STOPAZ"] = None
film1["HRAJI"] = ()
```
### Vlozime hodnoty pro existujici klice
Muzeme je vkladat primo s hodnotami ale pro ucely dnesni lekce je budeme
zadavat separatne. Vsimnete si, ze poradi ktere nam Python vraci nemusi
odpovidat poradi, ktere jsme zadavali.
```python
film1["JMENO"] = "Shawshank Redemption"
film1["HODNOCENI"] = "93/100"
film1["ROK"] = 1994
film1["REZISER"] = "Frank Darabont"
film1["STOPAZ"] = 144
film1["HRAJI"] = (
    "Tim Robbins",
    "Morgan Freeman",
    "Bob Gunton",
    "William Sadler",
    "Clancy Brown",
    "Gil Bellows",
    "Mark Rolston",
    "James Whitmore",
    "Jeffrey DeMunn",
    "Larry Brandenburg"
)
```
### Aktualizovani hodnot
Pomoci metody __.update()__ muzeme prepisovat aktualni hodnoty klicu:
```python
slovnik = {"Jmeno": "Matous", "Prijmeni": "Holinka"}  # Vytvorime slovnik
slovnik.update({"Jmeno": "Lukas"})                    # Prepiseme
print(slovnik))                                       # Zobrazime
```
Pojdme zamerne zkomolit jmena nami definovaneho klice `JMENO`.
```python
film.update({"JMENO": "Shawnshak Redemption"})
```

### Odstranovani
Celkem muzeme vyuzit 3 zpusobu, ktere odstrani klice a jejich hodnoty:
1. Zpusob jak mazat klice:
```python
slovnik = dict()
slovnik["JMENO"] = "Matous"
slovnik["PRIJMENI"] = "Holinka"
del slovnik["JMENO"]
```
2. Zpusob vraci hodnotu spojenou s klicem jako vystup a odebere par ze slovniku
```python
slovnik = dict()
slovnik["JMENO"] = "Matous"
slovnik["PRIJMENI"] = "Holinka"
slovnik.pop("PRIJMENI")
```
3. Zpusob `.popitem()` vrati naposledy pridanou polozku (par) do slovniku a odebere jej:
```python
slovnik = dict()
slovnik["JMENO"] = "Matous"
slovnik["PRIJMENI"] = "Holinka"
slovnik["EMAIL"] = "matous@matous.cz"
slovnik.popitem()
```
Takze nyni muzeme odstranit nami zkomoleny klice `JMENO` a vytvorit jej poradne.
```python
film.pop("JMENO")
film["JMENO"] = "Shawshank Redemption"
```

### Slovnik ve slovniku? Aneb nestovani

<p align="center">
  <img src="https://media.giphy.com/media/fpXxIjftmkk9y/source.gif" width="300" height="300">
</p>

Tento princip muzeme chapat jako vkladani slovniku do slovniku (plati i pro
jine datove typy jako senzamy aj.). Pomoci tohoto principu muzeme vytvaret
strukturovanejsi promenne.
```python
rodicovsky_slovnik = dict()
potomek1 = {"Jmeno": "Matous"}
potomek2 = {"Jmeno": "Lukas"}
potomek3 = {"Jmeno": "Jan"}

rodicovsky_slovnik["1_slovnik"] = potomek1
rodicovsky_slovnik["2_slovnik"] = potomek2
rodicovsky_slovnik["3_slovnik"] = potomek3
```
Nejprve nakopirujeme zadane slovniky (`film1`~`film4`) do naseho pracovniho
souboru a pote vkladame do noveho prazdneho slovniku.
```python
filmovy_slovnik = {}
filmovy_slovnik[film1["JMENO"]] = film1
filmovy_slovnik[film2["JMENO"]] = film2
filmovy_slovnik[film3["JMENO"]] = film3
filmovy_slovnik[film4["JMENO"]] = film4
```

## Vytvorime dotazovac
Chceme, aby cela procedura fungovala opet na zaklade komunikace uzivatele a
naseho programu. Vytvorime proto nejake dotazovaci prostredi uvnitr prikazove
radky. Uvod by mel obsahovat pozdrav a nabidku nasich filmu (tudiz musime
prochazet nas slovnik `filmovy_slovnik`).
```
################
    Pozdrav
################
    Nase filmy
################
    Moznosti
################
Vyberte moznost:
################
   Zobrazime
```

### Nejdriv oddelovani
Opet vytvorime promennou (konstantu), ktera nam pomuze text rozdelit:
```python
ODDELOVAC = '=' * 76
```

### Jak mohu zarovnat text?
Pomoci metody `center()` muzeme zarovnat nas text na stred urcite delky pole.
```python
print("Vitejte v nasi skromne filmove databazi".center(76, " "))
```

### Pohledy
Mezi dalsi metody slovniku patri takove, ktere nam umozni nahledy na jejich
obsah:
- `.items()` -> vratim objekt s klici a hodnotami
- `.keys()` -> vratim objekt jen s klici
- `.values()` -> vratim objekt jen s hodnotami
Jelikoz budeme chtit uzivateli zobrazit pouze nabidku filmu (jejich jmen),
pouzijeme proto prislusnou metodu:
```python
list(filmovy_slovnik.keys())
```
Pomoci built-in funkce `list()` prevedeme objekt vraceny z metody `keys()` na
obycejny seznam.

Cely zapis pro oznameni uzivateli bude potom vypadat nasledovne:
```python
ODDELOVAC = '=' * 76

print(ODDELOVAC)
print("Vitejte v nasi skromne filmove databazi".center(76, " "))

print(
f"""{ODDELOVAC}
Mame v nabidce tyto snimky:
{list(filmovy_slovnik.keys())}
{ODDELOVAC}
VYBERTE KATEGORII:
{ODDELOVAC}
{'DETAILY FILMU | SPOLECNE | PODMNOZINA | ROZDILNE'.center(76, " ")}
{ODDELOVAC}"""
)
```

## Strom podminek
Podminky nam umozni vzdy vybrat jeden proces, ktery budeme chtit aplikovat.
Mame 4 ruzne procesy, takze potrebujeme vytvorit 4 ruzne podminky:
```
bud TOTO; nebo TOTO; nebo TOTO; nebo TOTO -> if elif elif elif
```

### Vypiseme detaily filmu
Prvni podminka bude mit na starost obstarat vystup, ktery zahrnuje obsah
jednotlivych vnitrnich slovniku (tedy detaily konkretniho filmu).

Nejprve doplnime moznost zvolit si jeden rezim:
```python
vyber = input("VYBERTE MOZNOST: ")
```
Dale doplnime prvni podminkovou vetev s detaily:
```python
if vyber == "DETAILY FILMU":
    ...
```
Film pak muzeme ziskat pomoci dalsi metody slovniku `.get()`. Tato metoda ma
za cil jedine, najde klic, ktery ji zadame a ona vrati jeho hodnotu. Volitelne
pak muzeme nastavit, co vrati, pokud hledany klic nenajde.
```python
slovnik = dict()
slovnik["JMENO"] = "Matous"
slovnik["PRIJMENI"] = "Holinka"
slovnik["EMAIL"] = "matous@matous.cz"

print(slovnik)               # {'JMENO': 'Matous', ...
print(slovnik.get("EMAIL"))  # 'matous@matous.cz'
print(slovnik1.get("ADRESA", "Tento klic neni k dispozici")
```
Dopiseme zbytek nasi podminky v uloze:
```python
if vyber == "DETAILY FILMU".lower():
    print(ODDELOVAC)
    vyber_filmu = input("VYBERTE FILM: ")
    print(ODDELOVAC)
    print(filmovy_slovnik.get(vyber_filmu, "Vami zadany film neni v db"))
```

## Mnoziny
Mnozina neboli set je opet neserazena kolekce udaju, ktera je typicka tim, ze
uvnitr nenajdeme zadnou hodnotu dvakrat. Sety se pouzivaji zejmena kvuli svym
matematickym operacim:
1. __sjednoceni__
2. __prunik__
3. __rozdil__
4. __sym. rozdil__

### Jak vytvorit mnozinu
Vytvoreni mnozin je opet mozne pomoci dvou zpusobu:
```python
novy_set1 = set(); type(novy_set1)
novy_set2 = {"Matous", "Marek", "Lukas", "Jan"}; type(novy_set2)
```

### Pridavani/odebirani clenu
Pridavat data do mnoziny muzeme pomoci metody `add()` a odebirat
pomoci `discard()`:
```python
novy_set = set()

novy_set.add("Matous")
novy_set.add("Marek")
print(novy_set)

novy_set.discard("Matous")
print(novy_set)
```

### Spolecni herci
Chceme u dvou libovolne zadanych filmu zjistit, kteri herci se nachazeji u obou
zminenych.

<p align="center">
  <img src="https://media.giphy.com/media/11tKP5jvSJdLXi/source.gif" width="300" height="300">
</p>

### Jakou operaci vyuzijeme?
Protoze nas zajima, ktere udaje (herci) se vyskytuji soucasne v prvnim setu a
ve druhem setu, pouzijeme operator pro prunik `&`.
```python
set1 = {"Pavel", "Matous", "Tomas", "Martin"}
set2 = {"Martin", "Petr", "Vojtech"}

print(set1 & set2)  # "Martin"
```
Spolecnym jmenem v obou mnozinach, v nasem prikladu vyse, je `Martin`. Takze
ted muzeme dokoncit nasi druhou podminku:
```python
elif vyber == "SPOLECNE".lower():
    print(ODDELOVAC)
    vyber_film1 = input("Vyberte prvniho filmu: ")
    vyber_film2 = input("Vyberte druheho filmu: ")

    herci_film1 = set(filmovy_slovnik[vyber_film1]["HRAJI"])
    herci_film2 = set(filmovy_slovnik[vyber_film2]["HRAJI"])

    prunik = herci_film1 & herci_film2
    print(
    f"SPOLECNI HERCI PRO *{filmovy_slovnik[vyber_film1]['JMENO']}* A *{filmovy_slovnik[vyber_film2]['JMENO']}*: {prunik}"
    )

```

## Jde o podmnozinu?
Timto dotazem zjistujeme, jestli prislusny set obsahuje prvky, ktere mu predkladame. Cela operace je spojena s metodou _.issubset()_, ktera vraci boolean hodnotu (True/False).
__Priklad__:
```python
set1 = {"a", "b", "c", "d", "e"}
set2 = {"a", "b", "c"}
set3 = {1, 2, 3, "a", "b"}
set2.issubset(set1)  # True
set3.issubset(set1)  # False
set3.issubset(set1)  # False
```

__Doplnime__:
```python
elif vyber == "PODMNOZINA".lower():
    print(ODDELOVAC)
    vyber_film = input("Vyberte jmeno filmu: ")
    vzorek = input("ZADEJTE JMENA: ")
    print(set(vzorek.split(", ")).issubset(set(filmovy_slovnik[vyber_film]["HRAJI"])))
```

## Jsou tyto dva sety odlisne?
_.isdisjoint()_ je opet metoda. Tato ma ale potvrdit, ze ani jediny udaj ve dvou setech neni stejny.
__Priklad__:
```python
set5 = {"a", "b", "c", "d", "e"}
set6 = {"f", "g", "h"}
set7 = {"h", "i", "j", "k"}
set5.isdisjoint(set6)  # True
set6.isdisjoint(set7)  # False
```

__Doplnime__:
```python
elif vyber == "ROZDILNE".lower():
    print(ODDELOVAC)
    film1 = input("Vyberte jmeno filmu: ")
    vzorek = input("ZADEJTE JMENA: ")
    print(set(vzorek.split(", ")).isdisjoint(set(filmovy_slovnik[film1]["HRAJI"])))
```

Pokracovat na Lekci#04
