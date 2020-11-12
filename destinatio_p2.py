#!/usr/bin/python3
"""Lekce #2 - Uvod do programovani, 2/2 Destinatio """

MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
CENY = (150, 200, 120, 120, 100, 180)
SLEVY = ("Olomouc", "Ostrava")
ODDELOVAC = "=" * 35
AKT_ROK = 2020

print("VITEJTE U NASI APLIKACE DESTINATIO!")
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

cislo_lokality = int(input("VYBERTE CISLO LOKALITY: "))
if cislo_lokality > 1 or cislo_lokality < 6:
    destinace = MESTA[cislo_lokality - 1]
    cena = CENY[cislo_lokality - 1]
    print(f"DESTINACE: {destinace}")
    print(ODDELOVAC)
else:
    print("VAMI VYBRANE CISLO NENI V NABIDCE, UKONCUJI..")
    exit()

if destinace in SLEVY:
    cena_po_sleve = 0.75 * cena
else:
    cena_po_sleve = cena

jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
if jmeno.isalpha() and prijmeni.isalpha():
    print(f"JMENO: {jmeno}, PRIJMENI: {prijmeni}")
    print(ODDELOVAC)
else:
    print("JMENO A PRIJMENI MUSI OBSAHOVAT POUZE PISMENA, UKONCUJI..")
    exit()

vek = int(input("ROK NAROZENI: "))
if (AKT_ROK - vek) >= 18:
    print(f"POKRACUJI..")
    print(ODDELOVAC)
else:
    print("NASE SLUZBY MOHOU VYUZIVAT POUZE OSOBY STARSI 18 LET, UKONCUJI..")
    exit()

email = input("EMAIL: ")
if "@" in email:
    print("EMAIL V PORADKU, POKRACUJI..")
    print(ODDELOVAC)
else:
    print("NEPODPOROVANY FORMAT EMAILU, UKONCUJI..")
    exit()

heslo = input("HESLO: ")
if len(heslo) >= 8 or heslo.isalpha() and heslo.isnumeric():
    print("HESLO V PORADKU")
    print(ODDELOVAC)
    print("DESTINACE: " + destinace)
    print("DEKUJEME,", jmeno, "JIZDENKU POSLEME NA EMAIL:", email)
    print(f"CENA (CIL: {destinace}): {cena}")
    print(ODDELOVAC)
else:
    print(
        """TVOJE HESLO JE SPATNE ZADANE:
	1. MUSI OBSAHOVAT JAK PISMENA, TAK CISLICE,
	2. ALESPON 8 ZNAKU DLOUHE,
    """
    )

