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
2. Ciselne a textove hodnoty (prevadime?)
3. Promenne
4. Kontejnerove hodnoty (indexovani?)
5. Uvodni sekce
6. Vypisujeme
7. Ukladame
8. Formujeme lepsi vystup s rezetci
---

<details>
  <summary>⏯  Ukazka ulohy</summary>

  1. ✌  [Stahnete si prvni lekci jako **zip**](https://github.com/Bralor/python-academy/archive/lekce01.zip)
  2. 💪 Presunte se ke stazenemu souboru
  3. 🙏 Spustte soubor **movies** v PyCharm
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


---

</details>

---

</details>

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
---

</details>

---

<details>
  <summary>📬 Kontejnerove datove typy</summary>

<details>
  <summary>📑 Seznam (list)</summary>

  #### ☝ K zapamatovani
  - tvoreny hranatymi zavorkami
  - udaje oddelene _carkou_ (ucel carky je tedy datovy oddelovac)
  - muzeme pridavat a odebirat udaje (_zmenitelna_ posloupnost)
  - udaje maji dane _poradi_
  - muze obsahovat retezec, cela cisla, desetinna cisla i jine seznamy
  - muzeme _indexovat_

  #### ❔ Jak vypada seznam
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
  <summary>📑 Ntice (tupl)</summary>

  #### ☝ K zapamatovani
  - tvoreny kulatymi zavorkami
  - udaje oddelene _carkou_ (ucel carky je tedy datovy oddelovac)
  - **nemuzeme** pridavat a odebirat udaje (_nezmenitelna_ posloupnost)
  - udaje maji dane _poradi_
  - muze obsahovat retezec, cela cisla, desetinna cisla, seznamy a ntice
  - muzeme _indexovat_

  #### ❔ Jak vypada ntice
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
---

</details>

</details>

---

<details>
  <summary>Uvodni sekce</summary>

---

</details>

---

<details>
  <summary>Vypisujeme</summary>

---

</details>

---

<details>
  <summary>ukladame</summary>

---

</details>

---

<details>
  <summary>Formujeme vystup</summary>

---

</details>

---
[Promenne](https://engeto.com/cs/kurz/python-academy/studium/0ujrbVm0T_uX6LlvMP1D1g/1-intro-to-programming/data/variable) v Pythonu jsou je symbolickymi odkazy, ktere odkazuji na objekt v pameti.

__Predpis/syntaxe__ vypada nasledovne:
```python
<jmeno_promenne> = <hodnota> (retezec, cele_cislo, desetinne_cislo, aj.)
```

__Priklad__:
```python
MESTO = 'Praha'     # retezec, konstanta
MNOZSTVI = 2        # cele_cislo, konstanta
CENA = 1000.5       # desetinne_cislo, konstanta
```

## Promenne obsahujici vice udaju
### Seznam, list
List neboli seznam je zmenitelna posloupnost prvku. Tzn. jednotlive prvku muzeme menit, muzeme pracovat s libovolnou casti seznamu, muzeme jej rozsirovat nebo promazavat.

__Obecne__:
```python
<jmeno_seznamu> = <[>"udaj_1"<,> "udaj_2"<,> "udaj_3"<,> "udaj_4"<]>
```
__Priklad__:
```python
JMENA = ["Matous", "Marek", "Lukas", "Jan"]; type(JMENA)  # seznam s retezci
```

## N-tice, tuple
Tuple neboli n-tice je naopak nezmenitelna posloupnost prvku. Muzeme sice pouzivat jednotlive data, ale nemuzeme je menit.

__Obecne__:
```python
<jmeno_ntice> = <(>"udaj_1"<,> "udaj_2"<,> "udaj_3"<,> "udaj_4"<)>
```

__Priklad__:
```python
CISLICE = ("Biscuit", "in", "the", "basket"); type(numbers)  # n-tice s retezci
```

## Uz doopravdy muzeme zacit...
<p align="center">
  <img src="https://media.giphy.com/media/7XZEvQlmM3DJm/giphy.gif" width="300" height="300">
</p>

## Promenne na uvod
Zadame promenne, se kterymi chceme pracovat. Musime nekde uchovat jmena mest, cen a vizualni oddelovac.
```python
"""Lekce #1 - Uvod do programovani, 1/2 Destinatio"""
MESTA = ("Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava")
CENY = (150, 200, 120, 120, 100, 180)
ODDELOVAC = '==================================='
```

## Nas prvni vypis z programu
Chceme oficialne uvitat uzivatele, oznamit mu nase umysly a ukazat aktualni nabidku. Jak to provedeme?

### Funkce print()
Je to [vestavena funkce](https://engeto.com/cs/kurz/python-academy/studium/GzlxQFyiSSuTLjE_B99htw/1-intro-to-programming/basics/input-output-data) Pythonu (s Pythonem nainstalovana, neni nutne ji tvorit). Ucelem teto funkce je vypsat informace, ktere ji vlozime do kulatych zavorek.

__Obecne__:
```python
<jmeno_funce><(><hodnota_na_vypsani><)>
```

__Priklad__:
```python
print("Jimmy H.")
JMENO = 'James Marshall "Jimi" Hendrix'; print(JMENO)  # kombinace uvozovek!
```
Dopiseme pozdrav a info:
```python
print(ODDELOVAC)
print("Vitejte u nasi aplikace Destinatio!")
print(ODDELOVAC)
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

## Vkladame hodnoty pomoci input()
Jde opet o vestavenou funkci v Pythonu. Tato funkce ocekava od uzivatele nejakou vstupni informaci. Cokoliv do ni vlozime tato vestavena funkce standartne premeni na retezec!

__Priklad__:
```python
email = input("Your email address: "); print(email)  # matous@nic.cz
```
Od uzivatele chceme tyto vyplnene udaje:
1. Cislo mesta
2. Jmeno
3. Prijmeni
4. Rok narozeni
5. E-mail
6. Heslo

Dopsany kod:
```python
por_cislo = int(input("Vyberte cislo lokality: "))
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
rok_narozeni = int(input("ROK NAROZENI: "))
email = input("EMAIL: ")
heslo = input("HESLO: ")
print(ODDELOVAC)
```

## Cisla sedi?
Nas program vyzkousime a vybereme libovolnou hodnotu pro mesto, ktere pozadujeme:
```bash
===================================
Vitejte u nasi aplikace Destinatio!
===================================

1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180

===================================
Vyberte cislo lokality: 1
...
```
Jake mesto ale dostaneme?

## Jak vse zachranit?
### Pomoci _indexovani_
Jde o [cislo](https://engeto.com/cs/kurz/python-academy/studium/ahOxRKnuRB2NB2HCqIqRKA/1-intro-to-programming/sequence-data-types/indexing) v hranatych zavorkach zapsane ihned za jmenem promenne. Vraci objekt na urcene pozici. Zapamatujte si, ze index pozice prvni polozky je 0 (posledni -1).

__Obecne__:
```python
<jmeno_promenne_kde_mohu_indexovat><[><index><]>
```

__Priklad__:
```python
CISLICE = ("Biscuit", "in", "the", "basket")  # chci ziskat prvni, posledni udaj v ntici
CISLICE[0]; CISLICE[-1]
```
Nyni muzeme udaj opravit. Uzivatel ma totiz k dispozici pouze nas vypis. O indexovani nema ani potuchy. Proto je potreba provest zmeny na pozadi.

Doplnime zmeny s indexovanim:
```python
destinace = MESTA[por_cislo - 1]  # --> destiance[0] pokud bude por_cislo = 1
cena = CENY[por_cislo - 1]
```

## Nyni vratime, vypiseme uzivatelem vyplnene hodnoty
K tomu budeme opet potrebovat funkci _print()_ a nejen ji. Ve vzorovem vystupu vypisuji nejen predepsany text, ale obsah konkretnich promennych. Toho docilime z pravidla tremi postupy:

1. [Konkatenace](#-konkatenace-spojovani)
2. [Oddelovacem](#-oddelovac)
3. [f-string formatovani](#f-string-formatovani)

### Konkatenace, spojovani
Je to [proces](https://engeto.com/cs/kurz/python-academy/studium/1YyeD7QBTIuqU_BMzkcT_w/1-intro-to-programming/sequence-data-types/concatenation), ktery funguje jen u nekterych datovych typu (retezec, seznam, n-tice). Spoji dve ruzne promenne do jedne (pomoci "+" operatoru).

__Priklad__:
```python
print("DESTINACE: " + destinace)
```

## Oddelovac
Spojeni ruznych datovych typu na vystupu pomoci carky.

__Priklad__:
```python
DESTINACE = "Brno"
CENA = 80
print("Cestuji do", DESTINACE, "za pouhych", CENA, ",- .")
```

## F-string formatovani
Vysvetlime si podrobneji v dalsich lekcich. Zatim staci videt, jak jej pouzivat.

__Priklad__:
```python
JMENO = "Matous"
EMAIL = "matous@matous.cz"
print(f"{JMENO}, jizdenku posleme na Vasi emailovou adresu *{email}*")
```

Doplnime chybejici informace:
```python
print("UZIVATEL: " + jmeno)
print("DESTINACE: " + destinace)
print("CENA(cil:" + destinace + "): " + str(cena))
print(f"Jizdenku posleme na Vasi emailovou adresu: {email}")
```

## Malickost zaverem
Zpusob zapsani oddelovace je malicko nesikovna. Muzeme cely proces vylepsit [opakovanim](https://engeto.com/cs/kurz/python-academy/studium/QnEydRFvSu2qmTCPIVEW0Q/1-intro-to-programming/sequence-data-types/repetition). Tento proces se sklada ze sekvence, kterou budeme opakovat, operatoru pro opakovani "*" a za nim cele cislo, ktere specifikuje pocet opakovani.

__Obecne__:
```python
<uvozovky><co_opakovat><uvozovky> <operand> <kolikrat>
```

__Priklad__:
```python
"Matous" * 10
```

Nahradime hodnotu promenne __ODDELOVAC__:
```python
ODDELOVAC = "=" * 35
```

Pokracovat na [Lekci#02](https://github.com/Bralor/python-academy/blob/lekce02/README.md)
