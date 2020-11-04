➡ [vratit se na druhou lekci](https://github.com/Bralor/python-academy/tree/lekce02)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 3⃣ Python akademie
### 🗒 Dulezite odkazy
- [Python Academy, Engeto]()
- [The Shawshank Redemption]()
- [The Godfather]()
- [The Dark Knight]()
- [The Prestige]()
---

### 🗒 Obsah lekce
1. Ukazka ulohy
2. Vstupni data
3. Slovniky v Pythonu
4. Komunikace s uzivatelem
5. Slozitejsi podminkovy zapis
6. Mnoziny v Pythonu
---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si treti lekci jako **zip**](https://github.com/Bralor/python-academy/archive/lekce03.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **movies** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
  <summary>📥 Vstupni data</summary>

  ##### 💂 The Shawshank redemption
  ```python
  film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
  }
  ```

  ##### 👴 The Godfather
  ```python
  film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
  }
  ```

  ##### ⚔ The Dark knight
  ```python
  film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
  }
  ```

  ##### 🔥 The Prestige
  ```python
  film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
  }
  ```
</details>

---

<details>
  <summary>📔 Slovniky v Pythonu</summary>

<details>
  <summary>📂 Vytvorime adresar & novy soubor</summary>

  #### 📁 Vytvorime adresar pro nas kurz
  ```
  mkdir python-akademie
  ```
  #### 📁 Vytvorime adresar pro dnesni lekci
  ```
  mkdir python-akademie/lekce03
  ```
  #### 🎞 Vytvorime soubor pro dnesni lekce
  ```
  touch movies.py       # Linux
  copy nul "movies.py"  # Windows
  ```
---

</details>

<details>
  <summary>❓ Co je to slovnik</summary>

  #### ☝ K zapamatovani
  - **standartni datovy typ** Pythonu
  - tvoreny pary **klic: hodnota**
  - podle **klice** vratim (mapuji) **hodnotu** (ne naopak)
  - klic je **unikatni** (napr. retezec, cislo)
  - hodnota nemusi byt (napr. retezec, cislo, seznam, ntice, jiny slovnik)
  - nelze indexovat jako seznamy/ntice
  - nemaji poradi jako seznamy/ntice
---

</details>

<details>
  <summary>📓 Uvod k praci se slovniky</summary>

<details>
  <summary>📚 Vytvorime slovnik</summary>

  #### 👷 Procvicime dvoji zpusob
  ```python
  filmovy_slovnik = {}      # 1. zpusob
  filmovy_slovnik = dict()  # 2. zpusob
  ```
---

</details>

<details>
  <summary>🗝  Vlozime prvni klc</summary>

  #### 🔑 Vlozime klic
  Hranate zavorky u slovniku se nechovaji jako u seznamu:
  ```python
  filmovy_slovnik["jmeno"] = None
  ```

  #### 👑 Pridame hodnotu
  ```python
  filmovy_slovnik["jmeno"] = "Matous"
  ```
---

</details>

<details>
  <summary>😱 Ruzne hodnoty</summary>

  #### 😑 Seznam jako hodnota
  Do slovniku muzeme ke klici ulozit nejen cisla ci slova. Muzeme ulozit i
  seznamy a ntice:
  ```python
  PISMENA = ["a", "b", "c", "d"]
  filmovy_slovnik["pismena"] = PISMENA
  ```

  #### 🤦 Slovnik ve slovniku
  Do slovniku muzu vlozit i jine slovniky:
  ```python
  vnoreny_slovnik_1 = {"jmeno": "Lukas"}
  vnoreny_slovnik_2 = {"jmeno": "Jan"}

  filmovy_slovnik["1_slovnik"] = vnoreny_slovnik_1
  filmovy_slovnik["2_slovnik"] = vnoreny_slovnik_2
  ```
  Doplnime nase slovniky `film_1`, `film_2`, `film_3` a `film_4` do slovniku
  `filmovy_slovnik`:
  ```python
  filmovy_slovnik = {}

  filmovy_slovnik[film_1["JMENO"]] = film_1
  filmovy_slovnik[film_2["JMENO"]] = film_2
  filmovy_slovnik[film_3["JMENO"]] = film_3
  filmovy_slovnik[film_4["JMENO"]] = film_4
  ```
---

</details>

<details>
  <summary>⏪ Odstranime klice & hodnoty</summary>

  #### 🥉Zpusoby odstranovani
  - `del` - zabudovana funkce Pythonu
  - `pop` - metoda slovniku pro odstraneni klice
  - `popitem` - metoda slovniku pro odstraneni posledniho pridaneho klice
  ```python
  del filmovy_slovnik["1_slovnik"]
  filmovy_slovnik.pop("2_slovnik")
  ```

</details>

</details>

</details>

---

<details>
  <summary>📞 Komunikace s uzivatelem</summary>

<details>
  <summary>📡 Pozdravime uzivatele</summary>

  #### 🗣Uvitaci oznameni
  ```python
  print("VITEJTE V NASEM FILMOVEM SLOVNIKU!")
  ```
  #### 📖 Doplnime oddelovac
  Jde jen o vizualni prvek v ramci prikazoveho radku:
  ```python
  ODDELOVAC = "=" * 76

  print("VITEJTE V NASEM FILMOVEM SLOVNIKU!")
  print(ODDELOVAC)
  ```
---

</details>

<details>
  <summary>🔄 Zarovnani textu</summary>

  #### ↔ Centrovani zpravy
  Retezec muzeme zarovnat pomoci **metod**:
  
  - metoda `center`
  - metoda `ljust`
  - metoda `rjust`
  ```python
  ODDELOVAC = "=" * 76

  print("VITEJTE V NASEM FILMOVEM SLOVNIKU!".center(76, " "))
  print(ODDELOVAC)
  ```
---

</details>

<details>
  <summary>🔝 Vypis nabidky</summary>

  #### 😎 Zprava s nabidkou
  Vypiseme nabidku, kterou bude mit uzivatel k dispozici (pozdeji doplnime):
  ```python
  print("Vitejte v nasi skromne filmove databazi".center(76, " "))

  print(
  f"""{ODDELOVAC}
  VYBERTE KATEGORII:
  {ODDELOVAC}
  {'VSECHNY FILMY | DETAILY FILMU | SPOLECNI HERCI | VSICHNI REZISERI'.center(76, " ")}
  {ODDELOVAC}"""
  )
  ```
---

</details>

<details>
  <summary>☠  Volitelne klicove argumenty</summary>

  #### 📕 Zkraslime nas zapis
  U funkce `print` nas budou zajimat tyto:
  - `end` - nepovinny argument, ktery doplni libovolny znak na zaver vypisovani
  - `sep` - nepovinny argument, ktery se vklada mezi jednotlive udaje

  Pouziti argumentu `end`:
  ```python
  ODDELOVAC = "=" * 76

  print(
    "VITEJTE V NASEM FILMOVEM SLOVNIKU!".center(76, " "),
    end=f"\n{ODDELOVAC}\n"
  )
  ```

  Pouziti argumentu `sep`:
  ```python
  ODDELOVAC = "=" * 76

  print(
      "VYBERTE KATEGORII:",
      "VSECHNY FILMY | DETAILY FILMU | SPOLECNI HERCI | VSICHNI REZISERI".center(76, " "),
      sep=f"\n{ODDELOVAC}\n",
      end=f"\n{ODDELOVAC}\n"
  )
  ```
---

</details>

</details>

---

<details>
  <summary>🆎 Podminkovy zapis</summary>

<details>
  <summary>🌲 Strom podminek</summary>

  #### 🐭 Jak rozhodovat
  Podminky nam umozni vzdy vybrat jeden proces, ktery budeme chtit aplikovat.
  Mame 4 ruzne procesy, takze potrebujeme vytvorit 4 ruzne podminky:
  ```python
  # bud VSECHNY FILMY
  # nebo DETAILY FILMU
  # nebo SPOLECNI HERCI
  # neco VSICHNI REZISERI
  # jinak UKONCIT
  ```
---
</details>

<details>
  <summary>✅ Vyber uzivatele</summary>

  #### 🛐 Vstup od uzivatele
  Uzivatel si musi nejprve vybrat jednu moznost. Kod musi fungovat jak pro mala,
  tak pro velka pismena:
  ```python
  vyber = input("VYBERTE MOZNOST: ").lower()
  print(ODDELOVAC)
  ```
---

</details>

<details>
  <summary>🎬 Vypis vsechny filmy</summary>

  #### 👓 Pohledy slovniku
  Prvni vetev naseho podminkoveho zapisu vrati jmena vsech filmu. Pomohou nam
  pohledy slovniku (metody slovniku):
  - `items` - vrati objekt s klici a jejich hodnotami
  - `keys` - vrati objekt s klici
  - `values` - vrati objekt s hodnotami
  
  Nasledne prevedeme vysledny objekt pomoci built-in funkce `list`:
  ```python
  if vyber == "vsechny filmy":
      print(
          "Mame v nabidce tyto snimky:",
          list(filmovy_slovnik.keys()),
          end=f"\n{ODDELOVAC}\n"
      )
  ```
---

</details>

<details>
  <summary>🔎 Vypis detaily filmu</summary>

  #### 🔖 Metody slovniku
  Druha podminka bude mit na starost obstarat vystup, ktery zahrnuje obsah
  jednotlivych vnitrnich slovniku (tedy detaily konkretniho filmu).
  - `get` - pokud najde klic, vrati jeho hodnotu
  - `setdefault` - nastavi novy klic s hodnotou

  Film pak muzeme ziskat pomoci dalsi metody slovniku `get`. Tato metoda ma
  za cil jedine, najde klic, ktery ji zadame a ona vrati jeho hodnotu.
  Volitelne pak muzeme nastavit, co vrati, pokud hledany klic nenajde.
  ```python
  elif vyber == "detaily filmu":
      print(
          list(filmovy_slovnik.keys()),
          end=f"\n{ODDELOVAC}\n"
      )

      vyber_filmu = input("VYBERTE FILM: ")
      print(ODDELOVAC,
            filmovy_slovnik.get(vyber_filmu, "Vami zadany film neni v db"),
            sep="\n")
  ```
---

</details>

</details>

---

<details>
  <summary>🔢 Mnoziny</summary>

<details>
  <summary>❓ Co je to mnozina</summary>

  #### ☝ K zapamatovani
  - **standartni datovy typ** Pythonu
  - tvoreny **unikatnimi** hodnotami
  - nema poradi (podobne slovnikum)
  - idealni pro praci s matematickymi mnozinami
  - sjednoceni (`union`/ `|`)
  - prunik (`intersection`/ `&`)
  - rozdil (`difference`/ `-`)
  - symetricky rozdil (`^`)
---

</details>

<details>
  <summary>📓 Uvod k praci se mnozinami</summary>

  #### 📌 Vytvorime mnozinu
  ```python
  prvni_set = set()
  druhy_set = {"Matous", "Marek", "Lukas", "Jan"}
  ```

  #### 🔁 Pridavame, odebirame
  - `add` - pridame hodnoty
  - `discard` - odstranime hodnoty
  ```python
  prvni_set.add("Matous")
  prvni_set.add("Marek")
  print(prvni_set)

  druhy_set.discard("Matous")
  print(druhy_set)
  ```

  #### 🗽 Sjednotime mnoziny
  ```python
  print(prvni_set | druhy_set)
  ```
---

</details>


<details>
  <summary>🎎 Dalsi podminka</summary>

  #### 👪 Spolecni herci
  Nyni chceme zjistit, kteri herci hraji ve dvou ruznych libovolnych filmech:
  ```python
  elif vyber == "spolecni herci":
      print(
        list(filmovy_slovnik.keys()),
        end=f"\n{ODDELOVAC}\n"
        )

      prvni_film = input("VYBERTE I. FILM: ")
      druhy_film = input("VYBERTE II. FILM: ")

      herci_prvni_film = set(filmovy_slovnik[prvni_film]["HRAJI"])
      herci_druhy_film = set(filmovy_slovnik[druhy_film]["HRAJI"])

      prunik = herci_film1 & herci_film2
      print(f"SPOLECNI HERCI JSOU: {prunik}")
  ```
---

</details>

<details>
  <summary>🕰 Posledni podminka</summary>

  #### 📢 Vsichni reziseri
  Nakonec chceme vypsat vsechny rezisery:
  ```python
  elif "reziseri" in vyber:
      set_reziseri = set(
          filmovy_slovnik["The Dark Knight"]["REZISER"],
          filmovy_slovnik["The Godfather"]["REZISER"],
          filmovy_slovnik["Shawshank Redemption"]["REZISER"],
          filmovy_slovnik["The Prestige"]["REZISER"]
      )

      print(f"VSICHNI REZISERI: {set_reziseri}")
  ```
---

</details>

<details>
  <summary>🔚 Ukoncujici podminka</summary>

  #### 🤦 Posledni moznost
  Pokud uzivatele zada cokoliv jineho:
  ```python
  else:
    print(f"MOZNOST -> {vyber} NENI V NABIDCE! UKONCUJI..")
  ```

</details>

---

➡ [pokracovat na dalsi lekci](https://github.com/Bralor/python-academy/tree/lekce04)

