#!/usr//bin/python3.8
"""Lekce #11 - Uvod do programovani, csv/json - hlavni funkce"""
import sys

from pomocne import nacti_json, uprav_obsah, zapis_csv


def hlavni() -> None:
    if prevod == "do-csv":
        nacteny_json = nacti_json("ORIG.json")
        zkracene_udaje = uprav_obsah(nacteny_json)
        zapis_csv("vystupni.csv", zkracene_udaje)


if __name__ == "__main__":
    prevod = sys.argv[1]
    hlavni()

