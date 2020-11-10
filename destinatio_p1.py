#!/usr/local/bin/python3.8
"""Lekce #1 - Uvod do programovani, 1/2 Destinatio"""

MESTA = ("Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava")
CENY = (150, 200, 120, 120, 100, 180)
ODDELOVAC = "=" * 35

print(ODDELOVAC)
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

por_cislo = int(input("VYBERTE CISLO LOKALITY: "))
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
rok_narozeni = int(input("ROK NAROZENI: "))
email = input("EMAIL: ")
heslo = input("HESLO: ")
print(ODDELOVAC)

destinace = MESTA[por_cislo - 1]
cena = CENY[por_cislo - 1]

print("UZIVATEL: " + jmeno)
print("DESTINACE: " + destinace)
print("CENA(cil:" + destinace + "): " + str(cena))
print(f"JIZDENKU POSLEME NA VASI EMAILOVOU ADRESU: {email}")

