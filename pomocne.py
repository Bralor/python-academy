#!/usr/bin/python3
"""Lekce #11 - Uvod do programovani, importovani - pomocne"""
import os

def nacti_soubor(soubor: str, mod: str = "r") -> list:
    try:
        with open(soubor, mod) as txt:
            obsah = txt.readlines()

    except FileNotFoundError:
        print(f"SOUBOR: {soubor} NEEXISTUJE!")

    else:
        return obsah


def vytvor_adresar(jmeno: str) -> str:
    os.mkdir(jmeno)


def vytvor_soubor(jmeno_soubor: str, abs_cesta: str) -> None:
    try:
        novy_soubor = os.path.join(abs_cesta, jmeno_soubor)

        if not os.path.isfile(novy_soubor):
            with open(novy_soubor, "w") as nf:
                print(f"VYTVARIM: {novy_soubor}")
        else:
            raise Exception()

    except Exception:
        print(f"SOUBOR: {novy_soubor} JIZ EXISTUJE!")

    else:
        print("HOTOVO!")

