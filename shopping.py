# I. KROK
# Zadane udaje
from pprint import pprint

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
KOSIK = {}

# II. KROK
print(ODDELOVAC)
print("VITEJTE V NASEM VIRT. OBCHODE!", end=f"\n{ODDELOVAC}\n")
print("VYBERTE SI Z NASEHO ZBOZI:", end=f"\n{ODDELOVAC}\n")
pprint(POTRAVINY)
print(ODDELOVAC)

# III. KROK
# Vzit libovolny pocet potravin + celk. cena
while (vyber_zbozi := input("VYBER ZBOZI ('q' - konec): ")) != 'q':
    if vyber_zbozi not in POTRAVINY.keys():
        print(f"*{vyber_zbozi}* NEMAME!")
        continue

    else:
        KOSIK[vyber_zbozi] = POTRAVINY[vyber_zbozi][0]

else:
    print(ODDELOVAC)
    print("KOSIK JE PLNY! UKONCUJI", end=f"\n{ODDELOVAC}\n")
    print(KOSIK, end=f"\n{ODDELOVAC}\n")
    print(f"CENA CELKEM: {sum(KOSIK.values())} CZK", end=f"\n{ODDELOVAC}\n")







