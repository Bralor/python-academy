#!/usr/bin/python3
"""Lekce #07 - Uvod do programovani, kalkulacka.py"""


def main() -> None:
    """Hlavni ridici funkce nasi kalkulacky"""
    UVODNI_ZPRAVA = "VITEJTE V PROGRAMU KALKULACKA!"
    ODDELOVAC = f"\n{'=' * 50}\n"
    pozdrav_uzivatele(UVODNI_ZPRAVA, ODDELOVAC)

    while (operator := zvol_operator()) != "exit":
        if operator in ("+", "-", "*", "/"):
            x1, x2 = zvol_cisla().replace(" ", "").split(",")
            print(f"VYSLEDEK: {zpracuj_vypocet(x1, x2, operator)}",
                  end=ODDELOVAC)
        else:
            print("NEPODPOROVANY OPERATOR", end=ODDELOVAC)

    else:
        print("UKONCUJI KALKULACKU..")
        quit()

def pozdrav_uzivatele(uvod: str, oddelovac: str) -> None:
    print(f"{uvod}".center(50), end=oddelovac)


def vypis_nabidku(oddelovac: str, *args) -> None:
    print(f"{' | '.join(args)}".center(50), end=oddelovac)


def zvol_operator() -> str:
    return input("VYBER MATEMATICKOU OPERACI: ")


def zvol_cisla() -> str:
    return input("ZADEJ 2 CISLA ODDELENE CARKOU: ")


def zpracuj_vypocet(x1: str, x2: str, op: str) -> float:
    """
    Uzivatel vlozi hodnoty do parametru:
    x1 -> str [1, 1.1, 11.1, -1.11]
    x2 -> str [2, 2.2, 22.2, -2.22]
    op -> str ["+", "-", "*", "/"]

    Obecna proces funkce:
    x1 = 1, x2 = 2, op = "+" ->  1 + 2
    x1 = 1.11, x2 = 2.22, op = "-" ->  1.11 - 2.22
    """
    return {
      "+": float(x1) + float(x2),
      "-": float(x1) - float(x2),
      "*": float(x1) * float(x2),
      "/": float(x1) / float(x2)
    }.get(op)


main()

