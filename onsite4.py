""" Lekce #4 - Uvod do programovani, nakupni kosik """

KOSIK = {}
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

from pprint import pprint

print("VITEJTE V NASEM VIRTUALNIM OBCHODE!", end=f"\n{ODDELOVAC}\n")
print("VYBERTE SI Z NASEHO ZBOZI:", end=f"\n{ODDELOVAC}\n")
TABULKA = POTRAVINY.copy()

while TABULKA:
    radek_potravina = TABULKA.popitem()  # "pomeranc": [15, 10]
    print(f"POTRAVINA: {radek_potravina[0]},\tCENA: {radek_potravina[1][0]}")
else:
    print(ODDELOVAC)

while (vyber_potravinu := input("VYBERTE ZBOZI: ")) != "q":
    if vyber_potravinu not in POTRAVINY:
        print(f"*{vyber_potravinu}* NEMAME SKLADEM!")
    else:
        KOSIK[vyber_potravinu] = POTRAVINY[vyber_potravinu][0]
else:
    print(ODDELOVAC)
    print("KOSIK JE PLNY! UKONCUJI", end=f"\n{ODDELOVAC}\n")
    print(KOSIK, end=f"\n{ODDELOVAC}\n")
    print(f"CENA CELKEM: {sum(KOSIK.values())} CZK", end=f"\n{ODDELOVAC}\n")
