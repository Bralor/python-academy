#!/usr/bin/python3
"""Lekce #11 - Uvod do programovani, importovani - pomocne"""
import os

from typing import List


def nacti_soubor(soubor: str, mod: str = "r") -> List[str]:
    try:
        with open(soubor, mod) as txt:
            obsah = txt.readlines()

    except FileNotFoundError:
        print(f"SOUBOR: {soubor} NEEXISTUJE!")

    else:
        return obsah


def vytvor_soubor(jmeno_soubor: str, abs_cesta: str) -> None:
    try:
        novy_soubor = os.path.join(abs_cesta, jmeno_soubor)
        with open(novy_soubor, "w") as nf:
            print(f"VYTVARIM: {novy_soubor}")

    except FileExistsError:
        print(f"SOUBOR: {novy_soubor} JIZ EXISTUJE!")

    else:
        print("HOTOVO!")


def vytvor_adresar(jmeno: str, abs_cesta: str) -> str:
    try:
        os.mkdir(os.path.join(abs_cesta, jmeno))

    except FileExistsError:
        print(f"ADRESAR: {jmeno} EXISTUJE!")

    except FileNotFoundError:
        print(f"ABSOLUTNI CESTA: {abs_cesta} NEEXISTUJE!")


    else:
        return os.path.join(abs_cesta, jmeno)


