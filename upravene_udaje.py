#!/usr/bin/python3
"""Lekce #06 - Uvod do programovani, Uprav udaje"""

UDAJE = '''
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
byt0006,87m2,Olomouc,ul.Černá_cesta,
byt0007,95m2,Olomouc,ul.Kaštanová,
byt0003,74m2,Olomouc,ul.Nová_Ulice,
byt0003,75m2,Olomouc,ul.Nová_Ulice,
byt0004,86m2,Olomouc,ul.Hněvotínská,
byt0002,67m2,Olomouc,ul.Polská,
byt0007,120m2,Olomouc,ul.Dvořákova,
byt0004,90m2,Olomouc,ul.Dvořákova,
byt0004,86m2,Olomouc,ul.Nová_Ulice,
byt0003,75m2,Olomouc,ul.Nešverova,
byt0001,45m2,Olomouc,ul.Zirmova,
byt0008,45m2,Olomouc,ul.Zirmova,
byt0006,114m2,Olomouc,ul.Přichystalová,
'''

PREVOD_UDAJU = {
    "byt0001": "1+1",
    "byt0002": "2+1",
    "byt0003": "2+kk",
    "byt0004": "3+1",
    "byt0005": "3+kk",
    "byt0006": "4+1",
    "byt0007": "4+kk",
}


def prevodnik_bytu(typ_bytu: str, vzor: dict) -> tuple:
    """Prevede a zapocita stavajici typ bytu na novy"""
    if typ_bytu in vzor:
        typ_bytu = vzor[typ_bytu]
        return (typ_bytu, 1)
    else:
        return ("NEZNAMY TYP BYTU!", 0)


vysledky = set()
uspesne = 0

for radek in UDAJE.split():
      typ, *dalsi_udaje = radek.split(",", maxsplit=3)
      upraveny_typ, prirustek = prevodnik_bytu(typ, PREVOD_UDAJU)
      uspesne += prirustek
      upraveny_radek = f"{upraveny_typ},{','.join(dalsi_udaje)}"
      vysledky.add(upraveny_radek)

for vysledek in vysledky:
    if "NEZNAMY TYP BYTU!" in vysledek:
        continue
    else:
        print(f"{vysledek=}")
else:
    print(f"PREVEDENO: {uspesne} UDAJU")
    # print(f"CHYBA: -> {vysledek}") if "NEZNAMY TYP BYTU!" in vysledek \
    # else print(f"{vysledek=}")

# prevedene_typy = [
    # prevodnik_bytu(radek.split(",", maxsplit=3)[0], PREVOD_UDAJU)
    # for radek in UDAJE.split()
# ]

# vysledky = {
    # f"{prevedene_typy[index][0]},{radek.split(',', maxsplit=1)[1]}"
    # for index, radek in enumerate(UDAJE.split(), 0)
# }

# uspesne = [udaje[1] for udaje in prevedene_typy]

