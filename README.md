➡ [vratit se na treti lekci](https://github.com/Bralor/python-academy/tree/lekce03)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 4⃣ Python akademie
### 🗒 Dulezite odkazy
- [Python Academy, Engeto](https://engeto.com/)
- [Walrus operator, dokumentace](https://www.python.org/dev/peps/pep-0572/)
---

### 🗒 Obsah lekce
1. Ukazka ulohy
2. Vstupni data
3. Uvodni vypisovani
4. While cyklus
5. Nekonecna smycka
6. Preskocit/pokracovat ohlaseni
7. Walrus operator
---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si ctvrtou lekci jako **zip**](https://github.com/Bralor/python-academy/archive/lekce04.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **kosik** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
  <summary>📥 Vstupni data</summary>

  #### 🔰 Pracovni promenne
  ```python
  kosik = {}
  ODDELOVAC = "=" * 40
  POTRAVINY = {
      "mleko": [30, 5],
      "maso": [100, 1],
      "banan": [30, 10],
      "jogurt": [10, 5],
      "chleb": [20, 5],
      "jablko": [10, 10],
      "pomeranc": [15, 10]
  }
  ```

</details>

---

<details>
  <summary>📖 Uvodni vypisovani</summary>

<details>
  <summary>💿 Nova lekce, novy soubor</summary>

  #### 🗄 Vytvorime novy soubr
  ```
  cd python-akademie  # presunout
  mkdir lekce04       # vytvorit adresar
  touch kosik.py      # Linux
  copy nul "kosik.py" # Windows
  ```
---

</details>

<details>
  <summary>🗣  Pozdrav + vypis promennych</summary>

  #### 🗄 Pozdrav a oddelovac
  ```python
  print(
    "VITEJTE V NASEM VIRTUALNIM OBCHODE".center(40, " "),
    end=f"\n{ODDELOVAC}\n",
  )
  ```

  #### 🛍 Vypis dostupneho zbozi
  ```python
  print(
    POTRAVINY,
    end=f"\n{ODDELOVAC}\n"
  )
  ```

  #### 🛃 Zkombinujeme oboji
  ```python
  print(
    "VITEJTE V NASEM VIRTUALNIM OBCHODE".center(40, " "),
    POTRAVINY,
    sep=f"\n{ODDELOVAC}\n",
    end=f"\n{ODDELOVAC}\n"
  )
  ```

</details>

<details>
  <summary>🛒 Pridavame zbozi</summary>

  #### 👨 Vyber potraviny
  ```python
  vyber_1 = input("VYBERTE ZBOZI: ")
  ```

  #### 🔚 Prevedeni do kosiku
  ```python
  kosik[vyber_1] = POTRAVINY[vyber_1][0]
  ```

  #### 💲 Vypocet ceny
  Pomuzeme se zabudovanou funkci `sum`:
  ```python
  print(f"CELKEM: {sum(kosik.values())} CZK")
  ```
  **Doplnime pro 4 potraviny**

</details>

</details>

---

<details>
  <summary>♻ While cyklus</summary>

<details>
  <summary>❔Jak jej pozname </summary>

  #### 🔑 Klicove znaky
  1. `while`
  2. podminka
  3. ukoncujici dvojtecka
  4. odsazeni + serie instrukci
  ```python
  while podminka:
    # pokud je podminka True, proved TOTO
  # pokud je podminka False, proved TOTO
  ```

</details>

<details>
  <summary>⏯  Ukazka</summary>

  #### ❗Priklad
  ```python
  x = 0

  while x < 10:
    print(f"{x=}; {x}<10, v poradku!")
    x = x + 1

  print(f"{x=}; {x}=10, podminka neni pravdiva, pokracuje kod pod smyckou!")
  ```
</details>

<details>
  <summary>🔁 Upravime nas zapis</summary>

  #### ✌ Druhy pokus
  Stavajici kod prepiseme pomoci smycky `while`:
  ```python
  while len(kosik) < 4:
      vyber_zbozi = input(f"VYBERTE ZBOZI: ")
      kosik[vyber_zbozi] = POTRAVINY[vyber_zbozi][0]
  ```

  #### 🤷 Doplnime soucet
  Muzu pokracovat primo pod smyckou nebo pouzit `else`:
  ```python
  else:
    print(
      "KOSIK JE PLNY, UKONCUJI..",
      kosik,
      f"CENA CELKEM: {sum(kosik.values())} CZK",
      sep=f"\n{ODDELOVAC}\n",
      end=f"\n{ODDELOVAC}\n"
    )
  ```

</details>

</details>

---

<details>
  <summary>⚠ Nekonecna smycka</summary>

<details>
  <summary>❓ Jen ctyri produkty</summary>

  #### ☝ Spravna podminka
  Nechceme uzivatele omezit jen na 4 produkty

  #### 💁 Nekonecna smycka
  Podminku v hlavicce cyklu muzeme napsat i nasledovne:
  ```python
  x = 0

  while x < 10:
      print(f"x={x}; {x}<10, v poradku!")
  ```
  **Pro ukonceni nekonecne smycky Ctrl+C**

  #### ⁉ Je to vhodne
  Neumyslne zapis je samozrejme nezadouci. Ale muzeme jej spravit:
  ```python
  cislo = 1
  prepinac = True

  while prepinac:
      cislo = cislo ** 2
      kontrola = input("PRO UKONCENI NAPIS 'q': ").lower()

      if kontrola == "q":
              prepinac = False
      else:
              print(cislo)
  ```
<p align="center">
  <img src="https://media.giphy.com/media/qVVVfmHDMBZug/source.gif" width="300" height="300">
</p>

  #### ⏪ Prepiseme nasi podminku v cyklu
  ```python
  pokracovat = True                                                               
                                                                                  
  while pokracovat:                                                               
      vyber_zbozi = input(f"VYBERTE ZBOZI: ")

      if vyber_zbozi.lower() == 'q':
        pokracovat = False
      else:
        kosik[vyber_zbozi] = POTRAVINY[vyber_zbozi][0]
                                                                                  
  else:
    print(
      "KOSIK JE PLNY, UKONCUJI..",
      kosik,
      f"CENA CELKEM: {sum(kosik.values())} CZK",
      sep=f"\n{ODDELOVAC}\n",
      end=f"\n{ODDELOVAC}\n"
    )
  ```

</details>

<details>
  <summary>⛔ Chybne jmeno zbozi</summary>

  #### 🤦 Chybu udela kazdy
  Pokud se uzivatel splete, chceme ho upozornit:
  ```python
  if vyber_zbozi.lower() == "q":
      pokracovat = False
  elif vyber_zbozi not in POTRAVINY.keys():
      print(f"*{vyber_zbozi}* BOHUZEL NEMAME SKLADEM!")
  else:
      kosik[vyber_zbozi] = POTRAVINY[vyber_zbozi][0]
  ```

</details>

<details>
  <summary>🚯 Prehledna nabidka</summary>

  #### ⚒  Pomoci cyklu
  Chceme vypisovat pod sebe pomoci `while` cyklu:
  ```python
  TABULKA = POTRAVINY.copy()

  while TABULKA:
      radek_potravina = TABULKA.popitem()
      print(f"POTRAVINA: {radek_potravina[0]},\tCENA: {radek_potravina[1][0]}")
  ```

</details>

</details>

---

<details>
  <summary>😑 Preskocit nebo pokracovat</summary>

  #### ⏹ Ohlaseni break
  Pomoci klicoveho vyrazu `break` muzeme cyklus predcasne ukoncit:
  ```python
  cislo = 0
  veta = "Příliš žluťoučký kůň úpěl ďábelské ódy"

  while cislo < len(veta):
          pismeno = veta[cislo]
          if pismeno == "w":
              break
          else:
              print(f"{pismeno=}")
              cislo = cislo + 1

  else:
      print(f"POSLEDNI INDEX {len(veta[:cislo])}")
  ```

  #### 🌀 Ohlaseni continue
  Pomoci klicoveho vyrazu `continue` muzeme v cyklu preskakovat:
  ```python
  cislo = 0
  veta = "Příliš žluťoučký wkůň úpěl ďábelské ódy"

  while cislo < len(veta):
          pismeno = veta[cislo]

          if pismeno != "w":
              print(f"SPRAVNA HODNOTA --> {pismeno=}")
              cislo = cislo + 1
              continue
          else:
              print(f"NESPRAVNA HODNOTA --> {pismeno=}")
              cislo = cislo + 1

  else:
      print(f"POSLEDNI INDEX {len(veta[:cislo])}")
  ```

</details>

---

<details>
  <summary>🚼 Walrus operator</summary>

<details>
  <summary>❓ O co jde</summary>
  
  #### 📜 Prirazovaci operator 
  Patri mezi novejsi vyrazy (Python3.8+)

  #### 👷 Jak jej pouzivat
  ```python
  jmeno = "Matous"
  print(jmeno)
  print(jmeno_2 := "Lukas")
  ```

  #### 🔂 Aplikujeme v uloze
  Pouziti prirazovaciho operatoru v nasi uloze:
  ```python
  while (vyber_zbozi := input("VYBERTE ZBOZI: ")) != 'q':
      if vyber_zbozi not in POTRAVINY.keys():
          print(f"*{vyber_zbozi}* NEMAME SKLADEM!")
      else:
          kosik[vyber_zbozi] = POTRAVINY[vyber_zbozi][0]
  ```

</details>

</details>

---

<details>
  <summary>🏠 Procvicovani na doma</summary>

<details>
  <summary> 🚧 Vice kusu stejneho produktu</summary>

  #### 📜 Reseni prvniho ukolu
  ```python
  if vyber_zbozi not in POTRAVINY:
      print(f"{vyber_zbozi} NEMAME V NABIDCE!")

  elif vyber_zbozi not in kosik and POTRAVINY[vyber_zbozi][1] > 0:
      kosik[vyber_zbozi] = [POTRAVINY[vyber_zbozi][0], 1]
      POTRAVINY[vyber_zbozi][1] = POTRAVINY[vyber_zbozi][1] - 1

  elif vyber_zbozi in kosik and (pocet := POTRAVINY[vyber_zbozi][1]) > 0:
      kosik[vyber_zbozi][1] += 1
      POTRAVINY[vyber_zbozi][1] = POTRAVINY[vyber_zbozi][1] - 1

  elif POTRAVINY[vyber_zbozi][1] == 0:
      print(f"{vyber_zbozi.upper()} JIZ NENI SKLADEM!")
  ```

---

</details>

<details>
  <summary> 🚧 Novy vypocet ceny podle kusu</summary>

  #### 📜 Reseni druheho ukolu
  ```python
  else:
      print(f"{ODDELOVAC}\n",
          "KOSIK JE PLNY! UKONCUJI".center(40, " "),
          end=f"\n{ODDELOVAC}\n")

      index = 0
      cena_celkem = 0

      while index < len(kosik):
          polozka_v_kosiku = list(kosik.values())[index]
          cena_celkem = cena_celkem + (polozka_v_kosiku[0] * polozka_v_kosiku[1])
          index = index + 1

      else:
          print(f"CELKOVA CENA: {cena_celkem},-".center(40, " "),
              end=f"\n{ODDELOVAC}\n")
  ```
---

</details>

</details>

---

➡ [pokracovat na dalsi (05) lekci](https://github.com/Bralor/python-academy/tree/lekce05)

