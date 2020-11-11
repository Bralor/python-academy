#!/usr/bin/python3
"""Lekce #1 - Uvod do programovani, 1/2 Destinatio"""

MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
CENY = (150, 200, 120, 120, 100, 180)
ODDELOVAC = "=" * 35

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
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
rok_narozeni = int(input("ROK NAROZENI: "))
email = input("EMAIL: ")
heslo = input("HESLO: ")
print(ODDELOVAC)

destinace = MESTA[cislo_lokality - 1]
cena = CENY[cislo_lokality - 1]

print("DESTINACE: " + destinace)
print("DEKUJI,", jmeno, ". JIZDENKU POSLEME NA EMAIL:", email)
print("CENA(cil:" + destinace + "): " + str(cena))

