#!/usr/bin/python3
import os


def nacti_txt_soubor(jmeno: str, enc: str = "utf-8") -> list:
    try:
        with open(jmeno, mode="r", encoding=enc) as txt_s:
            obsah = txt_s.readlines()

    except FileNotFoundError:
        print(f"SOUBOR: {jmeno} NENALEZEN!", f"\nADRESAR: {os.getcwd()}",
            f"\nOBSAHUJE: {os.listdir()}", sep="\n")
    else:
        print(f"SOUBOR: {jmeno} NACTEN")
        return obsah
    finally:
        print(f"UKONCUJI FUNKCI: nacti_txt_soubor\n")


JMENO_SOUBORU = "countries_and_cities.txt"

for udaj in nacti_txt_soubor(JMENO_SOUBORU):
    if udaj == "quit":
        break
    else:
        zeme, mesto = udaj.split(", ")
        zeme = zeme.title()
        mesto = mesto.strip().title()
        print(f"{zeme=:<20} {mesto=}")

