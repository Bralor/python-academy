➡ [vratit se na sestou lekci](https://github.com/Bralor/python-academy/tree/lekce06)

<p align="center">
  <img alt="engeto-logo" width="100px" src="https://engeto.cz/wp-content/uploads/2019/01/engeto-square.png" />
</p>

## 7⃣ Python akademie
###  Dulezite odkazy
- [Portal Engeto.com](https://engeto.com/)
- [Seznamova komprehence](http://howto.py.cz/cap08.htm#10)
- [Ternarni operator](https://book.pythontips.com/en/latest/ternary_operators.html)
- [Python, dokumentace zabudovanych funkci](https://docs.python.org/3/library/functions.html)
- [Collections, standartni modul](https://docs.python.org/3/library/collections.html#collections.Counter)
- [Type hints, napovidani u funkci](https://www.python.org/dev/peps/pep-0484/)
- [Vice k jmennym prostredim a funkcnim ramcum](https://code.tutsplus.com/tutorials/what-are-python-namespaces-and-why-are-they-needed--cms-28598)
- [Namespaces and Scope in Python](https://realpython.com/python-namespaces-scope/)
---

###  Obsah lekce
1. Ukazka ulohy
2. Funkce, prace vice funkci
3. Jmenna prostredi v Pythonu
4. Funkcni ramce
5. Type hint, napovidani
6. Typy argumentu
7. Procvicovani na doma
---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si sedmou lekci jako **zip**](https://github.com/Bralor/python-academy/archive/lekce07.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **upravene_udaje** v PyCharm
  4. 🐍 Spustte program pomoci klaves **ctrl+shift+F10**
  5. 🎥 Zkousejte!

</details>

---

<details>
  <summary>🎹 Funkce, prace vice funkci</summary>

<details>
  <summary>🤖 Uvodni sekce</summary>

  #### ⚒ Struktura zapisu
  ```python
  #!/usr/bin/python3
  """Lekce #07 - Uvod do programovani, kalkulacka.py"""

  # definice: Hlavni funkce
      # spousteni: Pozdrav
      # spouteni: Nabidka


  # definice: Pozdrav


  # definice: Nabidka


  # spousteni: Hlavni funkce
  ```

---

</details>

<details>
  <summary>🖱 Definice funkci v uvodu</summary>

  #### 🎬 Definice hlavni funkce
  ```python
  def main() -> None:
      """Hlavni ridici funkce nasi kalkulacky"""
      pass
  ```

  #### 🗽 Definice pomocnych funkci
  ```python


  def pozdrav_uzivatele() -> None:
      pass


  def vypis_nabidku() -> None:
      pass
  ```
---

</details>

<details>
  <summary>📣 Dokonceni uvodu</summary>

  #### 👋 Pozdravime uzivatele
  1. Vypisime obsah promenne `uvod`
  2. Zarovname zpravu na stred
  3. Na zaver pridame `oddelovac`
  ```python
  def pozdrav_uzivatele(uvod: str, oddelovac: str) -> None:
      print(f"{uvod}".center(50), end=oddelovac)
  ```

  Definovanou funkci `pozdrav_uzivatele` spustime v ramci funkce `main`:
  ```python
  def main() -> None:
      """Hlavni ridici funkce nasi kalkulacky"""
      pozdrav_uzivatele()
  ```

  Doplnime ve funkci `main` potrebne promenne:
  ```python
  def main() -> None:
      """Hlavni ridici funkce nasi kalkulacky"""
      UVODNI_ZPRAVA = "VITEJTE V PROGRAMU KALKULACKA!"
      ODDELOVAC = f"\n{'=' * 50}\n"

      pozdrav_uzivatele(UVODNI_ZPRAVA, ODDELOVAC)
  ```

</details>

</details>

---

<details>
  <summary>📊 Jmenna prostredi</summary>

<details>
  <summary>❓ O co jde</summary>

  #### 🏖  Motivace
  1. Proc musime promenne zapsat ve funkci `main`?
  2. Muzu je zapsat do jine funkce?
  3. Je v tom vubec nejaky system?
  4. K cemu nas to vede?

  #### ✍ Definice
  Jmenne prostredi (_namespace_) je soubor aktualne zapsanych promennych
  a jejich hodnot. Pro lepsi predstavu si je muzeme vysvetlit jako nejaky druh
  slovniku.
  ```python
  # Pokud mame novy soubor
  namespace_1 = {}

  # Pokud doplnime promenne
  jmeno = "Matous"          # namespace_1
  vek = 33                  # namespace_1

  def f():
    nove_jmeno = "David"    # namespace_2

  # Funkce
  namespace_1 = {"jmeno": "Matous", "vek": 33}
  namespace_2 = {"nove_jmeno": "David"}
  ```
  **Pozor!**, vyse uvedeny priklad je pouze ilustrace.

---

</details>

<details>
  <summary>🌐 Shrnuti k prostredim</summary>

  #### ☝ K zapamatovani
  1. Kazda z funkci ma vlastni _namespace_
  2. Pokud chceme promennou vlozit, pouzijeme parametry funkce
  3. Pokud chceme promennou vratit, pouzijeme `return`
  4. Mimo funkce mame jine _namespace_
  5. Vytvari tedy oddelena prostredi
  6. [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
  7. Diky jmennym prostredim muzeme vytvorit ruzne funkcni ramce

</details>

</details>

---

<details>
  <summary>🎎 Funkcni ramce</summary>

<details>
  <summary>👭 Rozdeleni ramcu</summary>

  #### 🛡 Funkcni ramce (scopes)
  **Built-In**/zabudovany ramec obsahuje vsechny dostupne objekty, po celou dobu
  behu souboru.

  **Global**/globalni ramec vznika, kdyz spustime nas program a zanikne, jakmile
  interpret ukonci svoji cinnost. Globalni prostredi vytvori take pro nahrane
  moduly/baliky.

  **Local & enclosing**/lokalni & uzavreny ramec interpret vytvori, kdyz
  spusti funkci (pripadne funkci uvnitr funkce).

---
</details>

<details>
  <summary>📺 Ukazky</summary>

  #### 🔨 Zabudovane prostredi
  Pro vypis vsech objektu z tohoto jmenneho prostredi:
  ```
  >>> dir(__buildins__)
  ```

  #### 🌏 Globalni prostredi
  ```python
  JMENO = "Matous"

  def uprav_jmeno(jmeno: str, koncovka: str) -> str:
      return f"{jmeno}{koncovka}"

  zdrobnele = uprav_jmeno(JMENO, "ek")
  print(globals())
  ```

  #### ⛩ Lokalni prostredi
  ```python
  JMENO = "Matous"

  def uprav_jmeno(jmeno: str, koncovka: str) -> str:
      print(locals())
      return f"{jmeno}{koncovka}"

  zdrobnele = uprav_jmeno(JMENO, "ek")
  ```
  **Pozor!**, pokud `locals()` pouzijeme mimo funkcni jmenne prostredi,
  bude vystup stejny jako `globals()`.

  #### 🚧 Uzavrene prostredi
  Specialni varianta, kdy mam uvnitr jednoho prostredi prostredi jine:
  ```python
  def uzavirajici_fce():
      print("Zacina uzavirajici fce")


      def uzavrena_fce():
          print("Zacina uzavrena fce")
          print("Konci uzavrena fce")
          return


          uzavrena_fce()
          print("Konci uzavirajici_fce")
          return


  uzavirajici_fce()
  ```
---
</details>

<details>
  <summary>🎢 Aplikace ramcu</summary>

  #### ☝ K zapamatovani
  Ramce slouzi k oddeleni jednotlivych prostredi. Kazde je udrzovane zvlast,
  ma ruznou delku existence a neovlivnuji ostatni.

  #### 🎉 Dukaz
  ```python
  prostredi = "globalni"

  def a():
      prostredi = "uzavirajici"

      def b():
          prostredi = "lokalni"
          print(prostredi)

      b()
  a()
  ```

  #### ✌ Zaverem
  Struktura umoznuje hierarchicke hledani promennych:
  1. Nejprve prohleda funkci, v niz se nachazi
  2. Pokud neni uvnitr, zkus uzavirajici prostredi (pokud existuje)
  3. Pokud neni uvnitr uzavirajiciho prostredi, posli interpret do globalniho
  4. Pokud neni uvnitr globalniho, zkus seznam zabudovanych objektu
  5. `NameError`

</details>

</details>

---

<details>
  <summary>💬 Parametry funkci</summary>

  #### 📝 Moznosti zapisu
<details>
  <summary>🥇 Podle pozice</summary>

  #### ✏ Priklad
  ```python
  def func(par1, par2, par3):
      print(f"{par1=}")
      print(f"{par2=}")
      print(f"{par3=}")


  func(1, 2, 3)
  ```
---
</details>

<details>
  <summary>🗝  Podle klice</summary>

  #### ✏ Priklad
  ```python
  def func(par1, par2, par3):
      print(f"{par1=}")
      print(f"{par2=}")
      print(f"{par3=}")


  func(par2=2, par3=3, par1=1)
  ```
---
</details>

<details>
  <summary>🎰 Defaultni parametr</summary>

  #### ✏ Priklad
  ```python
  def func(par1, par2, par3=3):
      print(f"{par1=}")
      print(f"{par2=}")
      print(f"{par3=}")


  func(1, 2)
  func(1, 2, 4)
  ```
---
</details>

<details>
  <summary>🆕 Position-only parametry</summary>

  #### ✏ Priklad
  ```python
  def func(par1, /, par2, par3=3):
      print(f"{par1=}")
      print(f"{par2=}")
      print(f"{par3=}")


  func(0, 5, 5)
  func(0, b=5, c=5)
  func(0, c=5, b=5)
  func(a=0, c=5, b=5)
  ```
---
</details>

<details>
  <summary>😱 args</summary>

  #### ✏ Priklad
  ```python
  def func(*args):
      for arg in args:
 https://realpython.com/python-namespaces-scope/         print(f"{arg=}")


  func(0)
  func(0, "a", "b", "c", 10, 12)
  ```
---
</details>

<details>
  <summary>😵 kwargs</summary>

  #### ✏ Priklad
  ```python
  def func(**kwargs):
      for klic, hodnota in kwargs.items():
          print(f"{klic=} -> {hodnota=}")


  func(cislo=11)
  func(cislo=11, jmeno="Matous", datum="11.11.2011")
  ```
---
</details>

<details>
  <summary>🤺Dostupne operace</summary>

  #### ✏ Postup
  1. Chceme vypsat vice ruznych operaci
  2. Spojime symbolem `|`
  3. Na zaver oddelime
  ```python
  def vypis_nabidku(oddelovac: str, *args) -> None:
      print(f"{' | '.join(args)}".center(50), end=oddelovac)
  ```

---
</details>

<details>
  <summary>✍🏻 Uzivatelsky vstup</summary>

  #### ✏ Postup
  1. Uzivatele zada operator
  2. Operator ulozime do promenne
  ```python
  def zvol_operator() -> "str":
      return input("VYBER MATEMATICKOU OPERACI: ")


  operator = zvol_operator()
  ```

---
</details>

<details>
  <summary>🔢Vyber cisel</summary>

  #### ✏ Postup
  1. Uzivatele zada dve ciselne hodnoty oddelene carkou
  2. Udaj ulozime do promenne
  3. Oddelime obe hodnoty
  ```python
  def zvol_cisla() -> "str":
      return input("ZADEJ 2 CISLA ODDELENE CARKOU: ")


  x1, x2 = zvol_cisla()
            .replace(" ", "")
            .split(",")
  ```
---
</details>

<details>
  <summary>📳 Zpracovani hodnot</summary>

  #### ✏ Postup
  1. Vytvorime novou funkci, ktera pouzije 3 parametry
  2. I. parametr - cislo, II. parametr - cislo, III. parametr - operator
  3. Na zaklade operatoru postavime matematickou operaci
  4. Ohlaseni `return` vrati vyslednou hodnotu
  ```python
  def zpracuj_vypocet(x1: "float", x2: "float", op: "str") -> float:
      """
      Uzivatel vlozi hodnoty do parametru:
        x1 -> str [1, 1.1, 11.1, -1.11]
        x2 -> str [2, 2.2, 22.2, -2.22]
        op -> str ["+", "-", "*", "/"]

      Obecna proces funkce:
       x1 = 1, x2 = 2, op = "+" ->  1 + 2
       x1 = 1.11, x2 = 2.22, op = "-" ->  1.11 - 2.22
      """
      return {
        "+": float(x1) + float(x2),
        "-": float(x1) - float(x2),
        "*": float(x1) * float(x2),
        "/": float(x1) / float(x2)
      }.get(op)


  print(f"VYSLEDEK = {zpracuj_vypocet(1, 2, '+')}")
  ```

---
</details>

<details>
  <summary>🔔 Doplnime hlavni funkci</summary>

  #### ✏ Postup
  1. Kalkulacka probiha tak dlouho, dokud ji uzivatel neukonci
  2. Ukoncime pomoci vyrazu `exit`
  3. Zabranime pouziti nevalidnich operaci
  ```python
  def main() -> None:
      """Hlavni ridici funkce nasi kalkulacky"""
      UVODNI_ZPRAVA = "VITEJTE V PROGRAMU KALKULACKA!"
      ODDELOVAC = "=" * 50
      pozdrav_uzivatele(UVODNI_ZPRAVA, ODDELOVAC)

      while (operator := zvol_operator()) != "exit":
          if operator in ("+", "-", "*", "/"):
              x1, x2 = zvol_cisla().replace(" ", "").split(",")
              print(f"VYSLEDEK: {zpracuj_vypocet(x1, x2, operator)}",
                    end=ODDELOVAC)
          else:
              print("NEPODPOROVANY OPERATOR", end=ODDELOVAC)

      else:
          print("UKONCUJI KALKULACKU..")
          quit()
  ```
  **Pozor!**, nakonec nezapomene zavolat hlavni funkci `main`.

</details>

</details>

---

<details>
  <summary>🚧 Procvicovani na doma</summary>

<details>
  <summary>🚧 __doc__</summary>

---
</details>

<details>
  <summary>🚧 anotace funkci</summary>

---
</details>

<details>
  <summary>🚧 type hints</summary>

---
</details>

<details>
  <summary>🚧 Dopiseme funkci pro sumu cisel</summary>

  **Ukazka**
  ```python
# Vkladame libovolny pocet cisel
  1, 2, 3, 4, 5, 6, 7, 8, 9, 0

# Dostavame prumernou hodnotu
  4.5
  ```

  Podminka ve funkci `main`:
  ```python
  elif operator in ("abs", "prum", "prumer"):
      rada = vyber_radu_cisel()
      print(f"RADA CISEL: {rada}, VYSLEDEK: {sum(rada)/len(rada)}",
            end=ODDELOVAC)
  ```

  Samotna funkce:
  ```python
  def zvol_radu_cisel() -> "list":
      rada_cisel = input("VLOZTE CISLA ODDELENA CARKOU: ")
      return [
          float(cislo.strip())
          for cislo in rada_cisel.split(",")
          if cislo != ""
      ]
  ```

---
</details>

<details>
  <summary>🚧 Vlastni uzavrena funkce</summary>

  1. Napiste uzavirajici funkci `vnejsi`
  2. Tato funkce rozdeli string pomoci `@`
  3. Napiste uzavrenou funkci `vnitrni`
  4. Tato funkce vrati oba stringy po rozdeleni `.`
  ```python
  def vnejsi_func(em):
      mail = em.split("@")
      def vnitrni_func():
              return mail[1].split(".")
      domena, *zbytek = vnitrni_func()
      return domena

  print(f"Top-level domain: {vnejsi_func("Matous@gmail.com")}")
  ```

---
</details>

</details>

---
➡ [pokracovat na osmou lekci](https://github.com/Bralor/python-academy/tree/lekce08)

