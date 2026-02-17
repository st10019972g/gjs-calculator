"""
BASIESE SAKREKENAAR (CMD/Terminal)

"""

import os  # Word gebruik om stelsel-opdragte uit te voer (bv. skerm skoonmaak)


# -----------------------------
# FUNKSIES VIR BEREKENINGE
# -----------------------------

def tel_by(a: float, b: float) -> float:
    # Hierdie funksie tel twee getalle bymekaar en gee die som terug.
    return a + b


def trek_af(a: float, b: float) -> float:
    # Hierdie funksie trek die tweede getal van die eerste getal af en gee die antwoord terug.
    return a - b


def maal(a: float, b: float) -> float:
    # Hierdie funksie vermenigvuldig twee getalle en gee die produk terug.
    return a * b


def deel(a: float, b: float) -> float:
    # Hierdie funksie deel die eerste getal deur die tweede getal.
    # As die tweede getal 0 is, gooi ons 'n fout (ValueError) om deling deur nul te verhoed.
    if b == 0:
        raise ValueError("Jy kan nie deur 0 deel nie.")
    return a / b


# -----------------------------
# HULPFUNKSIES VIR INSET/UITSET
# -----------------------------

def maak_skerm_skoon() -> None:
    # Hierdie funksie "verwyder die uitset" deur die terminal-skerm skoon te maak.
    # Windows: cls
    # Linux/macOS: clear
    os.system("cls" if os.name == "nt" else "clear")


def lees_getal(vraag: str) -> float:
    # Hierdie funksie vra die gebruiker vir 'n getal.
    # Dit herhaal (loop) totdat die gebruiker 'n geldige numeriese waarde invoer.
    while True:
        invoer = input(vraag).strip()  # Lees die gebruiker se inset en verwyder ekstra spasies
        try:
            return float(invoer)  # Probeer om die inset na 'n float te omskep
        except ValueError:
            # As float() misluk, beteken dit die inset was nie 'n geldige getal nie
            print("Ongeldige getal. Probeer asseblief weer (bv. 10 of 10.5).")


def lees_keuse() -> str:
    # Hierdie funksie vra die gebruiker om 'n bewerking te kies.
    # Geldige opsies:
    # +  -  *  /  vir berekeninge
    # c         om skerm skoon te maak (uitset verwyder)
    # q         om te stop (sentinel)
    while True:
        keuse = input("Kies 'n bewerking (+, -, *, /), 'c' om skerm skoon te maak, of 'q' om te stop: ").strip().lower()
        if keuse in {"+", "-", "*", "/", "c", "q"}:
            return keuse
        print("Ongeldige keuse. Gebruik asseblief +, -, *, /, c of q.")


# -----------------------------
# HOOFPROGRAM (MAIN)
# -----------------------------

def main() -> None:
    # Hierdie is die hoof-funksie waar die program begin.
    
    #Maak die skerm skoon
    maak_skerm_skoon()
    
    # Ons gebruik 'n sentinel veranderlike ('q') om uit die while-loop te kan breek.
    sentinel = "q"  # As die gebruiker 'q' kies, stop die program

    print("Basiese Sakrekenaar (CMD/Terminal)")
    print("Opsies: +  -  *  /  |  c = skerm skoonmaak  |  q = stop\n")

    # Hierdie while-loop hou aan hardloop totdat die gebruiker die sentinel ('q') kies.
    while True:
        keuse = lees_keuse()  # Lees watter bewerking die gebruiker wil doen

        # As die gebruiker 'q' kies, verlaat ons die program.
        if keuse == sentinel:
            print("Totsiens.")
            break  # Breek uit die while-loop

        # As die gebruiker 'c' kies, maak ons die skerm skoon en gaan terug na die begin van die loop.
        if keuse == "c":
            maak_skerm_skoon()
            continue  # Slaan die res van die loop oor en begin weer van bo af

        # As ons hier kom, beteken dit die gebruiker het 'n berekening gekies (+, -, *, /).
        # Ons moet nou twee getalle lees.
        getal1 = lees_getal("Tik die eerste getal in: ")
        getal2 = lees_getal("Tik die tweede getal in: ")

        # Ons gebruik 'n try/except om deling deur nul (of ander ValueError) veilig te hanteer.
        try:
            # Kies die regte funksie op grond van die gebruiker se keuse.
            if keuse == "+":
                antwoord = tel_by(getal1, getal2)
            elif keuse == "-":
                antwoord = trek_af(getal1, getal2)
            elif keuse == "*":
                antwoord = maal(getal1, getal2)
            else:
                # As dit nie +, -, * is nie, moet dit / wees (volgens ons keuse-validasie).
                antwoord = deel(getal1, getal2)

            # Wys die resultaat aan die gebruiker.
            print(f"Antwoord: {antwoord}\n")

        except ValueError as fout:
            # Hierdie blok vang foute, soos deling deur nul.
            print(f"Fout: {fout}\n")


# Hierdie blok maak seker dat main() net hardloop as jy die lêer direk uitvoer.
# Dit help dat die kode later hergebruik kan word sonder dat dit outomaties hardloop as dit ingevoer word.
if __name__ == "__main__":
    main()
