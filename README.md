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
1. Odkazy
2. Demo
3. Vstupni data
4. Slovniky
5. Mnoziny
6. Dalsi podminky
7. Dalsi metody
---

<details>
  <summary>📔 Odkazy</summary>

 
  - [Vzdelavaci platforma Engeta](https://engeto.com)
  - [Vstupni data, Shawshank Redemption](https://www.imdb.com/title/tt0111161/?ref_=fn_al_tt_1)
  - [Vstupni data, Godfather](https://www.imdb.com/title/tt0068646/?ref_=fn_al_tt_1)
  - [Vstupni data, Dark Knight](https://www.imdb.com/title/tt0468569/?ref_=fn_al_tt_1)
  - [Vstupni data, Prestige](https://www.imdb.com/title/tt0482571/?ref_=fn_al_tt_1)

</details>

---

<details>
  <summary>⏯  Ukazka programu</summary>


  1. ✌  [Stahnete si treti lekci jako **zip**](https://github.com/Bralor/python-academy/archive/lekce03.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **movies** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
  <summary>📥 Vstupni data</summary>

  ##### The Shawshank redemption
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

  ##### The Godfather
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

  ##### The Dark knight
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

  ##### The Prestige
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

  ##### 📂 Vytvorime adresar & novy soubor
  <details>
    <summary>🔽 Zjisti vice...</summary>
    Vytvorime nejprve adresar pro nas kurz:
    ```
    mkdir python-akademie
    ```
    Potom adresar pro dnesni lekci:
    ```
    mkdir python-akademie/lekce03
    ```
    Posledni v rade bude dnesni uloha:
    ```
    touch movies.py       # Linux
    copy nul "movies.py"  # Windows
    ```

  </details>

  ##### ❓Co je to slovnik
  - **standartni datovy typ** Pythonu
  - tvoreny pary **klic: hodnota**
  - podle **klice** vratim (mapuji) **hodnotu** (ne naopak)
  - klic je **unikatni** (napr. retezec, cislo)
  - hodnota nemusi byt (napr. retezec, cislo, seznam, ntice, jiny slovnik)
  - nelze indexovat jako seznamy/ntice
  - nemaji poradi jako seznamy/ntice

  ##### 📓 Vytvorime prazdny slovnik
  ```python
  filmovy_slovnik = {}      # 1. zpusob
  filmovy_slovnik = dict()  # 2. zpusob
  ```

  ##### 🗝 Vlozime prvni klic
  Tak jak jsme pouzivali hranate zavorky u seznamu, je pouzijeme i u slovniku.
  Ale v tentokrat pro vytvoreni **klice a jeho **hodnoty**.
  ```python
  filmovy_slovnik["jmeno"] = None
  ```
  ##### 👑 Pridame hodnotu
  ```python
  filmovy_slovnik["jmeno"] = "Matous"
  ```

  ##### 😱 Pridame seznam jako hodnotu
  Do slovniku muzeme ke klici ulozit nejen cisla ci slova. Muzeme ulozit i
  seznamy a ntice:
  ```python
  PISMENA = ["a", "b", "c", "d"]
  filmovy_slovnik["pismena"] = PISMENA
  ```

  ##### 🤦 Slovnik ve slovniku
  Do slovniku muzu vlozit i jine slovniky:
  ```python
  vnoreny_slovnik_1 = {"jmeno": "Lukas"}
  vnoreny_slovnik_2 = {"jmeno": "Jan"}

  filmovy_slovnik["1_slovnik"] = vnoreny_slovnik_1
  filmovy_slovnik["2_slovnik"] = vnoreny_slovnik_2
  ```

  ##### ⏪ Odstranime klice & hodnoty
  - funkce `del`
  - metoda `pop`
  - metoda `popitem`
  ```python
  del filmovy_slovnik["1_slovnik"]
  filmovy_slovnik.pop("2_slovnik")
  ```

</details>

---

<details>
  <summary>📞 Komunikace s uzivatelem</summary>

  #### 📡 Pozdravime uzivatele
  Nejprve pozdravime uzivatele:
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

  #### 🔄 Zarovnani textu
  Retezec muzeme zarovnat pomoci **metod**:
  - metoda `center`
  - metoda `ljust`
  - metoda `rjust`
  ```python
  ODDELOVAC = "=" * 76

  print("VITEJTE V NASEM FILMOVEM SLOVNIKU!".center(76, " "))
  print(ODDELOVAC)
  ```

  #### 🔝 Vypiseme nabidku
  Vypiseme nabidku, kterou bude mit uzivatel k dispozici (pozdeji doplnime):
  ```python
  print(ODDELOVAC)
  print("Vitejte v nasi skromne filmove databazi".center(76, " "))

  print(
  f"""{ODDELOVAC}
  VYBERTE KATEGORII:
  {ODDELOVAC}
  {'VSECHNY FILMY | DETAILY FILMU | SPOLECNI HERCI | VSICHNI REZISERI'.center(76, " ")}
  {ODDELOVAC}"""
  )
  ```

  #### ☠  Volitelne klicove argumenty
  U funkce `print` nas budou zajimat tyto:
  - `end`
  - `sep`

  Pouziti argumentu `end`:
  ```python
  ODDELOVAC = "=" * 76

  print(
    "VITEJTE V NASEM FILMOVEM SLOVNIKU!".center(76, " "),
    end=f"\n{ODDELOVAC}"
  )
  ```

  Pouziti argumentu `sep`:
  ```python
  ODDELOVAC = "=" * 76

  print(
    "VYBERTE KATEGORII:",
    f"{'VSECHNY FILMY | DETAILY FILMU | SPOLECNI HERCI | VSICHNI REZISERI'.center(76, " ")}",
    sep=f"\n{ODDELOVAC}"
  )
  ```
---

<details>
  <summary>🆎 Podminkovy zapis</summary>

  #### 🌲 Strom podminek
  Podminky nam umozni vzdy vybrat jeden proces, ktery budeme chtit aplikovat.
  Mame 4 ruzne procesy, takze potrebujeme vytvorit 4 ruzne podminky:
  ```python
  # bud TOTO
  # nebo TOTO
  # nebo TOTO
  # jinak TOTO
  ```

  #### ✅ Vyber uzivatele
  Uzivatel si musi nejprve vybrat jednu moznost. Kod musi fungovat jak pro mala,
  tak pro velka pismena:
  ```python
  vyber = input("VYBERTE MOZNOST: ").lower()
  ```

  #### 🎬 Vypis vsechny filmy
  Prvni vetev naseho podminkoveho zapisu vrati jmena vsech filmu. Pomohou nam
  pohledy slovniku (metody slovniku):
  - `items` - vrati objekt s klici a jejich hodnotami
  - `keys` - vrati objekt s klici
  - `values` - vrati objekt s hodnotami
  
  Nasledne prevedeme vysledny objekt pomoci built-in funkce `list`:
  ```python
  if vyber == "vsechny filmy":
    print(ODDELOVAC)
    print(f"Mame v nabidce tyto snimky:")
    print(list(filmovy_slovnik.keys()))
    print(ODDELOVAC)
  ```

  #### 🔎 Detaily filmu
  Druha podminka bude mit na starost obstarat vystup, ktery zahrnuje obsah
  jednotlivych vnitrnich slovniku (tedy detaily konkretniho filmu).
  - `get` - pokud najde klic, vrati jeho hodnotu
  - `setdefault` - nastavi novy klic s hodnotou

  Film pak muzeme ziskat pomoci dalsi metody slovniku `get`. Tato metoda ma
  za cil jedine, najde klic, ktery ji zadame a ona vrati jeho hodnotu.
  Volitelne pak muzeme nastavit, co vrati, pokud hledany klic nenajde.
  ```python
  elif vyber == "detaily filmu":
    print(ODDELOVAC)
    print(list(filmovy_slovnik.keys()))
    print(ODDELOVAC)

    vyber_filmu = input("VYBERTE FILM: ")
    print(ODDELOVAC)
    pprint(filmovy_slovnik.get(vyber_filmu, "Vami zadany film neni v db"))
  ```

</details>
</details>

---

<details>
  <summary>🔢 Mnoziny</summary>

  #### 📊 Obecne
  Mnozina neboli set je opet neserazena kolekce udaju, ktera je typicka tim,
  ze uvnitr nenajdeme zadnou hodnotu dvakrat. Sety se pouzivaji zejmena kvuli
  svym matematickym operacim.
  - sjednoceni (`union`/ `|`)
  - prunik (`intersection`/ `&`)
  - rozdil (`difference`/ `-`)
  - symetricky rozdil (`^`)
  
  #### 📌 Vytvorime mnozinu
  ```python
  prvni_set = set()
  print(type(prvni_set))

  druhy_set = {"Matous", "Marek", "Lukas", "Jan"}
  print(type(druhy_set))
  ```

  #### 🔁 Pridavame, odebirame
  - `add`
  - `discard`
  ```python
  novy_set = set()

  novy_set.add("Matous")
  novy_set.add("Marek")
  print(novy_set)

  novy_set.discard("Matous")
  print(novy_set)
  ```

  #### 🎎 Spolecni herci
  Dalsi funkci bude zjistit spolecne herce pro dva ruzne filmy.
  ```python
  set1 = {"Pavel", "Matous", "Tomas", "Martin"}
  set2 = {"Martin", "Petr", "Vojtech"}

  print(set1 & set2)  # "Martin"
  ```
  Dokonceni dalsi podminky:
  ```python
  elif vyber == "spolecni herci":
      print(ODDELOVAC)
      print(list(filmovy_slovnik.keys()))
      print(ODDELOVAC)

      film1 = input("VYBERTE I. FILM: ")
      film2 = input("VYBERTE II. FILM: ")

      herci_film1 = set(filmovy_slovnik[film1]["HRAJI"])
      herci_film2 = set(filmovy_slovnik[film2]["HRAJI"])

      prunik = herci_film1 & herci_film2
      print(
          f"SPOLECNI HERCI PRO *{filmovy_slovnik[film1]['JMENO']}* \
          A *{filmovy_slovnik[film2]['JMENO']}*: {prunik}"
      )
  ```

  #### 📢 Vsichni reziseri
  Nakonec chceme zapsat podminkovou vetev, ktera nam vrati vsechny rezisery.
  ```python
  elif "reziseri" in vyber:
      print(ODDELOVAC)
      set_reziseri = (
          filmovy_slovnik["The Dark Knight"]["REZISER"],
          filmovy_slovnik["The Godfather"]["REZISER"],
          filmovy_slovnik["Shawshank Redemption"]["REZISER"],
          filmovy_slovnik["The Prestige"]["REZISER"]
      )

      print("VSICHNI REZISERI V NASEM SEZNAMU:")
      print(f"{set_reziseri}")
  ```

</details>

<details>
  <summary> 📦 Dalsi metody</summary>

  #### 🔢 Podmnozina
<details>
  <summary> 🔽 vice o...</summary>

  Jde o dalsi metodu typickou pro mnoziny...

</details>

  #### 🔢 Disjoint
<details>
  <summary> 🔽 vice o...</summary>

  Jde o dalsi metodu typickou pro mnoziny...

</details>

</details>

---

