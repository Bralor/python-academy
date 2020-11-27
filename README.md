➡ [vratit se na druhou lekci](https://github.com/Bralor/python-academy/tree/lekce02)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 3⃣ Python akademie
### 🗒 Dulezite odkazy
- [Python Academy, Engeto](https://engeto.com/)
- [The Shawshank Redemption](https://www.csfd.cz/film/2294-vykoupeni-z-veznice-shawshank/prehled/)
- [The Godfather](https://www.csfd.cz/film/1644-kmotr/prehled/)
- [The Dark Knight](https://www.csfd.cz/film/223734-temny-rytir/prehled/)
- [The Prestige](https://www.csfd.cz/film/223160-dokonaly-trik/prehled/)
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

  ##### 💂 Jednotlive slovniky s filmy
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
  <summary>❓ Co je to slovnik</summary>

  #### ☝ K zapamatovani
  - **standartni datovy typ** Pythonu
  - tvoreny pary **klic: hodnota**
  - podle **klice** vratim (mapuji) **hodnotu** (ne naopak)
  - klic je **unikatni** (napr. retezec, cislo)
  - hodnota nemusi byt (napr. retezec, cislo, seznam, ntice, jiny slovnik)
  - nelze indexovat jako seznamy/ntice
  - nemaji poradi jako seznamy/ntice

  #### ❓ Jak vypada slovnik
  ```python
  DETAILY = {"jmeno": "Matous", "email": "matous@matous.cz", "vek": 34}
  ```

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
  <summary>🗝  Vlozime prvni klic</summary>

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

  #### 🥉 Zpusoby odstranovani
  - `del` - zabudovana funkce Pythonu
  - `pop` - metoda slovniku pro odstraneni klice
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
  print(
      "VITEJTE V NASEM FILMOVEM SLOVNIKU!".center(76, " "),
      ODDELOVAC,
      "VYBERTE KATEGORII:",
      ODDELOVAC,
      "VSECHNY FILMY | DETAILY FILMU | SPOLECNI HERCI | VSICHNI REZISERI".center(76, " "),
      ODDELOVAC
  )
  ```
---

</details>

<details>
  <summary>☠  Volitelne klicove argumenty</summary>

  #### 📕 Zkraslime nas zapis
  Volitelny argument `sep`, ktery je dostupny u funkce `print` umozni prokladat
  jednotlive udaje volitenymi znaky:

  Pouziti argumentu `sep`:
  ```python
  ODDELOVAC = "=" * 76

  print(
      "VITEJTE V NASEM FILMOVEM SLOVNIKU!".center(76, " "),
      ODDELOVAC,
      "VYBERTE KATEGORII:",
      ODDELOVAC,
      "VSECHNY FILMY | DETAILY FILMU | SPOLECNI HERCI | VSICHNI REZISERI".center(76, " "),
      ODDELOVAC,
      sep="\n"
  )
  ```
---

</details>

</details>

---

<details>
  <summary>🆎 Slozitejsi podminkovy zapis</summary>

<details>
  <summary>🌲 Strom podminek</summary>

  #### 🐭 Jak rozhodovat
  Tentokrat bude nas *control-flow* ustit ve 5 potencialnich procesu:
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
  Uzivatel vybere jeden ze 4 procesu:
  ```python
  vyber = input("VYBERTE MOZNOST: ")
  print(ODDELOVAC)
  ```
  **Pozor!** doplnime funkcionalitu pro mala/velka pismena.
  ```python
  vyber = input("VYBERTE MOZNOST: ").lower()
  print(ODDELOVAC)
  ```

---

</details>

<details>
  <summary>🎬 Vypis vsechny filmy</summary>

  #### 👓 Pohledy slovniku
  Pomoci pohledu slovniku (metod), muzeme sledovat:
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
  Druha podminka vrati detaily vybraneho filmu:
  - `get` - pokud najde klic, vrati jeho hodnotu
  ```python
  DETAILY = {"jmeno": "Matous", "email": "matous@matous.cz", "vek": 34}
  DETAILY.get("jmeno")  # "Matous"
  DETAILY.get("adresa")  # "None"
  DETAILY.get("adresa", "Klic neexistuje!")  # "Klic neexistuje!"
  ```
  **Pozor!** vyhodou metody je, ze nam interpret neskonci vyjimkou.
  ```python
  elif vyber == "detaily filmu":
      print(
          list(filmovy_slovnik.keys()),
          end=f"\n{ODDELOVAC}\n"
      )

      vyber_filmu = input("VYBERTE FILM (OPATRNE NA VELKA/MALA PISMENA): ")
      print(ODDELOVAC,
            filmovy_slovnik.get(vyber_filmu, "Vami zadany film neni v db"),
            sep="\n")
  ```
---

</details>

</details>

---

<details>
  <summary>🔢 Mnoziny v Pythonu</summary>

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

  #### ❓Jak vypada slovnik
  ```python
  prvni_set = set()
  druhy_set = {"Matous", "Marek", "Lukas", "Jan"}
  ```

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
      if prunik:
          print(f"SPOLECNI HERCI JSOU: {prunik}")
      else:
          print("ZADNI SPOLECNI HERCI")
  ```
---

</details>

<details>
  <summary>🕰  Posledni overovaci podminka</summary>

  #### 📢 Vsichni reziseri
  Nakonec chceme vypsat vsechny rezisery:
  ```python
  elif "reziseri" in vyber:
      set_reziseri = set((
          filmovy_slovnik["The Dark Knight"]["REZISER"],
          filmovy_slovnik["The Godfather"]["REZISER"],
          filmovy_slovnik["Shawshank Redemption"]["REZISER"],
          filmovy_slovnik["The Prestige"]["REZISER"]
      ))

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
---

</details>

<details>
  <summary>🏠 Procvicovani na doma</summary>

<details>
  <summary>🚧 Volitelny argument end</summary>

  Dalsim volitelnym argumentem funkce `print` je `end`. Doplni libovolny znak
  na zaver vypisovani:
  ```python
  ODDELOVAC = "=" * 76

  print(
    "VITEJTE V NASEM FILMOVEM SLOVNIKU!".center(76, " "),
    end=f"\n{ODDELOVAC}\n"
  )
  ```

</details>

<details>
  <summary>🚧 Metoda slovniku popitem</summary>
  Odstrani posledni pridany klic a jeho hodnotu. Soucasne vrati jako vystup
  tuple tohoto paru:
  ```python
  DETAILY = {"jmeno": "Matous", "email": "matous@matous.cz", "vek": 34}
  DETAILY.popitem()
  ('vek', 34)
  ```
</details>

<details>
  <summary>🚧 Metoda slovniku setdefault</summary>
  Nastavi novy klic s defaultni, nebo definovanou hodnotou:
  ```python
  DETAILY = {"jmeno": "Matous", "email": "matous@matous.cz", "vek": 34}
  DETAILY.setdefault("adresa")  # "adresa": None
  DETAILY.setdefault("adresa", "Kpt. Jarose 7b")  # "adresa": "Kpt. Jarose 7b"
  ```

</details>

---

➡ [pokracovat na ctvrtou lekci](https://github.com/Bralor/python-academy/tree/lekce04)

