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
2. Doplnime ulohu z [prvni lekce](https://github.com/Bralor/python-academy/blob/lekce01/destinatio_p1.py)
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

<details>
  <summary>📝 Doplnime ulohu</summary>

  #### 💲 Pridame slevy
  Jakmile uzivatel nakoupi jizdenku do jedne z vybranych lokalit, dostane 25%
  slevu:
  ```python
  SLEVY = ("Olomouc", "Svitavy")
  AKT_ROK = 2020
  ```

</details>

---

<details>
  <summary>Jak pracovat s Pythonem</summary>

</details>

---


<details>
  <summary>📘 Datovy typ boolean</summary>

<details>
  <summary>📌 Boolean hodnoty</summary>
  #### ☝ K zapamatovani
  - specialni datovy typ spadajici pod _integer_
  - ciselne hodnoty **1** a **0**
  - hodnoty **True** a **False**
  - pomahaji resit, jestli je podminka/metoda pravdiva nebo neni
  
  #### ❓ Jak vypada boolean
  ```python
  jmeno_promenne = True
  ```

  #### 🔎 Co je vsechno pravda (v Pythonu)
  Funkce `bool` nam pomuze zjistovat, co je ci neni pravdive:
  ```python
  bool(1 < 3)   # True
  bool(1 < -3)  # False
  ```
  **Pozor!** Boolean hodnotu maji i hodnoty, u kterych bychom je necekali:
  ```python
  bool(2)           # True
  bool("Matous")    # True
  bool("")          # False
  bool(" ")         # True
  bool([])          # False
  bool([" "])       # True
  ```

</details>

---

<details>
  <summary>📌 Boolean hodnoty</summary>
  
  #### 💻 Logicke operatory
  S boolean hodnotami souvisi pouziti logickych operatoru:
  1. `and`
  2. `or`
  3. `not`
  ```python
  bool(True and True)       # True
  bool(True and False)      # False
  bool(False and False)     # False
  bool(not True)            # False

  bool(True or True)        # True
  bool(True or False)       # True
  bool(False or True)       # True
  bool(False or False)      # False
  ```
</details>

</details>

---

<details>
  <summary>👉 Podminkovy zapis</summary>

<details>
  <summary>🔧 Predpis podminkoveho zapisu</summary>
  Podminkovy zapis obsahuje:
  1. `if` klicovy vyraz
  2. `bool()` overovany vyraz
  3. `:` zahlavi zakoncene dvojteckou
  4. odsazeny odstavec instrukci

  #### 🎨 Jak vypada podminkovy zapis
  ```python
  X = 10_000
  Y = 15_000

  if X < Y:
    print("Ano, to je pravda!")
  else:
    print("Ne, toto neni pravda!")
  ```
  **control-flow** ve vzoru vyse je jednoduchy podminkovy zapis slozeny
  z dvou moznych scenaru.

---

</details>

<details>
  <summary>❎ Platne cislo lokality</summary>

  #### 📺 Podminka
  ```python
  if cislo_lokality <= 0 or cislo_lokality < 6:
    # pocitame cenu
  else:
    # ukoncime
  ```

  #### ↔ Delka objektu
  Pomoci funkce `len` muzeme zjistit delku objektu:
  ```python
  PISMENA = ["a", "b", "c"]; len(PISMENA) # 3
  JMENO = "Matous"; len(JMENO)            # 6
  ```

  #### ⏹ Ukonceni programu
  Pro ukonceni beziciho programu mame tyto moznosti:
  1. `exit()`
  2. `quit()`
  3. `sys.exit()`/`os._exit()`
  **Pozor!** `exit`/`quit` funkce ukazuji na stejny objekt
  **Varianta 3** vice se dozvime az v lekci o modulech v Pythonu

  #### 🔁 Opravime prvni podminku
  ```python
  cislo_lokality = int(input("VYBERTE CISLO LOKALITY: "))

  if 0 <= cislo_lokality < len(MESTA):
      destinace = MESTA[cislo_lokality - 1]
      cena = CENY[cislo_lokality - 1]
      print(f"DESTINACE: {destinace}")
      print(ODDELOVAC)
  else:
      print("VAMI VYBRANE CISLO NENI V NABIDCE, UKONCUJI..")
      quit()
  ```

</details>

---

<details>
  <summary>💰 Vypocet ceny po sleve</summary>

  #### 💁 Overeni clenstvi
  V podstate se ptame, jestli je nejaky udaj soucasti konkretni sekvence:
  ```python
  JMENA = ("Marek", "Lukas", "Jan")

  bool("Marek" in JMENA)  # True
  bool("Tomas" in JMENA)  # False
  ```

  #### 🆕 Nova cena
  Pokud je cilova lokalita mezi zlevnenymi, vypocitej novou cenu:
  ```python
  if destinace in SLEVY:
      cena_po_sleve = 0.75 * cena
      print("ZISKAVATE 25% SLEVU!")
  else:
      cena_po_sleve = cena
  ```

</details>

---

<details>
  <summary>📛 Spravne jmeno a prijmeni</summary>

  #### 🥅 Nas cil
  Potrebujeme overit, jestli promenne `jmeno` a `prijmeni` obsahuji pouze
  symboly pismen.

  #### 🖱 Metody retezcu
  Datove typy maji uzitecne pomucky pro efektivnejsi praci s nimi:
  1. `isalpha` - vrati `True` pokud jsou vsechny znaky pismena, jinak `False`
  2. `isnumeric` - vrati `True` pokud jsou vsechny znaky cislice, jinak `False`
  ```python
  help(str)  # napoveda pro retezce v ramci interpretu
  ```

  #### ➕ Overeni udaju
  ```python
  jmeno = input("JMENO: ")
  prijmeni = input("PRIJMENI: ")

  if jmeno.isalpha() and prijmeni.isalpha():
      print(f"JMENO: {jmeno}, PRIJMENI: {prijmeni}")
      print(ODDELOVAC)
  else:
      print("JMENO A PRIJMENI MUSI OBSAHOVAT POUZE PISMENA, UKONCUJI..")
      exit()
  ```

</details>

---

<details>
  <summary>👼 Overeni veku uzivatele</summary>

  #### 🥅 Nas cil
  Jen uzivatele starsi 18ti let mohou pouzivat nasi aplikaci. Ostatnim omezime
  pristup.

  #### 🖱 Metody retezcu
  ```python
  vek = int(input("ROK NAROZENI: "))

  if (AKT_ROK - vek) >= 18:
      print("POKRACUJI..")
      print(ODDELOVAC)
  else:
      print("NASE SLUZBY MOHOU VYUZIVAT POUZE OSOBY STARSI 18 LET, UKONCUJI..")
      quit()
  ```

</details>

---

<details>
  <summary>📮 Overeni emailu uzivatele</summary>

  #### 🥅 Nas cil
  Mailovou adresu overime pomoci dvou kriterii:
  1. Obsahuje znak `@`
  2. Obsahuje `.cz` (TLD)

  #### 🏫 Spojeni dvou podminek
  ```python
  email = input("EMAIL: ")

  if "@" in email and ".cz" in email:
      print("EMAIL V PORADKU, POKRACUJI..")
      print(ODDELOVAC)
  else:
      print("NEPODPOROVANY FORMAT EMAILU, UKONCUJI..")
      quit()
  ```

  #### 🔪Cast retezce
  Pokud chceme ziskat jen vyrez z retezce (slicing):
  ```python
  jmeno = "Matous"

  jmeno[0:2]  # jmeno[start:stop] -> prvni 3 pismena
  jmeno[:3]   # jmeno[start:stop] -> prvni 3 pismena
  jmeno[3:]   # jmeno[start:stop] -> bez prvnich 3 pismen
  jmeno[-3:]   # jmeno[start:stop] -> posledni 3 pismena
  ```
  #### 🆕 Upravena podminka
  Overime, ze se `.cz` nachazi na poslednich 3 indexech (pomoci `==`):
  ```python
  email = input("EMAIL: ")

  if "@" in email and email[-3:] == ".cz":
      print("EMAIL V PORADKU, POKRACUJI..")
      print(ODDELOVAC)
  else:
      print("NEPODPOROVANY FORMAT EMAILU, UKONCUJI..")
      quit()
  ```

</details>

<details>
  <summary>🛂 Overeni hesla</summary>

  #### 🥅 Nas cil
  Heslo musi splnovat nasledujici kriteria:
  1. Je dlouhe alespon 8 znaku
  2. Obsahuje cislice
  3. Obsahuje pismena

  #### 📏 Delka
  ```python
  heslo = "panpes738";bool(len(heslo) >= 8)
  ```

  #### 🔢 Cislice
  ```python
  heslo = "12345678";heslo.isnumeric()
  ```

  #### 🔡 Pismena
  ```python
  heslo = "abcdefgh";heslo.isalpha()
  ```

  #### 🤼 Zkombinujeme vse
  ```python
  if len(heslo) >= 8 and not heslo.isalpha() and not heslo.isnumeric():
      # True and not False and not False
      # True and True and True -> True
      print("HESLO V PORADKU")
      print(ODDELOVAC)
      print("DESTINACE: " + destinace)
      print("DEKUJEME,", jmeno, "JIZDENKU POSLEME NA EMAIL:", email)
      print(f"CENA (CIL: {destinace}): {cena}")
  else:
      # True and not True and not False
      # True and False and True -> False
      print(
          """TVOJE HESLO JE SPATNE ZADANE:
      1. MUSI OBSAHOVAT ALESPON 8 ZNAKU
      2. MUSI OBSAHOVAT PISMENA
      3. MUSI OBSAHOVAT CISLICE
      """
      )
  ```

</details>

---

Pokracovat na [Lekci#03](https://github.com/Bralor/python-academy/tree/lekce03)

