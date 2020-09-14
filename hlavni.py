#!/usr/bin/python3
"""Lekce #11 - Uvod do programovani, importovani - hlavni.py"""
import os
import sys

from pomocne import nacti_soubor
from pomocne import vytvor_adresar
from pomocne import vytvor_vsechny_soubory


def hlavni() -> None:
    jmena = nacti_soubor(jmena_souboru)

    if not os.path.isdir(jmeno_adresare):
        vytvor_adresar(jmeno_adresare)
        vytvor_vsechny_soubory(jmena, jmeno_adresare)

    else:
        print(f"SLOZKA: {jmeno_adresare}, EXISTUJE!")
        vytvor_vsechny_soubory(jmena, jmeno_adresare)


if len(sys.argv) != 3:
    print("POUZITI: python hlavni.py <txt_soubor> <jmeno_adresare>")

else:
    jmena_souboru = sys.argv[1]
    jmeno_adresare = sys.argv[2]
    hlavni()

