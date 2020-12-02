➡ [vratit se na sedmou lekci](https://github.com/Bralor/python-academy/tree/lekce07)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 8⃣ Python akademie
###  Dulezite odkazy
- [Portal Engeto.com](https://engeto.com/)
- [Seznamova komprehence](http://howto.py.cz/cap08.htm#10)
- [Ternarni operator](https://book.pythontips.com/en/latest/ternary_operators.html)
- [Python, dokumentace zabudovanych funkci](https://docs.python.org/3/library/functions.html)
- [Type hints, napovidani u funkci](https://www.python.org/dev/peps/pep-0484/)
- [Generator nahodnych slov](https://randomwordgenerator.com/)
- [Formatovani retezcu](https://realpython.com/python-string-formatting/)
---

###  Obsah lekce
1. Ukazka ulohy
2. Textove soubory
3. Formatovani retezcu
4. Modul random
5. Parametry funkci
6. Procvicovani na doma
---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si osmou lekci jako **zip**](https://github.com/Bralor/python-academy/archive/lekce08.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **upravene_udaje** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---
<details>
  <summary>📖 Textove soubory</summary>

<details>
  <summary>📂 Vytvorime novy soubor</summary>
  
  #### ⌨ Zaciname
  ```python
  #!/usr/bin/python3
  """Lekce #8 - Uvod do programovani, obesenec"""

  def main() -> None:
      """Hlavni ridici funkce nasi hry"""
      pass
  ```
---
</details>

<details>
  <summary>⚒ Jak pracovat s textovymi soubory</summary>

  #### ☝ K zapamatovani
  1. Nejprve pouzijeme funkci `open`, abychom ulozili cely soubor
  ```python
  soubor_se_slovy = open(jmeno_souboru, mode="r", encoding=None)
  ```

  2. Standartne potrebujeme vyplnit pouze prvni dva argumenty:
    - `jmeno_souboru` - i s priponou
    - `mode` - rezim, jak chceme soubor zpracovat ( **r**ead, **w**rite, **a**ppend)

  3. Pro cteni obsahu chceme zvolat `mode="r"` nebo jen `r`
  4. Pro nacteni obsahu pouzijeme jednu z metod:
    - `read` - nacteme cely obsah jako `str`
    - `readline` - nacteme pouze prvni radek
    - `readlines` - nacteme jako `list`, obsah rozdelime pomoci `\n`
  ```python
  obsazeny_text = soubor_se_slovy.read()
  ```

  5. Nakonec musime otevreny soubor zavrit pomoci metody `close`
  ```python
  soubor_se_slovy = open(jmeno_souboru, mode="r", encoding="utf8")
  obsazeny_text = soubor_se_slovy.read()
  soubor_se_slovy.close()
  ```
---
</details>

<details>
  <summary>⚙ Dalsi varianta</summary>

  #### 📀 Kontextovy manazer
  ```python
  with open(jmeno_souboru, mode="r") as txt_file:
      obsazeny_text = txt_file.read()
  ```

  #### 💾 Vlozime do funkce
  1. Vytvor funkci `nacitani_slov`
  2. Parametrem bude `jmeno_souboru`
  3. Chceme vracet `set` slov
  ```python
  def nacitani_slov(jmeno_souboru: str) -> set:
      with open(jmeno_souboru, mode="r") as txt_soubor:
          obsah = txt_soubor.readlines()
      return set(obsah)
  ```
  **Pozor!**, z funkce ziskame cely `set`

</details>

</details>

---
<details>
  <summary>❓ Modul random</summary>

<details>
  <summary>🔣 (Pseudo)nahodny vyber</summary>

  #### 📜 Modul random
  Standartni knihovna obsahuje modul `random`:
  ```python
  def vyber_nahodne_slovo(jmeno_souboru: str) -> str:
      from random import sample
      with open(jmeno_souboru, mode="r") as txt_soubor:
          obsah = txt_soubor.readlines()
          nahodne_slovo = sample(set(obsah), 1)
          ostripovane_sl = nahodne_slovo.pop().strip()
      return ostripovane_sl
  ```
  **Pozor!**, zapis muzeme refaktorovat

---
</details>

<details>
  <summary>🌚 Skryjeme slovo & vypocitame zivoty</summary>

  #### ✍ Jak to provest
  1. Vytvorime funkci `schovej_slovo`
  2. Popiseme jeji ucel ( _docstring_)
  3. Funkce ma jeden parametr `slovo`
  4. Funkce vraci retezec, kdy v tajnem slove nahradim jednotliva pismena `_`
  5. Funkce vrati cele cislo jako pocet zivotu, ktere hrac ziska
  6. Vyslednou hodnotu zaokrouhlime na cela cisla `round`
  ```python
  def schovej_slovo(slovo: str) -> list:
      """Nahradime pismena symbolem `_` a soucasne vypocita pocet pokusu"""
      return ["_"] * len(slovo), round(1.3 * len(slovo))
  ```

  #### 📩 Ulozime jmeno hrace
  ```python
  def pridej_hrace() -> str:
      return input("ZADEJTE JMENO HRACE: ")
  ```
---
</details>

<details>
  <summary>✍ Dosavadni zapis</summary>

  #### 📜 Reseni 
  ```python
  #!/usr/bin/python
  """Lekce #8 - Uvod do programovani, obesenec"""
  from random import sample


  def main() -> None:
      """Hlavni ridici funkce nasi hry"""
      pass


  def vyber_nahodne_slovo(jmeno_souboru: str) -> str:
      with open(jmeno_souboru, mode="r") as txt_soubor:
          return sample(set(txt_soubor.readlines()), 1).strip()


  def schovej_slovo(slovo: str) -> list:
      """Nahradime pismena symbolem `_` a soucasne vypocita pocet pokusu"""
      return ["_"] * len(slovo), round(1.3 * len(slovo))


  def pridej_hrace() -> str:
      return input("ZADEJTE JMENO HRACE: ")
  ```

</details>

</details>

---

<details>
  <summary>🗜 Formatovani retezcu</summary>

<details>
  <summary>📉 Stav hry</summary>

  #### 🥅 Nas cil 
  V kazdem kole chceme vypsat jmeno hrac, zbyvajici pocet pokusu a hadane slovo.

  #### Formatovani retezcu
  1. **Formatovaci vyraz**  (%-formatting)
  2. **Formatovaci metoda** (str.format())
  3. **f-string**           (f"")

---

</details>

<details>
  <summary>📎 Formatovaci vyraz</summary>

  #### ☝ K zapamatovani
  Je to prapuvodni zpusob formatovani v Pythonu uz od sameho zacatku:
  ```python
  JMENO = "Lukas"; VEK = 27
  "Ahoj, jmenuji se %s a je mi %d let" % (JMENO, VEK)
  ```
  **Pozor!**, dnes se jiz oficialne nedoporuje, jelikoz casto selhava,
  nespravne zobrazuje ntice nebo slovniky. Vypisovani neni prilis prakticke.

---
</details>

<details>
  <summary>🔗 Formatovaci metoda</summary>

  #### ☝ K zapamatovani
  Od verze Pythonu 2.6 mame k dispozici dalsi zpusob pro formatovani:
  ```python
  JMENO = "Eliska"; VEK = 26
  "Ahoj, jmenuji se {} a je mi {} let" .format(JMENO, VEK)
  ```
  **Pozor!**, pouziti je porad pomerne upovidane napr. pri zapisu vice
  promennych. Ma siroke moznosti formatovani ale ne vzdy pouzitelne.

---
</details>

<details>
  <summary>🔝 f-string</summary>

  #### ☝ K zapamatovani
  Od verze Pythonu 3.6 mame k dispozici jeste jednu metodu pro formatovani:
  ```python
  JMENO = "Lucie"; VEK = 28
  f"Ahoj, jmenuji se {JMENO} a je mi {VEK} let"
  ```
  Syntaxe je strucna presto citelna. Zvlada ruzne platne operace v Pythonu
  vcetne volani funkci. Opatrne pri psani uvozovek.

---
</details>

<details>
  <summary>🔧 Aplikace ve funkci</summary>

  #### ▶ Zobraz stav hry
  1. Funkce `vypis_stav_hry`
  2. Parametry `hrac`, `tajenka` a `zivoty`
  3. Vytvorime zpravu, zarovname oddelovacem a `print`
  ```python
  def vypis_stav_hry(hrac: str, tajenka: str, zivoty: int) -> None:
      zprava = f"|HRAC: {hrac} | STAV: {stav} | ZBYVA TAHU: {zbyva}|"
      oddelovac = len(zprava) * "-"
      print(oddelovac, zprava, oddelovac, sep="\n")
  ```
  #### 🗣 Hrac hada pismeno
  ```python
  def vyber_pismeno() -> str:
      return input("HADEJ PISMENO: ")
  ```
</details>

</details>

---
<details>
  <summary>♻ Vyber cyklu</summary>

<details>
  <summary>✅ Spravny odhad</summary>

  #### ⌨ Jak na to 
  1. Funkce `overeni_vyberu`
  2. Parametry `hadane_pismeno`, `tajenka` a `tajne_slovo`
  3. Pokud se ve slove hadane pismeno nachazi, nahrad podtrzitko
  ```python
  def overeni_vyberu(hadane_pismeno: str, tajenka: list, tajne_slovo: str) -> None:
      for index, pismeno in enumerate(tajne_slovo):
          if pismeno == hadane_pismeno:
              tajenka[index] = pismeno
  ```
---
</details>

<details>
  <summary>🔚Podminka pro ukonceni</summary>

  #### ✍ Jak na to
  1. Pokud `tajne_slovo` neobsahuje `_`, vitezstvi
  2. Pokud `tajne_slovo` obsahuje `_` a zbyva mu jeden pokus, prohra
  ```python
  def konec_kola(tajne_slovo: str, pokusy: int) -> None:
      if "_" not in tajne_slovo:
          print("VYHRALS!")
          quit()
      elif "_" in tajne_slovo and pokusy == 1:
          print("PROHRALS!")
          quit()
  ```

</details>

---
<details>
  <summary>🛡 oplnime hlavni funkci</summary>

  #### 🔍 Hlavni funkce
  ```python
  def main() -> None:
      """Hlavni ridici funkce nasi hry"""
      tajne_slovo = vyber_nahodne_slovo("slova.txt")    # je ve stejnem adresari
      prezdivka_hrace = pridej_hrace()
      tajenka, pokusy = schovej_slovo(tajne_slovo)      # udaje pro hrace

      while pokusy > 0:
          vypis_stav_hry(prezdivka_hrace, tajenka, pokusy)
          overeni_vyberu(vyber_pismeno(), tajenka, tajne_slovo)
          konec_kola(tajenka, pokusy)
          pokusy -= 1

  ```

</details>

</details>

---

<details>
  <summary>🚧 Procvicovani na doma</summary>

<details>
  <summary>🚧 Textovy soubor v interpretu</summary>

  #### 📚 Priklad

  Kurzor muzeme posunout pomoci metody `seek()`, kdy do kulate zavorky nastavime
  pozici, na ktere jej chceme nastavit:
  1. __seek(0)__ - pro zacatek souboru
  2. __seek(0, 2)__ - pro konec souboru

  Pokud potrebuji zjistit, kde se v souboru aktualne nachazim, pouziju metodu
  `tell()`.

---
</details>

<details>
  <summary>🚧 Rezimy funkce open()</summary>

  #### ⌨ Pomucka
  1. `r` - defaultne, otevri pro cteni
  2. `w` - otevri pro zapis (zapisuje od zacatku -> muze prepsat udaje)
  3. `x` - otevri pouze pro vytvoreni souboru (pokud existuje, selze)
  4. `a` - otevri pro zapis (zapisuje na konec -> pridava k stavajicim udajum)
  5. `b` - otevri v binarnim rezimu
  6. `+` - otevri pro aktualizovani (cteni i zapis)

</details>

</details>

---
➡ [pokracovat na devatou lekci](https://github.com/Bralor/python-academy/tree/lekce09)

