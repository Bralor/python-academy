Minula [lekce#11](https://github.com/Bralor/python-academy/tree/lekce11)

<p align="center">
  <img src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" width="300" height="300">
</p>

# Python academy, lekce 12
## Dulezite odkazy
- Portal [Engeto.com](https://engeto.com/)
- Python Academy [repozitar](https://github.com/Bralor/python-academy)
- [heroes III - cesko-slovenska liga](http://heroes3.cz/)

## Co nas ceka?
V ramci dnesniho webinare se budeme snazit _scrapovat_, tzn. ze za pomoci
Pythonu se budeme snazit shromazdovat nejake informace umistene ve formatu
`html` nekde na webu. Dale si povime:
1. Co je to __HTML__
2. __Kde__ jej najdeme
3. Jak jej __ziskat__, v Pythonu
4. Jak jej __zpracovat__, v Pythonu

## Scrapuj tabulku hracu
Cilem bude extrahovat data z [webu](http://heroes3.cz/) a ulozit je lokalne
do nejakeho textoveho souboru (optimalne `csv`).

## Ukazka na uvod
Spustime skript v adresari s prislusnym argumentem (tim bude adresa stranky, ze
ktere chceme `html` ziskat):
```
$ python scraper.py <url>
```
Nasledne by se mel objevit komentar v prikazovem radku a `csv` soubor
v aktualnim adresari:
```
ULOZENO DO: hraci1.csv
...
README.md
hraci_str1.csv
```

## Co budeme potrebovat?
- python 3.6+
- text. editor
- [for smycky](https://github.com/Bralor/python-academy/tree/lekce05)
- [funkce v Pythonu](https://github.com/Bralor/python-academy/tree/lekce06)
- [prace s text. soubory](https://github.com/Bralor/python-academy/tree/lekce08)
- [handlovani chyb](https://github.com/Bralor/python-academy/tree/lekce09)

## Nejprve web
Spolecne mrkneme na [tento](http://heroes3.cz/) web. V navigacni poli se
prepneme do sekce `Hraci`. Nas program by mel stahnout a upravit tyto udaje:
1. __Poradi__
2. __Jmeno__
3. __Body__
4. __Celkem her__
5. __Vitezstvi__
6. __Uspesnost__

Dalsi krok je zajistit, aby toto dovedl provest pro ruzne tabulku (pod tabulkou
se muzeme prepinat dale v poradi).

## V cem jsou nase udaje?
Data jsme nasli, nyni musime porozumet strukture, v niz jsou ulozena. Pravym
tlacitkem mysi si rozbalime nabidku a v ni najdeme __view page source__
(u prohlizece Mozilla). Ted se divame na zdrojovy kod a hned na uvod vidime, ze
jde o `html`:
```html
<!DOCTYPE html>
<html lang ="cs">
<head>
...
</head>
```

## Html (~HyperText Markup Language)
Jde opet o typ textoveho souboru, ktery je usporadany to tzv. _tagu_ (proto
markup elements). Nejcasteji tvori strukturu webovych stranek a je to tvoreny
napadnou hierarchickou strukturou (z __tagu__). My tuto strukturu na pozadi
casto nevnimame. Prohlizec nam casteji zprostredkuje vyrenderovanou grafickou
podobu.
```html
<!-- Pouze vzorovy zapis -->
<div id="menu"><ul>
    <li>
        <a href="http://XXXXXXX.cz" title="">Homepage</a>
    </li>
</div>
```
Hierarchie nasledne usporada `html` tak, ze nektere tagy jsou rodicovske a
obsahuji svoje potomky.

## Tagy
Krome jejich strukturniho vyznamu mohou mit doplnujici atributy, podle kterych
je muzeme velmi casto dohledat, pripadne obsahuji dalsi informace:
```html
<div id="menu">
    <a href="http://XXXXXXX.cz"></a>
<div class="sloupec">
```
Vidime, ze format se hodne podoba slovnikum v Pythonu, tedy:
```python
<klic> = "<hodnota>"
```

## Jak tedy ziskat potrebne udaje?
Abychom mohli s udaji, ktere jsou k dispozici na webu, pracovat, je potreba
ziskat konkretni `html` soubor. Tedy soubor, ve kterem jsou informace, co my
chceme zapsana.

## Python a html
Stejne jak jsme schopni pomoci Pythonu delegovat ukoly na nas operacni system
(vytvor adresar, smaz adresar, vytvor soubor, smaz soubor), muzeme na nej
delegovat ukol v podobe nalezeni a stazeni prislusneho `html`.

### Pozadavek
Aby Python mohl ziskat potrebne `html`, musi vyslat pozadavek (angl. _request_),
na server, kde se web nachazi(tedy standartni ukon prohlizece).

### Python a requesty
Za timto ucelem budeme pracovat s modulem __requests__(jejich samozrejme vice).
Ve svem aktivovanem prostredi nainstalujeme balicek
[`requests`](https://requests.readthedocs.io/en/master/)(pomoci `venv`, nebo
__PyCharm__(doporucene)).

### Terminal
Bud prikazem:
```bash
$ python -m venv env
$ source env/bin/activate
$ pip install requests
```

### IDE
1. Settings (`Ctrl+Alt+s`)
2. Project: `<jmeno_projektu>`
3. Python Interpreter
4. Symbol `+`, vedle tabulky

## Zacneme kodit
Dale balicek nahrajeme do naseho pracovniho souboru
[`scraper.py`](https://github.com/Bralor/python-academy/blob/lekce12/scraper.py)
```python
#!/usr/bin/python3.8
"""Lekce #12 - Uvod do programovani, web scraping"""

import requests
```
Nyni mame nainstalovany a soucasne nahrany modul treti strany `requests`.

## Zakladni prikazy
Komunikace se serverem probiha prakticky dvema zpusoby(viz. `help(requests)`:
1. Funkce __get__(`help(requests.get)`)
2. Funkce __post__(`help(requests.post)`)

Obe funkce slouzi k tomu, abychom ziskali odpoved serveru, ktera obsahuje nase
`html`, ale jak je pouzit?

### Get
Pomoci prohlizece, pojdme vysetrit, kterou funkci aplikovat. Vyuzijeme nastroje
`Inspect Element`. V nem se nam v zahlavi zobrazi hned nekolik moznych funkci:
1. __Inspektor__
2. Console
3. Debugger
4. __Network__

..a dalsi. Nas budou zajimat zejmena ty tucne zvyraznene. Pokud jste tedy na
hlavni strance, rozkliknete sekci `Network`. Nejprve uvidime prazdnou tabulku.
Ted kliknete (na puvodni webu) na sekci `Hraci` a vsimnete si, jak se obsah
`Network` zmenil.

Nas zajima hodnota `Method` u toho radku, ktery obsahuje hodnotu u `Status` 200.
Vice o jednotlivych statusech
[zde](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes):
```python
odpoved_serveru = requests.get(<url>, params=<params>)
odpoved_serveru.status_code
odpoved_serveru.encoding
odpoved_serveru.text
```
`URL` je nam znamy _uniform resource locator_
(vice [zde](https://en.wikipedia.org/wiki/URL).

### Post
Za predpokladu, ze bych dostal hodnotu u sloupce `Method` jako `POST`, budeme
muset sledovat dalsi podrobnosti (viz. na lekci).

## Pojdme na vec
<p align="center">
  <img src="https://media.giphy.com/media/TdiGSPC3P6QXvCBdWx/giphy.gif" width="300" height="300">
</p>

Nejprve jak chceme postupovat. Otevreme proto `scraper.py`:
```python
#!/usr/bin/python3.8
"""Lekce #12 - Uvod do programovani, web scraping"""

import requests

# hlavni funkce
    # volani func1
    # volani func2
    # ...

# vytvor pozadavek na server
# zpracuj pozadavek
# najdi nase hrace
# uloz soubor 'csv'

# volani hlavni funkce
```

## Nejprve abstraktne
Zkusime jednotlive funkce zapsat pomoci funkci `print` (neresime anotace):
```python
#!/usr/bin/python3.8
"""Lekce #12 - Uvod do programovani, web scraping"""

import requests

def hlavni() -> None:
    vytvor_pozadavek()
    zpracuj_pozadavek()
    hledej_hrace()
    uloz_csv()


def vytvor_pozadavek():  # vytvor pozadavek na server
    print("VYTVARIM POZADAVEK")


def zpracuj_pozadavek():  # zpracuj pozadavek
    print("ZPRACOVAVAM...")


def hledej_hrace():  # najdi nase hrace
    print("PROCHAZIM ZPRACOVANE HTML A HLEDAM...")


def uloz_csv():  # uloz soubor 'csv'
    print("UKLADAM CSV")


hlavni()  # volani hlavni funkce
```

## Co vraci funkce
Nyni se pokusme vyresit, co nam zrejme vrati jednotlive funkce a kam tyto
hodnoty ukladat:
```python
#!/usr/bin/python3.8
"""Lekce #12 - Uvod do programovani, web scraping"""

import requests

def hlavni() -> None:
    odpoved_serveru = vytvor_pozadavek("https://bezrealitky.cz")

    if odpoved_serveru:
        naparsovane = zpracuj_pozadavek(odpoved_serveru)

    hraci = hledej_hrace()
    uloz_csv()


def vytvor_pozadavek(url: str) -> str:  
    print(f"VYTVARIM POZADAVEK NA: {url}")
    return "odpoved"


def zpracuj_pozadavek(odpoved: str) -> str:
    print("ZPRACOVAVAM...")
    return "zpracovane"


def hledej_hrace(data: str) -> dict:
    print("PROCHAZIM ZPRACOVANE HTML A HLEDAM...")
    return {"hrac": "Matous"}


def uloz_csv() -> None:
    print("UKLADAM CSV")


hlavni()
```

## Vlozeni argumentu
Odkaz webu, ktery chceme scrapovat (resp. stranka hracu 1-xy), chceme zadavat
jako argument:
```python
#!/usr/bin/python3.8
"""Lekce #12 - Uvod do programovani, web scraping"""

import sys
import requests
...
def hlavni() -> None:
    odpoved_serveru = vytvor_pozadavek(url)
    ...

if __name__ == "__main__":
    url = sys.argv[1]
    hlavni()
```
Vytvorime promennou `url`, do ktere budu pri spousteni _py_ souboru ukladat
hodnotu argumentu z terminalu.

## Vytvoreni pozadavku
Nahradime _junk_ kod ve funkci `vytvor_pozadavek` radnym kodem v Pythonu. Mame
v podstate 2 moznosti jak tuto funkci zapsat:
1. Pomoci __Kontextoveho manazeru__
2. Reseni v [__uvodu__](#get)

Vyzkousime si jeste kont.manazer:
```python
def vytvor_pozadavek(url: str) -> str:
    with requests.Session() as se:
        return se.get(url)
```
Finalni objekt si nechame vypsat, at vidime s cim je potreba pracovat:
```python
#!/usr/bin/python3.8
"""Lekce #12 - Uvod do programovani, web scraping"""

import sys
import requests
...
def hlavni() -> None:
    odpoved_serveru = vytvor_pozadavek(url)
    print(odpoved_serveru.text)
    ...

if __name__ == "__main__":
    url = sys.argv[1]
    hlavni()
```

## Raw html
Vidime, ze podoba, ve ktere jsme v Pythonu nase `html` ziskali, neni moc
uzitecna. Bude je potreba vhodne _parsovat_ (jinak receno rozdelit).

### BeautifulSoup
Asi nejznamejsim balickem, ktery v Pythonu slouzi jako pomocnik pro _parsovani_
`html` (a `xml`) je `bs4`.

### Nahravani
Jde o balik, tudiz jej musime nejprve importovat:
```python
from bs4 import BeautifulSoup
```
Velmi casto doplnujeme __alias__, protoze jde o dlouhe jmeno:
```python
from bs4 import BeautifulSoup as bs
```

### Aplikace
Pro pouziti objektu `BeautifulSoup` potrebujeme dve veci:
1. __Promennou__, kterou chceme parsovat.
2. __Typ__ parseru

Protoze budeme chtit rozdelovat `html`, budeme pouzivat `html.parser` (vice
typu si ukazeme v napovede `help(BeautifulSoup.__init__)`
```python
parsovane = BeautifulSoup(odpoved_serveru.text, "html.parser")
type(parsovane)  # bs4.BeautifulSoup
```
Jakmile si budeme chtit projit nyni obsah promenne `parsovane`, uvidime
prehlednou strukturu.

## Vratme se k nasemu kodu
Nyni, kdyz vime, jak ve strucnosti balik `bs4` pracuje, pojdme zapsat dalsi
funkci naseho kodu:
```python
from bs4 import BeautifulSoup
...

def zpracuj_pozadavek(odpoved: str) -> bs4.BeautifulSoup:
    return BeautifulSoup(odpoved, "html.parser")
    ...
```
A prepiseme cast funkce `hlavni`:
```python
#!/usr/bin/python3.8
"""Lekce #12 - Uvod do programovani, web scraping"""

import sys

import requests
from bs4 import BeautifulSoup


def hlavni() -> None:
    odpoved_serveru = vytvor_pozadavek(url).text
    naparsovana_odp = zpracuj_pozadavek(odpoved_serveru)
    ...

if __name__ == "__main__":
    url = sys.argv[1]
    hlavni()
```

## Hledani tagu
V tento okamzik mame kompletni `html` cele stranky. Nicmene nepotrebujeme uplne
vsechno. Hlavni okamzik _scrapovani_ spociva v hledani presne tech `tagu`, ktere
obsahuji informace, co potrebujeme.

### Analyza Html
Pojdme se jeste jednou podivat na cileny web. Zacneme tim, ze si dohledame
(pomoci `Inspect Element` nastroje), rodice, ve kterem mame ulozene jmeno hrace.
Abychom se posunuli dal, musime si udelat poradek v nasledujicim:
1. Co predstavuje tag `<td></td>`?
2. Co predstavuje tag `<tr></tr>`?
3. Co predstavuje tag `<tbody></tbody>`?
4. Co predstavuje tag `<table></table>`?

Hierarchii jsme prosli a ted musime redukovat obsah promenne `naparsovana_odp`,
abychom mohli lepe pracovat s informacemi, ktere nas zajimaji.

## Rodicovsky element
Prvnim elementem (tedy tagem), ktery muzeme snadno identifikovat je `table`.
Duvodem, proc je snadne ho najit je jeho atribut `class`, ktery jej dela
jedinecnym.

## Table
Dalsi vec, kterou nam balik `bs4` nabizi, je moznost vyhledavat:
1. __BeautifulSoup.find()__ - `help(BeautifulSoup.find)` 
2. __BeautifulSoup.find()__ - `help(BeautifulSoup.find_all)`

Jelikoz se tabulek v nasem puvodnim `html` vyskytuje hodne, chceme najit prave
takovou, ktera disponuje atributem `class = "tab_top"`:
```python
def hledej_hrace(data: bs4.BeautifulSoup) -> dict:
    table = data.find("table", {"class": "tab_top"})
```
Tim padem zredukujeme puvodni promenne `naparsovana_odp` o vsechno, krome
nasi tabulky.

## tr
Mame samotnou tabulku a vime, ze hraci (a informace o nich), jsou situovany
do jednotlivych radku (tedy tag `tr`). Chceme tedy projit a posbirat vsechny
`tr`:
```python
...
def hledej_hrace(data: bs4.BeautifulSoup) -> dict:
    table = data.find("table", {"class": "tab_top"})
    trs = table.find_all("tr")[1:]
    return trs
```
Nyni mame pouze radky se jmeny, ktera se nachazi v tabulce a muzeme se zamerit
na extrakci jednotlivych udaju.
```python
...
def hlavni() -> None:
    odpoved_serveru = vytvor_pozadavek(url).text

    if odpoved_serveru:
        naparsovana_odp = zpracuj_pozadavek(odpoved_serveru)
        hraci = hledej_hrace(naparsovana_odp)
        ...
```

## td
Udaje, ktere nas zajimaji jsou nasledujici:
1. __Poradi__
2. __Jmeno__
3. __Body__
4. __Celkem her__
5. __Vitezstvi__
6. __Uspesnost__

Nejprve zkontrolujeme, jak jsou usporadane v radku:
```python
    ...
    hraci = hledej_hrace(naparsovana_odp)
    print(hraci)
```
Jde o seznam, takze pomoci indexu mohu jednotliva data vyuzit:
```python
...
def zpracuj_udaj(tr: str) -> dict:
    poradi = tr.find_all("td")[0].text
    jmeno = tr.find_all("td")[2].text
    body = tr.find_all("td")[3].text
    celkem = tr.find_all("td")[6].text
    vitezstvi = tr.find_all("td")[5].text
    uspesnost = tr.find_all("td")[7].text
    
    return {
        "poradi": poradi,
        "jmeno": jmeno,
        "body": body,
        "celkem": celkem,
        "vitezstvi": vitezstvi,
        "uspesnost": uspesnost,
    }
```
Nakonec vratim slovnik, ktery vsechno potrebne ulozi.
```python
    ...
    if odpoved_serveru:
        naparsovana_odp = zpracuj_pozadavek(odpoved_serveru)
        hraci = hledej_hrace(naparsovana_odp)
        udaje = [zpracuj_udaj(hrac) for hrac in hraci]
        ...
```

## Ukladani Csv
Nyni ziskavame vse potrebne a zbyva nam posledni krok. Tedy ulozit scrapovana
data do souboru na disk.
```python
def uloz_csv(data: dict, jmeno: str) -> None:
    with open(jmeno, "w", newline="") as csv_s:
        zahlavi = data[0].keys()
        writer = csv.DictWriter(csv_s, fieldnames=zahlavi)

        writer.writeheader()
        for index, _ in enumerate(data):
            writer.writerow(
                {
                    "poradi": data[index]["poradi"],
                    "jmeno": data[index]["jmeno"],
                    "body": data[index]["body"],
                    "celkem": data[index]["celkem"],
                    "vitezstvi": data[index]["vitezstvi"],
                    "uspesnost": data[index]["uspesnost"],
                }
            )
        return True
```
Jeste doplnime funkci `hlavni`:
```python
#!/usr/bin/python3.8
"""Lekce #12 - Uvod do programovani, web scraping"""

import sys
import csv

import requests
from bs4 import BeautifulSoup


def hlavni() -> None:
    odpoved_serveru = vytvor_pozadavek(url).text

    if odpoved_serveru:
        naparsovana_odp = zpracuj_pozadavek(odpoved_serveru)
        hraci = hledej_hrace(naparsovana_odp)
        udaje = [zpracuj_udaj(hrac) for hrac in hraci]

    if uloz_csv(udaje, soubor):
        print(f"ULOZENO DO: {soubor}")
    else:
        print(f"NELZE ULOZIT!")
...
if __name__ == "__main__":
    url = sys.argv[1]
    soubor = sys.argv[2]
    hlavni()
```

## Prvni tabulka nebo i jine?
Nyni pojdme vyzkouset jak nas kod funguje pro nasledujici stranky tabulky
`hraci`.

## Dulezite na zaver!
1. Nez se doopravdy pustite do scrapovani udaju, prectete si sekci
_pravidla&podminky_, abyste vedeli jak legalne data pouzivat. Ve vetsine
pripadu je zakazano pouzivat udaje pro komercni ucely.
2. Ujistete se, ze server nezatezujete velkym mnozstvim dotazu (dlouho a velke
mnozstvi). To muze mit za nasledek pad serveru a prinejmensim Vase zablokovani.

Zpet na [uvodni stranku](https://github.com/Bralor/python-academy)

