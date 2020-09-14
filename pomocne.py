#!/usr/bin/python3
"""Lekce #11 - Uvod do programovani, importovani - pomocne.py"""
import os


def nacti_soubor(soubor: str) -> list:
    try:
        with open(soubor, "r", encoding="utf-8") as txt:
            obsah = txt.readlines()

    except FileNotFoundError:
        print(f"TXT SOUBOR: {soubor}, NEEXISTUJE!")

    else:
        return obsah


def vytvor_adresar(jmeno_sl: str) -> None:
    os.mkdir(jmeno_sl)


def vytvor_soubor(jmeno_so: str) -> None:
    if not os.path.isfile(jmeno_so):
        with open(jmeno_so, "w") as soub:
            print(f"VYTVARIM: {jmeno_so}")
        print("HOTOVO!")

    else:
        print(f"SOUBOR: {jmeno_so} EXISTUJE!")


def vytvor_vsechny_soubory(vsechna_jm: list, jmeno_adresare: str) -> None:
    for jmeno in vsechna_jm:
        vytvor_soubor(
            os.path.join(
                os.path.abspath(jmeno_adresare),
                jmeno.strip())
        )

