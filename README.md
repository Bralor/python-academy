Minula [lekce#12](https://github.com/Bralor/python-academy/tree/lekce12)

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
Pythonu se budeme snazit shromazdovat nejake informace umistene ve formatu HTML
nekde na webu. Dale si povime:
1. Co je to __HTML__
2. __Kde__ jej najdeme
3. Jak s nim __ziskat__, v Pythonu
4. Jak jej __zpracovat__, v Pythonu

## Scrapuj tabulku hracu
Cilem bude extrahovat data z [webu](http://heroes3.cz/) a ulozit je lokalne
do nejakeho textoveho souboru (optimalne CSV).

## Ukazka na uvod
Spustime skript v adresari s prislusnym argumentem (tedy URL stranky, ze ktere
chceme HTML ziskat):
```
$ python scraper.py <url>
```
Nasledne by se mel objevit komentar v prikazovem radku a `csv` soubor
v aktualnim adresari:
```
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
Data jsme nasly, nyni musime porozumet strukture, v niz jsou ulozena. Pravym
tlacitkem mysi si rozbalime nabidku a v ni najdeme __view page source__
(u prohlizece Mozilla). Ted se divam na zdrojovy kod a hned na uvod vidime, ze
jde o _html_:
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
<a href="http://XXXXXXX.cz">
<div class="sloupec">
```
Vidime, ze format se hodne podoba slovnikum v Pythonu, tedy:
```python
<klic> = "<hodnota>"
```

## Jak tedy ziskat potrebne udaje?
Abychom mohli s udaji, ktere jsou k dispozici na webu, pracovat, je potreba
ziskat konkretni _HTML_ soubor. Tedy soubor, ve kterem jsou informace, co my
chceme zapsana.

## Python a Html
Stejne jak jsme schopni pomoci Pythonu delegovat ukoly na nas operacni system
(vytvor adresar, smaz adresar, vytvor soubor, smaz soubor), muzeme na nej
delegovat ukol v podobe nalezeni a stazeni prislusneho `html`.

### Pozadavek
Aby Python mohl ziskat potrebne `html`, musi vyslat pozadavek (angl. _request_),
na server, kde se web nachazi(tedy standartni ukon prohlizece).

### Python a requesty
Za timto ucelem budeme pracovat s modulem __requests__(jejich samozrejme vice).
Ve svem aktivovanem prostredi nainstalujeme balicek `requests`(pomoci `venv`,
nebo __PyCharm__(doporucene)).

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
1. Funkce __get__ (`help(requests.get)`)
2. Funkce __post__(`help(requests.post)`)

Obe funkce slouzi k tomu, abychom ziskali odpoved serveru, ktera obsahuje nase
`html`, ale jak je pouzit?

### Get
Pomoci prohlizece, pojdme vysetrit, kterou funkci aplikovat. Vyuzijeme nastroje
`inspect element`. V nem se nam v zahlavi zobrazi hned nekolik moznych funkci:
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

Nejprve jak chceme postupovat. Otevreme proto `scaper.py`:
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


def vytvor_pozadavek()  # vytvor pozadavek na server
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
    odpoved_serveru = vytvor_pozadavek()

    if odpoved_serveru:
        naparsovane = zpracuj_pozadavek(odpoved_serveru)

    hraci = hledej_hrace(naparsovane)
    uloz_csv()


def vytvor_pozadavek() -> str:  
    print("VYTVARIM POZADAVEK")
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

## Vytvoreni pozadavku
Zadane konkretni adresu:
```python
url = "XXX"
```
Ukazeme si, kde najit parametry:
```python
params = {
    'kraj': -1,
    'okres': -1,
    'razeni': 1, 'archiv': 0,
    'typ_polozky': -1,
    'page': 1
}
```

Odesleme pozadavek pomoci metody _post_ na server, ktery jej vyhodnoti a zpracuje:
```python
odpoved_serveru = requests.post(url, params=params)
odpoved_serveru.status_code
odpoved_serveru.text
```

## Mame zdroj!
Jakmile se nam konecne podari udaje nashromazdit. Musime se nimi probrat.

```python
odpoved_serveru = requests.get(URL)
odpoved_serveru.text  # metoda text nam umozni prohlednout obsah
```

## Aplikujeme v nasi uloze
```python
"""Lekce #15 - Uvod do programovani, web scraping"""

import csv
from typing import List

import requests
from bs4 import BeautifulSoup

URL = "http://heroes3.cz/hraci"


def hlavni() -> None:
    pass

if __name__ == "__main__":
    hlavni()
```
Pomocna funkce:
```python
def ziskej_odpoved():
    return requests.get(URL)
```

## Jak jej prochazet?
Zkusime z naseho zdroje neco dohledat:
```python
odpoved_serveru.text[0]  # ...
odpoved_serveru.text[1]  # ...
odpoved_serveru.text.split()  # ...
```
Nami zname zpusoby, kterymi muzeme text [parsovat](https://en.wikipedia.org/wiki/Parsing)(prochazet) tady nejsou moc platne. Budeme potrebovat silnejsi kalibr.

## Beautiful Soup
Nainstalujeme si do naseho prostredi dalsi [balicek](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

```bash
(env) matous@matous:~/projects/$ pip install beautifulsoup4
```

Modul BeautifulSoup se postara, abychom vytahli ze ziskaneho HTML (dale podporuje i XMLka) strom, skrze ktery je mozne snadno navigovat a vyhledavat.

Nacteme z balicku modul:
```python
from bs4 import BeautifulSoup
```

Pouziti obsahuje aplikaci dvou parametru. Prvnim je objekt, kde se syrove HTML nachazi, druhy je typ parseru:
```python
naparsovane = BeautifulSoup(odpoved_serveru.text, "html.parser")
```

## Aplikujeme v uloze
Doplnime dalsi pomocnou funkci a dopiseme hlavni():
```python
def vytahni_udaje(resp):
    return BeautifulSoup(resp.text, "html.parser")
```
## Musime najit konkretni tag!
Musime se zorientovat v nasem HTML-ku a uvedomit si, ve kterem elementu hledat. V prohlizeci, pomoci rezimu _inspect_ zjistime, o ktery jde.

```html
    <table class="tab_top">
        <tr></tr>
    </table>
```

## Mame vybrano, jak hledat?
Vyhledavat budeme zejmena pomoci typu elementu (_div_,_table_,..) v kombinaci s metodou __.find()__.  Pomocne pro nas mohou byt zejmena attributy (_"tab\_top"_). 

```python
...
naparsovane.find("table", {"class": "tab_top"})
...
```
## Opet aplikujeme
```python
def hledej_tabulku(cont):
    return cont.find("table", {"class": "tab_top"})
```

Timto nase puvodni HTML orezeme a dostaneme pouze obsah <table></table>

## Jak ziskat info o hraci?
Vidime, ze na kazdem radku mame jednoho hrace. Takze se musime probrat k jednotlivym radkum. Takze musime prochazet promennou, kam jsme ulozili tabulku a znovu projit. Muzeme si vsimnout, ze radku je tu hodne a proto nam klasicke __.find()__ nepomuze. To, totiz vrati pouze prvni nalezenou hodnotu.

```python
radky = tabulka.find("tr")  # nelze pouzit, pokud je vice radku
```

Pouzijeme __.find\_all()__, ktera nam vrati vsechny elementy v zadanem objektu.

```python
radky = tabulka.find_all("tr")
radky[0]; radky[1]  # muzeme vytahovat pomoci indexu
```
## Aplikujeme...
Opatrne na zahlavi v _HTML_. To muze komplikovat situaci:
```python
def hledej_radky(tabl) -> list:
    return tabl.find_all("tr")[1:]
```

## Ziskejme konkretni bunku!
Podobne jako u radku v tabulce musime premyslet o bunce v radku. Opet je pro ni typicky konkretni element a na nej se musim zamerit.

```python
hrac_1 = radky.find_all("td")[1]
```

Nami vyfiltrovane HTML nyni obsahuje udaje, patrici prvnimu hraci tabulky. Jak se ale dostaneme ke konkretnimu textovemu udaji?

## Jake bunky tabulky?
V tabulce je porad spousta udaju. Potrebujeme nas vyber jeste malicko zuzit. Rekneme, ze mame zajem pouze o poradi, nickname, body a uspesnost.

## Vrat hodnotu elementu
Pomuze nam metoda __.text__, ktera vraci pouze hodnotu elementu.

```python
hrac_1 = radky.find_all("td")[0]  # poradi
hrac_1 = radky.find_all("td")[2]  # nickname
hrac_1 = radky.find_all("td")[3]  # body
hrac_1 = radky.find_all("td")[7]  # uspesnost
```

## Doplnime...
Doplnujici funkce. Opet musime doplnit i funkci hlavni:
```python
def hraci_info(tr) -> dict:
    try:
        poradi = tr.find_all("td")[0].text
        ...

    except AttributeError:
        print("Indexy u jednotlivych bunek v radku nejsou v poradku")
```
## Ukladani do souboru
Vytvorime si doplnujici funkce. S pomoci modulu __csv__:
```python
def uloz_csv(data: List[dict]):
    with open("players.csv", "a", newline="") as csv_f:
        zahlavi = ["PORADI", "UZIVATEL", "BODY", "USPESNOST"]
        writer = csv.DictWriter(csv_f, fieldnames=zahlavi)
        writer.writeheader()

        for index, _ in enumerate(data):
            writer.writerow(
                {
                    "PORADI": data[index]["poradi"],
                    "UZIVATEL": data[index]["hrac"],
                    "BODY": data[index]["body"],
                    "USPESNOST": data[index]["uspesnost"],
                }
            )
```

## Generator nebo seznam?
Na zacatku, ve funkce _hlavni()_ se nabizi otazka. Je lepsi pouzit seznamovou komprehenci nebo generator?
```python
konecne_udaje = (hraci_info(row) for row in radky)  # generator
konecne_udaje = [hraci_info(row) for row in radky]  # seznam
```
## Dulezite na zaver!
1. Nez se doopravdy pustite do scrapovani udaju, prectete si sekci _pravidla&podminky_, abyste vedeli jak legalne data pouzivat. Ve vetsine pripadu je zakazano pouzivat udaje pro komercni ucely.
2. Ujistete se, ze udaje nestahujete ve velkem meritku(dlouho a velke mnozstvi). To muze mit za nasledek pad serveru a prinejmensim Vase zablokovani.

