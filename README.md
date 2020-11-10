➡ [vratit se na uvodni lekci](https://github.com/Bralor/python-academy/tree/master)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 1⃣ Python akademie
### 🗒 Dulezite odkazy
- [Repl.it](https://repl.it/)
- [Engeto.com](https://engeto.com/cs/)
- [Python Academy, Git](https://engeto.com/cs/kurz/git-zaklady-pro-uzivatele/lekce)
- [Python Academy, zaciname!](https://engeto.com/cs/kurz/python-academy/studium/SpmtH-mVRY6zPL9alhruMQ/home-set-up/basics-of-command-line)
- [Python, dokumentace zabudovanych funkci](https://docs.python.org/3/library/functions.html)
---

### 🗒 Obsah lekce
1. Ukazka ulohy
2. Ciselne a textove hodnoty
3. Promenne
4. Kontejnerove datove typy
5. Uvodni sekce
6. Vkladame udaje
7. Vystup programu
---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si prvni lekci jako **zip**](https://github.com/Bralor/python-academy/archive/lekce01.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **destinatio_p1** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
  <summary>🔜 Ciselne a textove hodnoty</summary>

<details>
  <summary>🔢 Cisla</summary>

  #### ✌ Cela cisla(integers)
  ```python
  100 + 200  # 300
  300 - 100  # 200
  type(1234) # overeni
  ```

  #### 💲 Desetinna cisla(floats)
  **Pozor!** Desetinnym oddelovacem je tecka. Carka slouzi k jinym ucelum.
  ```python
  0.1 + 0.3  # 0.4
  type(0.4)  # overeni
  ```
  **Plovouci radova carka** nektera desetinna cisla nemaji odpovidajici
  binarni tvar. Proto jsou ulozena jako priblizne hodnoty.
  ```python
  0.1 + 0.2  # 0.30000000000000004
  type(0.3)  # overeni
  ```

  #### 💹 Aritmeticke operace
  ```python
  10 + 5    # 15
  10 - 5    # 5
  10 * 5    # 50
  10 / 5    # 2.0 (?)
  10 // 3   # celociselne deleni
  10 % 3    # ziskani zbytku po deleni
  10 ** 3   # umocnovani
  ```
---

</details>

<details>
  <summary>🔡 Text</summary>

  #### 🆎 Retezce(strings)
  Ruzne dlouhe uskupeni znaku (cisla, pismena, specialni symboly), ohranicene
  uvozovkami:
  1. `'Matous'` jednoduche uvozovky
  2. `"Matous"` dvojite uvozovky
  3. `"""Matous"""` trojite uvozovky (take `'''Matous'''`)

  ```python
  "Matous Holinka"  # <class 'str'>
  '1234566789'      # <class 'str'>
  "!@#$%%^&*"       # <class 'str'>
  '''Matous
  Holinka'''        # 'Matous\nHolinka'
  ```

---

</details>

<details>
  <summary>🔁 Prevadeni</summary>

  #### 🔀 Z retezce na cislo
  ```python
  2 + 2         # 4
  "2" + "2"     # '22'
  type("2")          # <class 'str'>
  type(int("2"))     # <class 'int'>
  ```
  **Nektere datove typy neni mozne prevest!**

</details>

</details>

---

<details>
  <summary>📦 Promenne</summary>

  #### ☝ K zapamatovani
  - promenne jsou v podstate symbolicke odkazy
  - v pameti odkazuji na konkretni objekt
  - potrebne pokud chceme hodnotu opakovane pouzivat
  - v Pythonu muzeme prepisovat typ hodnoty

  #### 📺 Zapis
  ```python
  jmeno_promenne = "hodnota_promenne"
  ```
  **Pozor!** Jista [pravidla](https://easycodebook.com/python-variable-names-and-naming-rules/)
  musime dodrzet i pri vytvareni jmen promennych.

  ```python
  MESTO = 'Praha'     # <class 'str'>
  MNOZSTVI = 2        # <class 'int'>
  CENA = 1000.5       # <class 'float'>
  ```

</details>

---

<details>
  <summary>📬 Kontejnerove datove typy</summary>

<details>
  <summary>📑 Seznam(list)</summary>

  #### ☝ K zapamatovani
  - tvoreny hranatymi zavorkami
  - udaje oddelene _carkou_ (ucel carky je tedy datovy oddelovac)
  - muzeme pridavat a odebirat udaje (_zmenitelna_ posloupnost)
  - udaje maji dane _poradi_
  - muze obsahovat retezec, cela cisla, desetinna cisla i jine seznamy
  - muzeme _indexovat_

  #### ❓ Jak vypada seznam
  ```python
  jmeno_seznamu = ["udaj_1", "udaj_2", "udaj_3", "udaj_4"]
  ```

  #### 🔝 Nas prvni seznam
  **Konstanta** obsahuje mesta, ktere budeme pouzivat v prvni uloze:
  ```python
  MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
  type(MESTA)
  ```
  Indexovani umoznuje najit hodnotu pomoci jejiho indexu:
  ```python
  MESTA[0]  # vrati udaj s indexem 0 (prvni hodnotu v zavorkach)
  MESTA[-1] # vrati udaj s indexem -1 (posledni hodnota)
  MESTA[1]  # vrati udaj s indexem 1 (druha hodnota)
  ```
---

</details>

<details>
  <summary> 🤕 Ntice(tuple)</summary>

  #### ☝ K zapamatovani
  - tvoreny kulatymi zavorkami
  - udaje oddelene _carkou_ (ucel carky je tedy datovy oddelovac)
  - **nemuzeme** pridavat a odebirat udaje (_nezmenitelna_ posloupnost)
  - udaje maji dane _poradi_
  - muze obsahovat retezec, cela cisla, desetinna cisla, seznamy a ntice
  - muzeme _indexovat_

  #### ❓ Jak vypada ntice
  ```python
  jmeno_tuplu = ("udaj_1", "udaj_2", "udaj_3", "udaj_4")
  ```

  #### 🔝 Nas prvni tupl
  **Konstanta** obsahuje ceny imaginarniho jizdneho:
  ```python
  CENY = (150, 200, 120, 120, 100, 180)
  type(CENY)
  ```
  Indexovani umoznuje najit hodnotu pomoci jejiho indexu:
  ```python
  CENY[0]  # vrati udaj s indexem 0 (prvni hodnotu v zavorkach)
  CENY[-1] # vrati udaj s indexem -1 (posledni hodnota)
  CENY[1]  # vrati udaj s indexem 1 (druha hodnota)
  ```

</details>

</details>

---

<details>
  <summary>👋 Uvodni sekce</summary>

  #### 🛠 S cim budeme pracovat
  Nejprve potrebujeme promenne:
  ```python
  """Lekce #1 - Uvod do programovani, Destinatio, cast 1."""

  MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
  CENY = (150, 200, 120, 120, 100, 180)
  ODDELOVAC = "==================================="
  ```

  #### 🖨  Vypiseme pozdrav
  Pomoci zabudovane funkce `print`, pozdravime uzivatele:
  ```python
  print("VITEJTE U NASI APLIKACE DESTINATIO!")  # I. varianta

  pozdrav = "VITEJTE U NASI APLIKACE DESTINATIO!"
  print(pozdrav)  # II. varianta
  ```

  #### 🖌 Oddelime text
  ```python
  print("VITEJTE U NASI APLIKACE DESTINATIO!")  # I. varianta
  print(ODDELOVAC)
  ```

  #### 📋 Zobrazime nabidku
  Nakopirujeme nabidku a opet oddelime:
  ```python
  print(
  """
  1 - Praha   | 150
  2 - Viden   | 200
  3 - Olomouc | 120
  4 - Svitavy | 120
  5 - Zlin    | 100
  6 - Ostrava | 180
  """
  )
  print(ODDELOVAC)
  ```

</details>

---

<details>
  <summary>🗣 Vkladame udaje</summary>

  #### ✍ Zapiseme udaje
  Pomoci dalsi funkce, `input`, muzeme udaje do naseho programu ulozit:
  ```python
  jmeno = input("ZAPIS SVOJE JMENO: ")
  print(jmeno, type(jmeno))
  ```

  #### ☝ Jake udaje
  1. vyber lokality
  2. jmeno
  3. prijmeni
  4. rok narozeni
  5. e-mail
  6. heslo

  ```python
  cislo_lokality = int(input("VYBERTE CISLO LOKALITY: "))
  jmeno = input("JMENO: ")
  prijmeni = input("PRIJMENI: ")
  rok_narozeni = int(input("ROK NAROZENI: "))
  email = input("EMAIL: ")
  heslo = input("HESLO: ")
  print(ODDELOVAC)
  ```

  #### 🕹 Vyber lokalit
  Chceme propojit promennou `cislo_lokality` a nase `MESTA`:
  ```python
  MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
  MESTA[0]  # "Praha"
  MESTA[1]  # "Viden"

  vyber_1 = 0
  vyber_2 = 1
  ```

  #### ➕ Zapojeni vstupu
  ```python
  destinace = MESTA[cislo_lokality - 1]
  cena = CENY[cislo_lokality - 1]
  ```

</details>

---

<details>
  <summary>👥 Vystup programu</summary>

  #### 😧 Spojovani(concatenation)
  Ve funkci `print` budeme kombinovat retezce a hodnoty z promennych:
  ```python
  print("DESTINACE: " + destinace)
  ```

  #### 📎 Vice vystupu
  Funkce `print` umoznuje vypsat vice udaju:
  ```python
  print("DEKUJI, ", jmeno, "JIZDENKU POSLEME NA EMAIL: ", email)
  ```

  #### ⏩ F-string formatovani
  ```python
  print(f"CENA(cil: {destinace}): {cena}")
  ```

</details>

---


➡ [pokracovat na druhou lekci](https://github.com/Bralor/python-academy/tree/lekce02)

