# IMPORTS
import random
# IMPORTS


# LISTS
KleineLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
HoofdLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Nummers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
SpecialeTekens = ['@', '#', '$', '%', '&', '_', '?']
Wachtwoord = []
# LISTS


# VARIABELEN
ListLengte = len(Wachtwoord)
# VARIABELEN


# RANDOM PASSWORD GENERATOR
while ListLengte != 24:

    # VOEG KLEINE LETTERS TOE
    AantalKleineLetters = random.randint(8, 16)
    for i in range(AantalKleineLetters):
        RandomLettersVoorList = random.randint(0, 25)
        Wachtwoord.append(KleineLetters[RandomLettersVoorList])
    # VOEG KLEINEL ETTERS TOE

    # VOEG HOOFD LETTERS TOE
    AantalHoofdLetters = random.randint(2, 6)
    for i in range(AantalHoofdLetters):
        RandomPlaatsLetters = random.randint(0, ListLengte)
        RandomLettersVoorList = random.randint(0, 25)
        Wachtwoord.insert(RandomPlaatsLetters,HoofdLetters[RandomLettersVoorList])
    # VOEG HOOFD LETTERS TOE

    # VOEG SPECIALE TEKENS TOE
    for i in range(0, 4):
        ListLengte = len(Wachtwoord)
        MaximaleVerte = ListLengte - 3
        RandomTekensVoorList = random.randint(0, 6)
        RandomPlaatsTekens = random.randint(3, MaximaleVerte)
        Wachtwoord.insert(RandomPlaatsTekens,SpecialeTekens[RandomTekensVoorList])
    # VOEG SPECIALE TEKENS TOE

    # VOEG NUMMERS TOE
    AantalNummers = random.randint(4, 7)
    for i in range(AantalNummers):
        MaximaleVerte = ListLengte - 3
        RandomGetallenVoorList = random.randint(0, 8)
        RandomPlaatsNummers = random.randint(3, MaximaleVerte)
        Wachtwoord.insert(RandomPlaatsNummers, Nummers[RandomGetallenVoorList])
    # VOEG NUMMERS TOE

    # GEEF DE WACHTWOORD AAN DE GEBRUIKER
    ListLengte = len(Wachtwoord)
    if ListLengte == 24:
        print(*Wachtwoord, sep='')
    # GEEF DE WACHTWOORD AAN DE GEBRUIKER

    # START OPNIEUW ALS HET NIET VOLDOET AAN DE EISEN
    else:
        Wachtwoord.clear()
    # START OPNIEUW ALS HET NIET VOLDOET AAN DE EISEN


# RANDOM PASSWORD GENERATOR