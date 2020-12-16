➡ [vratit se ke treti casti](https://github.com/Bralor/python-workshop/tree/master/materials/03_loops)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 4⃣ Python workshop
### 🗒 Obsah lekce
1. Uzitecne odkazy
2. Ukazka ulohy
3. Moduly & baliky
4. Importovani
5. Rozdeleni podle puvodu
---


<details>
  <summary>☝ Uzitecne odkazy</summary>

  #### 🗒 Dulezite odkaz
  - [Instalator balicku, pip3](https://pypi.org/project/pip/)
  - [\_\_init\_\_.py](https://pythontips.com/2013/07/28/what-is-__init__-py/)
  - [Walrus operator, dokumentace](https://realpython.com/lessons/assignment-expressions/)
  - [Python.org, hledani modulu](https://docs.python.org/3/tutorial/modules.html#the-module-search-path)
  - [Pycharm importing](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)

</details>

---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si cely repozitar jako **zip**](https://github.com/Bralor/python-workshop/archive/mh-dev.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **materials/04_importing/hangman.py** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
   <summary>📦 Moduly & baliky</summary>

<details>
   <summary>💾 Uvod hry</summary>

   #### 🎮 Obesenec
   1. Pomocna promenna `SLOVO` (konstanta)
   2. Pomocna promenna `tajenka` (podtrzitka misto pismen)
   3. Pomocna promenna `zivoty` (hodnota = `7`)
   4. Pomocna promenna `hra_probiha` (hodnota = `True`)
   ```python
   #!/usr/bin/python3


   SLOVO = "obesenec"
   tajenka = len(SLOVO) * ["_"]
   zivoty = 7
   hra_probiha = True
   ```

---

</details>

<details>
   <summary>♻ Prubeh kol</summary>

   #### 🔚 Kdy hra konci
   1. Dokud ma hrac v promenne `zivoty` hodnotu vetsi jak `0`
   2. Nasledne zastavime prubeh pomoci `hra_probiha`
   ```python
   while hra_probiha and zivoty > 0:
       ...
   else:
       if not hra_probiha:
           print(f"Tajenka: {SLOVO}")
           print("Super! Vitezis, jsi frajer kurzu!")
       else:
           print(f"Bohuzel, prohrals. Hledane slovo: *{SLOVO}*")
   ```

   #### 👀 V kazdem kole
   1. Vypisu stav hry
   2. Necham hrace zadat pismeno/slovo (promenna `hadani`)
   3. Sestavime vhodne podminky
   ```python
   print(f"TAJENKA: {' '.join(tajenka)}, ZIVOTY: {zivoty}")
   hadani = input("Hadej pismeno nebo cele slovo:").lower()

   if hadani == SLOVO:
       hra_probiha = False

   elif len(hadani) == 1 and hadani in SLOVO:
       for index, pismeno in enumerate(SLOVO):
           if pismeno == hadani:
               tajenka[index] = hadani
       if "_" not in tajenka:
           hra_probiha = False

   else:
       zivoty -= 1
   ```

   #### ❓ Konec nebo ne
   Hra nam funguje. Co bychom mohli zlepsit?
       1. Vice hadanych slov
       2. Nahodny vyber slova
       3. Cistejsi vypis

---

</details>

<details>
   <summary>⚙ Moduly</summary>

   #### ☝ K zapamatovani
   1. Jde o soubor s priponou `py`
   2. Obsahuje promenne, datove typy, standartni algoritmy
   3. Nektere jiz mame k dispozici (napr. `usr/lib/python3.8/`)
   ```python
   import pprint


   UDAJE = {
       "jmeno": "Matous",
       "prijmeni": "Holinka",
       "email": "matous@matous.cz",
       "adresa": "Kocourkov, U Potoka 28"
   }

   pprint.pprint(UDAJE)
   ```
   [**Odkaz**](https://repl.it/@JustBraloR/importing#main.py) pro spusteni

---

</details>

<details>
   <summary>🗃 Baliky</summary>

   #### ☝ K zapamatovani
   1. Vetsinou sbirka nekolika modulu
   2. Spolecne umistene v adresari
   3. Baliky obsahuji `__init__.py`
   4. Baliky obsahuji `__pycache__`

   #### 🔍 Soubor init
   Tento, dost casto prazdny, soubor umoznuje interpretu najit & nahrat moduly.
   Pokud neni prazdny, obsahuje dokumentace, zavislosti, aj.

   #### ⏩ Slozka pycache
   Tato slozka vznika, kdyz spoustime kod a interpret jej zkompiluje
   na _bytecode_. Nasledne schova zkompilovany kod do tohoto adresare.

---

</details>

<details>
   <summary>⏪ Rekapitulace</summary>

   #### 💪 Souhrn vyhod modulu & baliku
   1. Nemusime opakovane prepisovat stejne instrukce
   2. Muzu opakovane pouzivat na vice mistech
   3. Citelnosti je ucineno zadost

</details>

</details>

---

<details>
   <summary>📥 Importovani</summary>

   #### ☝ K zapamatovani
   Predpis pro nahrani modulu/baliku ma svoje pravidla:
   1. `import pprint` - nahrajeme cely modul, pouziti `modul.funkce`
   2. `from pprint import *` - nahrajeme cely modul, pouziti `funkce`
   3. `from pprint import pprint` - nahraje pouze vybranou funkci (`funkce`)
   4. `as` - doplneni aliasu, pouziti `from pprint import pprint as pp` (`pp`)

   #### 📽 Hledani modul
   1. Interpret uvidi oznameni o nahravani modulu (pr. `import`)
   2. Prohleda zabudovane moduly: `sys.builtin_module_names`
   3. Dale prohleda: `sys.modules` (s podporou symlinku)
   4. Dale prohleda aktualni umisteni: `sys.path[0]` (pokud nejsou symlinky, bude 3.)
   5. Dale prohleda: `sys.path[1:]`
   6. Pokud **nenasel** -> `ModuleNotFound`
   7. Pokud **nasel** -> nahravam modul, prip. balik

</details>

---

<details>
   <summary>🗂 Rozdeleni podle puvodu</summary>

<details>
   <summary>🏘 Knihovny standartni</summary>

   #### ☝ K zapamatovani
   Nainstalujeme jazyk, interpret a tyto knihovny. Nemusim instalovat, staci
   nahrat a pouzivat.

   #### ❓Modul random
   1. Pokud vyzadujeme vyuziti prvku pseudo-nahody, pouzijeme standartni modul
   `random`, dale doplnime seznam s vice slovy:
   ```python
   import random

   SLOVA = ["obesenec", "autobus", "klavesnice", "nedele"]
   ```
   2. Vybereme vhodnou funkci pro selekci nahodne udaje ze sekvence dat:
   ```python
   slovo = random.choice(SLOVA)
   ```

   #### 🕺 Vlastni modul
   1. Spolecne si nahrajeme nas vlastni modul `figurka`
   2. Pouzijeme slovnik `hangman` uvnitr souboru
   3. Doplnime vypis v kazdem kole a pri prohre
   ```python
   import figurka


   print(figurka.hangman[7 - zivoty])
   ```

   #### 📺 Modul os
   1. Protoze je nase hra prilis upovidana, nahrajeme dalsi standartni modul,
   ktery nam pomuze udrzet vystup mene upovidany
   2. Aplikujeme funkci, pro strucny vystup ve vypisu a v zaveru
   ```python
   import os

   os.system("clear")
   ```

---
</details>

<details>
   <summary>👾 Knihovny tretich stran</summary>

   #### ☝ K zapamatovani
   Protoze je knihoven pro Python spousta, nektere je potreba doinstalovat rucne.

<br />
<p align="center">
  <img alt="terminal-icon" width="80px" src="https://cubiclenate.files.wordpress.com/2018/04/terminal-icon.png?w=286&h=286" />
</p>

   #### 🆑 Pomoci prikazoveho radku
   1. Vytvorime virtualni pracovni prostredi:
   ```bash
   python3 -m venv <jmeno_prostredi>
   ```

   2. Aktivujeme virtualni pracovni prostredi:
   ```bash
   source <jmeno_prostredi>/bin/activate
   ```
   **Pozor!** Po aktivaci dostaneme na zacatku dotazovaciho radku zavorku
   se jmenem prostredi (pr. `(env)`)

   3. Overime dostupnost spravce balicku `pip3 --version`

   4. Pokud mame, instalujeme balicky (nahled [pypi.org](https://pypi.org/)):
   ```bash
   pip3 install <jmeno_balicku>         # instalace
   pip3 uninstall <jmeno_balicku>       # odstraneni
   pip3 --help                          # napoveda
   ```

   5. Vytvoreni souboru `requirements.txt` se zavislostmi:
   ```bash
   pip3 freeze > requirements.txt
   ```

   6. Pomoci zavilosti mohou ostatni uzivatele nainstalovat externi knihovny z 
   naseho virtualniho prostredi:
   ```bash
   pip3 install -r requirements.txt
   ```

<br />
<p align="center">
  <img alt="pycharm-icon" width="80px" src="https://caktus-website-production-2015.s3.amazonaws.com/media/blog-images/logo.png" />
</p>

   #### 🐍 Pomoci PyCharm
   1. Spustime Pycharm a otevreme projekt
   2. `ctrl + alt + s` -> Settings
   3. -> Project: <jmeno_projektu>
   4. -> Project interpreter
   5. ⚙ `Add...` Pridat prostredi/pouzit stavajici
   6. ➕ Instalovat knihovny pomoci symbolu `+` dole pod nabidkou
   7. `Terminal` dole na liste pro export zavislosti (`pip3 freeze > requirements.txt`)

</details>

</details>

---

➡ [pokracovat k dalsi casti](https://github.com/Bralor/python-workshop/tree/master/materials/05_functions_and_text_files)

