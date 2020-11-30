#!/usr/bin/python3
"""Lekce #7 - Uvod do programovani, kalkulacka"""

NABIDKA = "DOSTUPNE OPERACE: "
ODDELOVAC = "=" * 50


def main() -> "None":
    "Hlavni ridici funkce nasi kalkulacky"
    uvodni_text("VITEJTE U PROGRAMU KALKULACKA")

    while True:
        dostupne_operace("+", "-", "*", "/", "abs")
        operace = vyber_operaci()
        vyber_operace(operace)


def uvodni_text(text: "str") -> None:
    "Uvodni text pred zacatkem cyklu"
    print(f"{text}".center(50), end=f"\n{ODDELOVAC}\n")


def dostupne_operace(*args) -> None:
    "Vypisovani dostupnych operaci uvnitr cyklu"
    print(f"{' | '.join(args)}".center(50), end=f"\n{ODDELOVAC}\n")


def vyber_operaci() -> "str":
    return input("VYBER MATEMATICKOU OPERACI: ")


def vyber_operace(op: "str") -> None:
    print(ODDELOVAC)

    if op in ("+", "-", "*", "/"):
        x1, x2 = vyber_cisla()
        vysledek = zakladni_operace(x1, x2, op)
        print(
            ODDELOVAC,
            f"x1 {op} x2: {x1} {op} {x2} = {vysledek}",
            ODDELOVAC,
            sep = "\n"
        )

    elif op in ("abs", "prum", "prumer"):
        rada = vyber_radu_cisel()
        print(
            ODDELOVAC,
            f"RADA CISEL: {rada}, VYSLEDEK: {sum(rada)/len(rada)}",
            ODDELOVAC,
            sep = "\n"
        )

    elif op in ("quit", "exit", "q", "e"):
        print("UKONCUJI...")
        exit()

    else:
        print(f"*{op}* NENI V NABIDCE")


def vyber_cisla() -> tuple:
    return float(input("x1: ")), float(input("x2: "))


def zakladni_operace(x: "float", y: "float", op: "str") -> float:
    return {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y
    }.get(op)


def vyber_radu_cisel() -> "list":
    rada_cisel = input("VLOZTE CISLA ODDELENA CARKOU: ")
    prevedene = [
        float(cislo.strip())
        for cislo in rada_cisel.split(",")
        if cislo != ""
    ]
    return prevedene


main()

