#!/usr/bin/python3
import os
from random import choice

import figurka


slovo = choice(["obesenec", "autobus", "klavesnice", "nedele"])
tajenka = len(slovo) * ["_"]
zivoty = 7
hra_probiha = True

while hra_probiha and zivoty > 0:
    os.system("clear")
    print(figurka.hangman[7 - zivoty])
    print(f"TAJENKA: {' '.join(tajenka)}, ZIVOTY: {zivoty}")
    hadani = input("ZADEJ PISMENO NEBO CELE SLOVO:").lower()

    if slovo == hadani:
        hra_probiha = False

    elif len(hadani) == 1 and hadani in slovo:
        for index, pismeno in enumerate(slovo):
            if pismeno == hadani:
                tajenka[index] = hadani

        hra_probiha = False if "_" not in tajenka else True

    else:
        zivoty -= 1

if not hra_probiha:
    print("SUPER, UHODL JSI TAJNE SLOVO!")
else:
    os.system("clear")
    print(figurka.hangman[7 - zivoty])
    print(f"PROHRAL JSI, TAJNE SLOVO BYLO *{slovo}*")
