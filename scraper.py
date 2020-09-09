#!/usr/bin/python3.8
"""Lekce #12 - Uvod do programovani, web scraping"""

import sys
import csv

import requests
from bs4 import BeautifulSoup


def hlavni() -> None:
    odpoved_serveru = vytvor_pozadavek(url).text

    if odpoved_serveru:
        naparsovana_odp = zpracuj_pozadavek(odpoved_serveru)
        hraci = hledej_hrace(naparsovana_odp)
        udaje = [zpracuj_udaj(hrac) for hrac in hraci]

    if uloz_csv(udaje, soubor):
        print(f"ULOZENO DO: {soubor}")
    else:
        print(f"NELZE ULOZIT!")


def vytvor_pozadavek(url: str) -> str:
    with requests.Session() as se:
        return se.get(url)


def zpracuj_pozadavek(odpoved: str) -> BeautifulSoup:
    return BeautifulSoup(odpoved, "html.parser")


def hledej_hrace(data: BeautifulSoup) -> list:
    table = data.find("table", {"class": "tab_top"})
    return table.find_all("tr")[1:]


def zpracuj_udaj(tr: str) -> dict:
    poradi = tr.find_all("td")[0].text
    jmeno = tr.find_all("td")[2].text
    body = tr.find_all("td")[3].text
    celkem = tr.find_all("td")[6].text
    vitezstvi = tr.find_all("td")[5].text
    uspesnost = tr.find_all("td")[7].text

    return {
        "poradi": poradi,
        "jmeno": jmeno,
        "body": body,
        "celkem": celkem,
        "vitezstvi": vitezstvi,
        "uspesnost": uspesnost,
    }


def uloz_csv(data: dict, jmeno: str) -> None:
    with open(jmeno, "w", newline="") as csv_s:
        zahlavi = data[0].keys()
        writer = csv.DictWriter(csv_s, fieldnames=zahlavi)

        writer.writeheader()
        for index, _ in enumerate(data):
            writer.writerow(
                {
                    "poradi": data[index]["poradi"],
                    "jmeno": data[index]["jmeno"],
                    "body": data[index]["body"],
                    "celkem": data[index]["celkem"],
                    "vitezstvi": data[index]["vitezstvi"],
                    "uspesnost": data[index]["uspesnost"],
                }
            )
        return True


if __name__ == "__main__":
    url = sys.argv[1]
    soubor = sys.argv[2]
    hlavni()
    # http://heroes3.cz/hraci/index.php?page=1&order=&razeni=DESC
