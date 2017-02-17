# program wybiera losowe slowo ktore gracz musi odgadnac. Komputer informuje gracza ile liter znajduje
# sie w wybranym slowie  a nastepnie gracz ma 5 szans na zadanie pytania czy jakas litera znajduje sie wslowie
# komputer odpowiada tak/nie, potem gracz musi odgadnac slowo

from treningCh6 import slownik_test

# baza slow
WORDS = ("daria", "bartek", "bercik", "anagram", "leszczynowa", "latwy", "trudny")
counter = 0
# wybor losowego slowa z sekwencji + odpowiedz prawidlowa
word = slownik_test.choice(WORDS)

print("W wylosowanym slowie znajduje sie",len(word), "liter. masz piec prob na odgadniecie 5 liter\n"
                                                     "potem musisz odgadnac slowo")

for i in range(5):
    char = input("Podaj litere")
    if char in word:
        print("YUP")
        counter =+ 1
    else:
        print("NOPE")
print("Zgadles", counter, "liter w slowie\nCzy wiesz co to za slowo?")
guess = input()
if guess == word:
    print("To wlasciwe slowo")
else:
    print("NOPE")


input("\nAby zakonczyc kliknij \"Enter\"")
