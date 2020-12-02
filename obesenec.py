#!/usr/bin/python3
"""Lekce #8 - Uvod do programovani, obesenec"""
from random import sample


def main() -> None:
    """Hlavni ridici funkce nasi hry"""
    hrac = pridej_hrace()
    vybrane_slovo = vyber_slovo("slova.txt")
    tajne_slovo, pokusy = schovej_slovo(vybrane_slovo)

    while pokusy:
        vypis_hry(hrac, tajne_slovo, pokusy)
        overeni_pismena(vyber_pismena(), tajne_slovo, vybrane_slovo)
        konec_kola(tajne_slovo, pokusy)
        pokusy -= 1


def pridej_hrace() -> str:
    return input("ZADEJTE JMENO HRACE: ")


def vyber_slovo(soubor: str) -> str:
    with open(soubor, "r") as txt:
        return sample(set(txt.readlines()), 1).pop().strip()


def schovej_slovo(slovo: str) -> tuple:
    return (len(slovo) * ["_"], round(len(slovo) * 1.4))


def vypis_hry(jmeno: str, tajenka: list, pokusy: int) -> None:
    zprava = \
    f"|HRAC: {jmeno} | SLOVO: {' '.join(tajenka)} | ZBYVA POKUSU: {pokusy} |"
    oddelovac = len(zprava) * "-"
    print(oddelovac, zprava, oddelovac, sep="\n")


def vyber_pismena() -> str:
    return input("VYBER PISMENO: ")


def overeni_pismena(pismeno: str, tajne: list, puvodni: str) -> None:
    for index, pism in enumerate(puvodni):
        if pism == pismeno:
            tajne[index] = pismeno


def ukonceni_hry(tajne_slovo: list, hrac: str, pokusy: int) -> None:
    if "_" not in tajne_slovo:
        vypis_hry(hrac, tajne_slovo, pokusy)
        print(f"VYHRALS, {hrac}, GRATULACE")
        exit()

    elif "_" in tajne_slovo and pokusy == 0:
        print(f"PROHRALS, {hrac}, NEKDY JINDY!")
        exit()


def konec_kola(tajne_slovo: str, pokusy: int) -> None:
    if "_" not in tajne_slovo:
        print("VYHRALS!")
        quit()
    elif "_" in tajne_slovo and pokusy == 1:
        print("PROHRALS!")
        quit()

main()

