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


cislo_lokality = int(input("Vyberte cislo lokality: "))
if cislo_lokality > 1 or cislo_lokality < 6:
    destinace = MESTA[cislo_lokality - 1]
    cena = CENY[cislo_lokality - 1]
    print(f"DESTINACE: {destinace}")
    print(ODDELOVAC)
else:
    print("Vami vybrane cislo neni v nabidce, ukoncuji")
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
    print("Jmeno a prijmeni musi obsahovat pouze pismena, ukoncuji")
    exit()

vek = int(input("ROK NAROZENI: "))
if (AKT_ROK - vek) >= 18:
    print(f"Pokracuji...")
    print(ODDELOVAC)
else:
    print("Nase sluzby mohou vyuzivat pouze osoby starsi 18 let, ukoncuji")
    exit()

email = input("EMAIL: ")
if "@" in email:
    print("Email v poradku, pokracuji...")
    print(ODDELOVAC)
else:
    print("Nepodporovany format emailu, ukoncuji")
    exit()

heslo = input("HESLO: ")
if len(heslo) >= 8 or heslo.isalpha() and heslo.isnumeric():
    print("Heslo v poradku")
    print("UZIVATEL: " + jmeno)
    print("DESTINACE: " + destinace)
    print("CENA(cil:" + destinace + "): " + str(cena_po_sleve))
    print(f"Jizdenku posleme na Vasi emailovou adresu: {email}")
    print(ODDELOVAC)
else:
    print(
        """Tvoje heslo je spatne zadane:
	1. Musi obsahovat jak pismena, tak cislice,
	2. Alespon 8 znaku dlouhe,
    """
    )

