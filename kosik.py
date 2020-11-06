#!/usr/bin/python3
""" Lekce #4 - Uvod do programovani, Nakupni kosik """

kosik = {}
ODDELOVAC = "=" * 40
POTRAVINY = {
  "mleko": [30, 5],
  "maso": [100, 1],
  "banan": [30, 10],
  "jogurt": [10, 5],
  "chleb": [20, 5],
  "jablko": [10, 10],
  "pomeranc": [15, 10]
}

print(
"VITEJTE V NASEM VIRTUALNIM OBCHODE".center(40, " "),
end=f"\n{ODDELOVAC}\n"
)
TABULKA = POTRAVINY.copy()

while TABULKA:
    radek_potravina = TABULKA.popitem()
    print(f"POTRAVINA: {radek_potravina[0]},\tCENA: {radek_potravina[1][0]}")
else:
    print(ODDELOVAC)

while (vyber_zbozi := input("VYBERTE ZBOZI: ")) != 'q':

    if vyber_zbozi not in POTRAVINY:
        print(f"{vyber_zbozi} NEMAME V NABIDCE!")

    elif vyber_zbozi not in kosik and POTRAVINY[vyber_zbozi][1] > 0:
        kosik[vyber_zbozi] = [POTRAVINY[vyber_zbozi][0], 1]
        POTRAVINY[vyber_zbozi][1] = POTRAVINY[vyber_zbozi][1] - 1

    elif vyber_zbozi in kosik and (pocet := POTRAVINY[vyber_zbozi][1]) > 0:
        kosik[vyber_zbozi][1] += 1
        POTRAVINY[vyber_zbozi][1] = POTRAVINY[vyber_zbozi][1] - 1

    elif POTRAVINY[vyber_zbozi][1] == 0:
        print(f"{vyber_zbozi.upper()} JIZ NENI SKLADEM!")

else:
    print(
        f"{ODDELOVAC}\n",
        "KOSIK JE PLNY! UKONCUJI".center(40, " "),
        end=f"\n{ODDELOVAC}\n"
    )
    index = 0
    cena_celkem = 0

    while index < len(kosik):
        polozka_v_kosiku = list(kosik.values())[index]
        cena_celkem = cena_celkem + (polozka_v_kosiku[0] * polozka_v_kosiku[1])
        index = index + 1

    else:
        print(
            f"CELKOVA CENA: {cena_celkem},-".center(40, " "),
            end=f"\n{ODDELOVAC}\n"
        )

