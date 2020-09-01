#!/usr/bin/python3.8
"""Lekce #12 - Uvod do programovani, csv/json - pomocne funkce"""
import csv
import json


def nacti_json(soubor: str, mod: str = "r") -> dict:
    try:
        with open(soubor, mod) as cteni:
            obsah = json.load(cteni)

    except FileNotFoundError:
        print(f"SOUBOR: {soubor} NEEXISTUJE!")

    else:
        return obsah


def uprav_obsah(data: dict) -> dict:
    """
    Zredukujeme puvodni slovnik 'data' pouze na 3 klice:
        1. jmeno
        2. prijmeni
        3. email

    Ulozime do noveho slovniku a vracime jej
    """
    upravene_udaje = {}

    for index, slovnik in enumerate(data, 1):
        upravene_udaje[f"id_{index}"] = {
            "jmeno": slovnik["first_name"],
            "prijmeni": slovnik["last_name"],
            "email": slovnik["email"]
        }
    return upravene_udaje


def zapis_csv(soubor: str, udaje: dict) -> None:
    try:
        with open(soubor, mode="w", newline="") as csv_f:
            zahlavi = udaje["id_1"].keys()
            zapisovac = csv.DictWriter(csv_f, fieldnames=zahlavi)
            
            zapisovac.writeheader()
            for zamestnanec in udaje:
                zapisovac.writerow({
                    "jmeno": udaje[zamestnanec]["jmeno"],
                    "prijmeni": udaje[zamestnanec]["prijmeni"],
                    "email": udaje[zamestnanec]["email"]
                })

    except KeyError:
        print("INCORRECT KEY!")

