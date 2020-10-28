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

#### 📔 Odkazy
<details>
  <summary>🔽 Zobrazit vsechny odkazy</summary>

  - [Vzdelavaci platforma Engeta](https://engeto.com)
  - [Vstupni data, Shawshank Redemption](https://www.imdb.com/title/tt0111161/?ref_=fn_al_tt_1)
  - [Vstupni data, Godfather](https://www.imdb.com/title/tt0068646/?ref_=fn_al_tt_1)
  - [Vstupni data, Dark Knight](https://www.imdb.com/title/tt0468569/?ref_=fn_al_tt_1)
  - [Vstupni data, Prestige](https://www.imdb.com/title/tt0482571/?ref_=fn_al_tt_1)

</details>

---

#### ⏯  Ukazka programu
<details>
  <summary>🔽 Zobrazit ukazku</summary>

  1. ✌  [Stahnete si treti lekci jako **zip**](https://github.com/Bralor/python-academy/archive/lekce03.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **movies** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

#### 📥 Vstupni data
<details>
  <summary>🔽 Zobrazit vstupni data</summary>

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

#### 📔 Slovniky v Pythonu
<details>
  <summary>🔽 Zobrazit slovniky v Pythonu</summary>

  ##### 📂 Vytvorime pracovni adresar
  Vytvorime prazdny adresar pro jednotlive lekce a do nej dalsi:
  ```
  mkdir python-akademie
  mkdir python-akademie/lekce03
  ```

  ##### 🗄  Vytorime novy soubor
  ```
  touch movies.py       # Linux
  copy nul "movies.py"  # Windows
  ```

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
  ```python
  PISMENA = ["a", "b", "c", "d"]
  filmovy_slovnik["pismena"] = PISMENA
  ```

  ##### 🤦 Slovnik ve slovniku
  Tento princip muzeme chapat jako vkladani slovniku do slovniku (plati i pro
  jine datove typy jako senzamy aj.)
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


