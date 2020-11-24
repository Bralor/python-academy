➡ [vratit se na patou lekci](https://github.com/Bralor/python-academy/tree/lekce05)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 6⃣ Python akademie
###  Dulezite odkazy
- [Portal Engeto.com](https://engeto.com/)
- [Seznamova komprehence](http://howto.py.cz/cap08.htm#10)
- [Ternarni operator](https://book.pythontips.com/en/latest/ternary_operators.html)
- [Python, dokumentace zabudovanych funkci](https://docs.python.org/3/library/functions.html)
- [Collections, standartni modul](https://docs.python.org/3/library/collections.html#collections.Counter)
---

###  Obsah lekce
1. Ukazka ulohy
2. Vstupni udaje
3. Funkce, zabudovane
4. Funkce, uzivatelem definovane
5. Prirazovani hodnot promennym
6. Zkraceny zapis
---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si sestou lekci jako **zip**](https://github.com/Bralor/python-academy/archive/lekce06.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **upravene_udaje** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
  <summary>📥 Vstupni udaje</summary>

  #### 📜 Upravene & scrapovane detaily
  ```python
  UDAJE = """
  byt0001,55m2,Olomouc,ul.Heyrovského,
  byt0003,65m2,Olomouc,ul.Novosadský_dvůr,
  byt0004,75m2,Olomouc,ul.Wolkerova,
  byt0004,68m2,Olomouc,ul.Zikova,
  byt0001,36m2,Olomouc,ul.Nová_Ulice,
  byt0003,46m2,Olomouc,ul.Nové_sady,
  byt0004,75m2,Olomouc,ul.Nová_Ulice,
  byt0003,42m2,Olomouc,ul.Nová_Ulice,
  byt0005,107m2,Olomouc,ul.Nová_Ulice,
  byt0003,74m2,Olomouc,ul.Uničovská,
  byt0003,42m2,Olomouc,ul.Nešverova,
  byt0002,55m2,Olomouc,ul.Dělnická,
  byt0004,59m2,Olomouc,ul.Zirmova,
  byt0007,92m2,Olomouc,ul.Nová_Ulice,
  byt0002,52m2,Olomouc,ul.Nová_Ulice,
  byt0004,76m2,Olomouc,ul.Nová_Ulice,
  byt0002,81m2,Olomouc,ul.Nová_Ulice,
  byt0003,64m2,Olomouc,ul.Za_vodojemem,
  byt0007,113m2,Olomouc,ul.Jihoslovanská,
  byt0005,94m2,Olomouc,ul.Uničovská,
  byt0003,42m2,Olomouc,ul.Rošického,
  byt0003,75m2,Olomouc,ul.Rošického,
  byt0004,48m2,Olomouc,ul.Handského,
  byt0004,68m2,Olomouc,ul.Komenského,
  byt0003,61m2,Olomouc,ul.Jarmily_Glazarové,
  byt0004,39m2,Olomouc,ul.Přichystalova,
  byt0003,70m2,Olomouc,ul.Foerstova,
  byt0005,61m2,Olomouc,ul.Nová_Ulice,
  byt0007,88m2,Olomouc,ul.Nová_Ulice,
  byt0003,92m2,Olomouc,ul.U_cukrovaru,
  byt0003,56m2,Olomouc,ul.U_cukrovaru,
  byt0004,56m2,Olomouc,ul.Paseka,
  byt0002,74m2,Olomouc,ul.Rokycanova,
  byt0007,116m2,Olomouc,ul.U_cukrovaru,
  byt0004,59m2,Olomouc,ul.Řezáčova,
  byt0004,100m2,Olomouc,ul.Libušina,
  byt0003,64m2,Olomouc,ul.Řezáčova,
  byt0001,33m2,Olomouc,ul.Libušina,
  byt0006,87m2,Olomouc,ul.Černá cesta,
  byt0007,95m2,Olomouc,ul.Kaštanová,
  byt0003,74m2,Olomouc,ul.Nová_Ulice,
  byt0003,75m2,Olomouc,ul.Nová_Ulice,
  byt0004,86m2,Olomouc,ul.Hněvotínská,
  byt0002,67m2,Olomouc,ul.Polská,
  byt0007,120m2,Olomouc,ul.Dvořákova,
  byt0004,90m2,Olomouc,ul.Dvořákova,
  byt0004,86m2,Olomouc,ul.Nová Ulice,
  byt0003,75m2,Olomouc,ul.Nešverova,
  byt0001,45m2,Olomouc,ul.Zirmova,
  byt0006,114m2,Olomouc,ul.Přichystalová,
  """

  PREVOD_UDAJU = {
    "byt0001": "1+1",
    "byt0002": "2+1",
    "byt0003": "2+kk",
    "byt0004": "3+1",
    "byt0005": "3+kk",
    "byt0006": "4+1",
    "byt0007": "4+kk",
  }
  ```

</details>

---

<details>
  <summary>👼 Funkce, zabudovane</summary>

  #### ☝ K zapamatovani
  - jako uzivatel je nemusim definovat
  - mohu je primo pouzit (_zavolat_)
  - soupisku vsech najdeme v sekci [odkazy](#dulezite-odkazy)
  - setrime vypisovani
  - zapis je citelnejsi
  - opakovane pouzitelne

  #### ❓ Jak vypada zabudovana funkce
  ```python
  print("Ahoj, vsem!")
  int(input("Zadejte cislo: "))
  ```

</details>

---

<details>
  <summary>🔥 Funkce, uzivatelem definovane</summary>

  #### ☝ K zapamatovani
  - neni soucasti standartni knihovny Pythonu
  - nejprve potrebuji zapsat jeji definici
  - pokud ji chci spustit, musim ji _zavolat_ (pouzit)
  - `def` klicovy vyraz v zahlavi definice
  - `vypocitej_sumu` nasleduje jmeno funkce, budu potrebovat pri spusteni
  - `cisla` v kulate zavorce je parametr funkce (idealne 2, max. 3)
  - pokud jmeno funkce neni dostatecne popisne, zapisu dokumentaci
  - `return` ohlaseni, pokud chci z funkce vratit nejaky udaj
  - `vypocitej_sumu()` spusteni funkce (_volani_)
  - `seznam_cisel` argument funkce, ktery chci pouzit ve funkci

  #### ❓ Jak vypada zabudovana funkce
  ```python
  def jmeno_funkce(parametr_1, parametr_2):
      # odsazeny kod
      # VOLITELNE: vraceni hodnoty
  ```
  **Priklad funkce**
  ```python
  def vypocitej_sumu(cisla):
      """Dokumentace funkce"""
      suma_cisel = list()

      for cislo in cisla:
          suma_cisel = suma_cisel + cislo

      return suma_cisel


  seznam_cisel = [11, 22, 33, 44, 55, 66, 77, 88, 99]
  vysledek = vypocitej_sumu(seznam_cisel)
  print(f"SUMA VSECH CISEL: {vysledek}")
  ```
  **Pozor!** Nas zapis muzeme vylepsit nekolika kroky:
  1. Napovidani datovych typu
  2. Zkraceny zapis
  3. f-string, volani funkce
  4. Idealne pouzit `sum` funkci 😏

<details>
  <summary>💣Nase prvni funkce</summary>

  #### 🥅 Nas cil
  Nejprve bez funkce. Chceme napsat mechanismus, ktery prevede `byt0001`
  na `1+1`.

  #### 1⃣ Prvni krok
  Nejprve pomocna promenna `udaj_1`:
  ```python
  udaj_1 = "byt0001"
  ```

  #### 2⃣ Control-flow
  Mechanismus, kterym provedu prevedeni:
  ```python
  if udaj_1 in PREVOD_UDAJU.keys():
      udaj_1 = PREVOD_UDAJU[udaj_1]
  ```
  Pokud nebude hodnota ve slovniku, musime myslet na `KeyError`:
  ```python
  else:
      print("NEZNAMY TYP BYTU!")
  ```
  **Pozor!** Nas zapis muzeme vylepsit nekolika kroky:
  1. Odstranit metodu `keys`
  2. Ternarni operator
  3. Metoda slovniku `get`

  #### 3⃣ Pomoci funkce
  Zapiseme pomoci funkce a doplnime pocitani:
  ```python
  def prevodnik_bytu(typ_bytu: str, vzor: dict) -> str:
      """Prevede a zapocita stavajici typ bytu na novy"""
      if typ_bytu in vzor:
          typ_bytu = vzor[typ_bytu]
          return typ_bytu
      else:
          print("NEZNAMY TYP BYTU!")

  vysledny_typ = prevodnik_bytu(udaj_1, PREVOD_UDAJU)
  print(f"PUVODNI: {udaj_1}, NOVY: {vysledny_typ}")
  ```

</details>

</details>

---

<details>
  <summary>🚦 Prirazovani hodnot promennym</summary>

<details>
  <summary>📜 Jak ziskat puvodni typ bytu</summary>

  #### 1⃣ Jak prochazet retezec po radcich
  ```python
  for radek in UDAJE.split():
      print(f"{radek=}")
  ```

  #### 2⃣ Jak rozdelit radek
  ```python
  for radek in UDAJE.split():
      radek = radek.split(",")
      print(f"""
        {radek[0]=}
        {radek[1]=}
        {radek[2]=}
        {radek[3]=}
      """)
  ```

  #### 3⃣ Vicenasobne prirazovani hodnot
  Pocet jmen promennych odpovida hodnotam:
  ```python
  for radek in UDAJE.split():
      typ, plocha, mesto, ulice = radek.split(",")
      print(f"""
        {typ=}
        {plocha=}
        {mesto=}
        {ulice=}
      """)
  ```

  Pocet jmen promennych neodpovida hodnotam (musim pouzit `*`):
  ```python
  for radek in UDAJE.split():
      typ, *dalsi_udaje = radek.split(",")
      print(f"""
        {typ=}
        {dalsi_udaje=}
      """)
  ```
  **Pozor!** Pokud si nebude pocet jmen promennych a hodnot promennych
  odpovidat, dostaneme `ValueError`

---

</details>

<details>
  <summary>📆 Jak inkrementovat uspesna prevedeni</summary>

  #### 🆘 Opet pouzijeme prirazovani vice hodnot
  Krome prevedeneho udaje vratime cele cislo `1`:
  ```python
  def prevodnik_bytu(typ_bytu: str, vzor: dict) -> str:
      """Prevede a zapocita stavajici typ bytu na novy"""
      if typ_bytu in vzor:
          typ_bytu = vzor[typ_bytu]
          return (typ_bytu, 1)      # vracim tuple s hodnotami
      else:
          print("NEZNAMY TYP BYTU!")
          return 0                  # vracim pouze 0
  ```
  **Pozor!** Aby nam zapis fungoval musime v obou variantach vracet `tuple` se
  dvema hodnotami! Provedeme drobnou upravu:
  ```python
      else:
          return ("NEZNAMY TYP BYTU!", 0)
  ```

  #### 🤙 Zavolame funkci
  Opravena funkce vraci dve hodnoty, takze musim davat pozor pri spousteni:
  ```python
  for radek in UDAJE.split():
      typ, *dalsi_udaje = radek.split(",")
      upraveny_typ, prirustek = prevodnik_bytu(typ, PREVOD_UDAJU)
  ```
  Doplnime pocitani uspesnych prevodu:
  ```python
  vysledek = set()
  uspesne = 0

  for radek in UDAJE.split():
      typ, *dalsi_udaje = radek.split(",")
      upraveny_typ, prirustek = prevodnik_bytu(typ, PREVOD_UDAJU)
      uspesne = uspesne + prirustek
      print(f"{uspesne=}, {upraveny_typ=}")
  ```

</details>

</details>

---

<details>
  <summary>🎯 Zkracene prirazovani</summary>

  #### ❓ Jak zkracene prirazeni vypada
  Zatim jsme si povidali pouze o nasledujicim zpusobu:
  ```
  x = x <operator> y
  ```
  Zkracene prirazeni vypada nasledovne:
  ```
  x <operator>= y
  ```

  #### 👌 Vyhody
  1. Zkratim zapis
  2. Neztratim citelnost zapisu
  3. Pouze upravim puvodni hodnotu (1 krok)
  4. Puvodni zapis vytvoreni promennou a priradi hodnotu (2 kroky)

<details>
  <summary>✂ Zkratime zapis</summary>

  #### ♻ Upravime cyklus
  ```python
  for radek in UDAJE.split():
      typ, *dalsi_udaje = radek.split(",")
      upraveny_typ, prirustek = prevodnik_bytu(typ, PREVOD_UDAJU)
      uspesne += prirustek
  ```

  #### 🕹 Spojime se zbytkem udaj
  ```python
  upraveny_radek = f"{upraveny_typ},{dalsi_udaje}"
  ```

  #### 🔛 Ulozime hotovy vysledek
  Potrebujeme jednotlive udaje spojit pomoci metody retezcu `join`:
  ```python
  ", ".join(["A", "B", "C"])        # 'A, B, C'
  "#".join(["A", "B", "C"])         # 'A#B#C'
  ```
  Upravene reseni:
  ```python
  upraveny_radek = f"{upraveny_typ},{','.join(dalsi_udaje)}"
  vysledky.add(upraveny_radek)
  ```

  #### 💌 Zaverecny vystup
  ```python
  for vysledek in vysledky:
      if "NEZNAMY TYP BYTU!" in vysledek:
          continue
      else:
          print(f"{vysledek=}")
  else:
      print(f"PREVEDENO: {uspesne} UDAJU")
  ```
  **Pozor!** Nas zapis muzeme dale vylepsit.

</details>

</details>

---

➡ [pokracovat na sedmou lekci](https://github.com/Bralor/python-academy/tree/lekce07)

