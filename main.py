"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Barbora Svobodová
email: stavby.hlavac@seznam.cz
"""
import re

# Seznam registrovaných uživatelů (jméno: heslo)
registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Seznam textů k analýze
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Přihlašování
username = input("Username: ")
password = input("Password: ")

# Ověření přihlašovacích údajů
if username in registrovani_uzivatele and registrovani_uzivatele[username] == password:
    print("----------------------------------------")
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")

    volba = input("Enter a number between 1 and 3 to select: ")

    # Ověření vstupu
    if not volba.isdigit():
        print("Error: Please enter a valid number. Terminating the program.")
        exit()
    
    volba = int(volba)
    if volba < 1 or volba > len(TEXTS):
        print("Error: Selected number does not match any text. Terminating the program.")
        exit()

    text_k_analyze = TEXTS[volba - 1]

    # Analýza textu
    slova = re.findall(r'\b\w+\b', text_k_analyze)
    pocet_slov = len(slova)
    velka_pismena = sum(1 for slovo in slova if slovo.istitle())
    cela_velka = sum(1 for slovo in slova if slovo.isupper())
    cela_mala = sum(1 for slovo in slova if slovo.islower())
    cisla = [int(cislo) for cislo in re.findall(r'\b\d+\b', text_k_analyze)]
    pocet_cisel = len(cisla)
    soucet_cisel = sum(cisla)

    print("----------------------------------------")
    print(f"There are {pocet_slov} words in the selected text.")
    print(f"There are {velka_pismena} titlecase words.")
    print(f"There are {cela_velka} uppercase words.")
    print(f"There are {cela_mala} lowercase words.")
    print(f"There are {pocet_cisel} numeric strings.")
    print(f"The sum of all the numbers: {soucet_cisel}")
    print("----------------------------------------")

    # Výpočet délek slov
    cetnosti = {}
    for slovo in slova:
        delka = len(slovo)
        cetnosti[delka] = cetnosti.get(delka, 0) + 1

    print("LEN | OCCURRENCES | NR.")
    print("----------------------------------------")
    for delka, pocet in sorted(cetnosti.items()):
        print(f"{delka:3} | {'*' * pocet:<15} | {pocet}")

else:
    print("Unregistered user, terminating the program.")
    