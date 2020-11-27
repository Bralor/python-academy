#!/usr/bin/python3
""" Lekce #3 - Uvod do programovani, Movies """

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
        "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
        "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
        "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
        "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine", "Piper Perabo",
        "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin", "David Bowie"
    )
}

ODDELOVAC = "=" * 76
filmovy_slovnik = dict()

filmovy_slovnik[film_1["JMENO"]] = film_1
filmovy_slovnik[film_2["JMENO"]] = film_2
filmovy_slovnik[film_3["JMENO"]] = film_3
filmovy_slovnik[film_4["JMENO"]] = film_4

print(
    "VITEJTE V NASEM FILMOVEM SLOVNIKU!".center(76, " "),
    ODDELOVAC,
    "VYBERTE KATEGORII:",
    ODDELOVAC,
    "VSECHNY FILMY | DETAILY FILMU | SPOLECNI HERCI | VSICHNI REZISERI".center(76, " "),
    ODDELOVAC,
    sep="\n"
)

vyber = input("VYBERTE MOZNOST: ").lower()
print(ODDELOVAC)

if vyber == "vsechny filmy":
    print("MAME V NABIDCE TYTO FILMY: ",
        list(filmovy_slovnik.keys()),
        end=f"\n{ODDELOVAC}\n")

elif vyber ==  "detaily filmu":
    print(list(filmovy_slovnik.keys()), end=f"\n{ODDELOVAC}\n")
    vyber_filmu = input("VYBERTE FILM (OPATRNE NA VELKA/MALA PISMENA): ")

    print(ODDELOVAC,
        filmovy_slovnik.get(vyber_filmu, "TAKOVY FILM NEEXISTUJE!"),
        sep="\n")

elif vyber == "spolecni herci":
    print(list(filmovy_slovnik.keys()), end=f"\n{ODDELOVAC}\n")
    print(
        "MAME V NABIDCE TYTO FILMY: ",
        list(filmovy_slovnik.keys()),
        end=f"\n{ODDELOVAC}\n"
    )

elif vyber ==  "detaily filmu":
    print(
        list(filmovy_slovnik.keys()),
        end=f"\n{ODDELOVAC}\n"
    )

    vyber_filmu = input("VYBERTE FILM (OPATRNE NA VELKA/MALA PISMENA): ")
    print(
        ODDELOVAC,
        filmovy_slovnik.get(vyber_filmu, "TAKOVY FILM NEEXISTUJE!"),
        sep="\n"
    )

elif vyber == "spolecni herci":
    print(
        list(filmovy_slovnik.keys()),
        end=f"\n{ODDELOVAC}\n"
    )

    prvni_film = input("VYBERTE I. FILM: ")
    druhy_film = input("VYBERTE II. FILM: ")

    herci_prvni_film = set(filmovy_slovnik[prvni_film]["HRAJI"])
    herci_druhy_film = set(filmovy_slovnik[druhy_film]["HRAJI"])
    prunik = herci_prvni_film & herci_druhy_film

    print(f"SPOLECNI HERCI: {prunik}") if prunik else print("ZADNI SPOLECNI HERCI")

elif "reziseri" in vyber.lower():
    set_reziseri = {
        filmovy_slovnik["The Dark Knight"]["REZISER"],
        filmovy_slovnik["The Godfather"]["REZISER"],
        filmovy_slovnik["Shawshank Redemption"]["REZISER"],
        filmovy_slovnik["The Prestige"]["REZISER"]
    }

    print(f"VSICHNI REZISERI: {set_reziseri}")

else:
    print(f"MOZNOST --> {vyber} NENI V NABIDCE, UKONCUJI..")

