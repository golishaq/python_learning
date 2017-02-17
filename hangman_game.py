# -*- coding: utf-8 -*-
# Szubienica
#
# Klasyczna gra w szubienicę.  Komputer losowo wybiera słowo,
# a gracz próbuje odgadnąć jego poszczególne litery.  Jeśli gracz
# nie odgadnie w porę całego słowa, mały ludzik zostaje powieszony.

# import modułów
import random

# stałe
HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   -+-
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   |
     |   |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | |
     |   | |
     |
    ----------
    """)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("DARIA", "BERCIK", "XBOXONE", "HOKUSPOKUSCZARYMARYTWOJASTARATOTWOJSTARY", "JAMAZUA", "MASLO")

# zmienne
word = random.choice(WORDS)
so_far = "-" * len(word)  # kreski obrazujace postep
wrong = 0  # liczba nietrafionych liter
used = []  # uzyte litery

print("Witaj w grze 'HANGMAN'. Powodzenia!")

while wrong < MAX_WRONG and so_far != word:  # glowna petla
    print(HANGMAN[wrong])
    print("\nWykorzystales juz nastepujace litery:\n", used)
    print("\nNa razie zagadkowe slowo wyglada tak:\n", so_far)

    guess = input("\nWprowadz litere: ")  # wprowadzanie litery i jej weryfikacja
    guess = guess.upper()

    while guess in used:
        print("Juz wykorzystales ", guess)
        guess = input("\nWprowadz litere: ")
        guess = guess.upper()

    used.append(guess)  # dodanie wybranej litery do zuzytych

    if guess in word:
        print("\nTo jedna z prawidlowych liter")

        # tworzenie nowego lancucha so_far z odgadnieta litera
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nNiestety nie zgadles")
        wrong += 1
    # zakonczenie gry
    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nZostales powieszony")
    elif so_far == word:
        print("\nOdgadles")

print("\nZagadkowe slowo to", word)

input("\nAby zakonczyc kliknij \"Enter\"")
